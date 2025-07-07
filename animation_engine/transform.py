from __future__ import annotations

from copy import deepcopy

from pyglm import glm

from animation_engine import math
from animation_engine.checkpoint_value import CheckpointValue
from animation_engine.math import float3, radians3, matrix44


class Transform:
    """
    A class representing a 3D transformation, including position, rotation, scale,
    and hierarchical relationships (parent-child).

    This class provides methods and properties to manage transformations in local
    and model space, as well as maintaining hierarchical relationships between
    transforms.
    """

    _dirty: bool
    """ Flag indicating whether the transform needs to be recalculated. """

    position = CheckpointValue[float3]()
    """ The position of the transform in local space. """
    rotation = CheckpointValue[radians3]()
    """ The rotation of the transform in local space (in radians). """
    scale = CheckpointValue[float3]()
    """ The scale of the transform in local space. """

    base_matrix: matrix44

    _parent: Transform | None
    """ The parent transform, if any. """
    _children: list[Transform]
    """ A list of child transforms. """

    _local_space_matrix: matrix44
    """ The local space transformation matrix. """
    _model_space_matrix: matrix44
    """ The model space transformation matrix. """

    _active: bool = True
    """
    Whether or not this Transform is active and if it's and it's children will receive matrix updates.
    Things associated with inactive Transforms (models, physics, etc) should also not be rendered or updated.
    """

    def __init__(
        self,
        /,
        position: float3 = float3(0),
        rotation: radians3 = radians3(0),
        scale: float3 = float3(1),
        base_matrix: matrix44 = None,
        parent: Transform | None = None,
        children: list[Transform] = None,
    ):
        """
        Initialize a new Transform instance. All params are keyword arguments.

        :param position: The initial position as a `float3` vector. Defaults to (0, 0, 0).
        :param rotation: The initial rotation as a `radians3` vector. Defaults to (0, 0, 0).
        :param scale: The initial scale as a `float3` vector. Defaults to (1, 1, 1).
        :param parent: The parent transform, or `None` if there is no parent. Defaults to `None`.
        :param children: A list of child transforms, or `None` to start with no children. Defaults to `None`.
        """
        self._dirty = True

        self.position = position
        self.rotation = rotation
        self.scale = scale

        self.base_matrix = base_matrix or glm.identity(glm.mat4)

        self._parent = parent
        if self._parent:
            self._parent.add_child(self)

        self._children = [] if children is None else children
        for child in self._children:
            child.parent = self

    # --------------------------------------#
    # region: Dirty Checking/Clearing Logic #
    # --------------------------------------#

    def _check_dirty(self):
        """
        Check if the transform is marked dirty or if the checkpoint values have changed.

        If the checkpoint have changed, then _set_dirty() is called.

        :return: True if the transform is dirty, False otherwise.
        """

        if (
            Transform.position.check_value_changed(self)
            or Transform.rotation.check_value_changed(self)
            or Transform.scale.check_value_changed(self)
        ):
            self._set_dirty()

        return self._dirty

    def _clear_dirty(self):
        """ Clear the dirty flag and checkpoint values. """
        self._dirty = False
        Transform.position.set_checkpoint(self)
        Transform.rotation.set_checkpoint(self)
        Transform.scale.set_checkpoint(self)

    def _set_dirty(self):
        """
        Mark this Transform as dirty, which will force a recalculation
        of the local and model space matrices the next time they are accessed.

        This method also marks all child transforms as dirty, ensuring that
        the entire downwards hierarchy is updated.
        """
        if self._dirty:
            return

        self._dirty = True
        for child in self._children:
            child._set_dirty()

    # -----------------------------------------#
    # endregion: Dirty Checking/Clearing Logic #
    # -----------------------------------------#

    # ------------------------------------------#
    # region: Parent/Child Hierarchy Management #
    # ------------------------------------------#

    @property
    def parent(self) -> Transform | None:
        """ :return: The parent transform, or `None` if there is no parent. """
        return self._parent

    @parent.setter
    def parent(self, value: Transform | None) -> None:
        """
        Set the parent transform.

        Also adds self to the parent's children (and removes self from old parent's children, if it exists)

        :param value: The new parent transform, or `None` to remove the parent.
        :raises ValueError: If the transform is set as its own parent.
        """
        if value is self:
            raise ValueError("A transform cannot be its own parent.")

        if self._parent is value:
            return

        if self._parent is not None:
            self._parent.remove_child(self)

        self._parent = value
        if self._parent is not None:
            self._parent.add_child(self)

    @parent.deleter
    def parent(self) -> None:
        """
        Remove the parent transform.
        """
        self.parent = None
        self._set_dirty()

    @property
    def children(self) -> list[Transform]:
        """
        Get the list of child transforms.

        :return: A list of child transforms.
        """
        return self._children

    @children.setter
    def children(self, value: list[Transform] | None) -> None:
        """
        Set the list of child transforms.

        :param value: A list of child transforms, or `None` to clear the children.
        """

        # using .parent property here will do the necessary bookkeeping, calling add/remove_child()
        for child in self._children:
            child.parent = None

        self._children = value or []
        for child in self._children:
            child.parent = self

    @children.deleter
    def children(self) -> None:
        """
        Remove all child transforms.
        """
        for child in self._children:
            child.parent = None
        self._children = []

    def add_child(self, child: Transform) -> None:
        """
        Add a child transform to this transform and marks it as dirty.

        :param child: The transform to add as a child.
        """
        if child not in self._children:
            self._children.append(child)

            child._parent = self
            child._set_dirty()

            self._sanity_check_hierarchy()

    def remove_child(self, child: Transform) -> None:
        """
        Remove a child transform from this transform and marks it as dirty.

        :param child: The transform to remove as a child.
        """
        if child in self._children:
            self._children.remove(child)

            child._parent = None
            child._set_dirty()

    def _sanity_check_hierarchy(self):
        """
        Check for circular references in the hierarchy and raise an error if found.
        """
        visited = set()
        current = self

        while current:
            if current in visited:
                raise ValueError("Circular reference detected in transform hierarchy.")
            visited.add(current)
            current = current._parent

    # ---------------------------------------------#
    # endregion: Parent/Child Hierarchy Management #
    # ---------------------------------------------#

    # -----------------------------------#
    # region: Matrix Properties/Updating #
    # -----------------------------------#

    @property
    def local_space_matrix(self) -> matrix44:
        """
        Get the local space transformation matrix.

        :return: The local space matrix as a `matrix44`.
        """
        if self._check_dirty():
            self.update_parent_matrices_recursively()
        return self._local_space_matrix

    @property
    def model_space_matrix(self) -> matrix44:
        """
        Get the model space transformation matrix.

        :return: The model space matrix as a `matrix44`.
        """
        if self._check_dirty():
            self.update_parent_matrices_recursively()
        return self._model_space_matrix

    def update_parent_matrices_recursively(self) -> None:
        """
        Update the model and local space matrices for this transform.

        First this function is called on the parent of this transform (and the parent of the parent... and so on).
        This is to ensure that the entire hierarchy from this transform upwards is up to date before calculating the space matrices for this transform.

        If this transform is not marked as dirty, it is skipped.
        (This also means that if a parent is already up to date, the recursive calls upwards stop there.)
        """

        if not self._dirty:
            return

        # Recurse up the parent-child hierarchy first
        if self._parent and self._parent._dirty:
            self._parent.update_parent_matrices_recursively()

        self._local_space_matrix = self.calculate_local_space_matrix()

        if self._parent:
            self._model_space_matrix = self._parent.model_space_matrix @ self._local_space_matrix
        else:
            self._model_space_matrix = deepcopy(self._local_space_matrix)

        self._clear_dirty()

    def calculate_local_space_matrix(self) -> matrix44:
        """
        Calculate the local space transformation matrix for this transform.

        The matrix is calculated using translation, rotation (in YXZ order),
        and scaling.

        :return: The local space matrix as a `matrix44`.
        """

        try:
            translation = glm.translate(self.position)
            rotation = (
                glm.rotate(self.rotation.y, math.Y_AXIS)
                @ glm.rotate(self.rotation.x, math.X_AXIS)
                @ glm.rotate(self.rotation.z, math.Z_AXIS)
            )
            scaling = glm.scale(self.scale)

            return self.base_matrix @ translation @ rotation @ scaling
        except Exception as e:
            print(f"Error calculating local space matrix: {e}")
            return glm.identity(glm.mat4)

    # --------------------------------------#
    # endregion: Matrix Properties/Updating #
    # --------------------------------------#

from __future__ import annotations

from pyglm import glm

from unit_animation_engine import math
from unit_animation_engine.math import float3, radians3, matrix44


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

    _position: float3
    """ The position of the transform in local space. """
    _rotation: radians3
    """ The rotation of the transform in local space (in radians). """
    _scale: float3
    """ The scale of the transform in local space. """

    _parent: Transform | None
    """ The parent transform, if any. """
    _children: list[Transform]
    """ A list of child transforms. """

    _local_space_matrix: matrix44
    """ The local space transformation matrix. """
    _model_space_matrix: matrix44
    """ The model space transformation matrix. """

    def _set_dirty(self):
        """
        Mark this Transform as dirty, which will force a recalculation
        of the local and model space matrices the next time they are accessed.

        This method also marks all child transforms as dirty, ensuring that
        the entire hierarchy is updated.
        """
        if self._dirty:
            # already dirty, avoid recursive calls
            return

        self._dirty = True
        for child in self._children:
            child._set_dirty()

    @property
    def position(self) -> float3:
        """
        Get the position of the transform in local space.

        :return: The position as a `float3` vector.
        """
        return self._position

    @position.setter
    def position(self, value: float3) -> None:
        """
        Set the position of the transform in local space.

        :param value: The new position as a `float3` vector.
        """
        if self._position == value:
            return

        self._position = value
        self._set_dirty()

    @property
    def rotation(self) -> radians3:
        """
        Get the rotation of the transform in local space.

        Note: The rotation is in YXZ order.

        :return: The rotation as a `radians3` vector.
        """
        return self._rotation

    @rotation.setter
    def rotation(self, value: radians3) -> None:
        """
        Set the rotation of the transform in local space.

        Note: The rotation is in YXZ order.

        :param value: The new rotation as a `radians3` vector.
        """
        if self._rotation == value:
            return

        self._rotation = value
        self._set_dirty()

    @property
    def scale(self) -> float3:
        """
        Get the scale of the transform in local space.

        :return: The scale as a `float3` vector.
        """
        return self._scale

    @scale.setter
    def scale(self, value: float3) -> None:
        """
        Set the scale of the transform in local space.

        :param value: The new scale as a `float3` vector.
        """
        if self._scale == value:
            return

        self._scale = value
        self._set_dirty()

    @property
    def parent(self) -> Transform | None:
        """
        Get the parent transform.

        :return: The parent transform, or `None` if there is no parent.
        """
        return self._parent

    @parent.setter
    def parent(self, value: Transform | None) -> None:
        """
        Set the parent transform.

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
        for child in self._children:
            # using .parent property here will do the necessary bookkeeping
            child.parent = None

        self._children = value if value is not None else []
        for child in self._children:
            # using .parent property here will do the necessary bookkeeping
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
        Add a child transform to this transform.

        :param child: The transform to add as a child.
        """
        if child not in self._children:
            self._children.append(child)

            # avoid recursive calls, access _parent directly
            child._parent = self
            child._set_dirty()

            self._sanity_check_hierarchy()

    def remove_child(self, child: Transform) -> None:
        """
        Remove a child transform from this transform.

        :param child: The transform to remove as a child.
        """
        if child in self._children:
            self._children.remove(child)

            # avoid recursive calls, access _parent directly
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

    @property
    def local_space_matrix(self) -> matrix44:
        """
        Get the local space transformation matrix.

        :return: The local space matrix as a `matrix44`.
        """
        if self._dirty:
            self.update_parent_matrices_recursively()
        return self._local_space_matrix

    @property
    def model_space_matrix(self) -> matrix44:
        """
        Get the model space transformation matrix.

        :return: The model space matrix as a `matrix44`.
        """
        if self._dirty:
            self.update_parent_matrices_recursively()
        return self._model_space_matrix

    def update_parent_matrices_recursively(self) -> None:
        """
        Update the transformation matrices recursively, starting from the root
        of the hierarchy. This ensures that all parent transforms are updated
        before updating this transform.
        """
        if not self._dirty:
            return  # Skip if this transform is already up-to-date

        # Ensure the parent is updated first
        if self._parent and self._parent._dirty:
            self._parent.update_parent_matrices_recursively()

        # Recalculate matrices for this transform
        self._local_space_matrix = self.calculate_local_space_matrix()
        self._model_space_matrix = self._local_space_matrix

        if self._parent:
            self._model_space_matrix = self._parent.model_space_matrix @ self._local_space_matrix

        # Mark this transform as clean
        self._dirty = False

    def calculate_local_space_matrix(self) -> matrix44:
        """
        Calculate the local space transformation matrix for this transform.

        The matrix is calculated using translation, rotation (in YXZ order),
        and scaling.

        :return: The local space matrix as a `matrix44`.
        """
        translation = glm.translate(self._position)
        rotation = (
            glm.rotate(self._rotation.y, math.Y_AXIS)
            @ glm.rotate(self._rotation.x, math.X_AXIS)
            @ glm.rotate(self._rotation.z, math.Z_AXIS)
        )
        scaling = glm.scale(self._scale)

        return translation @ rotation @ scaling

    def __init__(
        self,
        /,
        position: float3 = float3(0),
        rotation: radians3 = radians3(0),
        scale: float3 = float3(1),
        parent: Transform | None = None,
        children: list[Transform] = None,
    ):
        """
        Initialize a new Transform instance.

        :param position: The initial position as a `float3` vector. Defaults to (0, 0, 0).
        :param rotation: The initial rotation as a `radians3` vector. Defaults to (0, 0, 0).
        :param scale: The initial scale as a `float3` vector. Defaults to (1, 1, 1).
        :param parent: The parent transform, or `None` if there is no parent. Defaults to `None`.
        :param children: A list of child transforms, or `None` to start with no children. Defaults to `None`.
        """
        self._dirty = True

        self._position = position
        self._rotation = rotation
        self._scale = scale

        self._parent = parent
        if self._parent:
            self._parent.add_child(self)

        self._children = [] if children is None else children
        for child in self._children:
            child.parent = self

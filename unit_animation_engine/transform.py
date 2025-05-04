from __future__ import annotations

from copy import copy, deepcopy
from typing import TypeVar, Generic, Callable, Final

from pyglm import glm

from unit_animation_engine import math
from unit_animation_engine.math import float3, radians3, matrix44

T = TypeVar("T")

class WatchedValue(Generic[T]):
    NO_VALUE: Final = object()

    name: str
    storage_name: str
    default: T | None

    def __init__(self, default: T | None = None):
        self.default = default

    def __set_name__(self, owner, name):
        self.name = name
        self.storage_name = "_value_" + name

    def __get__(self, instance, owner=None):
        if instance is None:
            return self

        val = self._value(instance)
        if self._stored_value(instance) is WatchedValue.NO_VALUE:
            self._set_stored_value(instance, val)

        return val

    def __set__(self, instance: object, value):
        self._set_value(instance, value)

    def _value(self, instance: object) -> T | None:
        val = instance.__dict__.get(self.name)
        if val is None:
            new_val = deepcopy(self.default)
            instance.__dict__[self.name] = new_val
            return new_val
        else:
            return val

    def _set_value(self, instance: object, value: T) -> None:
        instance.__dict__[self.name] = deepcopy(value)

    def _stored_value(self, instance: object) -> T | WatchedValue.NO_VALUE:
        return instance.__dict__.get(self.storage_name, WatchedValue.NO_VALUE)

    def _set_stored_value(self, instance: object, value: T) -> None:
        instance.__dict__[self.storage_name] = deepcopy(value)

    def check_dirty(self, instance: object) -> bool:
        if self._stored_value(instance) is WatchedValue.NO_VALUE:
            return False
        return self._stored_value(instance) != self._value(instance)

    def clear_dirty(self, instance: object) -> None:
        self._set_stored_value(instance, WatchedValue.NO_VALUE)

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

    position = WatchedValue[float3]()
    """ The position of the transform in local space. """
    rotation = WatchedValue[float3]()
    """ The rotation of the transform in local space (in radians). """
    scale = WatchedValue[float3]()
    """ The scale of the transform in local space. """

    _parent: Transform | None
    """ The parent transform, if any. """
    _children: list[Transform]
    """ A list of child transforms. """

    _local_space_matrix: matrix44
    """ The local space transformation matrix. """
    _model_space_matrix: matrix44
    """ The model space transformation matrix. """

    def _check_dirty(self):
        """
        Check if the transform is dirty and needs to be recalculated.

        :param clear_watched_values: If True, clear the watched values after checking.
        :return: True if the transform is dirty, False otherwise.
        """

        if (
            Transform.position.check_dirty(self)
            or Transform.rotation.check_dirty(self)
            or Transform.scale.check_dirty(self)
        ):
            self._set_dirty()

        return self._dirty

    def _clear_dirty(self):
        """
        Clear the dirty flag and watched values.
        """
        self._dirty = False
        Transform.position.clear_dirty(self)
        Transform.rotation.clear_dirty(self)
        Transform.scale.clear_dirty(self)

    def _set_dirty(self):
        """
        Mark this Transform as dirty, which will force a recalculation
        of the local and model space matrices the next time they are accessed.

        This method also marks all child transforms as dirty, ensuring that
        the entire hierarchy is updated.
        """
        if self._dirty:
            return

        self._dirty = True
        for child in self._children:
            child._set_dirty()

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

        self._children = value or []
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
        Update the transformation matrices recursively, starting from the root
        of the hierarchy. This ensures that all parent transforms are updated
        before updating this transform.
        """

        if not self._dirty:
            return

        # Ensure the parent is updated first
        if self._parent and self._parent._dirty:
            self._parent.update_parent_matrices_recursively()

        # Recalculate matrices for this transform
        self._local_space_matrix = self.calculate_local_space_matrix()
        self._model_space_matrix = self._local_space_matrix

        if self._parent:
            # Combine with parent transform's matrix
            self._model_space_matrix = self._parent.model_space_matrix @ self._local_space_matrix

        # Mark this transform as clean
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

            return translation @ rotation @ scaling
        except Exception as e:
            print(f"Error calculating local space matrix: {e}")
            return glm.identity(glm.mat4)

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

        self.position = position
        self.rotation = rotation
        self.scale = scale

        self._parent = parent
        if self._parent:
            self._parent.add_child(self)

        self._children = [] if children is None else children
        for child in self._children:
            child.parent = self

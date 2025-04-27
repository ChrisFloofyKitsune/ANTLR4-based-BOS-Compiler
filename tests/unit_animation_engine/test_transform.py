import unittest

from pyglm import glm

from unit_animation_engine.math import float3, radians3, matrix44
from unit_animation_engine.transform import Transform


class TestTransform(unittest.TestCase):
    def test_initialization(self):
        transform = Transform()
        self.assertTrue(transform._dirty)
        self.assertEqual(transform.position, float3(0, 0, 0))
        self.assertEqual(transform.rotation, radians3(0, 0, 0))
        self.assertEqual(transform.scale, float3(1, 1, 1))
        self.assertIsNone(transform.parent)
        self.assertEqual(transform.children, [])

    def test_position_setter(self):
        transform = Transform()
        transform.position = float3(1, 2, 3)
        self.assertEqual(transform.position, float3(1, 2, 3))
        self.assertTrue(transform._dirty)

    def test_rotation_setter(self):
        transform = Transform()
        transform.rotation = radians3(0.1, 0.2, 0.3)
        self.assertEqual(transform.rotation, radians3(0.1, 0.2, 0.3))
        self.assertTrue(transform._dirty)

    def test_scale_setter(self):
        transform = Transform()
        transform.scale = float3(2, 2, 2)
        self.assertEqual(transform.scale, float3(2, 2, 2))
        self.assertTrue(transform._dirty)

    def test_parent_child_relationship(self):
        parent = Transform()
        child = Transform()
        child.parent = parent
        self.assertEqual(child.parent, parent)
        self.assertIn(child, parent.children)

        child.parent = None
        self.assertIsNone(child.parent)
        self.assertNotIn(child, parent.children)

    def test_add_remove_child(self):
        parent = Transform()
        child = Transform()
        parent.add_child(child)
        self.assertIn(child, parent.children)
        self.assertEqual(child.parent, parent)

        parent.remove_child(child)
        self.assertNotIn(child, parent.children)
        self.assertIsNone(child.parent)

    def test_local_space_matrix(self):
        transform = Transform(position=float3(1, 2, 3))
        self.assertEqual(glm.translate(float3(1, 2, 3)), transform.model_space_matrix)

    def test_model_space_matrix_with_parent(self):
        parent = Transform(position=float3(1, 0, 0))
        child = Transform(position=float3(0, 0, 1), parent=parent)
        self.assertEqual(glm.translate((1, 0, 1)), child.model_space_matrix)

        parent.scale = float3(2)
        self.assertEqual(float3(1, 0, 2), child.model_space_matrix[3].xyz)

        parent.rotation = radians3(0, glm.pi() / 2, 0)
        self.assertEqual(float3(3, 0, 0), glm.trunc(child.model_space_matrix[3].xyz))

    def test_self_parenting_raises_error(self):
        transform = Transform()
        with self.assertRaises(ValueError):
            transform.parent = transform

    def test_circular_hierarchy_raises_error(self):
        parent = Transform()
        child = Transform(parent=parent)
        ancestor = Transform(parent=child)
        with self.assertRaises(ValueError):
            parent.parent = ancestor

    def test_empty_children_list(self):
        transform = Transform(children=[Transform(), Transform()])
        transform.children = None
        self.assertEqual(transform.children, [])

    def test_duplicate_child_addition(self):
        parent = Transform()
        child = Transform()
        parent.add_child(child)
        parent.add_child(child)  # Add the same child again
        self.assertEqual(len(parent.children), 1)  # Ensure no duplicates

    def test_remove_non_existent_child(self):
        parent = Transform()
        child = Transform()
        parent.remove_child(child)  # Should not raise an error
        self.assertNotIn(child, parent.children)

    def test_no_unnecessary_dirty_flag(self):
        transform = Transform(position=float3(1, 2, 3))
        _ = transform.local_space_matrix # Access the matrix to set _dirty to False
        transform.position = float3(1, 2, 3)  # Set the same position
        self.assertFalse(transform._dirty)  # Should not be marked dirty

if __name__ == "__main__":
    unittest.main()

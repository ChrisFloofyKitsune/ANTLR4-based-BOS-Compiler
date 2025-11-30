from __future__ import annotations

import inspect
import types
from collections.abc import Sequence
from typing import (
    Annotated, Any, ClassVar, ForwardRef, Generic, TypeVar,
    get_args, get_origin, get_type_hints
)

import typing_extensions

RefType = TypeVar('RefType')


class IndexRef(Generic[RefType]):
    ref_type: ClassVar[type[Any] | ForwardRef]

    @staticmethod
    def _assign_forward_module(ref: ForwardRef) -> None:
        frame = inspect.currentframe()
        module = '__main__'
        if frame and frame.f_back:
            module = frame.f_back.f_globals.get('__module__', module)
        ref.__forward_module__ = module

    def __class_getitem__(cls, item: type[Any] | str) -> type[Any]:
        generic_alias = super().__class_getitem__(item)
        ref_target = get_args(generic_alias)[0]

        if isinstance(ref_target, ForwardRef):
            cls._assign_forward_module(ref_target)
            name = ref_target.__forward_arg__
        elif isinstance(ref_target, type):
            name = ref_target.__name__
        else:
            name = str(ref_target)

        return types.new_class(
            f'{cls.__name__}[{name}]',
            (generic_alias,),
            exec_body=lambda namespace: namespace.update(
                {'ref_type': ref_target, '__module__': cls.__module__}
            ),
        )

    @classmethod
    def _resolve_forward_ref(cls) -> None:
        ref_str = str(cls.ref_type)
        if isinstance(cls.ref_type, ForwardRef):
            cls.ref_type = typing_extensions.evaluate_forward_ref(cls.ref_type)

        if isinstance(cls.ref_type, type):
            return

        raise Exception(f'Could not resolve forward reference for IndexRef: {ref_str}')

    @classmethod
    def resolve(cls, target_obj: object, index: int) -> Any:
        cls._resolve_forward_ref()

        target_field = cls._find_target_field(type(target_obj))
        ref_collection = getattr(target_obj, target_field)
        return ref_collection[index]

    @classmethod
    def _find_target_field(cls, owner: type[Any]) -> str | None:
        type_hints = get_type_hints(owner)
        for field, hint in type_hints.items():
            origin = get_origin(hint)
            if origin is None or not issubclass(origin, Sequence):
                continue

            args = get_args(hint)
            if args and args[0] == cls.ref_type:
                return field

        return None

    @staticmethod
    def _strip_annotated(hint: Any) -> Any:
        if get_origin(hint) is Annotated:
            hint = get_args(hint)[0]
        return hint

    @staticmethod
    def get_from_field_annotation(obj: type[Any], field_name: str) -> type[IndexRef[Any]] | None:
        type_hints = get_type_hints(obj, include_extras=True)
        field_type = type_hints.get(field_name)
        if not field_type or get_origin(field_type) is not Annotated:
            return None

        for metadata in get_args(field_type)[1:]:
            if issubclass(metadata, IndexRef):
                return metadata

        return None


if __name__ == '__main__':
    class TestSource:
        my_field: Annotated[int, IndexRef['TestSource']]

        def __init__(self, idx: int):
            self.my_field = idx


    class TestContainer:
        sources: Annotated[list[Annotated[TestSource, 'junk string']], 'junk'] = [TestSource((i + 1) % 5) for i in range(5)]


    test_container = TestContainer()
    source_0 = test_container.sources[0]
    current: TestSource = source_0
    loops = 0

    ref_type = IndexRef.get_from_field_annotation(TestSource, 'my_field')
    print(ref_type)
    for _ in range(10):
        current = ref_type.resolve(test_container, current.my_field)
        if current is source_0:
            loops += 1

    assert loops == 2

import itertools
import struct
from typing import Final


class CobFile:
    COB_HEADER_STRUCT: Final[struct] = struct.Struct('<11L')
    """
    fields
    
    * version
    * function_count
    * piece_count
    * code_length
    * static_var_count
    * unused
    * function_code_ptrs_ptr
    * function_names_ptrs_ptr
    * piece_names_ptrs_ptr
    * code_ptr
    * strings_ptr
    """

    byte_data: bytearray

    static_var_count: int
    code: memoryview

    piece_names: list[str]

    function_names: list[str]
    function_ptrs: list[int]
    function_lengths: list[int]

    function_map: dict[str, int]

    name: str

    def __init__(self, data_source):
        self.byte_data = bytearray(data_source)

        (
            _version,
            function_count,
            piece_count,
            code_length,
            static_var_count,
            _unused,
            function_code_ptrs_ptr,
            function_names_ptrs_ptr,
            piece_names_ptrs_ptr,
            code_ptr,
            _strings_ptr,
        ) = CobFile.COB_HEADER_STRUCT.unpack_from(data_source, 0)

        self.static_var_count = static_var_count
        self.code = memoryview(self.byte_data)[code_ptr:code_ptr + (code_length * 4)].cast('L')

        def extract_strings(start_ptr: int, count: int):
            result = []
            for string_ptr in memoryview(self.byte_data[start_ptr:start_ptr + (count * 4)]).cast('L'):
                result.append(
                    self.byte_data[string_ptr:self.byte_data.find(b'\0', string_ptr)].decode('utf8')
                )
            return result

        self.function_ptrs = [
            *memoryview(self.byte_data[function_code_ptrs_ptr:function_code_ptrs_ptr + (function_count * 4)]).cast('L')
        ]
        self.function_lengths = [
            ptr_next - ptr for ptr, ptr_next in
            itertools.pairwise([*self.function_ptrs, code_ptr + code_length])
        ]

        self.function_names = extract_strings(function_names_ptrs_ptr, function_count)
        self.piece_names = extract_strings(piece_names_ptrs_ptr, piece_count)


if __name__ == '__main__':
    with open('./example_files/Units/legcom.cob', 'rb') as data:
        cob_file = CobFile(data.read())

    print(cob_file.__dict__)

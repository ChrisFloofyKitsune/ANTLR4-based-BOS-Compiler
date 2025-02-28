import struct
from array import array
from dataclasses import dataclass
from typing import ClassVar


@dataclass(kw_only=True)
class CobFile:
    COB_HEADER_STRUCT: ClassVar[struct] = struct.Struct('<11L')
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

    static_var_count: int
    code: array

    piece_names: list[str]
    function_map: dict[str, int]

    @property
    def function_names(self) -> list[str]:
        return list(self.function_map.keys())

    @property
    def function_ptrs(self) -> list[int]:
        return list(self.function_map.values())

    @property
    def function_lengths(self) -> list[int]:
        function_ptrs = self.function_ptrs
        return [end - start for start, end in zip(function_ptrs, function_ptrs[1:] + [len(self.code)])]

    def get_function_code(self, identifier: int | str) -> memoryview:
        if isinstance(identifier, str):
            try:
                start = self.function_map[identifier]
            except KeyError as err:
                raise ValueError(f"Function name '{identifier}' not found in function_map.") from err
        else:
            start = self.function_ptrs[identifier]

        length = self.function_lengths[self.function_ptrs.index(start)]
        return self.code[start:start + length]

    @classmethod
    def from_bytes(cls, data_source):
        byte_data = bytearray(data_source)

        (
            version,
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
        ) = cls.COB_HEADER_STRUCT.unpack_from(data_source, 0)
        
        if version != 4:
            raise ValueError(f"Unsupported COB version: {version}. Only version 4 is supported.")

        code = array('L', byte_data[code_ptr:code_ptr + (code_length * 4)])

        function_ptrs = [
            *memoryview(byte_data[function_code_ptrs_ptr:function_code_ptrs_ptr + (function_count * 4)]).cast('L')
        ]

        function_names = cls.extract_strings(byte_data, function_names_ptrs_ptr, function_count)
        piece_names = cls.extract_strings(byte_data, piece_names_ptrs_ptr, piece_count)

        function_map = dict(zip(function_names, function_ptrs))

        return cls(
            static_var_count=static_var_count,
            code=code,
            piece_names=piece_names,
            function_map=function_map
        )

    @staticmethod
    def extract_strings(byte_data: bytearray, start_ptr: int, count: int):
        result = []
        for string_ptr in memoryview(byte_data[start_ptr:start_ptr + (count * 4)]).cast('L'):
            result.append(
                byte_data[string_ptr:byte_data.find(b'\0', string_ptr)].decode('utf8')
            )
        return result

    def to_bytes(self) -> bytes:
        function_count = len(self.function_map)
        piece_count = len(self.piece_names)
        code_length_in_int32s = len(self.code)
        code_length_in_bytes = code_length_in_int32s * 4
        static_var_count = self.static_var_count

        code_ptr = self.COB_HEADER_STRUCT.size
        function_code_ptrs_ptr = code_ptr + code_length_in_bytes
        function_names_ptrs_ptr = function_code_ptrs_ptr + function_count * 4
        piece_names_ptrs_ptr = function_names_ptrs_ptr + function_count * 4
        strings_ptr = piece_names_ptrs_ptr + piece_count * 4

        function_ptrs = b''.join(struct.pack('<L', ptr) for ptr in self.function_ptrs)

        function_names = b''
        function_name_ptrs = b''
        for name in self.function_names:
            function_name_ptrs += struct.pack('<L', strings_ptr + len(function_names))
            function_names += name.encode('utf8') + b'\0'

        piece_name_ptrs = b''
        piece_names = b''
        for name in self.piece_names:
            piece_name_ptrs += struct.pack('<L', strings_ptr + len(function_names) + len(piece_names))
            piece_names += name.encode('utf8') + b'\0'

        code = self.code.tobytes()

        header = self.COB_HEADER_STRUCT.pack(
            4,
            function_count,
            piece_count,
            code_length_in_int32s,
            static_var_count,
            0,
            function_code_ptrs_ptr,
            function_names_ptrs_ptr,
            piece_names_ptrs_ptr,
            code_ptr,
            strings_ptr
        )

        return (
            header
            + code
            + function_ptrs + function_name_ptrs + piece_name_ptrs
            + function_names + piece_names
        )

    def save_to_file(self, file_path: str):
        with open(file_path, 'wb') as file:
            file.write(self.to_bytes())


if __name__ == '__main__':
    def _main():
        with open('./example_files/Units/legcom.cob', 'rb') as file:
            byte_data = file.read()
    
        cob_file = CobFile.from_bytes(byte_data)
        serialized_data = cob_file.to_bytes()
    
        with open('legcom_reserialized.cob', 'wb') as file:
            file.write(serialized_data)
    
        if byte_data != serialized_data:
            print("Byte data mismatch found:")
            for i, (original_byte, serialized_byte) in enumerate(zip(byte_data, serialized_data)):
                if original_byte != serialized_byte:
                    print(f"Byte {i}: original {original_byte} != serialized {serialized_byte}")
            if len(byte_data) != len(serialized_data):
                print(f"Length mismatch: original {len(byte_data)} != serialized {len(serialized_data)}")
        else:
            print("Byte data matches.")
    _main()
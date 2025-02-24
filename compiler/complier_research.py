import array

from cob.opcodes import OpCode
import bos.ast_nodes as nodes 

class Compiler:
    ...


def __main(file_node: nodes.File):
    
    
    
    
    code = array.array('L')
    code.append(OpCode.MOVE)
    print(code.tobytes())

if __name__ == '__main__':
    
    # with open('../bos/example_files/Units/legcom.bos'):
        
    
    __main()
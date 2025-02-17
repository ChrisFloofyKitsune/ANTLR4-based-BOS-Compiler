#pragma endian little
import std.mem;
import std.ptr;
import std.io;
import std.string;
import std.core;


// String stuff
using String = std::string::NullString;

struct StringPtr {
    String* val : u32;
} [[format("format_str_ptr")]];

fn format_str_ptr(ref StringPtr s_ptr) {
    return s_ptr.val;
};


enum CobOpCode : u32 {
    MOVE       = 0x10001000,
    TURN       = 0x10002000,
    SPIN       = 0x10003000,
    STOP_SPIN  = 0x10004000,
    SHOW       = 0x10005000,
    HIDE       = 0x10006000,
    CACHE      = 0x10007000,
    DONT_CACHE = 0x10008000,
    MOVE_NOW   = 0x1000B000,
    TURN_NOW   = 0x1000C000,
    SHADE      = 0x1000D000,
    DONT_SHADE = 0x1000E000,
    EMIT_SFX   = 0x1000F000,
    
    // Blocking operations
    WAIT_TURN  = 0x10011000,
    WAIT_MOVE  = 0x10012000,
    SLEEP      = 0x10013000,
    
    // Stack manipulation
    PUSH_CONSTANT    = 0x10021001,
    PUSH_LOCAL_VAR   = 0x10021002,
    PUSH_STATIC      = 0x10021004,
    CREATE_LOCAL_VAR = 0x10022000,
    POP_LOCAL_VAR    = 0x10023002,
    POP_STATIC       = 0x10023004,
    POP_STACK        = 0x10024000, ///< Not sure what this is supposed to do
    
    // Arithmetic operations
    ADD         = 0x10031000,
    SUB         = 0x10032000,
    MUL         = 0x10033000,
    DIV         = 0x10034000,
    MOD       = 0x10034001, ///< spring specific
    BITWISE_AND = 0x10035000,
    BITWISE_OR  = 0x10036000,
    BITWISE_XOR = 0x10037000,
    BITWISE_NOT = 0x10038000,
    
    // Native function calls
    RAND           = 0x10041000,
    GET_UNIT_VALUE = 0x10042000,
    GET            = 0x10043000,
    
    // Comparison
    SET_LESS             = 0x10051000,
    SET_LESS_OR_EQUAL    = 0x10052000,
    SET_GREATER          = 0x10053000,
    SET_GREATER_OR_EQUAL = 0x10054000,
    SET_EQUAL            = 0x10055000,
    SET_NOT_EQUAL        = 0x10056000,
    LOGICAL_AND          = 0x10057000,
    LOGICAL_OR           = 0x10058000,
    LOGICAL_XOR          = 0x10059000,
    LOGICAL_NOT          = 0x1005A000,
    
    // Flow control
    START           = 0x10061000,
    CALL            = 0x10062000, ///< converted when executed
    REAL_CALL       = 0x10062001, ///< spring custom
    LUA_CALL        = 0x10062002, ///< spring custom
    JUMP            = 0x10064000,
    RETURN          = 0x10065000,
    JUMP_NOT_EQUAL  = 0x10066000,
    SIGNAL          = 0x10067000,
    SET_SIGNAL_MASK = 0x10068000,
    
    // Piece destruction
    EXPLODE    = 0x10071000,
    PLAY_SOUND = 0x10072000,
    
    // Special functions
    SET    = 0x10082000,
    ATTACH = 0x10083000,
    DROP   = 0x10084000
};

fn get_operand_count(CobOpCode op_code) {
    match (op_code) {
        (
            CobOpCode::MOVE | CobOpCode::MOVE_NOW | CobOpCode::WAIT_MOVE |
            CobOpCode::TURN | CobOpCode::TURN_NOW | CobOpCode::WAIT_TURN |
            CobOpCode::SPIN | CobOpCode::STOP_SPIN |
            CobOpCode::CALL | CobOpCode::REAL_CALL | CobOpCode::LUA_CALL |
            CobOpCode::START
        ): return 2;
        
        (
            CobOpCode::SHADE | CobOpCode::DONT_SHADE |
            CobOpCode::CACHE | CobOpCode::DONT_CACHE |
            CobOpCode::HIDE | CobOpCode::SHOW |
            CobOpCode::EXPLODE |
            CobOpCode::PUSH_CONSTANT |
            CobOpCode::PUSH_STATIC | CobOpCode::POP_STATIC |
            CobOpCode::POP_LOCAL_VAR | CobOpCode::PUSH_LOCAL_VAR |
            CobOpCode::PLAY_SOUND | CobOpCode::EMIT_SFX |
            CobOpCode::JUMP_NOT_EQUAL | CobOpCode::JUMP
            
        ): return 1;
    }

    return 0;
};

struct CobInstruction {
    CobOpCode op_code;
    u32 operands[get_operand_count(op_code)];
} [[format_read("format_instruction")]];

fn axis_name(auto axis_num) {
    match (axis_num) {
        (0): return "X-axis";
        (1): return "Y-axis";
        (2): return "Z-axis";
    }
    return "huh?";
};

fn format_instruction(ref CobInstruction operation) {
    str output = std::string::to_string(operation.op_code);
    output = std::string::replace(output, "CobOpCode::", "");
    

    match (operation.op_code) {
        (
            CobOpCode::MOVE | CobOpCode::MOVE_NOW | CobOpCode::WAIT_MOVE |
            CobOpCode::TURN | CobOpCode::TURN_NOW | CobOpCode::WAIT_TURN |
            CobOpCode::SPIN | CobOpCode::STOP_SPIN
        ): 
            return std::format("{} \"{}\" {}", 
                output, 
                script.piece_names[operation.operands[0]].val, 
                axis_name(operation.operands[1])
            );
        
        (
            CobOpCode::SHADE | CobOpCode::DONT_SHADE |
            CobOpCode::CACHE | CobOpCode::DONT_CACHE |
            CobOpCode::HIDE | CobOpCode::SHOW |
            CobOpCode::EXPLODE
        ):
            return std::format("{} \"{}\"", output, script.piece_names[operation.operands[0]].val);
        
        (
            CobOpCode::CALL | CobOpCode::REAL_CALL | CobOpCode::LUA_CALL |
            CobOpCode::START
        ):
            return std::format("{} \"{}\" ({} args)", 
                output, 
                script.function_names[operation.operands[0]].val, 
                operation.operands[1]
            );
    }
    
    u8 operand_count = std::core::member_count(operation.operands);
    for (u8 i = 0, i < operand_count, i+=1) {
        output = output + " " + std::string::to_string(operation.operands[i]);
    }
    return output;
};



struct CobCode<auto start, auto until>  {
    CobInstruction instructions[while(!std::mem::reached(until))] @ start;
};


struct CobFunction {
    u32 index = std::core::array_index();
    u32 func_start = (parent.function_ptrs[index] * 4) + parent.code_start;
    u32 func_end = parent.code_end;

    if (index + 1 < std::core::member_count(parent.function_ptrs)) {
        func_end = parent.code_start + (parent.function_ptrs[index+1] * 4);
    }
    str name = parent.function_names[index].val [[export]];
    CobCode<func_start, func_end> function_code;
    
    std::print("{0:20}: {1:04X} - {2:04X} ({1:d} - {2:d})", name, func_start, func_end);
} [[format("format_cob_func")]];

fn format_cob_func(ref CobFunction func) {
    return std::format(
        "func {:20} size {}",
        func.name,
        std::string::to_string(std::core::member_count(func.function_code.instructions))
    );
};


struct CobScript {
    u32 version;
    u32 number_of_functions;
    u32 number_of_pieces;
    u32 total_script_length;
    u32 number_of_static_vars;
    
    padding[4];
    
    u32* function_ptrs[number_of_functions] : u32 [[inline]];
    StringPtr *function_names[number_of_functions] : u32 [[inline]];
    StringPtr *piece_names[number_of_pieces] : u32 [[inline]];
    
    u32 code_start = $ + 8;
    u32 code_end = code_end + total_script_length * 4;
    
    CobCode<code_start, code_end>* script_code : u32;
    String *script_strings[while(!std::mem::eof())] : u32 [[inline]];
    
    CobFunction functions[number_of_functions] [[no_unique_address]];
};

CobScript script @ 0x00;
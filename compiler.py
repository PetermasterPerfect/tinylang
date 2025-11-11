from llvmlite import ir

class FunCompileState:
    voidptr_ty = ir.IntType(8).as_pointer()
    format_func_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
    printf = None
    scanf = None

    def create_string_formats(self, fmt_str, name="format"):
        fmt_bytes = fmt_str.encode("utf8") + b"\00"
        c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt_bytes)), bytearray(fmt_bytes))
        gv = ir.GlobalVariable(self.module, c_fmt.type, name=name)
        gv.linkage = 'internal'
        gv.global_constant = True
        gv.initializer = c_fmt
        return gv


    def __init__(self, ast_node, module):
        self.module = module
        self.double = ir.DoubleType()
        func_type = ir.FunctionType(self.double, (self.double for x in ast_node.args))
        self.func = ir.Function(self.module, func_type, ast_node.name)
        self.args = dict()
        self.vars = dict()
        self.block = self.func.append_basic_block(name='entry')
        self.builder = ir.IRBuilder(self.block)

        if FunCompileState.printf is None:
            FunCompileState.global_printf_fmt = self.create_string_formats("%lf\n", "printf_fmt")
            FunCompileState.global_scanf_fmt  = self.create_string_formats("%lf", "scanf_fmt")
            FunCompileState.printf = ir.Function(self.module, FunCompileState.format_func_ty, name="printf")
            FunCompileState.scanf = ir.Function(self.module, FunCompileState.format_func_ty, name="scanf")

        for i in range(len(ast_node.args)):
            self.args[ast_node.args[i]] = self.builder.alloca(self.double, 8, ast_node.args[i])
            self.builder.store(self.func.args[i], self.args[ast_node.args[i]])

        for var in ast_node.vars:
            if var in ast_node.args:
                raise Exception('Same variables name already defined in functions arguments')

            self.vars[var] = self.builder.alloca(self.double, 8, var)


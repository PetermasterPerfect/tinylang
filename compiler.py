from llvmlite import ir

class FunCompileState:
    def __init__(self, ast_node, module):
        self.module = module
        self.double = ir.DoubleType()
        func_type = ir.FunctionType(self.double, (self.double for x in ast_node.args))
        self.func = ir.Function(self.module, func_type, ast_node.name)
        self.args = dict()
        self.vars = dict()
        self.block = self.func.append_basic_block(name='entry')
        self.builder = ir.IRBuilder(self.block)
        #breakpoint()
        for i in range(len(ast_node.args)):
            self.args[ast_node.args[i]] = self.builder.alloca(self.double, 8, ast_node.args[i])
            self.builder.store(self.func.args[i], self.args[ast_node.args[i]])

        for var in ast_node.vars:
            if var in ast_node.args:
                raise Exception('Same variables name already defined in functions arguments')

            self.vars[var] = self.builder.alloca(self.double, 8, var)


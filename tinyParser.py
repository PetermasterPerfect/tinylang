# Generated from tiny.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,23,157,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,1,1,1,1,1,3,
        1,28,8,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,38,8,2,1,2,5,2,41,8,
        2,10,2,12,2,44,9,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,5,3,54,8,3,10,
        3,12,3,57,9,3,1,4,1,4,1,4,5,4,62,8,4,10,4,12,4,65,9,4,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,82,8,5,10,
        5,12,5,85,9,5,1,5,1,5,3,5,89,8,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,97,
        8,5,10,5,12,5,100,9,5,1,5,1,5,3,5,104,8,5,1,6,1,6,1,6,5,6,109,8,
        6,10,6,12,6,112,9,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        3,7,125,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,5,7,145,8,7,10,7,12,7,148,9,7,1,8,1,8,1,8,3,
        8,153,8,8,1,8,1,8,1,8,0,1,14,9,0,2,4,6,8,10,12,14,16,0,0,171,0,21,
        1,0,0,0,2,24,1,0,0,0,4,31,1,0,0,0,6,50,1,0,0,0,8,58,1,0,0,0,10,103,
        1,0,0,0,12,105,1,0,0,0,14,124,1,0,0,0,16,149,1,0,0,0,18,20,3,4,2,
        0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,1,1,
        0,0,0,23,21,1,0,0,0,24,25,5,21,0,0,25,27,5,1,0,0,26,28,3,6,3,0,27,
        26,1,0,0,0,27,28,1,0,0,0,28,29,1,0,0,0,29,30,5,2,0,0,30,3,1,0,0,
        0,31,32,3,2,1,0,32,37,5,3,0,0,33,34,5,14,0,0,34,35,3,6,3,0,35,36,
        5,20,0,0,36,38,1,0,0,0,37,33,1,0,0,0,37,38,1,0,0,0,38,42,1,0,0,0,
        39,41,3,10,5,0,40,39,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,
        0,0,0,43,45,1,0,0,0,44,42,1,0,0,0,45,46,5,13,0,0,46,47,3,14,7,0,
        47,48,5,20,0,0,48,49,5,4,0,0,49,5,1,0,0,0,50,55,5,21,0,0,51,52,5,
        5,0,0,52,54,5,21,0,0,53,51,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,
        56,1,0,0,0,56,7,1,0,0,0,57,55,1,0,0,0,58,63,3,14,7,0,59,60,5,5,0,
        0,60,62,3,14,7,0,61,59,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,
        1,0,0,0,64,9,1,0,0,0,65,63,1,0,0,0,66,67,5,21,0,0,67,68,5,6,0,0,
        68,69,3,14,7,0,69,70,5,20,0,0,70,104,1,0,0,0,71,72,5,15,0,0,72,73,
        3,14,7,0,73,74,5,20,0,0,74,104,1,0,0,0,75,76,5,17,0,0,76,77,5,1,
        0,0,77,78,3,14,7,0,78,79,5,2,0,0,79,83,5,3,0,0,80,82,3,10,5,0,81,
        80,1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,86,1,0,0,
        0,85,83,1,0,0,0,86,88,5,4,0,0,87,89,3,12,6,0,88,87,1,0,0,0,88,89,
        1,0,0,0,89,104,1,0,0,0,90,91,5,19,0,0,91,92,5,1,0,0,92,93,3,14,7,
        0,93,94,5,2,0,0,94,98,5,3,0,0,95,97,3,10,5,0,96,95,1,0,0,0,97,100,
        1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,101,1,0,0,0,100,98,1,0,0,
        0,101,102,5,4,0,0,102,104,1,0,0,0,103,66,1,0,0,0,103,71,1,0,0,0,
        103,75,1,0,0,0,103,90,1,0,0,0,104,11,1,0,0,0,105,106,5,18,0,0,106,
        110,5,3,0,0,107,109,3,10,5,0,108,107,1,0,0,0,109,112,1,0,0,0,110,
        108,1,0,0,0,110,111,1,0,0,0,111,113,1,0,0,0,112,110,1,0,0,0,113,
        114,5,4,0,0,114,13,1,0,0,0,115,116,6,7,-1,0,116,125,5,22,0,0,117,
        125,5,21,0,0,118,119,5,1,0,0,119,120,3,14,7,0,120,121,5,2,0,0,121,
        125,1,0,0,0,122,125,5,16,0,0,123,125,3,16,8,0,124,115,1,0,0,0,124,
        117,1,0,0,0,124,118,1,0,0,0,124,122,1,0,0,0,124,123,1,0,0,0,125,
        146,1,0,0,0,126,127,10,9,0,0,127,128,5,9,0,0,128,145,3,14,7,10,129,
        130,10,8,0,0,130,131,5,10,0,0,131,145,3,14,7,9,132,133,10,7,0,0,
        133,134,5,7,0,0,134,145,3,14,7,8,135,136,10,6,0,0,136,137,5,8,0,
        0,137,145,3,14,7,7,138,139,10,5,0,0,139,140,5,12,0,0,140,145,3,14,
        7,6,141,142,10,4,0,0,142,143,5,11,0,0,143,145,3,14,7,5,144,126,1,
        0,0,0,144,129,1,0,0,0,144,132,1,0,0,0,144,135,1,0,0,0,144,138,1,
        0,0,0,144,141,1,0,0,0,145,148,1,0,0,0,146,144,1,0,0,0,146,147,1,
        0,0,0,147,15,1,0,0,0,148,146,1,0,0,0,149,150,5,21,0,0,150,152,5,
        1,0,0,151,153,3,8,4,0,152,151,1,0,0,0,152,153,1,0,0,0,153,154,1,
        0,0,0,154,155,5,2,0,0,155,17,1,0,0,0,15,21,27,37,42,55,63,83,88,
        98,103,110,124,144,146,152
    ]

class tinyParser ( Parser ):

    grammarFileName = "tiny.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "','", "'='", 
                     "'+'", "'-'", "'*'", "'/'", "'=='", "'>'", "'return'", 
                     "'var'", "'output'", "'input'", "'if'", "'else'", "'while'", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ADD", "SUB", 
                      "MUL", "DIV", "EQ", "GR", "RETURN", "VAR", "OUTPUT", 
                      "INPUT", "IF", "ELSE", "WHILE", "SEMI", "ID", "INT", 
                      "WS" ]

    RULE_program = 0
    RULE_fun_head = 1
    RULE_fun = 2
    RULE_id_list = 3
    RULE_exp_list = 4
    RULE_stm = 5
    RULE_else = 6
    RULE_exp = 7
    RULE_fun_call = 8

    ruleNames =  [ "program", "fun_head", "fun", "id_list", "exp_list", 
                   "stm", "else", "exp", "fun_call" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    ADD=7
    SUB=8
    MUL=9
    DIV=10
    EQ=11
    GR=12
    RETURN=13
    VAR=14
    OUTPUT=15
    INPUT=16
    IF=17
    ELSE=18
    WHILE=19
    SEMI=20
    ID=21
    INT=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fun(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tinyParser.FunContext)
            else:
                return self.getTypedRuleContext(tinyParser.FunContext,i)


        def getRuleIndex(self):
            return tinyParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = tinyParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 18
                self.fun()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fun_headContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(tinyParser.ID, 0)

        def id_list(self):
            return self.getTypedRuleContext(tinyParser.Id_listContext,0)


        def getRuleIndex(self):
            return tinyParser.RULE_fun_head

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFun_head" ):
                return visitor.visitFun_head(self)
            else:
                return visitor.visitChildren(self)




    def fun_head(self):

        localctx = tinyParser.Fun_headContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_fun_head)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(tinyParser.ID)
            self.state = 25
            self.match(tinyParser.T__0)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 26
                self.id_list()


            self.state = 29
            self.match(tinyParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fun_head(self):
            return self.getTypedRuleContext(tinyParser.Fun_headContext,0)


        def RETURN(self):
            return self.getToken(tinyParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(tinyParser.ExpContext,0)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(tinyParser.SEMI)
            else:
                return self.getToken(tinyParser.SEMI, i)

        def VAR(self):
            return self.getToken(tinyParser.VAR, 0)

        def id_list(self):
            return self.getTypedRuleContext(tinyParser.Id_listContext,0)


        def stm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tinyParser.StmContext)
            else:
                return self.getTypedRuleContext(tinyParser.StmContext,i)


        def getRuleIndex(self):
            return tinyParser.RULE_fun

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFun" ):
                return visitor.visitFun(self)
            else:
                return visitor.visitChildren(self)




    def fun(self):

        localctx = tinyParser.FunContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_fun)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.fun_head()
            self.state = 32
            self.match(tinyParser.T__2)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 33
                self.match(tinyParser.VAR)
                self.state = 34
                self.id_list()
                self.state = 35
                self.match(tinyParser.SEMI)


            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2785280) != 0):
                self.state = 39
                self.stm()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
            self.match(tinyParser.RETURN)
            self.state = 46
            self.exp(0)
            self.state = 47
            self.match(tinyParser.SEMI)
            self.state = 48
            self.match(tinyParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(tinyParser.ID)
            else:
                return self.getToken(tinyParser.ID, i)

        def getRuleIndex(self):
            return tinyParser.RULE_id_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




    def id_list(self):

        localctx = tinyParser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_id_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(tinyParser.ID)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 51
                self.match(tinyParser.T__4)
                self.state = 52
                self.match(tinyParser.ID)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tinyParser.ExpContext)
            else:
                return self.getTypedRuleContext(tinyParser.ExpContext,i)


        def getRuleIndex(self):
            return tinyParser.RULE_exp_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_list" ):
                return visitor.visitExp_list(self)
            else:
                return visitor.visitChildren(self)




    def exp_list(self):

        localctx = tinyParser.Exp_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_exp_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.exp(0)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 59
                self.match(tinyParser.T__4)
                self.state = 60
                self.exp(0)
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(tinyParser.ID, 0)

        def exp(self):
            return self.getTypedRuleContext(tinyParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(tinyParser.SEMI, 0)

        def OUTPUT(self):
            return self.getToken(tinyParser.OUTPUT, 0)

        def IF(self):
            return self.getToken(tinyParser.IF, 0)

        def stm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tinyParser.StmContext)
            else:
                return self.getTypedRuleContext(tinyParser.StmContext,i)


        def else_(self):
            return self.getTypedRuleContext(tinyParser.ElseContext,0)


        def WHILE(self):
            return self.getToken(tinyParser.WHILE, 0)

        def getRuleIndex(self):
            return tinyParser.RULE_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStm" ):
                return visitor.visitStm(self)
            else:
                return visitor.visitChildren(self)




    def stm(self):

        localctx = tinyParser.StmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_stm)
        self._la = 0 # Token type
        try:
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.match(tinyParser.ID)
                self.state = 67
                self.match(tinyParser.T__5)
                self.state = 68
                self.exp(0)
                self.state = 69
                self.match(tinyParser.SEMI)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.match(tinyParser.OUTPUT)
                self.state = 72
                self.exp(0)
                self.state = 73
                self.match(tinyParser.SEMI)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self.match(tinyParser.IF)
                self.state = 76
                self.match(tinyParser.T__0)
                self.state = 77
                self.exp(0)
                self.state = 78
                self.match(tinyParser.T__1)
                self.state = 79
                self.match(tinyParser.T__2)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2785280) != 0):
                    self.state = 80
                    self.stm()
                    self.state = 85
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 86
                self.match(tinyParser.T__3)
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==18:
                    self.state = 87
                    self.else_()


                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 90
                self.match(tinyParser.WHILE)
                self.state = 91
                self.match(tinyParser.T__0)
                self.state = 92
                self.exp(0)
                self.state = 93
                self.match(tinyParser.T__1)
                self.state = 94
                self.match(tinyParser.T__2)
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2785280) != 0):
                    self.state = 95
                    self.stm()
                    self.state = 100
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 101
                self.match(tinyParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(tinyParser.ELSE, 0)

        def stm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tinyParser.StmContext)
            else:
                return self.getTypedRuleContext(tinyParser.StmContext,i)


        def getRuleIndex(self):
            return tinyParser.RULE_else

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse" ):
                return visitor.visitElse(self)
            else:
                return visitor.visitChildren(self)




    def else_(self):

        localctx = tinyParser.ElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_else)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(tinyParser.ELSE)
            self.state = 106
            self.match(tinyParser.T__2)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2785280) != 0):
                self.state = 107
                self.stm()
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 113
            self.match(tinyParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(tinyParser.INT, 0)

        def ID(self):
            return self.getToken(tinyParser.ID, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tinyParser.ExpContext)
            else:
                return self.getTypedRuleContext(tinyParser.ExpContext,i)


        def INPUT(self):
            return self.getToken(tinyParser.INPUT, 0)

        def fun_call(self):
            return self.getTypedRuleContext(tinyParser.Fun_callContext,0)


        def MUL(self):
            return self.getToken(tinyParser.MUL, 0)

        def DIV(self):
            return self.getToken(tinyParser.DIV, 0)

        def ADD(self):
            return self.getToken(tinyParser.ADD, 0)

        def SUB(self):
            return self.getToken(tinyParser.SUB, 0)

        def GR(self):
            return self.getToken(tinyParser.GR, 0)

        def EQ(self):
            return self.getToken(tinyParser.EQ, 0)

        def getRuleIndex(self):
            return tinyParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = tinyParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 116
                self.match(tinyParser.INT)
                pass

            elif la_ == 2:
                self.state = 117
                self.match(tinyParser.ID)
                pass

            elif la_ == 3:
                self.state = 118
                self.match(tinyParser.T__0)
                self.state = 119
                self.exp(0)
                self.state = 120
                self.match(tinyParser.T__1)
                pass

            elif la_ == 4:
                self.state = 122
                self.match(tinyParser.INPUT)
                pass

            elif la_ == 5:
                self.state = 123
                self.fun_call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 146
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 144
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = tinyParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 126
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 127
                        self.match(tinyParser.MUL)
                        self.state = 128
                        self.exp(10)
                        pass

                    elif la_ == 2:
                        localctx = tinyParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 129
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 130
                        self.match(tinyParser.DIV)
                        self.state = 131
                        self.exp(9)
                        pass

                    elif la_ == 3:
                        localctx = tinyParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 132
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 133
                        self.match(tinyParser.ADD)
                        self.state = 134
                        self.exp(8)
                        pass

                    elif la_ == 4:
                        localctx = tinyParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 135
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 136
                        self.match(tinyParser.SUB)
                        self.state = 137
                        self.exp(7)
                        pass

                    elif la_ == 5:
                        localctx = tinyParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 138
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 139
                        self.match(tinyParser.GR)
                        self.state = 140
                        self.exp(6)
                        pass

                    elif la_ == 6:
                        localctx = tinyParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 141
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 142
                        self.match(tinyParser.EQ)
                        self.state = 143
                        self.exp(5)
                        pass

             
                self.state = 148
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Fun_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(tinyParser.ID, 0)

        def exp_list(self):
            return self.getTypedRuleContext(tinyParser.Exp_listContext,0)


        def getRuleIndex(self):
            return tinyParser.RULE_fun_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFun_call" ):
                return visitor.visitFun_call(self)
            else:
                return visitor.visitChildren(self)




    def fun_call(self):

        localctx = tinyParser.Fun_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_fun_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(tinyParser.ID)
            self.state = 150
            self.match(tinyParser.T__0)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 6356994) != 0):
                self.state = 151
                self.exp_list()


            self.state = 154
            self.match(tinyParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.exp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         





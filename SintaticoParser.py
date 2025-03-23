# Generated from Sintatico.g4 by ANTLR 4.13.1
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
        4,1,31,61,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,
        1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,3,2,51,8,2,3,2,53,8,2,1,3,1,3,1,3,1,3,3,3,59,8,
        3,1,3,0,0,4,0,2,4,6,0,3,1,0,15,16,1,0,23,25,1,0,17,22,70,0,8,1,0,
        0,0,2,11,1,0,0,0,4,52,1,0,0,0,6,58,1,0,0,0,8,9,3,2,1,0,9,10,5,0,
        0,1,10,1,1,0,0,0,11,12,5,1,0,0,12,13,3,6,3,0,13,14,3,6,3,0,14,15,
        3,4,2,0,15,16,5,2,0,0,16,3,1,0,0,0,17,53,5,3,0,0,18,53,5,4,0,0,19,
        53,5,5,0,0,20,53,5,6,0,0,21,53,5,7,0,0,22,53,5,9,0,0,23,53,5,8,0,
        0,24,53,5,10,0,0,25,53,5,11,0,0,26,27,5,12,0,0,27,28,5,13,0,0,28,
        29,7,0,0,0,29,30,5,27,0,0,30,31,5,1,0,0,31,32,5,10,0,0,32,33,5,2,
        0,0,33,34,5,28,0,0,34,35,5,10,0,0,35,36,7,1,0,0,36,53,5,26,0,0,37,
        38,5,14,0,0,38,39,5,10,0,0,39,40,7,2,0,0,40,41,5,26,0,0,41,42,5,
        28,0,0,42,43,5,10,0,0,43,44,7,1,0,0,44,50,5,26,0,0,45,46,5,29,0,
        0,46,47,5,28,0,0,47,48,5,10,0,0,48,49,7,1,0,0,49,51,5,26,0,0,50,
        45,1,0,0,0,50,51,1,0,0,0,51,53,1,0,0,0,52,17,1,0,0,0,52,18,1,0,0,
        0,52,19,1,0,0,0,52,20,1,0,0,0,52,21,1,0,0,0,52,22,1,0,0,0,52,23,
        1,0,0,0,52,24,1,0,0,0,52,25,1,0,0,0,52,26,1,0,0,0,52,37,1,0,0,0,
        53,5,1,0,0,0,54,59,5,26,0,0,55,59,3,2,1,0,56,59,5,10,0,0,57,59,5,
        30,0,0,58,54,1,0,0,0,58,55,1,0,0,0,58,56,1,0,0,0,58,57,1,0,0,0,59,
        7,1,0,0,0,3,50,52,58
    ]

class SintaticoParser ( Parser ):

    grammarFileName = "Sintatico.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'+'", "'-'", "'*'", "'/'", 
                     "'|'", "'%'", "'^'", "'MEM'", "'RES'", "'for'", "'i'", 
                     "'if'", "'in'", "'not in'", "'=='", "'<'", "'>'", "'<='", 
                     "'>='", "'!='", "'='", "'+='", "'-='", "<INVALID>", 
                     "'range'", "':'", "'else'", "'$'" ]

    symbolicNames = [ "<INVALID>", "LPAREN", "RPAREN", "PLUS", "MINUS", 
                      "MULTIPLY", "DIVIDE", "MODULO", "PERCENT", "POWER", 
                      "MEM", "RES", "FOR", "I", "IF", "IN", "NOT_IN", "EQUALS", 
                      "LESS_THAN", "GREATER_THAN", "LESS_THAN_OR_EQUAL", 
                      "GREATER_THAN_OR_EQUAL", "NOT_EQUALS", "ASSIGN", "INCREMENT", 
                      "DECREMENT", "NUM", "RANGE", "DOISPONTOS", "ELSE", 
                      "VAZIO", "WS" ]

    RULE_program = 0
    RULE_expression = 1
    RULE_operando = 2
    RULE_op = 3

    ruleNames =  [ "program", "expression", "operando", "op" ]

    EOF = Token.EOF
    LPAREN=1
    RPAREN=2
    PLUS=3
    MINUS=4
    MULTIPLY=5
    DIVIDE=6
    MODULO=7
    PERCENT=8
    POWER=9
    MEM=10
    RES=11
    FOR=12
    I=13
    IF=14
    IN=15
    NOT_IN=16
    EQUALS=17
    LESS_THAN=18
    GREATER_THAN=19
    LESS_THAN_OR_EQUAL=20
    GREATER_THAN_OR_EQUAL=21
    NOT_EQUALS=22
    ASSIGN=23
    INCREMENT=24
    DECREMENT=25
    NUM=26
    RANGE=27
    DOISPONTOS=28
    ELSE=29
    VAZIO=30
    WS=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SintaticoParser.ExpressionContext,0)


        def EOF(self):
            return self.getToken(SintaticoParser.EOF, 0)

        def getRuleIndex(self):
            return SintaticoParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = SintaticoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.expression()
            self.state = 9
            self.match(SintaticoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(SintaticoParser.LPAREN, 0)

        def op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SintaticoParser.OpContext)
            else:
                return self.getTypedRuleContext(SintaticoParser.OpContext,i)


        def operando(self):
            return self.getTypedRuleContext(SintaticoParser.OperandoContext,0)


        def RPAREN(self):
            return self.getToken(SintaticoParser.RPAREN, 0)

        def getRuleIndex(self):
            return SintaticoParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = SintaticoParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.match(SintaticoParser.LPAREN)
            self.state = 12
            self.op()
            self.state = 13
            self.op()
            self.state = 14
            self.operando()
            self.state = 15
            self.match(SintaticoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(SintaticoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(SintaticoParser.MINUS, 0)

        def MULTIPLY(self):
            return self.getToken(SintaticoParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(SintaticoParser.DIVIDE, 0)

        def MODULO(self):
            return self.getToken(SintaticoParser.MODULO, 0)

        def POWER(self):
            return self.getToken(SintaticoParser.POWER, 0)

        def PERCENT(self):
            return self.getToken(SintaticoParser.PERCENT, 0)

        def MEM(self, i:int=None):
            if i is None:
                return self.getTokens(SintaticoParser.MEM)
            else:
                return self.getToken(SintaticoParser.MEM, i)

        def RES(self):
            return self.getToken(SintaticoParser.RES, 0)

        def FOR(self):
            return self.getToken(SintaticoParser.FOR, 0)

        def I(self):
            return self.getToken(SintaticoParser.I, 0)

        def RANGE(self):
            return self.getToken(SintaticoParser.RANGE, 0)

        def LPAREN(self):
            return self.getToken(SintaticoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(SintaticoParser.RPAREN, 0)

        def DOISPONTOS(self, i:int=None):
            if i is None:
                return self.getTokens(SintaticoParser.DOISPONTOS)
            else:
                return self.getToken(SintaticoParser.DOISPONTOS, i)

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(SintaticoParser.NUM)
            else:
                return self.getToken(SintaticoParser.NUM, i)

        def IN(self):
            return self.getToken(SintaticoParser.IN, 0)

        def NOT_IN(self):
            return self.getToken(SintaticoParser.NOT_IN, 0)

        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(SintaticoParser.ASSIGN)
            else:
                return self.getToken(SintaticoParser.ASSIGN, i)

        def INCREMENT(self, i:int=None):
            if i is None:
                return self.getTokens(SintaticoParser.INCREMENT)
            else:
                return self.getToken(SintaticoParser.INCREMENT, i)

        def DECREMENT(self, i:int=None):
            if i is None:
                return self.getTokens(SintaticoParser.DECREMENT)
            else:
                return self.getToken(SintaticoParser.DECREMENT, i)

        def IF(self):
            return self.getToken(SintaticoParser.IF, 0)

        def EQUALS(self):
            return self.getToken(SintaticoParser.EQUALS, 0)

        def LESS_THAN(self):
            return self.getToken(SintaticoParser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(SintaticoParser.GREATER_THAN, 0)

        def LESS_THAN_OR_EQUAL(self):
            return self.getToken(SintaticoParser.LESS_THAN_OR_EQUAL, 0)

        def GREATER_THAN_OR_EQUAL(self):
            return self.getToken(SintaticoParser.GREATER_THAN_OR_EQUAL, 0)

        def NOT_EQUALS(self):
            return self.getToken(SintaticoParser.NOT_EQUALS, 0)

        def ELSE(self):
            return self.getToken(SintaticoParser.ELSE, 0)

        def getRuleIndex(self):
            return SintaticoParser.RULE_operando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperando" ):
                listener.enterOperando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperando" ):
                listener.exitOperando(self)




    def operando(self):

        localctx = SintaticoParser.OperandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_operando)
        self._la = 0 # Token type
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.match(SintaticoParser.PLUS)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.match(SintaticoParser.MINUS)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 19
                self.match(SintaticoParser.MULTIPLY)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 20
                self.match(SintaticoParser.DIVIDE)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 5)
                self.state = 21
                self.match(SintaticoParser.MODULO)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 6)
                self.state = 22
                self.match(SintaticoParser.POWER)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 7)
                self.state = 23
                self.match(SintaticoParser.PERCENT)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 8)
                self.state = 24
                self.match(SintaticoParser.MEM)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 9)
                self.state = 25
                self.match(SintaticoParser.RES)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 10)
                self.state = 26
                self.match(SintaticoParser.FOR)
                self.state = 27
                self.match(SintaticoParser.I)
                self.state = 28
                _la = self._input.LA(1)
                if not(_la==15 or _la==16):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 29
                self.match(SintaticoParser.RANGE)
                self.state = 30
                self.match(SintaticoParser.LPAREN)
                self.state = 31
                self.match(SintaticoParser.MEM)
                self.state = 32
                self.match(SintaticoParser.RPAREN)
                self.state = 33
                self.match(SintaticoParser.DOISPONTOS)
                self.state = 34
                self.match(SintaticoParser.MEM)
                self.state = 35
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 36
                self.match(SintaticoParser.NUM)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 11)
                self.state = 37
                self.match(SintaticoParser.IF)
                self.state = 38
                self.match(SintaticoParser.MEM)
                self.state = 39
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8257536) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 40
                self.match(SintaticoParser.NUM)
                self.state = 41
                self.match(SintaticoParser.DOISPONTOS)
                self.state = 42
                self.match(SintaticoParser.MEM)
                self.state = 43
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 44
                self.match(SintaticoParser.NUM)
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==29:
                    self.state = 45
                    self.match(SintaticoParser.ELSE)
                    self.state = 46
                    self.match(SintaticoParser.DOISPONTOS)
                    self.state = 47
                    self.match(SintaticoParser.MEM)
                    self.state = 48
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 49
                    self.match(SintaticoParser.NUM)


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


    class OpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(SintaticoParser.NUM, 0)

        def expression(self):
            return self.getTypedRuleContext(SintaticoParser.ExpressionContext,0)


        def MEM(self):
            return self.getToken(SintaticoParser.MEM, 0)

        def VAZIO(self):
            return self.getToken(SintaticoParser.VAZIO, 0)

        def getRuleIndex(self):
            return SintaticoParser.RULE_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp" ):
                listener.enterOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp" ):
                listener.exitOp(self)




    def op(self):

        localctx = SintaticoParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_op)
        try:
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.match(SintaticoParser.NUM)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.expression()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.match(SintaticoParser.MEM)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self.match(SintaticoParser.VAZIO)
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






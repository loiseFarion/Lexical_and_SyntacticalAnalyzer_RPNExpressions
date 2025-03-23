# Generated from Sintatico.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SintaticoParser import SintaticoParser
else:
    from SintaticoParser import SintaticoParser

# This class defines a complete listener for a parse tree produced by SintaticoParser.
class SintaticoListener(ParseTreeListener):

    # Enter a parse tree produced by SintaticoParser#program.
    def enterProgram(self, ctx:SintaticoParser.ProgramContext):
        pass

    # Exit a parse tree produced by SintaticoParser#program.
    def exitProgram(self, ctx:SintaticoParser.ProgramContext):
        pass


    # Enter a parse tree produced by SintaticoParser#expression.
    def enterExpression(self, ctx:SintaticoParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SintaticoParser#expression.
    def exitExpression(self, ctx:SintaticoParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SintaticoParser#operando.
    def enterOperando(self, ctx:SintaticoParser.OperandoContext):
        pass

    # Exit a parse tree produced by SintaticoParser#operando.
    def exitOperando(self, ctx:SintaticoParser.OperandoContext):
        pass


    # Enter a parse tree produced by SintaticoParser#op.
    def enterOp(self, ctx:SintaticoParser.OpContext):
        pass

    # Exit a parse tree produced by SintaticoParser#op.
    def exitOp(self, ctx:SintaticoParser.OpContext):
        pass



del SintaticoParser
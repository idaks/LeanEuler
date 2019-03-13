# Generated from CleanTax.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("N\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\6\2\24\n\2\r\2\16\2\25\3\2\3\2\3\3\3")
        buf.write("\3\6\3\34\n\3\r\3\16\3\35\3\3\7\3!\n\3\f\3\16\3$\13\3")
        buf.write("\3\4\3\4\6\4(\n\4\r\4\16\4)\3\4\3\4\3\5\3\5\6\5\60\n\5")
        buf.write("\r\5\16\5\61\3\5\7\5\65\n\5\f\5\16\58\13\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\5\7B\n\7\3\b\3\b\3\t\3\t\6\tH\n\t")
        buf.write("\r\t\16\tI\3\t\3\t\3\t\2\2\n\2\4\6\b\n\f\16\20\2\3\3\2")
        buf.write("\6\7\2M\2\23\3\2\2\2\4\31\3\2\2\2\6%\3\2\2\2\b-\3\2\2")
        buf.write("\2\n9\3\2\2\2\fA\3\2\2\2\16C\3\2\2\2\20E\3\2\2\2\22\24")
        buf.write("\5\4\3\2\23\22\3\2\2\2\24\25\3\2\2\2\25\23\3\2\2\2\25")
        buf.write("\26\3\2\2\2\26\27\3\2\2\2\27\30\5\b\5\2\30\3\3\2\2\2\31")
        buf.write("\33\7\3\2\2\32\34\7\r\2\2\33\32\3\2\2\2\34\35\3\2\2\2")
        buf.write("\35\33\3\2\2\2\35\36\3\2\2\2\36\"\3\2\2\2\37!\5\6\4\2")
        buf.write(" \37\3\2\2\2!$\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#\5\3\2\2")
        buf.write("\2$\"\3\2\2\2%\'\7\4\2\2&(\7\r\2\2\'&\3\2\2\2()\3\2\2")
        buf.write("\2)\'\3\2\2\2)*\3\2\2\2*+\3\2\2\2+,\7\5\2\2,\7\3\2\2\2")
        buf.write("-/\t\2\2\2.\60\7\r\2\2/.\3\2\2\2\60\61\3\2\2\2\61/\3\2")
        buf.write("\2\2\61\62\3\2\2\2\62\66\3\2\2\2\63\65\5\n\6\2\64\63\3")
        buf.write("\2\2\2\658\3\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2\67\t\3")
        buf.write("\2\2\28\66\3\2\2\29:\7\b\2\2:;\7\r\2\2;<\5\f\7\2<=\7\r")
        buf.write("\2\2=>\7\t\2\2>\13\3\2\2\2?B\5\16\b\2@B\5\20\t\2A?\3\2")
        buf.write("\2\2A@\3\2\2\2B\r\3\2\2\2CD\7\f\2\2D\17\3\2\2\2EG\7\n")
        buf.write("\2\2FH\7\f\2\2GF\3\2\2\2HI\3\2\2\2IG\3\2\2\2IJ\3\2\2\2")
        buf.write("JK\3\2\2\2KL\7\13\2\2L\21\3\2\2\2\n\25\35\")\61\66AI")
        return buf.getvalue()


class CleanTaxParser ( Parser ):

    grammarFileName = "CleanTax.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'taxonomy'", "'('", "')'", "'articulation'", 
                     "'articulations'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "RCC_BASIC_5", "TEXT", "WHITESPACE" ]

    RULE_ct_input = 0
    RULE_tax_desc = 1
    RULE_tax_sub_desc = 2
    RULE_articulations_desc = 3
    RULE_articulation = 4
    RULE_relation = 5
    RULE_rcc5_rel = 6
    RULE_rcc32_rel = 7

    ruleNames =  [ "ct_input", "tax_desc", "tax_sub_desc", "articulations_desc", 
                   "articulation", "relation", "rcc5_rel", "rcc32_rel" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    RCC_BASIC_5=10
    TEXT=11
    WHITESPACE=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Ct_inputContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def articulations_desc(self):
            return self.getTypedRuleContext(CleanTaxParser.Articulations_descContext,0)


        def tax_desc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CleanTaxParser.Tax_descContext)
            else:
                return self.getTypedRuleContext(CleanTaxParser.Tax_descContext,i)


        def getRuleIndex(self):
            return CleanTaxParser.RULE_ct_input

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCt_input" ):
                listener.enterCt_input(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCt_input" ):
                listener.exitCt_input(self)




    def ct_input(self):

        localctx = CleanTaxParser.Ct_inputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_ct_input)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.tax_desc()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CleanTaxParser.T__0):
                    break

            self.state = 21
            self.articulations_desc()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Tax_descContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(CleanTaxParser.TEXT)
            else:
                return self.getToken(CleanTaxParser.TEXT, i)

        def tax_sub_desc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CleanTaxParser.Tax_sub_descContext)
            else:
                return self.getTypedRuleContext(CleanTaxParser.Tax_sub_descContext,i)


        def getRuleIndex(self):
            return CleanTaxParser.RULE_tax_desc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTax_desc" ):
                listener.enterTax_desc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTax_desc" ):
                listener.exitTax_desc(self)




    def tax_desc(self):

        localctx = CleanTaxParser.Tax_descContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_tax_desc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(CleanTaxParser.T__0)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.match(CleanTaxParser.TEXT)
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CleanTaxParser.TEXT):
                    break

            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CleanTaxParser.T__1:
                self.state = 29
                self.tax_sub_desc()
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Tax_sub_descContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(CleanTaxParser.TEXT)
            else:
                return self.getToken(CleanTaxParser.TEXT, i)

        def getRuleIndex(self):
            return CleanTaxParser.RULE_tax_sub_desc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTax_sub_desc" ):
                listener.enterTax_sub_desc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTax_sub_desc" ):
                listener.exitTax_sub_desc(self)




    def tax_sub_desc(self):

        localctx = CleanTaxParser.Tax_sub_descContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_tax_sub_desc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(CleanTaxParser.T__1)
            self.state = 37 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self.match(CleanTaxParser.TEXT)
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CleanTaxParser.TEXT):
                    break

            self.state = 41
            self.match(CleanTaxParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Articulations_descContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(CleanTaxParser.TEXT)
            else:
                return self.getToken(CleanTaxParser.TEXT, i)

        def articulation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CleanTaxParser.ArticulationContext)
            else:
                return self.getTypedRuleContext(CleanTaxParser.ArticulationContext,i)


        def getRuleIndex(self):
            return CleanTaxParser.RULE_articulations_desc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArticulations_desc" ):
                listener.enterArticulations_desc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArticulations_desc" ):
                listener.exitArticulations_desc(self)




    def articulations_desc(self):

        localctx = CleanTaxParser.Articulations_descContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_articulations_desc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            _la = self._input.LA(1)
            if not(_la==CleanTaxParser.T__3 or _la==CleanTaxParser.T__4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 45 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 44
                self.match(CleanTaxParser.TEXT)
                self.state = 47 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CleanTaxParser.TEXT):
                    break

            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CleanTaxParser.T__5:
                self.state = 49
                self.articulation()
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArticulationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(CleanTaxParser.TEXT)
            else:
                return self.getToken(CleanTaxParser.TEXT, i)

        def relation(self):
            return self.getTypedRuleContext(CleanTaxParser.RelationContext,0)


        def getRuleIndex(self):
            return CleanTaxParser.RULE_articulation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArticulation" ):
                listener.enterArticulation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArticulation" ):
                listener.exitArticulation(self)




    def articulation(self):

        localctx = CleanTaxParser.ArticulationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_articulation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(CleanTaxParser.T__5)
            self.state = 56
            self.match(CleanTaxParser.TEXT)
            self.state = 57
            self.relation()
            self.state = 58
            self.match(CleanTaxParser.TEXT)
            self.state = 59
            self.match(CleanTaxParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RelationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rcc5_rel(self):
            return self.getTypedRuleContext(CleanTaxParser.Rcc5_relContext,0)


        def rcc32_rel(self):
            return self.getTypedRuleContext(CleanTaxParser.Rcc32_relContext,0)


        def getRuleIndex(self):
            return CleanTaxParser.RULE_relation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelation" ):
                listener.enterRelation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelation" ):
                listener.exitRelation(self)




    def relation(self):

        localctx = CleanTaxParser.RelationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_relation)
        try:
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CleanTaxParser.RCC_BASIC_5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.rcc5_rel()
                pass
            elif token in [CleanTaxParser.T__7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.rcc32_rel()
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

    class Rcc5_relContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RCC_BASIC_5(self):
            return self.getToken(CleanTaxParser.RCC_BASIC_5, 0)

        def getRuleIndex(self):
            return CleanTaxParser.RULE_rcc5_rel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRcc5_rel" ):
                listener.enterRcc5_rel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRcc5_rel" ):
                listener.exitRcc5_rel(self)




    def rcc5_rel(self):

        localctx = CleanTaxParser.Rcc5_relContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_rcc5_rel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(CleanTaxParser.RCC_BASIC_5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Rcc32_relContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RCC_BASIC_5(self, i:int=None):
            if i is None:
                return self.getTokens(CleanTaxParser.RCC_BASIC_5)
            else:
                return self.getToken(CleanTaxParser.RCC_BASIC_5, i)

        def getRuleIndex(self):
            return CleanTaxParser.RULE_rcc32_rel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRcc32_rel" ):
                listener.enterRcc32_rel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRcc32_rel" ):
                listener.exitRcc32_rel(self)




    def rcc32_rel(self):

        localctx = CleanTaxParser.Rcc32_relContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_rcc32_rel)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(CleanTaxParser.T__7)
            self.state = 69 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 68
                self.match(CleanTaxParser.RCC_BASIC_5)
                self.state = 71 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CleanTaxParser.RCC_BASIC_5):
                    break

            self.state = 73
            self.match(CleanTaxParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






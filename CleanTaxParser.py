# Generated from CleanTax.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\rK\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4")
        buf.write(u"\b\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\3\3\3\6\3\31\n\3\r\3")
        buf.write(u"\16\3\32\3\3\7\3\36\n\3\f\3\16\3!\13\3\3\4\3\4\6\4%\n")
        buf.write(u"\4\r\4\16\4&\3\4\3\4\3\5\3\5\6\5-\n\5\r\5\16\5.\3\5\7")
        buf.write(u"\5\62\n\5\f\5\16\5\65\13\5\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write(u"\7\3\7\5\7?\n\7\3\b\3\b\3\t\3\t\6\tE\n\t\r\t\16\tF\3")
        buf.write(u"\t\3\t\3\t\2\2\n\2\4\6\b\n\f\16\20\2\2\2I\2\22\3\2\2")
        buf.write(u"\2\4\26\3\2\2\2\6\"\3\2\2\2\b*\3\2\2\2\n\66\3\2\2\2\f")
        buf.write(u">\3\2\2\2\16@\3\2\2\2\20B\3\2\2\2\22\23\5\4\3\2\23\24")
        buf.write(u"\5\4\3\2\24\25\5\b\5\2\25\3\3\2\2\2\26\30\7\3\2\2\27")
        buf.write(u"\31\7\f\2\2\30\27\3\2\2\2\31\32\3\2\2\2\32\30\3\2\2\2")
        buf.write(u"\32\33\3\2\2\2\33\37\3\2\2\2\34\36\5\6\4\2\35\34\3\2")
        buf.write(u"\2\2\36!\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 \5\3\2\2\2")
        buf.write(u"!\37\3\2\2\2\"$\7\4\2\2#%\7\f\2\2$#\3\2\2\2%&\3\2\2\2")
        buf.write(u"&$\3\2\2\2&\'\3\2\2\2\'(\3\2\2\2()\7\5\2\2)\7\3\2\2\2")
        buf.write(u"*,\7\6\2\2+-\7\f\2\2,+\3\2\2\2-.\3\2\2\2.,\3\2\2\2./")
        buf.write(u"\3\2\2\2/\63\3\2\2\2\60\62\5\n\6\2\61\60\3\2\2\2\62\65")
        buf.write(u"\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64\t\3\2\2\2\65")
        buf.write(u"\63\3\2\2\2\66\67\7\7\2\2\678\7\f\2\289\5\f\7\29:\7\f")
        buf.write(u"\2\2:;\7\b\2\2;\13\3\2\2\2<?\5\16\b\2=?\5\20\t\2><\3")
        buf.write(u"\2\2\2>=\3\2\2\2?\r\3\2\2\2@A\7\13\2\2A\17\3\2\2\2BD")
        buf.write(u"\7\t\2\2CE\7\13\2\2DC\3\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3")
        buf.write(u"\2\2\2GH\3\2\2\2HI\7\n\2\2I\21\3\2\2\2\t\32\37&.\63>")
        buf.write(u"F")
        return buf.getvalue()


class CleanTaxParser ( Parser ):

    grammarFileName = "CleanTax.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'taxonomy'", u"'('", u"')'", u"'articulations'", 
                     u"'['", u"']'", u"'{'", u"'}'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"RCC_BASIC_5", u"TEXT", u"WHITESPACE" ]

    RULE_ct_input = 0
    RULE_tax_desc = 1
    RULE_tax_sub_desc = 2
    RULE_articulations_desc = 3
    RULE_articulation = 4
    RULE_relation = 5
    RULE_rcc5_rel = 6
    RULE_rcc32_rel = 7

    ruleNames =  [ u"ct_input", u"tax_desc", u"tax_sub_desc", u"articulations_desc", 
                   u"articulation", u"relation", u"rcc5_rel", u"rcc32_rel" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    RCC_BASIC_5=9
    TEXT=10
    WHITESPACE=11

    def __init__(self, input, output=sys.stdout):
        super(CleanTaxParser, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Ct_inputContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CleanTaxParser.Ct_inputContext, self).__init__(parent, invokingState)
            self.parser = parser

        def tax_desc(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CleanTaxParser.Tax_descContext)
            else:
                return self.getTypedRuleContext(CleanTaxParser.Tax_descContext,i)


        def articulations_desc(self):
            return self.getTypedRuleContext(CleanTaxParser.Articulations_descContext,0)


        def getRuleIndex(self):
            return CleanTaxParser.RULE_ct_input

        def enterRule(self, listener):
            if hasattr(listener, "enterCt_input"):
                listener.enterCt_input(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCt_input"):
                listener.exitCt_input(self)




    def ct_input(self):

        localctx = CleanTaxParser.Ct_inputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_ct_input)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.tax_desc()
            self.state = 17
            self.tax_desc()
            self.state = 18
            self.articulations_desc()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Tax_descContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CleanTaxParser.Tax_descContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i=None):
            if i is None:
                return self.getTokens(CleanTaxParser.TEXT)
            else:
                return self.getToken(CleanTaxParser.TEXT, i)

        def tax_sub_desc(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CleanTaxParser.Tax_sub_descContext)
            else:
                return self.getTypedRuleContext(CleanTaxParser.Tax_sub_descContext,i)


        def getRuleIndex(self):
            return CleanTaxParser.RULE_tax_desc

        def enterRule(self, listener):
            if hasattr(listener, "enterTax_desc"):
                listener.enterTax_desc(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTax_desc"):
                listener.exitTax_desc(self)




    def tax_desc(self):

        localctx = CleanTaxParser.Tax_descContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_tax_desc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(CleanTaxParser.T__0)
            self.state = 22 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 21
                self.match(CleanTaxParser.TEXT)
                self.state = 24 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CleanTaxParser.TEXT):
                    break

            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CleanTaxParser.T__1:
                self.state = 26
                self.tax_sub_desc()
                self.state = 31
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

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CleanTaxParser.Tax_sub_descContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i=None):
            if i is None:
                return self.getTokens(CleanTaxParser.TEXT)
            else:
                return self.getToken(CleanTaxParser.TEXT, i)

        def getRuleIndex(self):
            return CleanTaxParser.RULE_tax_sub_desc

        def enterRule(self, listener):
            if hasattr(listener, "enterTax_sub_desc"):
                listener.enterTax_sub_desc(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTax_sub_desc"):
                listener.exitTax_sub_desc(self)




    def tax_sub_desc(self):

        localctx = CleanTaxParser.Tax_sub_descContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_tax_sub_desc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(CleanTaxParser.T__1)
            self.state = 34 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 33
                self.match(CleanTaxParser.TEXT)
                self.state = 36 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CleanTaxParser.TEXT):
                    break

            self.state = 38
            self.match(CleanTaxParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Articulations_descContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CleanTaxParser.Articulations_descContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i=None):
            if i is None:
                return self.getTokens(CleanTaxParser.TEXT)
            else:
                return self.getToken(CleanTaxParser.TEXT, i)

        def articulation(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CleanTaxParser.ArticulationContext)
            else:
                return self.getTypedRuleContext(CleanTaxParser.ArticulationContext,i)


        def getRuleIndex(self):
            return CleanTaxParser.RULE_articulations_desc

        def enterRule(self, listener):
            if hasattr(listener, "enterArticulations_desc"):
                listener.enterArticulations_desc(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArticulations_desc"):
                listener.exitArticulations_desc(self)




    def articulations_desc(self):

        localctx = CleanTaxParser.Articulations_descContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_articulations_desc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(CleanTaxParser.T__3)
            self.state = 42 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 41
                self.match(CleanTaxParser.TEXT)
                self.state = 44 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CleanTaxParser.TEXT):
                    break

            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CleanTaxParser.T__4:
                self.state = 46
                self.articulation()
                self.state = 51
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

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CleanTaxParser.ArticulationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i=None):
            if i is None:
                return self.getTokens(CleanTaxParser.TEXT)
            else:
                return self.getToken(CleanTaxParser.TEXT, i)

        def relation(self):
            return self.getTypedRuleContext(CleanTaxParser.RelationContext,0)


        def getRuleIndex(self):
            return CleanTaxParser.RULE_articulation

        def enterRule(self, listener):
            if hasattr(listener, "enterArticulation"):
                listener.enterArticulation(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitArticulation"):
                listener.exitArticulation(self)




    def articulation(self):

        localctx = CleanTaxParser.ArticulationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_articulation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(CleanTaxParser.T__4)
            self.state = 53
            self.match(CleanTaxParser.TEXT)
            self.state = 54
            self.relation()
            self.state = 55
            self.match(CleanTaxParser.TEXT)
            self.state = 56
            self.match(CleanTaxParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RelationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CleanTaxParser.RelationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def rcc5_rel(self):
            return self.getTypedRuleContext(CleanTaxParser.Rcc5_relContext,0)


        def rcc32_rel(self):
            return self.getTypedRuleContext(CleanTaxParser.Rcc32_relContext,0)


        def getRuleIndex(self):
            return CleanTaxParser.RULE_relation

        def enterRule(self, listener):
            if hasattr(listener, "enterRelation"):
                listener.enterRelation(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRelation"):
                listener.exitRelation(self)




    def relation(self):

        localctx = CleanTaxParser.RelationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_relation)
        try:
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CleanTaxParser.RCC_BASIC_5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.rcc5_rel()
                pass
            elif token in [CleanTaxParser.T__6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
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

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CleanTaxParser.Rcc5_relContext, self).__init__(parent, invokingState)
            self.parser = parser

        def RCC_BASIC_5(self):
            return self.getToken(CleanTaxParser.RCC_BASIC_5, 0)

        def getRuleIndex(self):
            return CleanTaxParser.RULE_rcc5_rel

        def enterRule(self, listener):
            if hasattr(listener, "enterRcc5_rel"):
                listener.enterRcc5_rel(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRcc5_rel"):
                listener.exitRcc5_rel(self)




    def rcc5_rel(self):

        localctx = CleanTaxParser.Rcc5_relContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_rcc5_rel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(CleanTaxParser.RCC_BASIC_5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Rcc32_relContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CleanTaxParser.Rcc32_relContext, self).__init__(parent, invokingState)
            self.parser = parser

        def RCC_BASIC_5(self, i=None):
            if i is None:
                return self.getTokens(CleanTaxParser.RCC_BASIC_5)
            else:
                return self.getToken(CleanTaxParser.RCC_BASIC_5, i)

        def getRuleIndex(self):
            return CleanTaxParser.RULE_rcc32_rel

        def enterRule(self, listener):
            if hasattr(listener, "enterRcc32_rel"):
                listener.enterRcc32_rel(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRcc32_rel"):
                listener.exitRcc32_rel(self)




    def rcc32_rel(self):

        localctx = CleanTaxParser.Rcc32_relContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_rcc32_rel)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(CleanTaxParser.T__6)
            self.state = 66 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 65
                self.match(CleanTaxParser.RCC_BASIC_5)
                self.state = 68 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CleanTaxParser.RCC_BASIC_5):
                    break

            self.state = 70
            self.match(CleanTaxParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






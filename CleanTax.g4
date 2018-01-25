grammar CleanTax;

options {
    language = Python2;
}

//			Parser Rules

input = tax_desc tax_desc articulations_desc ;

tax_desc = 'taxonomy' TEXT (tax_sub_desc)*

tax_sub_desc = '(' TEXT ')'

articulations_desc = 'articulations' TEXT (articulation)*

articulation = '[' TEXT RELATION TEXT ']'

//			Lexer Rules

TEXT: [a-zA-Z0-9\\_.,/:\-<>"!=]+ ;

WHITESPACE : ( '\t' | ' ' | '\r' | '\n'| '\u000C' )+ -> skip ;

RELATION : 
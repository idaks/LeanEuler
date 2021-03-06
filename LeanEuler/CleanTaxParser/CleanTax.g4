grammar CleanTax;

options {
    language = Python3;
}

//			Parser Rules

ct_input : tax_desc+ articulations_desc ;

tax_desc : 'taxonomy' TEXT+ (tax_sub_desc)* ;

tax_sub_desc : '(' TEXT+ ')' ;

articulations_desc : ('articulation' | 'articulations') TEXT+ (articulation)* ;

articulation : '[' TEXT relation TEXT ']' ;

relation : rcc5_rel | rcc32_rel ;

rcc5_rel : RCC_BASIC_5 ;

rcc32_rel : '{' (RCC_BASIC_5)+ '}' ;


//			Lexer Rules

RCC_BASIC_5 : '><' | '<' | '>' | '==' | '=' | '!' | 'o' | 'is_included_in' | 'includes' | 'equals' | 'disjoint' | 'overlaps' ;

TEXT: [a-zA-Z0-9\\_.,/:\-"]+ ;

WHITESPACE : ( '\t' | ' ' | '\r' | '\n'| '\u000C' )+ -> skip ;


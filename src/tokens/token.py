from typing import NamedTuple

TokenType = str

class Token(NamedTuple):
    type: TokenType
    literal: str

class TokenConsts:
    ILLEGAL = "ILLEGAL"
    EOF = "EOF"

    # identifiers + literals
    IDENT = "IDENT" # names of variables/functions etc: add, foobar, x, y
    INT = "INT" # integers 3, 4, 5 ...

    # operators
    PLUS = "+"
    ASSIGN = "="
    MINUS = "-"
    BANG = "!"
    ASTERISK = "*"
    SLASH = "/"

    LT = "<"
    GT = ">"
    EQ = "=="
    NOT_EQ = "!="

    # Delimiters
    COMMA = ","
    SEMICOLON = ";"

    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"

    # keywords
    FUNCTION = "FUNCTION"
    LET = "LET"
    RETURN = "RETURN"
    TRUE = "TRUE"
    FALSE = "FALSE"
    IF = "IF"
    ELSE = "ELSE"


KEYWORDS = {
    'let': TokenConsts.LET,
    'fn': TokenConsts.FUNCTION,
    'if': TokenConsts.IF,
    'return': TokenConsts.RETURN,
    'true': TokenConsts.TRUE,
    'false': TokenConsts.FALSE,
    'else': TokenConsts.ELSE,
}

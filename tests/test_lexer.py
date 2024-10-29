from src.tokens.token import Token, TokenConsts
from src.lexer.lexer import Lexer, is_letter
import string

def test_next_token():
    input = """let five = 5;
    let ten = 10;
    
    let add = fn(x, y) {
        x + y;
    };

    let result = add(five, ten);
    !-/*5;
    5 < 10 > 5;

    if (5 < 10) {
        return true;
    } else {
        return false;
    }

    10 == 10;
    10 != 9;
    """

    expected = [
        Token(TokenConsts.LET, "let"),
        Token(TokenConsts.IDENT, "five"),
        Token(TokenConsts.ASSIGN, "="),
        Token(TokenConsts.INT, "5"),
        Token(TokenConsts.SEMICOLON, ";"),

        Token(TokenConsts.LET, "let"),
        Token(TokenConsts.IDENT, "ten"),
        Token(TokenConsts.ASSIGN, "="),
        Token(TokenConsts.INT, "10"),
        Token(TokenConsts.SEMICOLON, ";"),

        Token(TokenConsts.LET, "let"),
        Token(TokenConsts.IDENT, "add"),
        Token(TokenConsts.ASSIGN, "="),
        Token(TokenConsts.FUNCTION, "fn"),
        Token(TokenConsts.LPAREN, "("),
        Token(TokenConsts.IDENT, "x"),
        Token(TokenConsts.COMMA, ","),
        Token(TokenConsts.IDENT, "y"),
        Token(TokenConsts.RPAREN, ")"),
        Token(TokenConsts.LBRACE, "{"),

        Token(TokenConsts.IDENT, "x"),
        Token(TokenConsts.PLUS, "+"),
        Token(TokenConsts.IDENT, "y"),
        Token(TokenConsts.SEMICOLON, ";"),
        Token(TokenConsts.RBRACE, "}"),
        Token(TokenConsts.SEMICOLON, ";"),

        Token(TokenConsts.LET, "let"),
        Token(TokenConsts.IDENT, "result"),
        Token(TokenConsts.ASSIGN, "="),
        Token(TokenConsts.IDENT, "add"),
        Token(TokenConsts.LPAREN, "("),
        Token(TokenConsts.IDENT, "five"),
        Token(TokenConsts.COMMA, ","),
        Token(TokenConsts.IDENT, "ten"),
        Token(TokenConsts.RPAREN, ")"),
        Token(TokenConsts.SEMICOLON, ";"),

        Token(TokenConsts.BANG, "!"),
        Token(TokenConsts.MINUS, "-"),
        Token(TokenConsts.SLASH, "/"),
        Token(TokenConsts.ASTERISK, "*"),
        Token(TokenConsts.INT, "5"),
        Token(TokenConsts.SEMICOLON, ";"),

        Token(TokenConsts.INT, "5"),
        Token(TokenConsts.LT, "<"),
        Token(TokenConsts.INT, "10"),
        Token(TokenConsts.GT, ">"),
        Token(TokenConsts.INT, "5"),
        Token(TokenConsts.SEMICOLON, ";"),

        Token(TokenConsts.IF, "if"),
        Token(TokenConsts.LPAREN, "("),
        Token(TokenConsts.INT, "5"),
        Token(TokenConsts.LT, "<"),
        Token(TokenConsts.INT, "10"),
        Token(TokenConsts.RPAREN, ")"),
        Token(TokenConsts.LBRACE, "{"),

        Token(TokenConsts.RETURN, "return"),
        Token(TokenConsts.TRUE, "true"),
        Token(TokenConsts.SEMICOLON, ";"),
        Token(TokenConsts.RBRACE, "}"),

        Token(TokenConsts.ELSE, "else"),
        Token(TokenConsts.LBRACE, "{"),
        Token(TokenConsts.RETURN, "return"),
        Token(TokenConsts.FALSE, "false"),
        Token(TokenConsts.SEMICOLON, ";"),
        Token(TokenConsts.RBRACE, "}"),

        Token(TokenConsts.INT, "10"),
        Token(TokenConsts.EQ, "=="),
        Token(TokenConsts.INT, "10"),
        Token(TokenConsts.SEMICOLON, ";"),

        Token(TokenConsts.INT, "10"),
        Token(TokenConsts.NOT_EQ, "!="),
        Token(TokenConsts.INT, "9"),
        Token(TokenConsts.SEMICOLON, ";"),

        Token(TokenConsts.EOF, ""),
    ]
    # input = "let five = 5;"
    lexer = Lexer(input)

    # breakpoint()
    for exp in expected:
        token = lexer.next_token()
        print(token)
        assert exp == token
        # print(f"{lexer.next_token()}")


def test_is_letter():
    for ch in string.ascii_letters:
        assert is_letter(ch)
    
    assert is_letter("_")

    for ch in string.digits:
        assert not is_letter(ch)
    
    assert not is_letter(" ")



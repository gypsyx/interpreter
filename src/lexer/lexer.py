from tokens.token import Token, TokenConsts, KEYWORDS

def is_letter(ch: str) -> bool:
    return (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z') or (ch == "_")

def is_digit(ch: str) -> bool:
    return (ch >= '0' and ch <= '9')

class Lexer:
    def __init__(self, input: str):
        self.input = input
        self.position = 0
        self.read_position = 0
        self.ch = ''
        self.read_char()
        print(f"input : {input}")


    def skip_whitespace(self):
        while self.ch in [' ', '\t', '\n', '\r']:
            self.read_char()
    

    def peek_char(self):
        if self.read_position >= len(self.input):
            return 0
        else:
            return self.input[self.read_position]


    def read_char(self):
        if self.read_position >= len(self.input):
            self.ch = 0
        else:
            self.ch = self.input[self.read_position]
        
        self.position = self.read_position
        self.read_position += 1


    def read_identifier(self) -> Token:
        start = self.position

        while is_letter(self.ch):
            self.read_char()

        val = self.input[start: self.position]
        
        if val in KEYWORDS:
            return Token(KEYWORDS[val], val)
        return Token(TokenConsts.IDENT, val)
        

    def read_number(self) -> Token:
        start = self.position

        while is_digit(self.ch):
            self.read_char()

        val = self.input[start : self.position]
        return Token(TokenConsts.INT, val) 


    def next_token(self) -> Token:
        token = None
        # print(f"[INFO] char {self.ch}")
        self.skip_whitespace()
        
        match self.ch:
            case "=":
                if self.peek_char() == "=":
                    self.read_char()
                    token = Token(TokenConsts.EQ, "==")
                else:
                    token =  Token(TokenConsts.ASSIGN, self.ch)
            case "(":
                token =  Token(TokenConsts.LPAREN, self.ch)
            case ")":
                token =  Token(TokenConsts.RPAREN, self.ch)
            case "{":
                token =  Token(TokenConsts.LBRACE, self.ch)
            case "}":
                token =  Token(TokenConsts.RBRACE, self.ch)
            case ",":
                token =  Token(TokenConsts.COMMA, self.ch)
            case ";":
                token =  Token(TokenConsts.SEMICOLON, self.ch)
            case "+":
                token = Token(TokenConsts.PLUS, self.ch)
            case "-":
                token = Token(TokenConsts.MINUS, self.ch)
            case "/":
                token = Token(TokenConsts.SLASH, self.ch)
            case "*":
                token = Token(TokenConsts.ASTERISK, self.ch)
            case "!":
                if self.peek_char() == "=":
                    self.read_char()
                    token = Token(TokenConsts.NOT_EQ, "!=")
                else:
                    token = Token(TokenConsts.BANG, self.ch)
            case "<":
                token = Token(TokenConsts.LT, self.ch)
            case ">":
                token = Token(TokenConsts.GT, self.ch)
            case 0:
                token =  Token(TokenConsts.EOF, "")
            
            case _:
                if is_letter(self.ch):
                    token = self.read_identifier()
                    # early exit as the above call internally calls self.read_char(), if we
                    # don't exit here self.read_char() will be called again skipping a token potentially
                    return token
                elif is_digit(self.ch):
                    token = self.read_number()
                    return token
                else:
                    token = Token(TokenConsts.ILLEGAL, self.ch)
        
        self.read_char()
        return token
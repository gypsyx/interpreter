from lexer.lexer import Lexer
from tokens.token import TokenConsts

PROMPT = ">>"

def start():

    while True:
        print(PROMPT, sep=" ")
        s = input()
        if not s:
            return
        lexer = Lexer(s)
        token = lexer.next_token()
        while token.type != TokenConsts.EOF:
            print(token)
            token = lexer.next_token()

if __name__ == '__main__':
    start()
from type import Type
from token import Token

class Lexer():

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]
    
    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
    
    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        
        return int(result)

    def get_next_token(self):
        
        while self.current_char is not None:
            
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            
            if self.current_char.isdigit():
                return Token(Type.INTEGER, self.integer())
            
            if self.current_char == "+":
                self.advance()
                return Token(Type.PLUS, "+")

            if self.current_char == '-':
                self.advance()
                return Token(Type.MINUS, '-')
            
            if self.current_char == '*':
                self.advance()
                return Token(Type.MULT, '*')
            
            if self.current_char == '/':
                self.advance()
                return Token(Type.DIV, '/')

            if self.current_char == '(':
                self.advance()
                return Token(Type.STARTP, '(')
            
            if self.current_char == ')':
                self.advance()
                return Token(Type.ENDP, ')')
            
            self.error()
        
        return Token(Type.EOF, None)




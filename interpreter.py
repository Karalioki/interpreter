from type import Type
from token import Token

class Interpreter():

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Error while parsing input')

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

    def term(self):
        token = self.current_token
        self.eat(Type.INTEGER)
        return token.value
    
    def get_next_token(self):
        
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            
            if self.current_char.isdigit():
                return Token(Type.INTEGER, self.integer())

            if self.current_char == '+':
                self.advance()
                return Token(Type.PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(Type.MINUS, '-')
            
            if self.current_char == '*':
                self.advance()
                return Token(Type.MULT, '*')
            
            if self.current_char == '/':
                self.advance()
                return Token(Type.DIV, '/')
            
            self.error()
        
        return Token(Type.EOF, None)

    def eat(self, type):
        if self.current_token.type == type:
            
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        self.current_token = self.get_next_token()

        result = self.term()
        while self.current_token.type in (Type.PLUS, Type.MINUS):
            token = self.current_token

            if(token.type == Type.PLUS):
                self.eat(Type.PLUS)
                result = result + self.term()
            elif token.type == Type.MINUS:
                self.eat(Type.MINUS)
                result = result - self.term()
        
        return result
    
def main():
    while True:
        try:
            text = input('>>> ')
            if(text == 'exit'):
                break
        except EOFError:
            print("Error Occured")
            break
        
        if not text:
            continue

        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == "__main__":
    main()
            

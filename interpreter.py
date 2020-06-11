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

        left = self.current_token
        self.eat(Type.INTEGER)
        
        while self.current_char is not None:
            op = self.current_token
            self.eat(op.type)
            

            right = self.current_token
            self.eat(Type.INTEGER)

            if (op.type == Type.PLUS):
                result = left.value + right.value
            elif  op.type == Type.MINUS:
                result = left.value - right.value
            elif op.type == Type.MULT:
                result = left.value * right.value
            elif op.type == Type.DIV:
                result = left.value / right.value
            
            left.value = result
        
        return left.value
    
def main():
    while True:
        try:
            text = input('> ')
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
            

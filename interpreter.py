from type import Type
from token import Token
from lexer import Lexer

class Interpreter():

    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if(self.current_token.type == type):
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()
    
    def factor(self):
        """Return an INTEGER token value.

        factor : INTEGER
        """
        token = self.current_token
        self.eat(Type.INTEGER)
        return token.value

    def term(self):
        ''' for multiplication and division'''
        result = self.factor()

        while self.current_token.type in (Type.MULT, Type.DIV):
            token = self.current_token
            if token.type == Type.MULT:
                self.eat(Type.MULT)
                result = result * self.factor()
            elif token.type == Type.DIV:
                self.eat(Type.DIV)
                result = result * self.factor()
            
        return result
            
    
    def expr(self):
        """
        for addition and substraction
        """
        result = self.term()
        while self.current_token.type in  (Type.PLUS, Type.MINUS):
            token = self.current_token
            if token.type == Type.PLUS:
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
            break
        
        if not text:
            continue
        
        lexer = Lexer(text)
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        print(result)



if __name__ == "__main__":
    main()
            

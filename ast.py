from type import Type
from token import Token

class AST():
    pass

class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right
    
    def __str__(self):
        return self.token
    

class Num(AST):

    def __init__(self, token):
        self.token = token
        self.value = token.value

    def __str__(self):
        return 'Node Num[{}]'.format(self.value)
    
class Parser():

    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
    
    def error(self):
        raise Exception("Invalic syntax")
    
    def eat(self, current_token):
        if self.current_token.type == current_token:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()
    
    def factor(self):
        token = self.current_token
        if token.type == Type.INTEGER:
            self.eat(Type.INTEGER)
            return Num(token)
        elif token.type == Type.STARTP:
            self.eat(Type.STARTP)
            node = self.expr()
            self.eat(Type.ENDP)
            return node
        
    def term(self):
        node = self.factor()
        
        while self.current_token.type in (Type.MULT, Type.DIV):
            token = self.current_token
            if token.type == Type.MULT:
                self.eat(Type.MULT)
            elif token.type == Type.DIV:
                self.eat(Type.DIV)
            node = BinOp(left = node, op = token, right = self.factor())
            
        
        return node
    

    def expr(self):
        node = self.term()
    
        while self.current_token.type in (Type.PLUS, Type.MINUS):
            token = self.current_token
            if token.type == Type.PLUS:
                self.eat(Type.PLUS)
            elif token.type == Type.MINUS:
                self.eat(Type.MINUS)
            node = BinOp(left = node, op = token, right = self.term())
        
        return node
    
    def parse(self):
        node = self.expr()

        if self.current_token.type != Type.EOF:
            self.error()
        return node
    
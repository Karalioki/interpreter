from type import Type
from token import Token
from lexer import Lexer
from ast import AST, BinOp, Num, Parser


class NodeVisitor():
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)
    
    def generic_visit(self, node):
        raise Exception("No visit_{} method".format(type(node).__name__))



class Interpreter(NodeVisitor):
    '''
    Grammar

        expr : term ((PLUS | MINUS) term) *
        term : factor ((MULT | DIV) factor) *
        factor : INTEGER | (STARTP expr ENDP)
    '''
    def __init__(self, parser):
        self.parser = parser
    
    def visit_BinOp(self, node):
        if node.op.type == Type.PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == Type.MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == Type.MULT:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == Type.DIV:
            return self.visit(node.left) / self.visit(node.right)
    
    def visit_Num(self, node):
        return node.value
    
    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)
    
    

def main():
    while True:
        try:
            text = input('>>> ' )
            if(text.strip() == 'exit'):
                break
        except EOFError:
            break
        
        if not text:
            continue
        
        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        result = interpreter.interpret()

        print('>>> ' + str(result))



if __name__ == "__main__":
    main()
            

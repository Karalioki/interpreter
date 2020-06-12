from enum import Enum

class Type(Enum):
    INTEGER = 1

    PLUS = 2

    MINUS = 3

    MULT = 4

    DIV = 5

    EOF = 6

    STARTP = 7 #parentheses start

    ENDP = 8 #parentheses end 


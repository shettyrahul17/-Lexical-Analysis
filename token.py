# This is used to check attributes of Tokens.
import re
import errors

class Tokens:

    def __init__(self):
        self.alphabets = ["a", "b", "c", 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p''q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z',
                          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.keywords = ["if", "else", "while", "do", "break", "continue", "int", "double",
                         "float", "return", "char", 'case', "sizeof", "long", "switch", "struct", "static"]
        self.delimiters = [" ", "+", "-", "*", "/", ",", ";", ">",
                           "<", "=", "(", "()", ")", "[", "]", "{", "}"]
        self.operator = ["+", "-", "*", "/", ">",
                         "<", "=", "<=", ">=", "++", "--"]
        self.attr_ = {
            self.isOperator: "Operator",
            self.isKeyword: "Keyword",
            #self.isInteger: "Integer",
           # self.isFloat: "Float",
            self.isvalidIdentifier: "Identifier",
        }

    def isDelimiter(self,ch):
        if ch in self.delimiters:
            return True
        return False

    def isOperator(self,ps,pe, ch):
        if ch in self.operator:
            return True
        return False

    def isKeyword(self,ps,pe, lexeme):
        if lexeme in self.keywords:
            return True
        return False
    
    def isvalidIdentifier(self,ps,pe, lexeme):
        lex = lexeme.lstrip()
        vaild = self.alphabets+["_"]
        if len(lex) > 0:
            for i in lex:
                if i not in vaild:
                    print(errors.IdentifierError(ps,pe,"Invalid Identifier name defined","'"+lex+"'").as_string())
                    exit(self)
                else:
                    return True
        return 

    def isInteger(self,ps,pe, lexeme):
        if len(lexeme) < 0:
            return False
        for i in lexeme:
            if i in self.digits or i == "-":
                return True
        return False

    def isFloat(self,ps,pe, lexeme):
        if len(lexeme) > 0:
            return False
        for i in lexeme:
            if i in self.digits or i == "-" or i == ".":
                return True
        return False

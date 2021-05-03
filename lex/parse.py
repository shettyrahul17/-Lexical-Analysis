import token




class Parse:
    def __init__(self,code):
        self.code = code
        self.obj = token.patter()
    

    def parser(self):
        len_ = len(self.code)

        for right in range(len_):
            lex = self.code[right]
            if self.obj.isOperator(lex):
                print("<",lex,":is an operator >")
            elif self.obj.isKeyword(lex):
                print("<",lex,":is a keyword >")
            elif self.obj.isInteger(lex):
                print("<", lex,":is an integer >")
            elif self.obj.isFloat(lex):
                print("<", lex,":is a Real Number >")
            elif self.obj.isvalidIdenentifier(lex) : 
                print("<",lex,":is an identifier >")                
            elif self.obj.isDelimiter(lex):
                print("<",lex,":is an delimiter >")
            elif not self.obj.isvalidIdenentifier(lex) :
                print("<",lex,":is not an valid identifier >")
        return


    
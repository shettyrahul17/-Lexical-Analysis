import token


class Position:

    def __init__(self,idx,ln,col):
        self.idx = idx
        self.ln = ln
        self.col = col

    def move(self,current_char):
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col = 0
        return self
        
    def copy(self):
        return Position(self.idx,self.ln,self.col)

class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokenObjects = token.Tokens()
        self.len = len(self.code)
        self.pos = Position(-1,0,-1)
        self.current_char = None

    def move(self):
        self.pos.move(self.current_char) 
        self.current_char = self.code[self.pos.idx] if self.pos.idx < self.len else None
        
    def get_token_atrr(self,ch):
        attributes = self.tokenObjects.attr_
        print("hell")
        for key in attributes.keys():
            if key(ch):
                return attributes[key]
        return

    def make_tokens(self):
        tokens = {}

        while self.current_char != None:
            if self.current_char is "\t":
                self.move()
            else:
                tokens[self.current_char] = self.get_token_atrr(self.current_char)
                self.move()
        return tokens



def run(code):
    lexer = Lexer(code)
    tokens = lexer.make_tokens()

    return tokens
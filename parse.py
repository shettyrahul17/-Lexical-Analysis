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


#==============================================================
# Lexer Class
#==============================================================


class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokenObjects = token.Tokens()
        self.len = len(self.code)
        self.pos = Position(-1,0,-1)
        self.current_char = None
        self.move()

    def move(self):
        self.pos.move(self.current_char)
        self.current_char = self.code[self.pos.idx] if self.pos.idx < self.len else None
        
    def get_token_atrr(self,ch):
        attributes = self.tokenObjects.attr_
        pos_start = self.pos.ln+1
        for key in attributes.keys():
            if key(pos_start,self.pos.col,ch):
                return attributes[key]
        return

    def make_tokens(self):
        tokens = {}
        i = 0
        while self.current_char != None:
            if self.current_char == "\t":
                self.move()
            else:
                if self.tokenObjects.isDelimiter(self.code[self.pos.idx]):
                    tok = self.code[i:self.pos.idx].strip()
                    if self.get_token_atrr(tok): tokens[tok] = self.get_token_atrr(tok)
                    i = self.pos.col
                self.move()
        return tokens



def run(code):
    lexer = Lexer(code)
    tokens = lexer.make_tokens()

    return tokens
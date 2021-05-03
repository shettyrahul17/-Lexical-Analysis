import parse

string = input("Enter one line snippet[Ex:int i = a + b]: ")
tokens = parse.Parse(string.split())
tokens.parser()
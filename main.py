import parse



# To take Multiline input from user
print("Enter/Paste your code.Ctrl-Z ( windows ) to save it.")
contents = []
while True:
    try:
        line = input(">> ")
    except EOFError:
        break
    contents.append(line)


for con in contents:
    token = parse.Parse(con)
    token.parser()
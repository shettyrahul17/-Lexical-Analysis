import parse
import token



# To take Multiline input from user.
print("Enter/Paste your code.Ctrl-Z ( windows ) to save it.")
contents = []
while True:
    try:
        line = input(">> ")
    except EOFError:
        break
    contents.append(line)

result = parse.run(contents)
print(result)
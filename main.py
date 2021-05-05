import parse
import token



# To take Multiline input from user.
print("Enter/Paste your code.Ctrl-Z ( windows ) to save it.")
contents = ""
while True:
    try:
        contents += input(">> ") + "\t"
    except EOFError:
        break

result = parse.run(contents)
print(result)

import parse
import token


<<<<<<< HEAD
=======
#nithin
>>>>>>> f379c722a4f4805cee94246e3910f464267475ff
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

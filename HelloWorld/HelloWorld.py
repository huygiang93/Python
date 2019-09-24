firstName = "Huy "
lastName = "Giang"
fullName = firstName + " " + lastName

def countws(name):
    whitespace = 0
    for i in name:
        if i == " ":
            whitespace = whitespace + 1
        else:
            continue
        return whitespace


print("Hello, %s"%firstName)
print(len(fullName))
print("number of whitespace:%d"%countws(fullName))
print(len(fullName) - countws(fullName))

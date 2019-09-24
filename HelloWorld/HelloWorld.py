firstName = "Huy"
lastName = "Giang"
fullName = firstName + " " + lastName

def countws(string):
    whitespace = 0
    for i in string:
        if (i.isspace() == True):
            whitespace+=1
    return whitespace
        


string0 = "Hello, %s"%fullName

print(string0)
#print("length of string: %d"%len(string0))
print("number of whitespace: %d"%countws(string0))

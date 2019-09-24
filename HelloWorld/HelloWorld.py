

firstName =input("Enter your first name: ")
lastName = input("Enter your last name: ")

def autoCap(string):
    if string[0].islower():
        return string[0].upper() + string[1:len(string)]

autoCap(firstName)
autoCap(lastName)
fullName = autoCap(firstName) + " " + autoCap(lastName)


def countws(string):
    whitespace = 0
    for i in string:
        if (i.isspace() == True):
            whitespace+=1
    return whitespace
        


string0 = "Hello, %s"%fullName

print(string0)
print("length of string: %d"%len(string0))
print("number of whitespace: %d"%countws(string0))
print("length w/o whitespace: %d"%(len(string0) - countws(string0)))
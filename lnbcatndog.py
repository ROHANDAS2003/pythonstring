str = input("Enter a string:\n")
str = str.lower()

if "cat" in str:
    indx = str.index("cat")
    if str[indx+3:indx+6]=="cat":
        print("False")
    else:
        print("True")
elif "dog" in str:
    indx = str.index("dog")
    if str[indx+3:indx+6]=="dog":
        print("False")
    else:
        print("True")
else:
    print("False")

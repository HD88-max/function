string = input("Enter a word: ").upper()
for i in string:
    print(i,end="=")
    if i == "A":
        print("A found",)
        break
    else:
        print("Not found")
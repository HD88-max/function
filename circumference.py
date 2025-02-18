def circumference(n):
    if n>0:
        return 2*3.14159*n
    else:
        print(False)
n = int(input("Give the radius of a circle: "))
print(circumference(n))
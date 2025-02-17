# Define a function to find a cube and define another function which let execute the cube function if the number is divisible by 3
def cube1(n):
    return n*n*n
def cube2(n):
    if n%3==0:
        return cube1(n)
    else:
        return False
n = int(input("Enter a number: "))
print(cube2(n))
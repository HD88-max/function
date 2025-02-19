def shutdown(n):
    return "SHUTTING DOWN"
n = input("Do you want to shutdown(y for yes and n for no): ").upper()
if n == "Y":
    print(shutdown(n))
elif n == "N":
    print("Shutdown cancelled")
else:
    print(False)
#error handling or exception handling
#control over the error in programs


#error in program
#print(x)

#solution
try:
    print(x)
except NameError:
    print("x is not defined")
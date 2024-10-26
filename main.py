def printPyramid(x):
    for i in range(1,x+1):
        print((i*2)-1,end="")
    pass
def main():
    x = int(input("Enter number of rows: "))
    printPyramid(x)
    
main()
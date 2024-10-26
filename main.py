# O(x*i), x*i being the product of number of rows and elements in each row 
def printPyramid(x):
    # O(x), x being the input by user
    for i in range(1, x + 1):
        # reset each row to empty array
        row = []
        # O(i), i being the number of numbers in a row
        for j in range(i):
            # add odd numbers to row based on j
            row.append(str(2 * j + 1))
        # convert array to a string and print it
        print(" ".join(row))
def main():
    try:
        x = int(input("Enter number of rows: "))
        printPyramid(x)
    except ValueError:
        print("Enter an integer")
main()
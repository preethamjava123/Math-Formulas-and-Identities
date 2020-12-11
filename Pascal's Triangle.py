import math
def pascaltriangle():
    print("Enter the last row of Pascal's Triangle you would like to see: ")
    pascalrow = int(input())
    ans = ""
    for i in range(pascalrow+1):
        for j in range(i+1):
            x = int(math.factorial(i)/(math.factorial(j)*math.factorial(i-j)))
            ans += str(x) + "\t"
        ans += "\n"
    print()
    print(ans)
pascaltriangle()
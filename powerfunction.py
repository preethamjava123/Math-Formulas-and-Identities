x = int(input())
def power2(x):
	if(x == 0):
		return 1
	else:
		return(2 * power2(x - 1))

n = int(input())
def power(n):
	if(n == 0):
		return 1
	else:
		return(x * power(n - 1))

print(power(n))
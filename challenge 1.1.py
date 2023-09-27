# Implementing recursive function to find the factorial of number
def recursive_fact(n):
  if n==0 or n==1:
    return 1
  else:
    return n*recursive_fact(n-1)
number=4
result=recursive_fact(number)
print("The Factorial of {} is {}".format (number, result))
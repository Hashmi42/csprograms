#  File: Goldbach.py

#  Description:

#  Student Name: Logan Hashmi

#  Student UT EID: Sah4334

#  Course Name: CS 303E

#  Unique Number:51850

#  Date Created: 3-22-17

#  Date Last Modified: 3-22-17
def is_prime (n):
  if (n == 1):
    return False

  limit = int (n ** 0.5) + 1
  divisor = 2
  while (divisor < limit):
    if (n % divisor == 0):
      return False
    divisor += 1
  return True

def Goldbach():
    lower= int(input("Enter the lower limit: "))
    upper= int(input("Enter the upper limit: "))
    while lower>=upper or lower<=3 or lower%2!=0 or upper%2!=0:
        lower = int(input("Enter the lower limit: "))
        upper = int(input("Enter the upper limit: "))

    for i in range(lower,upper+1,2):
        output = str(i) + " = "
        for j in range(i):
            if is_prime(j):
                for k in range(j,i):
                    if is_prime(k) and k+j==i:
                        output+=str(k)+" + "+str(j)+" = "
        print(output[:-2])

Goldbach()

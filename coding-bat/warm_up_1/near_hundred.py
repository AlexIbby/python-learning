# Problem

#Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

def near_hundred(n):
  for number in range(90,111,1):
    if number == n:
      return True 
  for number in range(190,211,1):
    if number == n:
      return True
  else:
    return False 

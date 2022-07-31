#Problem

#The parameter weekday is true if it is a weekday, and the parameter vacation is true if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return true if we sleep in.


def sleep_in(weekday, vacation):
  if weekday == False:
    return True 
  if vacation == True:
    return True 
  if weekday == True and vacation == False:
    return False 
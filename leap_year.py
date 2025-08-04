
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4 == 0 and year%100 != 0 :
        return True
    elif year%400 == 0 :
        return True
    else:
        return leap

year = int(input("Enter a year: "))
print(is_leap(year))
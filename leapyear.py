check_year = int(input("Please input a year for checking if it is leap or not: "))

if (check_year % 4 == 0) and (not (check_year % 100 == 0) or  (check_year % 400 == 0)):
    print(check_year, " is a leap year.")
else:
    print(check_year, " is not a leap year!")


# # METHOD-2: Shortest solution (wihtout any if-else block or loop)

check_year = int(input("Please input a year for checking if it is leap or not: "))

print((check_year % 4 == 0) and (not (check_year % 100 == 0) or  (check_year % 400 == 0)))


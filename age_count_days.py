# By Tiffany Souterre
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#



def findBissextileYears (start_year, end_year):
    bissextile_years = 0

    for year in range(start_year, end_year):
        if isBissextile(year) == True:
            bissextile_years = bissextile_years + 1

    return bissextile_years

def numberOfDaysBtwYear (start_year, end_year):
    bissextile_years = findBissextileYears(start_year, end_year)
    number_of_days_btw_year = bissextile_years * 366 + ((end_year - start_year) - bissextile_years) * 365

    return number_of_days_btw_year

def isBissextile (year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def countDaysSinceStartYear (day, month, year):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    nbr_of_days = 0

    for m in range(0, month - 1):
        nbr_of_days = nbr_of_days + months[m]
    nbr_of_days = nbr_of_days + day
    if isBissextile(year) == True and month > 2:
        nbr_of_days = nbr_of_days + 1

    return nbr_of_days

def daysBetweenDates (year1, month1, day1, year2, month2, day2):
    return numberOfDaysBtwYear(year1, year2)- countDaysSinceStartYear(day1, month1, year1) + countDaysSinceStartYear(day2, month2, year2)



#Test routine
def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed",result, answer
        else:
            print "Test case passed!"

test()

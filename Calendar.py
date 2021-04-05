# Assignment 7: Calendar.py

def leap_year(y):
    # THIS WORKS
    #print('leap_year:debug')
    is_leap_year = 0
    if y % 4 == 0:
        is_leap_year += 1
        if y % 100 == 0:
            if y % 400 == 0:
                is_leap_year += 1
            else:
                is_leap_year = 0
    if is_leap_year > 0:
        return True
    else:
        return False
    
def number_of_days(m, y):
    # THIS WORKS
    #print('number_of_days:debug')
    days = 0
    if m > 0 and m <= 12:
        if m < 8 and m % 2 == 0 and m != 2:
            days = 30
        elif m < 8 and m % 2 == 1:
            days = 31
        elif m > 7 and m % 2 == 1:
            days = 30
        elif m > 7 and m % 2 == 0:
            days = 31
        elif m == 2:
            if leap_year(y):
                days = 29
            else:
                days = 28
    
    return days

def days_left(d, m, y):
    #print('days_left:debug')
    total_days = 0
    day_of_year = 0
    remaining_days = 0
    for i in range(13):
        total_days += number_of_days(i, y)
    for i in range(m+1):
        if i == m:
            day_of_year += d
        else:
            day_of_year += number_of_days(i, y)
    remaining_days = total_days - day_of_year
    
    return remaining_days
    
    
def main():
    #print('main:debug')
    print('Please enter a date')
    day = int(input('Day: '))
    month = int(input('Month: '))
    year = int(input('Year: '))
    print('Menu:')
    print('1) Calculate the number of days in the given month.')
    print('2) Calculate the number of days left in the given year.')
    selection = int(input(''))
    
    if selection == 1:
        print(number_of_days(month, year))
    elif selection == 2:
        print(days_left(day, month, year))
    
main()


day = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]                               #Days list
mon = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"] #Months list
m_30 = ["Apr","Jun","Sep","Nov"]                                                #Days with 30 days
m_31 = ["Jan","Mar","May","Jul","Aug","Oct","Dec"]                              #Days with 31 days
def first_day(g_year):                                                          #function for first day in the year
    s_year = 1901                                                               #Starting year is 1901
    t_years = (g_year - 1) - s_year
    l_years = t_years//4
    t_days = (t_years - l_years)*365 + l_years*366 + 1
    d = t_days%7                                            #remainder as index for starting day
    f_d = ["Tue","Wed","Thu","Fri","Sat","Sun","Mon"]       #Days list as starting day "Tue" in 1901
    return f_d[d]                                           #return starting day of any year 
def leap_year(g_year):                                      #function for Leap Year determination
    if g_year%4 == 0 and g_year%100 != 0 or g_year%400 == 0:#conditions for leap year
        return 29
    else:
        return 28
def space(day):                                             #function for space before asterisk in particular day
    l_d = len(str(day))
    if l_d == 1:
        return 1
    else:
        return 0
while True:                                                         #while loop for year validation from 1901 to 2099
    try:
        y = int(input("Give a Year:  "))                            #Input year
    except ValueError:
        continue
    if y >= 1901 and y <= 2099:
         break
    else:
        print("Give a year from 1901 to 2099")
while True:                                                         #while loop for month validation from 1 to 12
    try:
        m = int(input("Choose a month: "))                          #Input month
    except ValueError:
        continue
    if m >= 1 and m <= 12:
         break
    else:
        print("Give a month from 1 to 12")            
while True:                                         #while loop for day validation from 1 to 28, 29, 30 or 31
    try:
        d = int(input("Choose a day :   "))         #Input day no.
    except ValueError:
        continue
    if m == 2 and d >= 1 and d <= leap_year(y):     #conditions for February with or without leap year
        break
    elif m in [4, 6, 9, 11] and d in range(1, 31):  #conditions for month with 30 days i.e. 1 = Jan, 2 = Feb...
        break
    elif m in [1, 3, 5,7,8,9,10,12] and d in range(1, 32):      #conditions for month with 31 days
        break
    else:
        print("Give a valid day in the range for ", mon[m-1] )                                                

m_no = 0                        # Month index as m_no = 0 for January
start = first_day(y)            #return of first day for specific year
condition = True
while condition:                #while loop for calculating January to specific month of the given year
    fdi = day.index(start)      #first day index as fdi for next month's first day calculation
    if mon[m_no] in m_30:       #to check 30 days length month
        length = 30
    elif mon[m_no] in m_31:     #to check 30 days length month
        length = 31     
    else:                       #to check 28 or 29 days for February
        length = leap_year(y)   #leap_year(y) returns 29 days for leap year or 28 days for general year
   
    r = (length + fdi)%7        #index for next month's first day calculation
    d_next = day[r]
    start = d_next              #assigning first day for next month
    m_no += 1                   #increment of month upto the given month
    if m_no == m:               #condition to print the specific month
        print(" "*7, mon[m_no-1], y)
        for k in day:
            print(k, end = " ")
        print(end = "\n")
        print(f"    "*fdi, end = "")      #to print spaces at the beginning of the month for days with no date
        s = space(d)                      # space(d) returns 0 or 1 for space before (*) asterisk day
        for j in range(1, length + 1):
            if j == d:
                print(" "*s,"*",j,sep = "",  end = " ")  #to print day with asterisk
            else:
                print(f"{j:3d}", end = " ")              #to print all others days
            
            if (j+ fdi)%7 ==0:                           #to print new line after every 7 days
                print(end = "\n")
        condition = False                                #terminate while loop when m_no == given month m        
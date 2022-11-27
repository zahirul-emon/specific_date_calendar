day = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]                               #Days list
mon = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"] #Months list
m_30 = ["Apr","Jun","Sep","Nov"]                                                #Days with 30 days
m_31 = ["Jan","Mar","May","Jul","Aug","Oct","Dec"]                              #Days with 31 days
y = int(input("Give a Year:  "))                                                #Input year
m = int(input("Give a Month: "))                                                #Input month no.
d = int(input("Give a Day:   "))                                                #Input day no.
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
m_no = 0                        # Month index as m_no = 0 for January
start = first_day(y)            #return of first day for specific year
condition = True
while condition:
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
    if m_no == m:               #condition for given month printing
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
                 

       

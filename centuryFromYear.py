print("what is 1/10 in Python:"     ,      1/10    )# ex  1 / 10 -> 0.1
# integer cast
print("1/10 with an integer cast:  ", int( 1/10 )  )#  int( 1/ 10 ) -> 0

print( 10 / 3 )
print( int( 10/3 ) )

# 1    ->    1st century
# 33   ->   1st century
# 100  ->   1st century
# 1900 -> 19 th century
# 1901 -> 20 th century
# 2000 -> 20 th century




# which one will be the most helpful ??
print( "div by 1000 ==", 5000 / 1000 )
print( "div by 1000 ==", 5000 / 100 )  # <- most helpful , why ??? almost Determines century ?
print( "div by 1000 ==", 5000 / 10 )
print("div by 1000 ==",  5000 / 1 )



# year = 1     ->   1st century
print( 1/100 )
# year = 33    ->   1st century
print( 33/100 )
# year = 100   ->   1st century
print( 100/100 )
# year = 101   ->   2nd century
print( 101/100 )


# year = 1805 -> 19 th century
print( "1805 % 100 ", 1805 % 100)  # 5
# year = 1888 -> 19 th century
print( "1888 % 100 ", 1888 % 100)  # 88
# year = 1891 -> 19 th century
print( "1891 % 100 ", 1891 % 100)  # 91


# year = 1901 -> 20 th century
# year = 1950 -> 20 th century
# year = 2000 -> 20 th century


# year = 5010 -> 51 st century
# year = 5070 -> 51 st century
# year = 5088 -> 51 st century


def centuryFromYear(year):
    # Hints: 
    #   if - elif - else statement
    #   mod       operator  
    #   int()     function 

    # what do we know:
    # 1.) century is 100 years 
    # 2.) max year is 2005 

    # notes:
    # - noticing that when the year is perf its correct 
    # - off by 1 bug when the ones or tens place is filled up

    rounded_century = int(year / 100)
    remainder = year % 100

    if remainder > 0:
        return rounded_century + 1

    else:
        return rounded_century



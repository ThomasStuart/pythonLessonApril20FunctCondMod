# How do we create an EMPTY list in python ?
container = []  # by putting square brackets on the RHS of equal sign

print( "print the empty list elements: ", container )

# How do we create an NON-empty list in python ?
non_empty_list = [1,2,3]  # by putting square brackets on the RHS of equal sign
                          # also,  put data seperated bu comma's

print( "print the non-empty list  of elements: ", non_empty_list )

# is there a limit to the size of a list ? Yes, it is determined by your computer memeory
                                            # however, its very hard to get there

# Python allows lists to store data of differnt types
list_of_differnt_types = [ 1 ,   'C',  "string",       True,   3.14 ]
                        # int , char , string  , boolean  ,  float
print(list_of_differnt_types )


# indexing - grab an element from the list
# in most programming  languages (C++, java , python ).  Lists are "ZERO indexed"
print( "non_empty_list @ index 0 == " , non_empty_list[0] ) # start grabbing values at 0
print( "non_empty_list @ index 1 == " , non_empty_list[1] )
print( "non_empty_list @ index 2 == " , non_empty_list[2] )
# IndexError: list index out of range
# print( "non_empty_list @ index 3 == " , non_empty_list[3] ) # ERROR ? WHY , theres no 4th element


# Question, how can we determine if the index is within a range that doesnt cause an error ?
index = 3

if  index   <  len( non_empty_list ) :
    print( "it is okay to print, passed the check: ", non_empty_list[index] )
else:
    print("BAD index, will blow up the compiler.")

# len() - its a function, that returns the size of a list
print ( "len( container )" , len( container ) )
print("what is the length of the non-empty list ?? " , len( non_empty_list )  )
print("len( list_of_differnt_types) ==  ", len( list_of_differnt_types ) )

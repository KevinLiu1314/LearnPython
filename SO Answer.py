months = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31,
          "June": 30, "July": 31, "August": 31, "September": 30, "October": 31,
          "November": 30, "December": 31}

def mykey(t):
    """ Customize your sorting logic using this function.  The parameter to
    this function is a tuple.  Comment/uncomment the return statements to test
    different logics.
    """
    return t[1]              # sort by number of days in the month
    #return t[1], t[0]       # sort by number of days, then by month name
    #return len(t[0])        # sort by length of month name
    #return t[0][-1]         # sort by last character of month name

# Since a dictionary can't be sorted by value, what you can do is to convert
# it into a list of tuples with tuple length 2.
# You can then do custom sorts by passing your own function to sorted().
months_as_list = sorted(months.items(), key=mykey, reverse=False)

for month in sorted(months):
    print month

for month in months_as_list:
    print month

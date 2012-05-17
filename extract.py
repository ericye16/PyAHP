
#This file will contain the mappings of data to location they are stored in.
#The location will be given as a tuple:
        #(row, column, number of digits, decimal place, units)

#Please note: mappings are zero-indexed, lengths are lengths.

#note regarding decimal place: 0 means no decimal, 1, means one from the right,
#2 means two from the right, etc.

mapping = {'AP': (0, 0, 2, 0, 'None'),
           'GTS': (0, 2, 3, 0, 'None'),
           'Page': (0, 5, 1, 0, 'None'),
           'Time': (0, 6, 4, 0, 'None'),
           'Weather': (0, 10, 0, 'Check'),
           

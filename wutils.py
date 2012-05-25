

# The titles of the columns.
frow = ['GTS', 'AP9', 'AP10', 'AP11', 'AP12', 'AP13']
# AP8 reading capability is not good enough to be included.

def writeToCSV(data, filename):
    '''Take data, as a 2D list, and write it to filename.csv'''

    import csv
    writer = csv.writer(open(filename + '.csv', 'wb'))
    
    writer.writerow(frow)
    writer.writerows(data)


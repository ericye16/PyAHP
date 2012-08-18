

# The titles of the columns.
from util import listAP
frow = ['GTS']
allAPs = listAP()
allAPs = ['AP{0}'.format(x) for x in allAPs] #convert to string
frow.extend(allAPs)


def writeToCSV(data, filename):
    '''Take data, as a 2D list, and write it to filename.csv'''

    import csv
    writer = csv.writer(open(filename + '.csv', 'wb'))
    
    writer.writerow(frow)
    writer.writerows(data)


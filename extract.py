
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
           'Weather': (0, 10, 0, 'Check'), #Check means you have to refer to other sheets
           'DO': (1, 26, 5, 0, 'ppm'),
           'Water pH': (2, 26, 4, 0, 'pH'),
           }
#TODO: This is woefully incomplete. Please finish the rest of the mappings

def getLoc(target):
    '''Takes a target, such as 'Water pH', and returns
    the location and length of the target in a .dat file.'''
    if target not in mapping:
        print "{0} is not a valid field.".format(target)
    else:
        return mapping[target][:3]

def extract(target, AP, GTS, withDec = True, asText = False):
    '''Extracts the target from the specific .dat of the specified
    AP number and GTS.
    
    If withDec is True, then a decimal will be inserted according to the mapping
    rules. Otherwise it will be given 'raw', i.e. if there was a decimal
    already in the data, it will be returned but none will be added.
    
    If asText is True, then a string will be returned with the units,
    if available. Otherwise a float value will be returned.
    '''
    from read import openFile
    stationdata = openFile(AP, GTS)
    x, y, leng = getLoc(target)
    value = float(stationdata[x][y:y+leng])

    if value = None:
        print 'Data for this target and year are not availabe.'
        return
    
    if withDec:
        if value.is_integer: #insert the decimal point
            dec = mapping[target][3]
            value /= 10^dec
            
    if asText: #return a string with units
        unit = mapping[target][4]
        if unit != 'None':
            return "{0} {1}".format(value, unit)
        else:
            return "{0}".format(value)
    else:
        return value

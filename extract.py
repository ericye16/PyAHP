
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
           'Habitat': (1, 0, 2, 0, 'Check'),

           #PROBES SOIL DATA
           'SAT-HOG': (1, 2, 2, 1, 'm'),
           'SAT-SUN': (1, 4, 3, 1, '*C'),
           'SAT-SHA': (1, 7, 3, 1, '*C'),
           'SWT1': (1, 10, 3, 1, '*C'),
           'SWT2': (1, 13, 3, 1, '*C'),

           #PROBES WATER DATA
           'HYPRO2': (1, 16, 3, 1, '*C'),
           'HYPRO4': (1, 19, 3, 1, '*C'),
           'HYPRO6': (1, 22, 3, 1, '*C'),
           'HYPRO8': (2, 0, 3, 1, '*C'),
           'HYPRO1': (2, 3, 3, 1, '*C'),

           #PROBES SUN SOIL TEMPERATURES
           'STSL-S': (2, 6, 3, 1, '*C'),
           'STSL-2': (2, 9, 3, 1, '*C'),
           'STSL-4': (2, 12, 3, 1, '*C'),
           'STSL-6': (2, 15, 3, 1, '*C'),
           'STSL-8': (2, 18, 3, 1, '*C'),
           'STSL-1': (2, 21, 3, 1, '*C'),

           #PROBES SHADE SOIL TEMPERATURES
           'STSH-S': (3, 0, 3, 1, '*C'),
           'STSH-2': (3, 3, 3, 1, '*C'),
           'STSH-4': (3, 6, 3, 1, '*C'),
           'STSH-6': (3, 9, 3, 1, '*C'),
           'STSH-8': (3, 12, 3, 1, '*C'),
           'STSH-1': (3, 15, 3, 1, '*C'),

           #TDS and TUR
           'TDS1': (4, 6, 3, 0, 'mg/L'),
           'TDS2': (4, 9, 3, 0, 'mg/L'),
           'TUR1': (4, 12, 3, 0, 'NTU'),
           'TUR2': (4, 15, 3, 0, 'NTU'),

           #ALBEDO
           #okay actually I'll do that later. I have a request from IoO's to do the images.

           #IMAGES
           #Targets that are DSCN numbers must end in 'IMG'           
           'Sun Soil IMG': (4, 18, 4, 0, 'None'),
           'Shade Soil IMG': (4, 22, 4, 0, 'None'),
           'First Pan IMG': (5, 22, 4, 0, 'None'),
           #Do not encode the # of pans as an 'IMG'.
           'PanNum': (5, 20, 2, 0, 'None'),
           'VC1 IMG': (7, 22, 4, 0, 'None'),
           'VC2 IMG': (8, 0, 4, 0, 'None'),
           'GND CVR IMG': (8, 4, 4, 0, 'None'),
           'BB1 IMG': (8, 8, 4, 0, 'None'),
           'BB2 IMG': (8, 12, 4, 0, 'None'),
           'Weather IMG': (9, 0, 4, 0, 'None'),
           'DO/Soil pH IMG': (9, 4, 4, 0, 'None'),
           'PHOS/NH4 IMG': (9, 8, 4, 0, 'None'),
           'Stereo IMG': (9, 12, 4, 0, 'None'),
           '5 in 1 IMG': (9, 16, 4, 0, 'None'),
           'Chlorine IMG': (9, 20, 4, 0, 'None'),
           
           #OTHER THINGS NOT IN FDSs BUT STILL IMPORTANT
           #Eric is a n00b. :)
           'DO': (1, 26, 5, 0, 'ppm'),
           'Soil pH': (2, 26, 4, 0, 'pH'),
           'Nitrates': (3, 26, 5, 0, 'mmol'), #NOTE UNIT MAY BE INCORRECT
           'Nitrites': (4, 26, 4, 0, 'mmol'),
           'Ammonia': (5, 26, 5, 0, 'ppm'),
           'Phosphates': (6, 26, 5, 0, 'ppt'),
           'Chlorine': (7, 26, 4, 0, 'ppt'),
           'Water Hardness': (8, 26, 5, 0, 'ppt'), #Units?
           'Alkalinity': (9, 26, 5, 0, 'ppt'),
           'Water pH': (10, 26, 4, 0, 'pH'),

           #Note: I'm not sure about Water and Soil pH--it's unclear as to
           #which is which. PH vs. SP on the AHP, but Soil pH is taken with DO,
           #So I thought it'd be right after DO.

           #The official (reference) AHP lists PH and SP, and
           #I'm not quite sure which is soil pH and which is water pH. Help?
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

    Errors: If no value is found, due to lack of files or lack of data,
    None is returned.
    '''
    from read import openFile
    from ext_exceptions import isException
    import re

    if isException(target, AP, GTS):
        from exceptions import exceptionExtract
        return exceptionExtract(target, AP, GTS, withDec, asText)
    
    stationdata = openFile(AP, GTS)
    if not stationdata: #no file found
        return
    x, y, leng = getLoc(target)
    try:
        value = stationdata[x][y:y+leng]
    except:
        value = None

    #return None if it's just whitespace.
    if re.match(r'\W+$', value)is not None: #double negatives ftw.
        return
    
    if not value:
        print "No {0} data was found for AP{1}-{2}.".format(target, AP, GTS)
        return
    else:
        try:
            value = float(value) #In AP13-725, there's an H that messed this up.
        except:
            print 'Non-numeric value read:{0} for {1} in AP{2}-{3}'.format(
                value, target, AP, GTS)
            return

#I don't remember what the following is for. It looks redundant.
##    if value == None:
##        print 'Data for this target and Sample Station are not availabe.'
##        return
    
    if withDec:
        if value.is_integer(): #insert the decimal point
            dec = mapping[target][3]
            value /= 10**dec
            
    if asText: #return a string with units
        unit = mapping[target][4]
        if unit != 'None': #if there are units
            return "{0} {1}".format(value, unit)
        else:
            return "{0}".format(value) #just print the value as a string if no units
    else: #return just the value without units and as a float
        return value

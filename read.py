
def makePath(AP, GTS, t = None): #If t is not supplied, GTS
                                 #is the GTS. Else, it is the G-value.
    '''Takes an AP and GTS number and returns
    the Windows Path to the .dat file as a string.'''

    base = 'AHPDATA\\AP{0}\\'.format(AP)
    
    if t: #create directory for the traverse rather than for the specific
            #sample station
        return '{bases}FIT{0}\\T{1}'.format(GTS, t, bases = base)
    
    #Eric's a bunny
    #Disguised as a human
    #ZOMG
    #kbtw teenie was here
    #AWWWOOOOOOOOOOOOO.

    #AP13 GTS 622 should be:
    #AHPDATA\AP13\FIT6\T2\Data\13-622.dat
    else:
        G = GTS/100
        T = (GTS-G*100) / 10
        return r'{bases}FIT{1}\T{2}\Data\{3}-{4}.dat'.format(\
            AP, G, T, AP, GTS, bases = base)

def openFile(AP, GTS):
    '''Open the .dat file and split it.'''
    loc = makePath(AP, GTS)
    with open(loc, 'r') as fil:
        f = fil.read().split()
    return f

def existGTS(AP, GTS):
    '''Check if a GTS and its .dat file exists.'''
    try:
        f = open(makePath(AP, GTS))
    except IOError:
        print "AP{0}-{1} does not exist.".format(AP, GTS)
        return False
    f.close()
    return True

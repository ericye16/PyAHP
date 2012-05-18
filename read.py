
def makePath(AP, GTS, t = None, pics = False): #If t is not supplied, GTS
                                 #is the GTS. Else, it is the G-value.
    '''Takes an AP and GTS number and returns
    the Windows Path to the .dat file as a string.

    If t is supplied, GTS is taken as the G-value and t the T-value.
    
    If pics is True, return a path to the images directory instead.
    For IoO people.

    If both t and pics are specified, which should never happen, pics has precedence.'''

    base = 'AHPDATA\\AP{0}\\'.format(AP)
    G = GTS/100
    T = (GTS-G*100) / 10
    S = GTS%10
    
    if pics:
        return '{bases}FIT{0}\\T{1}\\SS{2}\\Images\\Raw'.format(G, T, S, bases = base)


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
        return r'{bases}FIT{1}\T{2}\Data\{3}-{4}.dat'.format(\
            AP, G, T, AP, GTS, bases = base)

def openFile(AP, GTS):
    '''Open the .dat file and split it.'''
    loc = makePath(AP, GTS)
    try:
        with open(loc, 'r') as fil:
            f = fil.read().split() #read the file into the variable f.
    except IOError: #If the file is not there
        print "AP{0}-{1} does not exist.".format(AP, GTS)
        return
    return f

def existGTS(AP, GTS):
    '''Check if a GTS and its .dat file exists.

    Now deprecated (that was fast!) since openFile checks within the function.
    '''
    try:
        f = open(makePath(AP, GTS))
    except IOError:
        #print "AP{0}-{1} does not exist.".format(AP, GTS)
        return False
    f.close()
    return True

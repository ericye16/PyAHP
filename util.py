

############################List functions!
def listSS(AP, G, T):
    '''List the available sample stations for a given AP, FIT and Traverse.'''
    from os import listdir
    from read import makePath
    try:
        dirnames = listdir(makePath(AP, 6, T))
    except:
        return #versatility in case no such AP/G/T exists.
    dirnames.remove('Data')
    ss = [int(station[2:]) for station in dirnames]
    return ss

def listT(AP, G):
    '''List the available traverses for a given AP and FIT.

    Basically, it returns [1, 2, 3].'''

    T = range(1, 4)
    return T

def listG(AP):
    '''List the FITs for a given AP.'''
    if AP == 13:
        return range(1, 8)
    else:
        return range(1, 7)


################################Traverse functions!

###Note: for all traverse functions, remember to put the import statements
###within stmt
def traverseSS(AP, G, T, stmt):
    '''Runs 'stmt' for *all* sample stations in a given AP, G, and T.'''

    allSS = listSS(AP, G, T)
    for S in allSS:
        #provide some context for stmt to reference.
        GTS = G*100 + T*10 + S
##        try:
##            exec(stmt)
##        except:
##            print 'Error -- did not run at AP{0}-{1}.'.format(AP, GTS)
        exec(stmt)
        
def traverseT(AP, G, stmt):
    '''Runs 'stmt' for all sample stations in a given AP and G.'''

    allT = listT(AP, G)
    for T in allT:
        traverseSS(AP, G, T, stmt)

def traverseAP(AP, stmt):
    '''Runs 'stmt' for all sample stations in a given AP.'''

    allG = listG(AP)
    for G in allG:
        traverseT(AP, G, stmt)

def traverseAll(stmt):
    '''Runs 'stmt' for *all* sample stations in all APs.'''

##    for AP in range(8, 14):
##        numG = listG(AP)
##        for G in listG:
##            numT = listT(AP, G)
##            for T in numT:
##                numSS = listSS(AP, G, T)
##                for S in listSS:
##
##                    #Give stmt some context.
##                    GTS = G*100 + T * 10 + S
##                    try:
##                        exec(stmt)
##                    except:
##                        print 'Did not run properly for AP{0}-{1}'.format(AP, GTS)
    for AP in range(8, 14):
        traverseAP(AP, stmt)


####################Using the traverse functions!
def forAllAPs(target, GTS):
    '''Gets all the values of the target for all of that GTS through AP 8 - 13.
    In other words, if you wanted 'Water pH', 622, it would get you that value
    for Water pH in AP8-622, AP9-622, etc.

    Returns a  list of the format [AP8.val, AP9.val...AP13.val]. If no value
    exists, None is put in its place.
    '''

    from extract import extract

    l = [GTS]
    #AP8 is not included because I am not satisfied with
    #how PyAHP reads its data.
    for AP in range(9, 14):
        l.append(extract(target, AP, GTS))

    return l

def forAllAPsGTS(target):
    '''Gets the value of the target for all GTSs for all APs.

    Essentially, repeatedly calls forAllAPs.
    '''

    l = []
    AP = 13 #reference AP
    for G in range(1, 8):
        for T in listT(AP, G):
            for S in listSS(AP, G, T):
                GTS = G*100+T*10+S
                l.append(forAllAPs(target, GTS))
    return l


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

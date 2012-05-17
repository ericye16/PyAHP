
def listSS(AP, G, T):
    '''List the available sample stations for a given AP, FIT and Traverse.'''
    from os import listdir
    from read import makePath
    dirnames = listdir(makePath(AP, 6, T))
    dirnames.remove('Data')
    ss = [station[2:] for station in dirnames]    
    return ss

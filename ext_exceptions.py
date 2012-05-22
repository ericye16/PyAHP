
###This file will handles AP/GTSs that do not follow the structure as given in
###extract.py


###How to implement? As a large dict? Hm.


###Until a better structure is created, fill isException with exceptions,
###and make sure there is an appropriate handler-of-exception in the
###exceptionExtract function.

def isException(target, AP, GTS):
    '''True if the given target, AP and GTS require special handling.
    To do the proper extraction of excepted targets, use exceptionExtract.
    '''
    return False #We're working on it...

def exceptionExtract(target, AP, GTS, withDec = True, asText = False):
    '''If the target-AP-GTS combination is not covered by the orthodox
    extract function, this will extract it, if applicable.
    '''
    return #Also finish this.

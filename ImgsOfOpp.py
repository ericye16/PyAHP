

####MAIN
def main():
    '''Copy the images of opportunity from all/most APs into
    the folder at once.'''

    from util import listSS
    from IoOUtil import copyIoOs
    
##    for AP in range(10, 14):

    #Freedom of choice woot!
    AP = int(raw_input('Enter the AP you want to sort IoOs for: '))
    if 7<AP<14:
        if AP == 13: #Did you know that we're the only year with 7 FITs?
            numG = 7
        else:
            numG = 6
            
        for G in range(1, numG + 1):
            for T in range(4):
                numSS = listSS(AP, G, T)
                if numSS:
                    for station in numSS:
                        GTS = G*100 + T*10 + station
                        print 'Sorting AP{0}-{1}.'.format(AP, GTS)
                        pics = copyIoOs(AP, GTS)
                        if pics:
                            print 'Copied {0} Images of Opportunity from AP{1}-{2}'.\
                                  format(len(pics), AP, GTS)
    else:
        print 'Only APs 8 through 13 exist.'

if __name__ == '__main__':
    main()

def clean():
    '''This will delete all Images of Opportunities folders.
        Use this to clean up the mess if main() messes up really bad.'''

    from shutil import rmtree
    from util import listSS
    from read import makePath

    #Uh oh, I just copied-and-pasted code.
    #I guess this means I'm doing something wrong.
    for AP in range(10, 14):
        if AP == 13: #Did you know that we're the only year with 7 FITs?
            numG = 7
        else:
            numG = 6
            
        for G in range(1, numG + 1):
            for T in range(4):
                numSS = listSS(AP, G, T)
                if numSS:
                    for station in numSS:
                        GTS = G*100 + T*10 + station
                        print 'Deleting IoOs from: AP{0}-{1}.'.format(AP, GTS)
                        rmtree('{0}\Images of Opportunity'.format(
                            makePath(AP, GTS, pics = True)), True)
            

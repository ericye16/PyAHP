
def main():
    '''Copy the images of opportunity from all/most APs into
    the folder at once.'''

    from util import listSS
    from IoOUtil import copyIoOs
    
    for AP in range(8, 14):
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

if __name__ == '__main__':
    main()

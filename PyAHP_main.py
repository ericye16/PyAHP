###Main interface (finally?)

def main():
    '''Main function for PyAHP.'''

    from extract import mapping
    from util import forAllAPsGTS, forAllAPs
    from wutils import writeToCSV

    #Run on the command line so: python PyAHP_main.py HYPRO1 HYPRO2 HYPRO4 etc.
    import sys
    for wanted in sys.argv[1:]:
        if wanted in mapping:
            print 'Collecting data...'
            data = forAllAPsGTS(wanted)
            print 'Data collected. Writing to {0}.csv'.format(wanted)
            writeToCSV(data, wanted)
            print 'File written in this folder as {0}.csv'.format(wanted)
        else:
            print 'Skipped unknown mapping ', wanted
    
    while True:
        wanted = raw_input('What field?')
        if wanted not in mapping:
            print 'Please look at the README to see what fields are available.'
        else:
            break

# Too much complexity.

##    while True:
##        wantedGTS = raw_input('Specific GTS? (y/n): ')
##        if wantedGTS.lower() == 'y':
##            specificGTS = True
##            wantedGTS = raw_input('Which one? ')
##            break
##        elif wantedGTS.lower() == 'n':
##            specificGTS = False
##            break
            
    
    print 'Collecting data...'
##    if specificGTS:
##        data = forAllAPs(wanted, wantedGTS)
##    else:
##        data = forAllAPsGTS(wanted)
    data = forAllAPsGTS(wanted)
    print 'Data collected. Writing to {0}.csv'.format(wanted)
       
    writeToCSV(data, wanted)
    print 'File written in this folder as {0}.csv'.format(wanted)
    

if __name__ == '__main__':
    main()

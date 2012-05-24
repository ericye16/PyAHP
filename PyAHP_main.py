###Main interface (finally?)

def main():
    '''Main function for PyAHP.'''

    from extract import mapping
    from util import forAllAPsGTS, forAllAPs
    from wutils import writeToCSV
    
    while True:
        wanted = raw_input('What field?')
        if wanted not in mapping:
            print 'Please look at the README to see what you can look up.'
        else:
            break

    while True:
        wantedGTS = raw_input('Specific GTS? (y/n): ')
        if wantedGTS.lower() == 'y':
            specificGTS = True
            wantedGTS = raw_input('Which one? ')
            break
        elif wantedGTS.lower() == 'n':
            specificGTS = False
            break
            
    
    print 'Collecting data...'
    if specificGTS:
        data = forAllAPs(wanted, wantedGTS)
    else:
        data = forAllAPsGTS(wanted)
    print 'Data collected. Writing to {0}.csv'.format(wanted)
       
    writeToCSV(data, wanted)
    print 'File written in this folder as {0}.csv'.format(wanted)
    

if __name__ == '__main__':
    main()

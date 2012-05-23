###Main interface (finally?)

def main():
    '''Main function for PyAHP.'''

    from extract import mapping
    from util import forAllAPsGTS
    from wutils import writeToCSV
    
    while True:
        wanted = raw_input('What would you like to look for?')
        if wanted not in mapping:
            print 'Please look at the README to see what you can look up.'
        else:
            break
    
    print 'Collecting data...'
    data = forAllAPsGTS(wanted)
    print 'Data collected. Writing to {0}.csv'.format(wanted)
       
    writeToCSV(data, wanted)
    print 'File written in this folder as {0}.csv'.format(wanted)
    

if __name__ == '__main__':
    main()

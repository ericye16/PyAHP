

####MAIN
def main():
    '''Copy the images of opportunity from all/most APs into
    the folder at once.'''

    from util import traverseAP
    
    #Freedom of choice woot!
    AP = int(raw_input('Enter the AP you want to sort IoOs for: '))
    if 7<AP<14:

        code = '''
from IoOUtil import copyIoOs
print 'Sorting AP{0}-{1}.'.format(AP, GTS)
pics = copyIoOs(AP, GTS)
if pics:
    print 'Copied {0} Images of Opportunity from AP{1}-{2}'.\
          format(len(pics), AP, GTS)
'''

        traverseAP(AP, code)
    else:
        print 'Only APs 8 through 13 exist.'


def clean():
    '''This will delete all Images of Opportunities folders.
        Use this to clean up the mess if main() messes up really bad.'''

    from util import traverseAll
    code = '''
from shutil import rmtree
from read import makePath
print 'Deleting IoOs from: AP{0}-{1}'.format(AP, GTS)
rmtree('{0}\Images of Opportunity'.format(\
makePath(AP, GTS, pics = True)), True)
'''
    traverseAll(code)


if __name__ == '__main__':
    main()  


#This file will help IoO people sort out the images that are and aren't relevent.

def listImgs(AP, GTS):
    '''List the images that *have* been used by the AHP.
    In other words, the images that are *not* images of opportunity.'''

    from extract import mapping, extract
    #Select the targets that produce image numbers
    relKeys = [key for key in mapping if key[-3:] == 'IMG']
    imgs = []
    for key in relKeys:
        dscnNum = extract(key, AP, GTS)
        if dscnNum:#if the image is there
            imgs.append(str(int(dscnNum)).zfill(4))

    ##TODO: Add support for pans
    return imgs

#TODO: finish this.
def selectImgs(AP, GTS):
    '''A list of Images of Opportunity available for a given AP and GTS.'''
    from os import listdir
    from read import makePath
    import re

    #Create a list 'allPics' that stores the names of all the pictures in 'raw'
        #for the given AP and GTS.
    try:
        allPics = [picture for picture in
                   listdir(makePath(AP, GTS, pics = True))
                   if picture[-4:].upper() == ".JPG"]
        
    except: #if you can't find anything
        print "No pictures found for AP{0}-{1}".format(AP, GTS)
        return

    #for example, 'DSC_' or 'IMG_'--we only want the numbers
    head = allPics[0][:-8] 

    #strip away the head and .jpg.
    pics = [pic[-8:-4] for pic in allPics]
    #filter the images that are accounted for by the FDS
    FDSImgs = listImgs(AP, GTS)
    pics = [pic for pic in pics if pic not in FDSImgs]

    #put the header and .jpg back on:
    pics = ['{0}{1}.JPG'.format(head, pic) for pic in pics]

    print pics
    

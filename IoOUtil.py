
#This file will help IoO people sort out the images that are and aren't relevent.


############################ListImgs########
def listImgs(AP, GTS):
    '''List the images that *have* been used by the AHP.
    In other words, the images that are *not* images of opportunity.'''

    from extract import mapping, extract
    #Select the targets that produce image numbers

    #Everything labelled in mapping as IMG
    relKeys = [key for key in mapping if key[-3:] == 'IMG']
    imgs = set()
    for key in relKeys:
        dscnNum = extract(key, AP, GTS)
        if dscnNum:#if the image is there
            imgs.add(str(int(dscnNum)).zfill(4))

    #Add the other images in the pan:
    panImg = extract("First Pan IMG", AP, GTS)
    if panImg:
        numInPan = extract('PanNum', AP, GTS)
        panImg = int(panImg) #convert to integer from float
        numInPan = int(numInPan)
        for number in range(1, numInPan):
            #The first image is already there, so don't add it again.
            imgs.add(str((panImg + number) % 10000).zfill(4))

    #Add the second image of the stereo pair:
    sterImg = extract('Stereo IMG', AP, GTS)
    if sterImg:
        imgs.add(str((int(sterImg) + 1) % 10000).zfill(4))
    return imgs


#############################################SelectImgs#####
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

    if len(allPics) < 1: #in case there aren't any pictures
        return

    #for example, 'DSC_' or 'IMG_'--we only want the numbers
    head = allPics[0][:-8]

    #strip away the head and .jpg.
    pics = [pic[-8:-4] for pic in allPics]
    #filter the images that are accounted for by the FDS
    FDSImgs = listImgs(AP, GTS)
    pics = [pic for pic in pics if pic not in FDSImgs]

    #put the header and .jpg back on:
    pics = ['*{0}.JPG'.format(pic) for pic in pics]

    return pics


#########################################Copy IoOs####
def copyIoOs(AP, GTS):
    '''Copy the IoOs of an AP and GTS into a different folder.'''

    from os import mkdir
    from os.path import isdir
    from shutil import copy2
    from read import makePath
    import glob

    loc = makePath(AP, GTS, pics = True) #current pictures directory

    target = '{0}\\Images of Opportunity\\'.format(loc)


    pics = selectImgs(AP, GTS)
    print pics

    if not pics: #again, in case no images were matched
        return

    #The following line has the ability to write in the folders. Be careful.

    if not isdir(target):
        try:
            mkdir(target)
        except WindowsError:
            print '''The directory cannot be created.'''
            return

    ### TODO: ADD WILDCARD SUPPORT

    wentOn = True
    for pic in pics:
        print pic
        picFile = glob.glob('{0}\\{1}'.format(loc, pic))[0]
        print picFile
        
        try:
            copy2(picFile, target)
        except:
            print "Something happened and I'm not quite sure what, but go on anyways."
            wentOn = False #make False if something goes wrong.

    if not wentOn:
        return
    return pics #to give some info to the caller.

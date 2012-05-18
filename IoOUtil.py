
#This file will help IoO people sort out the images that are and aren't relevent.

def listImgs(AP, GTS):
    '''List the images that *have* been used by the AHP.
    In other words, the images that are *not* images of opportunity.'''

    from extract import mapping, extract
    relKeys = [key for key in mapping if key[-3:] == 'IMG']
    imgs = []
    for key in relKeys:
        dscnNum = extract(key, AP, GTS)
        if dscnNum:
            imgs.append(str(int(dscnNum)).zfill(4))
    return imgs

#TODO: finish this.

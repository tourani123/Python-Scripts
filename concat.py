
import sys
import numpy as np
from PIL import Image
import os


suss = []


indir = '/home/satyajittourani/Desktop/PScript'
for root, dirs, filenames in os.walk(indir):
    for f in filenames:
        suss.append(f)

suss.sort()

print(len(suss))
print(suss)
P = 0

while(P < (len(suss) - 2)):
        
        zList = []
        zList.append(suss[P])
        zList.append(suss[P + 1])
        zList.append(suss[P + 2])
        zList.append(suss[P + 3])
        imgs    = [ Image.open('/home/satyajittourani/Desktop/PScript' + '/' + i) for i in zList ]
        min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
        imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
        imgs_comb = Image.fromarray( imgs_comb)
        imgs_comb.save( 'Trifecta {}.jpg'.format(P) ) 
        P += 4
#print(len(suss))

'''
list_im = ['suss.jpg', 'colors.jpg', 'b.jpg', 'colors1.jpg']
imgs    = [ Image.open(i) for i in list_im ]
# pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )

# save that beautiful picture
imgs_comb = Image.fromarray( imgs_comb)
imgs_comb.save( 'Trifecta1.jpg' )    
'''

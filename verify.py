import numpy as np
from skimage import io   # scikit-image==0.16.2
images = np.load('images.npy')

# index of tiles
rows = []
cols = []
for i in range(6):
    rows += [i+1]*18
    cols += list(range(1,19)) if i%2==0 else list(range(18,0,-1))

# paste tiles
output = np.zeros((6*512,18*512),dtype=np.uint16)
for i in range(images.shape[0]):
    x0,x1 = (cols[i]-1)*512, cols[i]*512
    y0,y1 = (rows[i]-1)*512, rows[i]*512
    output[y0:y1,x0:x1] = images[i]

# imsave
io.imsave('unprocessed.tif',output)	
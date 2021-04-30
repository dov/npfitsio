from npfitsio import write_fits, read_fits
import numpy as np

a = np.array([[[0,1],[2,3]]])
write_fits(a,'/tmp/foo.fits', flip_y=False)
b = read_fits('/tmp/foo.fits', flip_y=True)
print(b)



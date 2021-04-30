# numpy fits simplified io interface for np arrays
#
# Copyright (c) 2021 Dov Grobgeld <dov.grobgeld@gmail.com>
#
#
# This library is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation; either version 2.1 of the License, or (at your
# option) any later version.
# 
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
# for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with this library; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
#
from astropy.io import fits as pyfits
import os

def write_fits(ary, filename, flip_y=False):
  if os.path.exists(filename):
    os.unlink(filename)
  hdul = pyfits.HDUList()
  hdul.append(pyfits.ImageHDU())
  if flip_y:
    if len(ary.shape)==2:
      ary = ary[::-1,:]
    elif len(ary.shape)==3:
      ary = ary[:,::-1,:]
    else:
      raise RuntimeError('Can only flip_y for 2D and 3D arrays!')

  hdul[0].data = ary
  
  hdul.writeto(filename)    

def read_fits(fits_filename, flip_y=False):
  ary = pyfits.open(fits_filename)[0].data

  if flip_y:
    if len(ary.shape)==2:
      ary = ary[::-1,:]
    elif len(ary.shape)==3:
      ary = ary[:,::-1,:]
    else:
      raise RuntimeError('Can only flip_y for 2D and 3D arrays!')

  return ary

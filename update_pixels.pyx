from cpython cimport array
from cython import boundscheck
from cython.parallel import parallel, prange

cdef int width = 1024 
cdef int height = 960

@boundscheck(False)
def paint_pixels_per_circle(int h, int k, int rad, int rc, int gc, int bc, int[:] ri, int[:] gi, int[:] bi):
    cdef int i
    cdef int j

    for i in range(height):
      for j in prange(width, nogil=True):
         if ((j-h)**2 + (i-k)**2 <= rad**2):
            ri[j + i*width] = ri[j + i*width] ^ rc
            gi[j + i*width] = gi[j + i*width] ^ gc 
            bi[j + i*width] = bi[j + i*width] ^ bc 
    return ri, gi, bi
import array
from multiprocessing import Pool

width = 1024
height = 960

# DESC: Escribe la imagen
# NOTES: Utilizar solo una vez
# def writePPM(red, green, blue, width, height, filename):
def writePPM(red, green, blue, filename):
  ppm_header = f'P6 {width} {height} {255}\n'
  rgb = []
  for i in range(len(red)):
      rgb.append(red[i]) # Red 
      rgb.append(green[i]) # Green 
      rgb.append(blue[i]) # Blue
  image = array.array('B', rgb)

  with open(filename + '.ppm', 'wb') as f:
    f.write(bytearray(ppm_header, 'ascii'))
    image.tofile(f)

def initializer():
  r = []
  g = []
  b = []

  for _ in range(width*height):
    r.append(0)
    g.append(0)
    b.append(0)
  
  return r, g, b

# NOTES: Lo mandamos a cython
# def paint_pixels_per_circle(h, k, rad, rc, gc, bc, ri, gi, bi):

#   for i in range(height):
#     for j in range(width):
#        if ((j-h)**2 + (i-k)**2 <= rad**2):
#           ri[j + i*width] = ri[j + i*width] ^ rc
#           gi[j + i*width] = gi[j + i*width] ^ gc 
#           bi[j + i*width] = bi[j + i*width] ^ bc 

#   return ri, gi, bi

# def paint_pixels_per_circle(circle):

#     h = circle[0]
#     k = circle[1]
#     rad = circle[2]
#     rc = circle[3]
#     gc = circle[4]
#     bc = circle[5]
#     ri = circle[6]
#     gi = circle[7]
#     bi = circle[8]

#     for i in range(height):
#       for j in range(width):
#          if ((j-h)**2 + (i-k)**2 <= rad**2):
#             ri[j + i*width] = ri[j + i*width] ^ rc
#             gi[j + i*width] = gi[j + i*width] ^ gc 
#             bi[j + i*width] = bi[j + i*width] ^ bc 

#     return ri, gi, bi

if __name__ == "__main__":

    # circles = 5

    data = [[500,231,30,27, 242, 31],[20,800,50,27, 69, 242],[512,480,100,241, 8, 8],[900,600,18,241, 8, 8]]

    r, g, b = initializer()

    for circle in data:
      r, g, b = paint_pixels_per_circle(circle[0],circle[1],circle[2],circle[3],circle[4],circle[5],r, g, b)

    # with Pool() as pool:
    #     pool.map(paint_pixels_per_circle, data)

    
    writePPM(r, g, b, "circles")





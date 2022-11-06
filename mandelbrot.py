from PIL import Image
import numpy as np

DEPTH = 1000 # how precise the check will be to see if number is in mandelbrot set: increase this when zooming in more to the set

def is_in_mandelbrot(real_c, imag_c): # function to check if a number is in the mandelbrot set

    c = complex(real_c, imag_c)
    z = c

    for i in range(1, DEPTH+1):

        z = z*z + c # perform the step of the iterative sequence
        if z.real*z.real + z.imag*z.imag > 4: # rather than abs(z) > 2, avoid taking the square root as it is a slow operation
            return 0.5 * (1 + 1/i)
    
    else:
        return 0

    
IMAGE_WIDTH, IMAGE_HEIGHT = 1200, 800
ACTUAL_WIDTH, ACTUAL_HEIGHT = 3, 2

SCALE = int(IMAGE_WIDTH / ACTUAL_WIDTH) # how many times smaller the mathematical dimensions are than the screen dimensions

X_SHIFT = -2
Y_SHIFT = -1

set_array = np.zeros((IMAGE_HEIGHT, IMAGE_WIDTH)) # initialize the array to all be zeros

for y in range(IMAGE_HEIGHT):

    for x in range(IMAGE_WIDTH):
        real = x / SCALE + X_SHIFT
        imag = -y / SCALE - Y_SHIFT

        set_array[y][x] = is_in_mandelbrot(real, imag)
        
set_array = (set_array*255).astype(np.uint8) # multiply values by 255 to produce an array which can create an image

picture = Image.fromarray(set_array)
picture.show()

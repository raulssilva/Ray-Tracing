from utils.ppm import PPM
from utils.progress_bar import ProgressBar

img_width = 256
img_height = 256

progress_bar_render = ProgressBar('Rendering', img_height*img_width)

ppm = PPM(img_width, img_height, 255)

for x in range(ppm.width-1, -1, -1):
    for y in range(0, ppm.height):
        r = y/(ppm.height-1)
        g = x/(ppm.width-1)
        b = 0.25

        pixel = {
            'r': int(255.999*r),
            'g': int(255.999*g),
            'b': int(255.999*b)
        }
        ppm.add_pixel((x-ppm.width+1)*-1, y, pixel)

        progress_bar_render.update()

progress_bar_render.finish()

ppm.save_file()
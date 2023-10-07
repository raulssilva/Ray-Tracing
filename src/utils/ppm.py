from datetime import datetime
from .progress_bar import ProgressBar

class PPM:

    image = []
    
    def __init__(self, width, height, color_range):
        self.width = width
        self.height = height
        self.color_range = color_range

        for i in range(0, width):
            line = []
            for j in range(0, height):
                pixel = {
                    'r': 0,
                    'g': 0,
                    'b': 0
                }
                line.append(pixel)
            self.image.append(line)
    
    def add_pixel(self, x, y, pixel):
        self.image[x][y] =  pixel
    
    def save_file(self, file_name=None):
        file_dir = '../img/'

        if (file_name == None):
            file_name = datetime.now().strftime('%Y%m%d-%H%M%S.ppm')
        
        file = open(file_dir + file_name, 'w+')
        file.write('P3\n')
        file.write('{} {}\n'.format(self.width, self.height))
        file.write(str(self.color_range) + '\n')
        
        progress_bar = ProgressBar('Saving', self.height*self.width)
        for x in range(0, self.width):
            for y in range(0, self.height):
                file.write(str(self.image[x][y]['r']) + ' ' + str(self.image[x][y]['g']) + ' ' + str(self.image[x][y]['b']) + '\n')
                progress_bar.update()
        file.close()
        progress_bar.finish()
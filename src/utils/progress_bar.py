import sys

class ProgressBar():

    def __init__(self, message, size, toolbar_width=40):
        self.toolbar_width = toolbar_width
        self.size = size
        sys.stdout.write((message + "... [%s]") % (" " * toolbar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (toolbar_width+1))
        self.rendering_flag = 0
        self.counter = 1

    def update(self):
        self.counter += 1

        if (int((self.counter*40)/(self.size)) != self.rendering_flag):
            self.rendering_flag = int((self.counter*40)/(self.size))
            sys.stdout.write(u'\u2585')
            sys.stdout.flush()
    
    def finish(self):
        sys.stdout.write("]\n")
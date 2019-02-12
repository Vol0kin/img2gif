import os               # os.listdir
import os.path          # os.path.isfile
import imageio

supported_formats = ('.jpg', '.png')

class GifConverter:
    def __init__(self, in_dir = '.', out_file = 'out.gif'):
        self.image_list = []
        self.input_dir = input_dir
        self.output_file = out_file

    def read_images(self):
        # Get all the images that are stored in the directory
        self.image_list = [imageio.imread(img) for img in os.listdir(self.input_dir) if os.path.isfile(img)
                           if img.endswith(supported_formats)]
        # Sort the images so they are in order
        self.image_list.sort()

    def convert_img_gif(self):
        imageio.mimsave(self.out_file, self.image_list)

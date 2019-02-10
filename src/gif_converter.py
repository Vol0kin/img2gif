import os
import imageio

class GifConverter:
    def __init__(in_dir, out_file="out.gif"):
        self.image_list = []
        self.input_dir = input_dir
        self.output_file = out_file

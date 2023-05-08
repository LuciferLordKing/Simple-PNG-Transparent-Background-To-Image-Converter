#!/usr/bin/env python3
from PIL import Image
import argparse, sys

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input-filename', help='The Full Input Filename (Must Be *png)')
parser.add_argument('-a', '--background-opacity', help='The alpha value a of the background pixels where 0 ≤ a ≤ 255 (Default: 255)')
parser.add_argument('-o', '--output-filename', help='The Full Output Filename (Default: shadow-art.png)')

if parser.parse_args().input_filename is None:
    filename = input('input-filename: ')
else:
    filename = parser.parse_args().input_filename

with Image.open(filename, 'r') as im:
    if not im.filename.endswith('.png'):
        sys.exit('File extension is not PNG.')

    if parser.parse_args().background_opacity is None:
        opacity = int(input('background-opacity[255]: ') or 255)
    else:
        opacity = int(parser.parse_args().background_opacity)

    pixels = im.load()
    background_colour = tuple()
    while len(background_colour) != 4:
        background_colour = tuple(map(int, (input('background-colour[0, 0, 0]: ') or '0, 0, 0').split(','))) + (opacity, )
    image_colour = tuple()
    while len(image_colour) != 4:
        image_colour = tuple(map(int, (input('image-colour[0, 0, 0, 0]: ') or '0, 0, 0, 0').split(',')))

    for i in range(im.size[0]):
        for j in range(im.size[1]):
            if pixels[i, j][3] == 0:
                pixels[i, j] = background_colour
            else:
                pixels[i, j] = image_colour

    if parser.parse_args().output_filename is None:
        out = input('output-filename[shadow-art.png]: ') or 'shadow-art.png'
    else:
        out = parser.parse_args().output_filename

    im.save(out)
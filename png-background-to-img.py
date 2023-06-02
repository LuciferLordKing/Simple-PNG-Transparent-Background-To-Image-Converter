#!/usr/bin/env python3
from PIL import Image
import argparse, sys

def get_input_filename():
    return input('input-filename: ')

def get_background_opacity():
    return int(input('background-opacity[255]: ') or 255)

def get_background_colour(opacity):
    colour = input('background-colour[0, 0, 0]: ') or '0, 0, 0'
    return tuple(map(int, colour.split(','))) + (opacity, )

def get_image_colour():
    colour = input('image-colour[0, 0, 0, 0]: ') or '0, 0, 0, 0'
    return tuple(map(int, colour.split(',')))

def get_output_filename():
    return input('output-filename[shadow-art.png]: ') or 'shadow-art.png'

def process_image(input_filename, background_colour, image_colour, output_filename):
    with Image.open(input_filename) as im:
        if not im.filename.endswith('.png'):
            raise ValueError('File extension is not PNG.')

        pixels = im.load()

        for i in range(im.size[0]):
            for j in range(im.size[1]):
                if pixels[i, j][3] == 0:
                    pixels[i, j] = background_colour
                else:
                    pixels[i, j] = image_colour

        im.save(output_filename)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-filename', help='The Full Input Filename (Must Be *png)')
    parser.add_argument('-a', '--background-opacity', type=int, help='The alpha value "a" of the background pixels where 0 ≤ a ≤ 255 (Default: 255)')
    parser.add_argument('-o', '--output-filename', help='The Full Output Filename (Default: shadow-art.png)')
    args = parser.parse_args()

    input_filename = args.input_filename or get_input_filename()
    background_opacity = args.background_opacity or get_background_opacity()
    background_colour = get_background_colour(background_opacity)
    image_colour = get_image_colour()
    output_filename = args.output_filename or get_output_filename()

    process_image(input_filename, background_colour, image_colour, output_filename)

if __name__ == '__main__':
    main()

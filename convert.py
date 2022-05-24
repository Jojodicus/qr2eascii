#! /usr/bin/env python3

from argparse import ArgumentParser
from numpy import array
from os import path
from PIL import Image
from qrcode import QRCode, constants
from sys import stdout

# parse arguments
parser = ArgumentParser(description='Convert a QR-Code image to E-ASCII-Art.')
parser.add_argument('-i', '--input', help='Input image file/text')
parser.add_argument('-o', '--output', help='Output file')
parser.add_argument('--invert', help='Invert colors', action='store_true')
parser.add_argument('-w', '--white', help='Characters used for white (default "██")', default='██')
parser.add_argument('-b', '--black', help='Characters used for black (default "  ")', default='  ')
parser.add_argument('-v', '--version', help='Generated QR-Code version (default 1)', default=1, type=int)
parser.add_argument('--border', help='Generated QR-Code border size (default 1)', default=1, type=int)
parser.add_argument('-c', '--correction', help='Error correction modes (default M)', choices=['L', 'M', 'Q', 'H'], default='M')
args = parser.parse_args()

# generate/load image
if args.input is None or not path.isfile(args.input):
    if args.input:
        data = args.input
    else:
        data = input('Enter data to encode: ')

    # parse error correction
    # @TODO: update with match case after py3.10 gets widely adopted
    if args.correction == 'L':
        ecc = constants.ERROR_CORRECT_L
    elif args.correction == 'Q':
        ecc = constants.ERROR_CORRECT_Q
    elif args.correction == 'H':
        ecc = constants.ERROR_CORRECT_H
    else: # default M
        ecc = constants.ERROR_CORRECT_M

    qr = QRCode(version=args.version, box_size=1, border=args.border, error_correction=ecc)
    qr.add_data(data)
    qr.make(fit=True)
    image = qr.make_image(fill_color=(0, 0, 0), back_color=(255, 255, 255))
else:
    try:
        image = Image.open(args.input)
    except:
        parser.error("unable to open file")
        exit(1)
image_array = array(image.getdata())

width = image.size[0]
height = image.size[1]

# get offset
offset = 0
while image_array[offset * width + offset][0] == 255:
    offset += 1

# get scale
scale = 1
while image_array[(offset + scale) * width + (offset + scale)][0] == 0:
    scale += 1

# resize
image = image.resize((width // scale, height // scale), Image.Resampling.NEAREST)
image_array = array(image.getdata())
width = image.size[0]
height = image.size[1]

# inverted colors
if args.invert:
    image_array = 255 - image_array

# print image
with open(args.output, 'w', encoding='utf-8') if args.output else stdout as f:
    for i in range(height):
        for j in range(width):
            if image_array[i * width + j][0] < 128:
                print(args.white, end='', file=f)
            else:
                print(args.black, end='', file=f)
        print(file=f)

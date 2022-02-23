from PIL import Image
from qrcode import QRCode
from argparse import ArgumentParser
import numpy
import sys

# parse arguments
parser = ArgumentParser(description='Convert a QR-Code image to E-ASCII-Art.')
parser.add_argument('-i', '--input', help='Input image file')
parser.add_argument('-o', '--output', help='Output file')
parser.add_argument('--invert', help='Invert colors', action='store_true')
parser.add_argument('-w', '--white', help='Characters used for white (default "██")', default='██')
parser.add_argument('-b', '--black', help='Characters used for black (default "  ")', default='  ')
args = parser.parse_args()

# generate/load image
if args.input is None:
    data = input('Enter data to encode: ')
    qr = QRCode(version=1, box_size=1, border=1)
    qr.add_data(data)
    qr.make(fit=True)
    image = qr.make_image(fill_color=(0, 0, 0), back_color=(255, 255, 255))
else:
    image = Image.open(args.input)
image_array = numpy.array(image.getdata())

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
image = image.resize((width // scale, height // scale), Image.NEAREST)
image_array = numpy.array(image.getdata())
width = image.size[0]
height = image.size[1]

# inverted colors
if args.invert:
    image_array = 255 - image_array

# print image
with open(args.output, 'w', encoding='utf-8') if args.output else sys.stdout as f:
    for i in range(height):
        for j in range(width):
            if image_array[i * width + j][0] < 128:
                print(args.white, end='', file=f)
            else:
                print(args.black, end='', file=f)
        print(file=f)
from PIL import Image
import qrcode
import numpy
import sys
import argparse

# parse arguments
parser = argparse.ArgumentParser(description='Convert a QR-Code image to E-ASCII-Art.')
parser.add_argument('-i', '--input', help='Input image file')
parser.add_argument('-o', '--output', help='Output file')
parser.add_argument('--invert', help='Invert colors', action='store_true')
args = parser.parse_args()

# generate/load image
if args.input is None:
    data = input('Enter data to encode: ')
    qr = qrcode.QRCode(version=1, box_size=1, border=1)
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
    for i in range(0, height):
        for j in range(0, width):
            if image_array[i * width + j][0] < 128:
                print('██', end='', file=f)
            else:
                print('  ', end='', file=f)
        print(file=f)
# QR-Code to E-ASCII
Generate a QR-code in E-ASCII-art using the black square symbol (█, U+2588, Alt+219). As input either an already generated picture of a QR-code or text can be used.

## Requirements
- [numpy](https://numpy.org)
- [pillow](https://pillow.readthedocs.io)
- [qrcode](https://pypi.org/project/qrcode/)

## Usage
``py convert.py [-h] [-i INPUT] [-o OUTPUT] [--invert] [-w WHITE] [-b BLACK] [-v VERSION] [--border BORDER] [-c {L,M,Q,H}]``
- ``-h``, ``--help``: Show help message.
- ``-i INPUT``: Input file.
- ``-o OUTPUT``: Output file.
- ``--invert``: Invert colors.
- ``-w WHITE``: Characters for white pixel (default "██")
- ``-b BLACK``: Characters for black pixel (default "  ")
- ``-v VERSION``: QR-Code version (default 1)
- ``--border BORDER``: Border size of generated QR-Code (default 1)
- ``-c [L,M,Q,H]``: Error correction mode (default M)

If no input file is given, the program reads the data from stdin.

## Notes when converting images
The conversion of images will only work reliably on pure black/white QR-codes with square eyes and dots. The border around the code should also be uniform for the scaling to work correctly. Codes that work can be generated with websites like [qr-code-generator.com](https://qr-code-generator.com/).

---

## Example
### From text
```
py convert.py --invert
> Enter data to encode: github.com/jojodicus
```
yields:
```
██████████████████████████████████████████████████████
██              ████      ██    ██████              ██
██  ██████████  ██  ██  ██    ████  ██  ██████████  ██
██  ██      ██  ██      ██████    ████  ██      ██  ██
██  ██      ██  ██  ████████  ██    ██  ██      ██  ██
██  ██      ██  ████  ██  ████  ██  ██  ██      ██  ██
██  ██████████  ████████  ████  ██████  ██████████  ██
██              ██  ██  ██  ██  ██  ██              ██
██████████████████      ██  ██  ██  ██████████████████
██  ██████████  ██  ██            ██    ████      ████
██  ██    ██  ████████    ██████  ██████          ████
██  ████        ██████  ████  ██      ██      ██    ██
██  ██        ██  ██  ████████                ██    ██
████████  ████    ██  ██████    ██        ██  ██  ████
██      ██████████████  ██    ██    ████  ████  ██████
██  ██              ████████      ██  ██      ██    ██
██  ████      ██    ██████            ████        ████
██  ██  ██  ██  ██████  ██  ██  ██          ██      ██
██████████████████  ██  ██████████  ██████    ████████
██              ██████████      ██  ██  ██  ██  ██  ██
██  ██████████  ██████    ████      ██████    ████  ██
██  ██      ██  ██████    ██████                    ██
██  ██      ██  ████  ████    ██  ██    ██████      ██
██  ██      ██  ████    ████    ██  ████  ██    ██  ██
██  ██████████  ████    ██    ████  ██████  ██████  ██
██              ██  ████      ████    ██████  ████  ██
██████████████████████████████████████████████████████
```
---

```
py convert.py -i example/qr-code.png -o example/qr-code.txt --invert
```

see [example/qr-code.png](example/qr-code.png) and [example/qr-code.txt](example/qr-code.txt)

![](example/qr-code.png)

yields:

```
████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████
████              ██████████  ██    ██  ██████              ████
████  ██████████  ██    ██  ██  ██    ████████  ██████████  ████
████  ██      ██  ██  ██          ██████  ████  ██      ██  ████
████  ██      ██  ██    ████  ████    ██    ██  ██      ██  ████
████  ██      ██  ████  ██    ██    ██      ██  ██      ██  ████
████  ██████████  ████      ████  ████████  ██  ██████████  ████
████              ██  ██  ██  ████  ██  ██  ██              ████
████████████████████  ██████████    ██      ████████████████████
████  ██████████  ██      ████████    ██  ██    ████      ██████
████      ██  ██████  ██        ██        ██  ██    ██    ██████
████    ████████    ████████        ██  ██████████  ████████████
████████  ████  ████    ██  ██  ████████  ██  ██████  ██████████
██████████        ██████  ██        ██████  ██    ████████  ████
████  ████  ██████    ████  ██████  ██  ██  ██      ████    ████
████    ██████  ██  ██  ████████  ██████  ██████    ██  ██  ████
██████████  ████  ████        ████    ██  ██  ██  ██    ████████
████  ████████  ██    ██    ██  ████████  ████      ██      ████
████    ██        ██    ██  ████  ██  ██  ████████    ████  ████
████  ████████████  ████    ██  ██████████  ██  ████████████████
████  ██████        ██      ████  ██  ██            ██      ████
████████████████████  ██  ██  ████████████  ██████    ██████████
████              ████  ████  ██████        ██  ██      ████████
████  ██████████  ████  ██    ██    ████    ██████  ████████████
████  ██      ██  ████  ██  ██  ████                  ██████████
████  ██      ██  ██████    ██  ████          ██████      ██████
████  ██      ██  ████  ████          ██                  ██████
████  ██████████  ████  ████  ████      ██████    ██    ██  ████
████              ██        ████  ██████  ████      ██  ████████
████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████
```

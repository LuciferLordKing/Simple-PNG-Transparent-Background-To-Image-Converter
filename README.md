# Simple-PNG-Transparent-Background-To-Image-Converter
Convert the transparent background of a PNG image to opaque while image to transparent

---
# prerequisite
* [Python3](https://www.python.org/downloads/)
* [pip](https://packaging.python.org/en/latest/tutorials/installing-packages/#ensure-you-can-run-pip-from-the-command-line)
  * `python3 -m ensurepip --default-pip`
* [Pillow](https://pypi.org/project/Pillow/)
  * `python3 -m pip install Pillow`

---
```
usage: png-background-to-img.py [-h] [-i INPUT_FILENAME]
                                [-a BACKGROUND_OPACITY] [-o OUTPUT_FILENAME]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_FILENAME, --input-filename INPUT_FILENAME
                        The Full Input Filename (Must Be *png)
  -a BACKGROUND_OPACITY, --background-opacity BACKGROUND_OPACITY
                        The alpha value a of the background pixels where 0 ≤ a
                        ≤ 255 (Default: 255)
  -o OUTPUT_FILENAME, --output-filename OUTPUT_FILENAME
                        The Full Output Filename (Default: shadow-art.png)
```

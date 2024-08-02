from os import PathLike
from os.path import basename, splitext
from pathlib import Path

from PIL import Image


def convert_to_png(source: str | bytes | PathLike, dest: str | bytes | PathLike):
    image_name = splitext(basename(source))[0]
    img = Image.open(source)
    return img.save(Path(dest).joinpath(f"{image_name}.png"), format="png")

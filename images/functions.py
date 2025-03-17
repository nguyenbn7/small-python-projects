import asyncio
import logging
from os import PathLike
from os.path import basename, splitext
from pathlib import Path
from typing import List

from PIL import Image

logging.basicConfig(level=logging.CRITICAL)


def convert_to_png(
    jpeg_image: str | bytes | PathLike, dest_folder: str | bytes | PathLike
):
    try:
        image_name = splitext(basename(jpeg_image))[0]
        img = Image.open(jpeg_image)
        img.save(Path(dest_folder).joinpath(f"{image_name}.png"), format="png")
        logging.debug(f"saved file {image_name}.png")
    except Exception as e:
        logging.debug(e)
    finally:
        img.close()


def convert_all_to_png(
    jpeg_images: List[str | bytes | PathLike], dest_folder: str | bytes | PathLike
):
    for jpeg_image in jpeg_images:
        convert_to_png(jpeg_image, dest_folder)


async def _remove_meta(image_path: Path, des_path: Path):
    # https://stackoverflow.com/questions/19786301/python-remove-exif-info-from-images
    try:
        img = Image.open(image_path)

        data = list(img.getdata())
        img_without_exif = Image.new(img.mode, img.size)
        img_without_exif.putdata(data)
        img_without_exif.save(des_path.joinpath(image_path.name))
    except Exception as e:
        print(e)
    finally:
        img.close()


async def remove_meta(src_path: Path, des_path: Path):
    if not des_path.exists():
        des_path.mkdir()

    if src_path.is_file():
        await _remove_meta(src_path, des_path)
        return

    # TODO: add more support file images
    tasks = [
        _remove_meta(image_path, des_path)
        for image_path in src_path.glob("*.[jpg][png][jpeg]")
    ]
    await asyncio.gather(*tasks)

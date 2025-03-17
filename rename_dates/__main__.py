# Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY.
import os
import re
import shutil

date_pattern = re.compile(
    r"""
    ^(.*?)              # all text before date
    ((0|1)?\d)-         # one or two digits for month
    ((0|1|2|3)?\d)-     # one or two digits for the day
    ((19|20)\d\d)       # four digits for year
    (.*?)$              # all text after the date
    """,
    re.VERBOSE,
)


for amer_filename in os.listdir(os.path.dirname(os.path.abspath(__file__))):
    mo = date_pattern.search(amer_filename)

    if mo is None:
        continue

    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

    euro_filename = (
        before_part + day_part + "-" + month_part + "-" + year_part + after_part
    )

    abs_working_dir = os.path.abspath(".")
    abs_amer_filename = os.path.join(abs_working_dir, amer_filename)
    abs_euro_filename = os.path.join(abs_working_dir, euro_filename)

    print(f'Renaming "{abs_amer_filename}" to "{abs_euro_filename}"...')
    # shutil.move(abs_amer_filename, abs_euro_filename) # uncomment after testing

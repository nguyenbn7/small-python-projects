# Copies an entire folder and its contents into a ZIP file whose filename increments.
import os
import zipfile


def backup_to_zip(folder):
    folder = os.path.abspath(folder)

    # Figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        zip_filename = os.path.basename(folder) + "_" + str(number) + ".zip"
        if not os.path.exists(zip_filename):
            break
        number += 1

    print(f"Creating {zip_filename}...")
    with zipfile.ZipFile(zip_filename, "w") as backup_zip:
        for foldername, subfolders, filenames in os.walk(folder):
            print(f"Adding files in {foldername}...")
            # Add the current folder to the ZIP file.
            backup_zip.write(foldername)
            # Add all the files in this folder to the ZIP file.
            for filename in filenames:
                new_base = os.path.basename(folder) + "_"
                if filename.startswith(new_base) and filename.endswith(".zip"):
                    continue  # don't backup the backup ZIP files
                backup_zip.write(os.path.join(foldername, filename))

    print("Done.")


backup_to_zip(os.path.join(os.path.dirname(os.path.abspath(__file__)), "delicious"))

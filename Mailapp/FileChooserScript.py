from tkinter import filedialog as fd


def choose_file():
    filenames = fd.askopenfilenames(filetypes = (("JPEG Files", "*.jpeg"), ("PNG Files", "*.png"), ("JPG Files", "*.jpg"), ("PDF Files", "*.pdf"), ("PPT Files", "*.ppt"), ("DOCX Files", "*.docx")))
    print(filenames)
    return filenames
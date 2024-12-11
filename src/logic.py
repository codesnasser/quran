import os
from PIL import Image, ImageTk


MIN_INDEX = 0
MAX_INDEX = 603

FILE_INDEX = 'assets/index/index.txt'
FOLDER_PAGES = 'assets/quran-pages'


def current_page_index(cidx=None):
    """
    Retrieves or updates the current page index stored in a file.

    Parameters:
        cidx (int, optional): 
            - If None, the function reads the current index from the file and returns it.
            - If an integer is provided, the function updates the file with this value.

    Returns:
        int: The current page index. Returns 0 if the file is not found or is empty.
    """
    try:
        if cidx is None:
            with open(FILE_INDEX, 'r') as file:
                cidx = file.read()
                return int(cidx) if cidx else 0
        else:
            with open(FILE_INDEX, 'w') as file:
                file.write(str(cidx))
    except FileNotFoundError:
        return 0


def move_index(index: int, mode='f'):
    """
    Adjusts the index by incrementing ('f') or decrementing ('b') within set limits.

    Parameters:
        index (int): The current index.
        mode (str): 'f' for forward, 'b' for backward (default is 'f').

    Returns:
        int: The updated index within the range [MIN_INDEX, MAX_INDEX].
    """
    if mode == 'f':
        return index + 1 if index < MAX_INDEX else MAX_INDEX
    if mode == 'b':
        return index - 1 if index > MIN_INDEX else MIN_INDEX
    

def quran_pages():
    """Load images of Quran pages from the specified folder."""
    page_images = [
        ImageTk.PhotoImage(Image.open(os.path.join(FOLDER_PAGES, page)))
        for page in sorted(os.listdir(FOLDER_PAGES))
    ]
    return page_images

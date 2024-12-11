from tkinter import *
from src.gui import Window, current_page_index



def main():
    root = Tk()
    quran = Window(root)
    quran.run()
    current_page_index(quran.cidx)



if __name__ == '__main__':
    main()

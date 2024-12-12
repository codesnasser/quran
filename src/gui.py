from tkinter import *
from tkinter import ttk
from assets.surahs_index import index
from .logic import quran_pages, current_page_index, move_index


WINCLOR = '#2e2e2e'



class Window:
    def __init__(self, root):
        self.root = root
        screenw = self.root.winfo_screenwidth() // 2 - 250
        screenh = self.root.winfo_screenheight()
        self.root.geometry(f'{screenw}x{screenh}')
        self.root.resizable(0, 0)
        self.root.title('القرآن الكريم')
        self.root.config(bg=WINCLOR)

        self.pages = quran_pages()

        self.page_frame = Frame(self.root, width=screenw, height=screenh)
        self.page_frame.pack(pady=100)

        self.cidx = current_page_index()
        self.page_lable = Label(self.page_frame, image=self.pages[self.cidx])
        self.page_lable.pack()

        self.create_combobox()

        # Create buttons
        self.next_button = self.create_next_button()
        self.back_button = self.create_back_button()

    def create_combobox(self):
        surah_list = [f"{surah_order} - {surah_name}" for surah_order, (page_index, surah_name) in index.items()]
        
        # Create Combobox for selecting Surah
        self.surah_combobox = ttk.Combobox(self.root, values=surah_list, state="readonly", width=50)
        self.surah_combobox.place(relx=0.5, rely=0.05, anchor='center')
        self.surah_combobox.set("Select Surah")  # Default text
        self.surah_combobox.bind("<<ComboboxSelected>>", self.on_surah_select)

    def create_next_button(self):
        button = Button(self.root, text='<', command=self.next)
        button.place(relx=0.1, rely=0.45, anchor='center')
        return button

    def create_back_button(self):
        button = Button(self.root, text='>', command=self.back)
        button.place(relx=0.9, rely=0.45, anchor='center')
        return button

    def next(self):
        """
        Navigates to the next page of the Quran if it is not the last page.
        Updates the displayed page image accordingly.
        """
        self.cidx = move_index(self.cidx)
        self.page_lable.config(image=self.pages[self.cidx])

    def back(self):
        """
        Navigates to the previous page of the Quran if it is not the first page.
        Updates the displayed page image accordingly.
        """
        self.cidx = move_index(self.cidx, mode='b')
        self.page_lable.config(image=self.pages[self.cidx])

    def on_surah_select(self, event):
        # Get the selected Surah
        selected_surah = self.surah_combobox.get()
        for surah_order, (page_index, surah_name) in index.items():
            if selected_surah == f"{surah_order} - {surah_name}":
                self.cidx = page_index - 1
                break
        
        # Update the displayed Surah
        self.page_lable.config(image=self.pages[self.cidx])

    def run(self):
        self.root.mainloop()

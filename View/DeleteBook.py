import tkinter as tk
from tkinter import ttk


class DeleteBook(ttk.Frame):
    def __init__(self, parent, app, controller):
        ttk.Frame.__init__(self, parent)
        self.style = ttk.Style(self)
        self.controller = controller
        self.app = app

        # Widgets
        label_title = ttk.Label(self, text="Delete Book", font=("Helvetica", 20, 'bold'))
        label_title.pack(pady=10)

        frame_isbn = ttk.Frame(self)
        frame_isbn.pack(pady=10)

        self.entry_isbn = ttk.Entry(frame_isbn)
        self.entry_isbn.pack(side="left", padx=10)
        self.entry_isbn.insert(0, "ISBN")

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10)

        button_delete_book = ttk.Button(button_frame, text="Delete Book", command=self.delete_book)
        button_delete_book.pack(side="left", padx=10)

        button_back = ttk.Button(button_frame, text="Back", command=self.go_back)
        button_back.pack(side="left", padx=10)

    def delete_book(self):
        isbn = self.entry_isbn.get()

        # Delete book logic
        # ...

    def go_back(self):
        pass

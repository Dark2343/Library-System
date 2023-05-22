 
LARGEFONT =("Verdana", 35)
  
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
class App(tk.Tk):
    
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        from Login import Login
        from AddBook import AddBook
        from AddUser import AddUser
        from Browse import Browse
        from SearchBook import SearchBook
        from UpdateBookDetails import UpdateBookDetails
        from UpdateUserDetails import UpdateUserDetails
        from DeleteBook import DeleteBook
        from DeleteUser import DeleteUser
        from BookLocation import BookLocation
        from BorrowBook import BorrowBook
        print("I AM RUNNING")     
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = ttk.Frame(self)
        #set width and height
        container.config(width=1000,height=580)
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        self.frames = {}
        for F in (Login,AddBook, AddUser,Browse,SearchBook,UpdateBookDetails,UpdateUserDetails,DeleteBook,DeleteUser,BookLocation,BorrowBook):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Login")
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
 
  
  

  
# Driver Code
app = App()
app.title("Library System")
style = ThemedStyle(app)
style.set_theme("equilux")
app.geometry("1000x580")
app.mainloop()
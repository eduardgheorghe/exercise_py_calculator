from tkinter import *

def close_app():
    window.destroy()

if __name__ == "__main__":
    window = Tk()
    window.title("PyCalc")
    window.minsize(300, 250)

    expression_field = Entry(window, width=30)
    expression_field.grid(row=0, column=0, columnspan=4)

    close_button = Button( window, text="Close", command=close_app)
    close_button.grid(row=8, column=8, columnspan=1)


    window.mainloop()
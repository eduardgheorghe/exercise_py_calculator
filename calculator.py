from tkinter import *

def close_app():
    window.destroy()

if __name__ == "__main__":
    window = Tk()
    window.title("PyCalc")
    window.minsize(300, 250)

    expression_field = Entry(window, width=30)
    expression_field.grid(row=0, column=0, columnspan=4, sticky="nw")


    for i in range(1, 10):
        # Create a button with the number as the text
        button = Button(window, text=str(i), height=3, width=3, borderwidth=1)

        # Configure the button to expand horizontally (sticky="ew")
        button.grid(row=(i+2)//3, column=(i-1)%3, sticky="ew")

        # Bind the click event to the button_click function
        button.config(command=lambda num=i: button_click(num))

    close_button = Button( window, text="Close", command=close_app)
    close_button.grid(row=8, column=8, sticky="sw")


    window.mainloop()
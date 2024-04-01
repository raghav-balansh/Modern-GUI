from tkinter import Button, Tk, Label
from tkcalendar import Calendar

root = Tk()


def select_date():
    my_date = my_cal.get_date()
    selected_date = Label(text=my_date)
    selected_date.pack(padx=2, pady=2)


my_cal = Calendar(root, selectmode='day', date_pattern='d/m/yy')
my_cal.pack(padx=15, pady=15)

open_cal = Button(root, text='select Date', command=select_date)
open_cal.pack(padx=15, pady=15)

root.geometry('300x300')
root.title('Calendar')
root.configure(bg='lightblue')

root.mainloop()

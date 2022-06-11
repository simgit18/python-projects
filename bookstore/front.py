from cProfile import label
from distutils.log import error
from tkinter import *

from matplotlib import cm
import back


def get_selection(event):
    try:
        index = list1.curselection()
        global selected_tuple
        selected_tuple = list1.get(index)

        print(selected_tuple)
        return selected_tuple

    except error:
        pass


def view_command():
    list1.delete(0, END)
    for row in back.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)

    for row in back.search(title_value.get(), author_value.get(), year_value.get(), isbn_value.get()):
        list1.insert(END, row)


def add_entry():
    back.insert(title_value.get(), author_value.get(),
                year_value.get(), isbn_value.get())
    list1.delete(0, END)
    list1.insert(END, (title_value.get(), author_value.get(),
                 year_value.get(), isbn_value.get()))


def delete_entry():
    back.delete(selected_tuple[0])
    view_command()


def close_window():
    window.destroy()


def update_command():
    back.update(selected_tuple[0], title_value.get(),
                author_value.get(), year_value.get(), isbn_value.get())
    view_command()


window = Tk()

title_value, author_value, year_value, isbn_value = StringVar(
), StringVar(), StringVar(), StringVar()

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)


e1 = Entry(window, textvariable=title_value)
e1.grid(row=0, column=1)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

e2 = Entry(window, textvariable=author_value)
e2.grid(row=0, column=3)


l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

e3 = Entry(window, textvariable=year_value)
e3.grid(row=1, column=1)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

e4 = Entry(window, textvariable=isbn_value)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=7, width=35)
list1.grid(row=2, column=0, columnspan=2, rowspan=6)

list1.bind('<<ListboxSelect>>', get_selection)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

viewAll_b = Button(window, text="View All", width=12, command=view_command)
viewAll_b.grid(row=2, column=3)

search_b = Button(window, text="Search Entry",
                  width=12, command=search_command)
search_b.grid(row=3, column=3)

addEntry_b = Button(window, text="Add Entry", width=12, command=add_entry)
addEntry_b.grid(row=4, column=3)

update_b = Button(window, text="Update", width=12, command=update_command)
update_b.grid(row=5, column=3)

delete_b = Button(window, text="Delete", width=12, command=delete_entry)
delete_b.grid(row=6, column=3)

close_b = Button(window, text="Close", width=12, command=close_window)
close_b.grid(row=7, column=3)

window.mainloop()

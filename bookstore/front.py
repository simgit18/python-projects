from cProfile import label
from tkinter import *
import back


def view_command():
    for row in back.view():
        list1.insert(END, row)


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

l3 = Label(window, text="ISBN")
l3.grid(row=1, column=2)

e3 = Entry(window, textvariable=isbn_value)
e3.grid(row=1, column=3)

l4 = Label(window, text="Year")
l4.grid(row=1, column=0)

e4 = Entry(window, textvariable=year_value)
e4.grid(row=1, column=1)

list1 = Listbox(window, height=7, width=35)
list1.grid(row=2, column=0, columnspan=2, rowspan=6)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

viewAll_b = Button(window, text="View All", width=12, command=view_command)
viewAll_b.grid(row=2, column=3)

search_b = Button(window, text="Search Entry", width=12)
search_b.grid(row=3, column=3)

addEntry_b = Button(window, text="Add Entry", width=12)
addEntry_b.grid(row=4, column=3)

update_b = Button(window, text="Update", width=12)
update_b.grid(row=5, column=3)

delete_b = Button(window, text="Delete", width=12)
delete_b.grid(row=6, column=3)

close_b = Button(window, text="Close", width=12)
close_b.grid(row=7, column=3)

window.mainloop()

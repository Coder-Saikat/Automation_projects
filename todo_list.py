from tkinter import *

root=Tk()
root.title('To Do List')
root.geometry('300x400')
root.resizable(500, 800)
root.config(bg="PaleVioletRed")
#Heading Label

Label(root, text='To Do List', bg='PaleVioletRed', font=("Monotype Corsiva", 15), wraplength=300).place(x=35, y=0)

# Listbox with all the tasks with a Scrollbar
tasks = Listbox(root, selectbackground='Gold', bg='grey', font=('Helvetica', 12), height=12, width=25)
scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
scroller.place(x=260, y=50, height=232)
tasks.config(yscrollcommand=scroller.set)
tasks.place(x=35, y=50)

# Adding items to the Listbox
with open('tasks', 'r+') as tasks_list:
    for task in tasks_list:
        tasks.insert(END, task)
    tasks_list.close()

#creating the entry widget where user can enter new item
new_item_entry=Entry(root,width=37)
new_item_entry.place(x=35,y=310)

#creating button
add_btn=Button(root,text="ADD ITEM",bg='AZURE',width=10,font=('Helvetica',12),command=lambda :add_item(new_item_entry,tasks))
add_btn.place(x=45,y=350)

delete_btn=Button(root,text="DELETE ITEM",bg='AZURE',width=10,font=('Helvetica',12),command=lambda :delete_item(tasks))
delete_btn.place(x=155,y=350)

# Adding and Deleting items functions
def add_item(entry: Entry, listbox: Listbox):
    new_task = entry.get()

    listbox.insert(END, new_task)

    with open('tasks', 'a') as tasks_list_file:
        tasks_list_file.write(f'\n{new_task}')


def delete_item(listbox: Listbox):
    listbox.delete(ACTIVE)

    with open('tasks', 'r+') as tasks_list_file:
        lines = tasks_list_file.readlines()

        tasks_list_file.truncate()

        for line in lines:
            if listbox.get(ACTIVE) == line[:-2]:
                lines.remove(line)
            tasks_list_file.write(line)

        tasks_list_file.close()

# Finalizing the window
root.update()
root.mainloop()
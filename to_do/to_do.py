from tkinter import *
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

root = Tk()
root.title('TO-DO LIST')
root.geometry('400x650+400+100')
root.resizable(False, False)

task_list = []


def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open(os.path.join(base_dir, 'Tasklist.txt'), 'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)


def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open(os.path.join(base_dir, 'tasklist.txt'), 'w') as taskfie:
            taskfie.write(task+'\n')

        listbox.delete(ANCHOR)


def openTaskFile():
    try:
        global task_list
        with open(os.path.join(base_dir, 'tasklist.txt'), 'r') as taskfile:
            tasks = taskfile.readline()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END, task)

    except:
        file = open(os.path.join(base_dir, 'tasklist.txt'), 'w')
        file.close()


# icon
Image_icon = PhotoImage(file=os.path.join(base_dir, 'task.png'))
root.iconphoto(False, Image_icon)

# top bar
TopImage = PhotoImage(file=os.path.join(base_dir, 'topbar.png'))
Label(root, image=TopImage).pack()

dockImage = PhotoImage(file=os.path.join(base_dir, 'dock.png'))
Label(root, image=dockImage, bg='#193047').place(x=30, y=25)

heading = Label(root, text='ALL TASK', font='arial 20 bold', fg='white', bg='#32405b')
heading.place(x=130, y=20)

# main
frame = Frame(root, width=400, height=50, bg='grey')
frame.place(x=0, y=180)

task = StringVar()
task_entry = Entry(frame, width=18, font='arial 20', bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

button = Button(frame, text='ADD', font='arial 20 bold', width=6, bg='#5a95ff', fg='white', bd=0, command=addTask, background='#0c0c0d')
button.place(x=300, y=0)
# list box
frame1 = Frame(root, bd=3, width=700, height=280, bg='#0c0d0c')
frame1.pack(pady=(160, 0))

listbox = Listbox(frame1, font=('arial', 12), width=40, height=16, bg='#032c40', fg='#c9d2d6', cursor='hand2', selectbackground='#0aa6f2')
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview())

openTaskFile()

# delete
Delete_icon = PhotoImage(file=os.path.join(base_dir, 'delete.png'))
Button(root, image=Delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)

root.mainloop()

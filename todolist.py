import tkinter
import random
import tkinter.messagebox

#create root window
root=tkinter.Tk()
#change background color
root.configure(bg="white")
#change title
root.title("To-Do List")
#change window size
root.geometry("325x275")
#create empty list
tasks=[]
#for testing puopses use a default list
#tasks=["call mom","buy a guitar","sushi"]

#create functions
def update_listbox():
    #clear the current list
    clear_listbox()
    #polulate the list box
    for task in tasks:
        lb_tasks.insert("end",task)
def clear_listbox():
    lb_tasks.delete(0,"end")
def add_task():
    #get the task to add
    task=txt_input.get()
    #make sure tasks is not empty
    if task !="":
        #append to the list
        tasks.append(task)
        #update the listbox
        update_listbox()
    else:
        tkinter.messagebox.showwarning("Warning", "You need to enter the task")
    txt_input.delete(0,"end")
def del_all():
    confirmed=tkinter.messagebox.askyesno("Please confirm","Do you really want to delete all?")
    if confirmed==True:
        #since we are changeing the lists it needs to be global
        global tasks
        #clear the tasks list
        tasks=[]
        #update the list box
        update_listbox()
def del_one():

    #get the text of currently selected task
    task=lb_tasks.get("active")
    #confirms it in a list
    if task in tasks:
        tasks.remove(task)
    #update the listbox
    update_listbox()
def sort_asc():
    #sort the list
    tasks.sort()
    #update the list box
    update_listbox()
def sort_desc():
    #sort the list
    tasks.sort()
    #reverse the list
    tasks.reverse()
    #update the list box
    update_listbox()
def choose_random():
    #choose a random taks
    task=random.choice(tasks)
    #update the display label
    lbl_display["text"]=task
def show_number_of_tasks():
   #get the number of tasks
    number_of_tasks=len(tasks)
    #creaate and format the message
    msg="Number of tasks: %s" %number_of_tasks
    #display the message
    lbl_display["text"]=msg


#create lables and buttons
lbl_title=tkinter.Label(root,text="To-Do-List",bg="white")
lbl_title.grid(row=0,column=0)

lbl_display=tkinter.Label(root,text="",bg="white")
lbl_display.grid(row=0,column=1)

txt_input=tkinter.Entry(root,width=15)
txt_input.grid(row=1,column=1)

btn_add_task=tkinter.Button(root,text="Add Task",fg="green",bg="white",width=15,command=add_task)
btn_add_task.grid(row=1,column=0)

btn_del_all=tkinter.Button(root,text="Delete All",fg="green",bg="white",width=15,command=del_all)
btn_del_all.grid(row=2,column=0)

btn_del_one=tkinter.Button(root,text="Delete One",fg="green",bg="white",width=15,command=del_one)
btn_del_one.grid(row=3,column=0)

btn_sort_asc=tkinter.Button(root,text="Sort(Asc)",fg="green",bg="white",width=15,command=sort_asc)
btn_sort_asc.grid(row=4,column=0)

btn_sort_desc=tkinter.Button(root,text="Sort(Desc)",fg="green",bg="white",width=15,command=sort_desc)
btn_sort_desc.grid(row=5,column=0)

btn_choose_random=tkinter.Button(root,text="Choose Random",fg="green",bg="white",width=15,command=choose_random)
btn_choose_random.grid(row=6,column=0)

btn_number_of_tasks=tkinter.Button(root,text="Number of Tasks",fg="green",bg="white",width=15,command=show_number_of_tasks)
btn_number_of_tasks.grid(row=7,column=0)

btn_exit=tkinter.Button(root,text="Exit",fg="green",bg="white",width=15,command=exit)
btn_exit.grid(row=8,column=0)

lb_tasks=tkinter.Listbox(root)
lb_tasks.grid(row=2,column=1,rowspan=7)

#starts the main event loop
root.mainloop()
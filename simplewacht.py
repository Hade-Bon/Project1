import datetime
from tkinter import *
import os

times = datetime.datetime.now()

def create_dir():  # Creamos la capeta para almacenar users
    path_current = os.path.dirname(__file__)
    if  os.path.exists(os.path.join(path_current, "Save_User")):
        print("Existe")
    else:    
        os.mkdir(os.path.join(path_current, "Save_User")) # Creamos un directory en donde se encuentra el archivo 

    open(os.path.join(path_current,"Save_User/user_t.txt"), "a").close()
    open(os.path.join(path_current, "Save_User/passwd_t.txt"), "a").close()

create_dir() 
root = Tk()
root.title("Virtual_Test")

first = Frame(root, background="black", width=350, height=200)
first.grid(column=0, row=0)


second = Frame(root, background="gray", width=350, height=200)
second.grid(row=1, column=0)

Label(second, text="User_Name: ",).grid(row=0, column=0)
user_n = Entry(second, )
user_n.grid(row=0, column=1)

Label(second, text="Password: ").grid(row=1, column=0)
passwd_u = Entry(second, )
passwd_u.grid(row=1, column=1)

#=============================================================================================

def verification_u():  # Function for check users and password

    user_entry = user_n.get()
    passwd_tets = passwd_u.get()
    #print(f"========= {user_entry} ===============")

    save_u = os.path.dirname(__file__) # Get the path in the current folder
    
    for i in open(os.path.join(save_u ,"Save_User/user_t.txt"), "r"): # For review if the user exist
        for x in open(os.path.join(save_u, "Save_User/passwd_t.txt"), "r"): # For check the password 
            
            if user_entry == "" or passwd_tets == "": 
                print("Insert your users and password")
                #Label(second, text="Insert your user and password").grid(row=3, column=0)
            elif user_entry in i and passwd_tets in x:
                print("I am, ", user_entry)
                Label(second, text="Welcome").grid(row=3, column=0)

def make_user():  # Function for create new user
    three = Frame(root, background="black", padx=10, pady=10)
    three.grid(row=2, column=0)

    Label(three, text="Name_User: ", foreground="green", background="black",).grid(row=0, column=0)
    Label(three, text="Create_Password: ", foreground="green", background="black",).grid(row=1, column=0)
    Label(three, text="Repit_Password: ", foreground="green", background="black",).grid(row=2, column=0)

    new_u = Entry(three,)
    new_u.grid(row=0, column=1)
        
    create_passw = Entry(three,)
    create_passw.grid(row=1, column=1)

    repit_passw = Entry(three,)
    repit_passw.grid(row=2, column=1)

    #----------------------------------------------------------------------------------------------

    def get_datas():
        save_uC = os.path.dirname(__file__)

        get_newU = new_u.get()
        get_createP = create_passw.get()

        if get_newU == "" or get_createP == "":
            print("Insert your datas correctly")
        elif get_newU and get_createP:
            if get_createP == repit_passw.get():
                add_user = open(os.path.join(save_uC, "Save_User/user_t.txt"), "a")
                add_user.write(f"\n{get_newU}\n")
                add_user.close()

                add_passwd = open(os.path.join(save_uC, "Save_User/passwd_t.txt"), "a")
                add_passwd.write(f"\n{get_createP}\n")
                add_passwd.close()
            elif repit_passw.get() == "":
                print("Confirm the password")
            elif repit_passw.get() != get_createP:
                print("The passwords do not coicidence")

    #----------------------------------------------------------------------------------------------

    avalible = Button(three, text="Create", pady=10, command=get_datas)
    avalible.grid(row=3, column=0, pady=10)

    disable = Button(three, text="Cancel", pady=10)
    disable.grid(row=3, column=1, pady=10)                 

#===================================================================================================    

enter = Button(second, text="Enter", command=verification_u)
enter.grid(row=2, column=0)

make_u = Button(second, text="Make_User", command=make_user)
make_u.grid(row=2, column=1)

cancel = Button(second, text="Exit")
cancel.grid(row=2, column=2)

while True:
    Label(first, text=times.time(), foreground="green").pack()

    break

root.mainloop()
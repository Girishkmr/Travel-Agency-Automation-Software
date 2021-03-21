from src.classes.customer import *
from src.screens import clear
from src import button
import tkinter as tk
from tkinter import messagebox


def new_customer(root, head):
    clear.clear(root)
    temp = Customer(head.customers[len(head.customers)-1].id+1)
    frame = tk.Frame(root, width="625", height="400", bg="purple3")
    frame.place(relx=0.2, rely=0.2)
    lb0 = tk.Label(text="Sign up now!", width="95", fg="blue", font=("Arial Bold", 15))
    lb1 = tk.Label(text="Name :", width="18", justify=tk.LEFT, bg="purple3", anchor='sw', font=("Arial Bold", 12))
    lb2 = tk.Label(text="Phone Number :", width="18", justify=tk.LEFT, bg="purple3", anchor='sw', font=("Arial Bold", 12))
    lb3 = tk.Label(text="Email :", width="18", justify=tk.LEFT, bg="purple3", anchor='sw', font=("Arial Bold", 12))
    lb4 = tk.Label(text="Driving Licence :", justify=tk.LEFT, bg="purple3", anchor='sw', width="18", font=("Arial Bold", 12))
    lb5 = tk.Label(text="Make Pin :", width="18", justify=tk.LEFT, bg="purple3", anchor='sw', font=("Arial Bold", 12))
    lb0.place(relx=0, rely=0)
    lb1.place(relx=0.25, rely=.25)
    lb2.place(relx=0.25, rely=.32)
    lb3.place(relx=0.25, rely=.39)
    lb4.place(relx=0.25, rely=.46)
    lb5.place(relx=0.25, rely=.53)
    en1 = tk.Entry(width="25", font=("Arial Bold", 12))
    en2 = tk.Entry(width="25", font=("Arial Bold", 12))
    en3 = tk.Entry(width="25", font=("Arial Bold", 12))
    en4 = tk.Entry(width="25", font=("Arial Bold", 12))
    en5 = tk.Entry(width="25", font=("Arial Bold", 12))
    en1.place(relx=0.4, rely=.25)
    en2.place(relx=0.4, rely=.32)
    en3.place(relx=0.4, rely=.39)
    en4.place(relx=0.4, rely=.46)
    en5.place(relx=0.4, rely=.53)
    en1.focus()
    signup_button = tk.Button(text="Sign up", width="20", font=("Arial Bold", 12), bg="gray80",
                              command=lambda: signup(head, temp, en1, en2, en3, en4, en5))
    signup_button.place(relx=0.3, rely=0.63)
    back_button = tk.Button(text="back",
                            width="12",
                            background="gray80",
                            font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "start"))
    back_button.place(relx=0.0, rely=0.9)
    next_button = tk.Button(text="Sign in",
                            width="12",
                            background="gray80",
                            font=("Arial Bold", 10),
                            command=lambda: button.button(root, head, "login_customer"))
    next_button.place(relx=0.91, rely=0.9)

    def signup(head, temp, en1, en2, en3, en4, en5):
        if en1.get() != "":
            if en2.get() != "":
                if en3.get() != "":
                    if en4.get() != "":
                        if en5.get() != "":
                            temp.profile(en1.get(),
                                         en2.get(),
                                         en3.get(),
                                         en4.get(),
                                         -1,
                                         0,
                                         0,
                                         0,
                                         en5.get())
                            if not head.is_double_customer(temp):
                                if head.is_possible_password(temp.password):
                                    head.customers.append(temp)
                                    head.history.append("Account created")
                                    messagebox.showinfo("Account", "Your account has been created!")
                                    head.logged_in_customer = "yes"
                                    head.customer_id = temp.id
                                    button.button(root, head, "customer")
                                else:
                                    messagebox.showerror("Account", "choose a different pin")
                                    en5.delete(0, tk.END)
                            else:
                                messagebox.showerror("double", "Another account with same details exits")
                                en1.delete(0, tk.END)
                                en2.delete(0, tk.END)
                                en3.delete(0, tk.END)
                        else:
                            messagebox.showinfo("Fill up", "Make a User pin for future login use!")
                    else:
                        messagebox.showinfo("Fill up", "Enter driving licence!")
                else:
                    messagebox.showinfo("Fill up", "Enter your Email id!")
            else:
                messagebox.showinfo("Fill up", "Enter contact number!")
        else:
            messagebox.showinfo("Fill up", "Enter your full name!")
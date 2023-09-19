from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymysql
import re


class Register:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  # for valid email
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="grey")

        

        # Registration frame
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        title = Label(frame1, text="REGISTER HERE", font=(
            "times new roman", 20, "bold"), bg="white", fg="dark blue")
        title.place(x=50, y=30)

        # Define variables to store the user input
        self.other_qualification = StringVar()
        self.qualification_var = StringVar()

        f_name = Label(frame1, text="Name", font=(
            "times new roman", 12, "bold"), bg="white", fg="black")
        f_name.place(x=50, y=80)
        self.txt_fname = Entry(frame1, font=(
            "times new roman", 12), bg="lightgrey")
        self.txt_fname.place(x=50, y=110, width=250)

        l_name = Label(frame1, text="User ID", font=(
            "times new roman", 12, "bold"), bg="white", fg="black")
        l_name.place(x=370, y=80)
        self.txt_lname = Entry(frame1, font=(
            "times new roman", 12), bg="lightgrey")
        self.txt_lname.place(x=370, y=110, width=250)

        # ---------------row2
        contact = Label(frame1, text="Contact", font=(
            "times new roman", 12, "bold"), bg="white", fg="black")
        contact.place(x=50, y=150)
        self.txt_contact = Entry(frame1, font=(
            "times new roman", 12), bg="lightgrey")
        self.txt_contact.place(x=50, y=180, width=250)

        email = Label(frame1, text="Email", font=(
            "times new roman", 12, "bold"), bg="white", fg="black")
        email.place(x=370, y=150)
        self.txt_email = Entry(frame1, font=(
            "times new roman", 12), bg="lightgrey")
        self.txt_email.place(x=370, y=180, width=250)

        # --------------row3

        answer = Label(frame1, text="Qualification", font=(
            "times new roman", 12, "bold"), bg="white", fg="grey")
        answer.place(x=50, y=220)
        self.cmb_ans = ttk.Combobox(frame1, font=(
            "times new roman", 11), state="readonly")
        self.cmb_ans['values'] = ("Select", "High School", "Associate's Degree",
                                  "Bachelor's Degree", "Master's Degree", "Doctorate/Ph.D.", "Other")
        self.cmb_ans.place(x=50, y=250, width=250)
        self.cmb_ans.current(0)
        

        # Function to show the text field for "Other" qualification
        def show_other_text_field():
            if self.cmb_ans.get() == "Other":
                other.place(x=370, y=220)
                self.other_qualification_entry.place(x=370, y=250, width=250)
            else:
                self.other_qualification_entry.place_forget()
                other.place_forget()

        # Call the function when the user selects an option from the combobox
        self.cmb_ans.bind("<<ComboboxSelected>>",
                          lambda event: show_other_text_field())

        # Text field for "Other" qualification
        other = Label(frame1, text="Enter Qualification", font=("times new roman", 12, "bold"), bg="white", fg="black")
        self.other_qualification_entry = Entry(frame1, font=("times new roman", 12), bg="lightgrey", textvariable=self.other_qualification)

        # ============row4

        password = Label(frame1, text="Password", font=(
            "times new roman", 12, "bold"), bg="white", fg="black")
        password.place(x=50, y=290)
        self.txt_password = Entry(frame1, font=("times new roman", 12), bg="lightgrey",show="*")
        self.txt_password.place(x=50, y=320, width=250)

        c_password = Label(frame1, text="Confirm Password", font=(
            "times new roman", 12, "bold"), bg="white", fg="black")
        c_password.place(x=370, y=290)
        self.txt_c_password = Entry(frame1, font=(
            "times new roman", 12), bg="lightgrey",show="*")
        self.txt_c_password.place(x=370, y=320, width=250)

        # ---terms & conditions
        self.var_check = IntVar()
        chk = Checkbutton(frame1, text="I Agree The Terms & Conditions", variable=self.var_check,
                          onvalue=1, offvalue=0, bg="white", font=("times new roman", 12))
        chk.place(x=50, y=380)

        btn = Image.open(
            "C:\\Users\\Tanya Tiwari\\Desktop\\project\\GUI\\images\\Register-Button-Transparent-Background.png")
        self.btn_img = ImageTk.PhotoImage(btn.resize((120, 40)))
        btn_btn = Button(frame1, image=self.btn_img, bd=0,
                         cursor="hand2", bg="white", command=self.register_data)
        btn_btn.place(x=50, y=420)

        login_btn = Image.open(
            "C:\\Users\\Tanya Tiwari\\Desktop\\project\\GUI\\images\\imgonline-com-ua-ReplaceColor-IbGPBKlSfF1DnVyt.jpg")
        self.login_btn = ImageTk.PhotoImage(login_btn.resize((80, 30)))
        btn_login = Button(frame1, image=self.login_btn, bd=0, cursor="hand2",
                           bg="white", command=self.login).place(x=540, y=20, width=150)

        # Update the qualification variable when "Other" qualification is filled and Enter is pressed
        def update_qualification(event):
            self.qualification_var.set(self.cmb_ans.get())
            if self.cmb_ans.get() == "Other":
                self.qualification_var.set(self.other_qualification.get())

        self.other_qualification_entry.bind("<Return>", update_qualification)

    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_c_password.delete(0, END)
        self.cmb_ans.current()

    

    def register_data(self):
        if self.txt_fname.get() == "" or self.txt_lname.get() == "" or self.txt_contact.get() == "" or self.txt_email.get() == "" or self.cmb_ans.get() == "Select" or self.txt_password.get() == "" or self.txt_c_password.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
            
        elif self.cmb_ans.get()=="Other" and self.other_qualification_entry.get()=="":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        

        elif re.match(Register.pattern,self.txt_email.get()) is None:
            messagebox.showerror("Error", "Invalid email", parent=self.root)

        elif self.txt_password.get() != self.txt_c_password.get():
            messagebox.showerror("Error", "Confirm Password should be same as Password", parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please Agree on the Terms & Conditions", parent=self.root)
        else:
            try:
                connection = pymysql.connect(
                    host="localhost", user="root", password="12345", database="users")
                cur = connection.cursor()
                cur.execute("select * from register where l_name= %s",self.txt_lname.get())
                cur2=connection.cursor()
                cur2.execute("select * from register where email= %s",self.txt_email.get())
                row = cur.fetchone()
                row2 = cur2.fetchone()
                if row != None or row2 != None:
                    messagebox.showerror("Error", "User Already Exists", parent=self.root)
                else:
                    if self.cmb_ans.get() == "Other":
                        cur.execute("insert into register (f_name,l_name,contact,email,answer,password) values(%s,%s,%s,%s,%s,%s)",
                                    (self.txt_fname.get(),
                                     self.txt_lname.get(),
                                     self.txt_contact.get(),
                                     self.txt_email.get(),
                                     self.other_qualification_entry.get(),
                                     self.txt_password.get()
                                     ))
                        connection.commit()
                        connection.close()
                        messagebox.showinfo("Success", "Registered Sucessfully")
                        self.clear()

                    else:

                        cur.execute("insert into register (f_name,l_name,contact,email,answer,password) values(%s,%s,%s,%s,%s,%s)",
                                (self.txt_fname.get(),
                                 self.txt_lname.get(),
                                 self.txt_contact.get(),
                                 self.txt_email.get(),
                                 self.cmb_ans.get(),
                                 self.txt_password.get()
                                 ))
                        connection.commit()
                        connection.close()
                        messagebox.showinfo("Success", "Registered Sucessfully")
                        self.clear()

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root)
            
    def login(self):
        self.root.destroy()
        import login

root = Tk()
obj = Register(root)
root.mainloop()

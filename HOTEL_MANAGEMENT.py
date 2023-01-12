import mysql.connector as c
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime as dt
import time
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


# creating the main window class


class App(tk.Tk):

    ''' this is the class that creates the tkinter window and contains the basic elements such as the geometry
    it contains all the frames in a container frame that are switched by creating a dictionary of frame objects
    and using the .tkraise() function to stack them on each other'''

    def __init__(self,*args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Reva's Hotel Management System")

        self.icon=tk.PhotoImage(file="hotel_icon_photo.png")

        self.iconphoto(False, self.icon )

        self.geometry("1260x640")

        self.grid_rowconfigure(0, weight=1) 
        self.grid_columnconfigure(0, weight=1)

        self.config(bg="#f2f2f2")

        self.minsize(400,400)

        # creating a container to hold frames

        container=tk.Frame()
        container.grid(row=0, column=0, sticky="NSEW")

        container.grid_rowconfigure(0, weight=1) 
        container.grid_columnconfigure(0, weight=1)

        # initializing the frame object dictionary 

        self.frames={}

        # filling the frame object dictionary with the main two frames

        for f in {frame_login, frame_main}:
            frame_name=f.__name__
            frame= f(parent=container, controller=self)
            frame.grid(row=0, column=0, sticky="NSEW")
            self.frames[frame_name]=frame

        self.show_frame("frame_login")

    # class function to show the frame

    def show_frame(self, frame_name):
        frame=self.frames[frame_name]
        frame.tkraise()


# ======================================================================================================================
# ================================================ main login frame class===============================================
# ======================================================================================================================


class frame_login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

        frame_heading= tk.Frame(self, bg="#0e6fed")
        frame_heading.pack(side="top", fill="x") 

        heading=tk.Label(frame_heading, text="Welcome To The Hotel Management System!", fg="white", bg="#0e6fed", font="ariel 20 bold")
        heading.pack(pady=10)
        subheading=tk.Label(frame_heading, text="Manage your Hotel with ease...", fg="white", bg="#0e6fed", font="ariel 15 bold")
        subheading.pack(pady=10)
        created_by=tk.Label(frame_heading, text=''' MADE BY : REVA BHARARA
        BTECH COMPUTER SCIENCE ENGINEERING STUDENT AT VIT BHOPAL
        CONTACT INFO:
        revabharara@gmail.com
        reva.bharara2021@vitbhopal.ac.in''', fg="white", bg="#0e6fed", font="ariel 10 bold")
        created_by.pack(pady=5)


# ======================================================================================================================
# ================================================ Login for existing users ============================================
# ======================================================================================================================


        frame_main1=tk.Frame(self,bg="#f2f2f2")
        frame_main1.pack(fill="both", side="left")


        existing_user=tk.Label(frame_main1, text= "Login for existing users", fg="black", bg="#f2f2f2", font="ariel 15 bold")
        existing_user.grid(padx=15, pady=20)

        existing_user_message=tk.Label(frame_main1, text= "Enter your details:", bg="#f2f2f2", font="ariel 12")
        existing_user_message.grid(row=1, padx=15, pady=10)

        manager_id=tk.Label(frame_main1, text="Manager Id", bg="#f2f2f2",font="ariel 12")
        Username=tk.Label(frame_main1, text="Username", bg="#f2f2f2",font="ariel 12")
        Password=tk.Label(frame_main1, text="Password",bg="#f2f2f2", font="ariel 12")

        manager_id.grid(row=2,padx=15, pady=10)
        Username.grid(row=3,padx=15, pady=10)
        Password.grid(row=4, padx=15, pady=10)

        self.manager_idval=tk.IntVar()
        self.existingusernameval=tk.StringVar()
        self.existingpasswordval=tk.StringVar()

        manager_id_entry=tk.Entry(frame_main1, textvariable=self.manager_idval)
        username_entry=tk.Entry(frame_main1, textvariable=self.existingusernameval)
        password_entry=tk.Entry(frame_main1, textvariable=self.existingpasswordval)

        manager_id_entry.grid(row=2,column=1, pady=20, padx=10)
        username_entry.grid(row=3,column=1, pady=20, padx=10)
        password_entry.grid(row=4, column=1 , pady=10, padx=10)

        Login_button=tk.Button(frame_main1,text="Login", fg="white", bg="#1DB74E", font="ariel 15 bold", activebackground="#79F7A1", command=self.manager_login)
        Login_button.grid(row=5, column=1, pady=10)


# ====================================================================================================================
# ============================================== Sign up for new users ===============================================
# ====================================================================================================================


        frame_main2=tk.Frame(self,bg="#f2f2f2")
        frame_main2.pack(fill="both", side="left")

        New_user=tk.Label(frame_main2, text= "Signup for new users", fg="black", bg="#f2f2f2", font="ariel 15 bold")
        New_user.grid(padx=45, pady=20)

        # this small code block helps to print the auto generated manager id from the database

        manager_id_query="SELECT COUNT(*) FROM managers "
        cursor.execute(manager_id_query)
        ids=cursor.fetchone()
        self.auto_manager_id=(ids[0]+1)

        Manager_Id=tk.Label(frame_main2, text=f"Your auto generated Manager Id is: {self.auto_manager_id} ", bg="#f2f2f2",font="ariel 12", justify="left")
        Username=tk.Label(frame_main2, text="Username", bg="#f2f2f2",font="ariel 12", justify="left")
        Password=tk.Label(frame_main2, text="Password",bg="#f2f2f2", font="ariel 12",justify="left")
        Confirm_Password=tk.Label(frame_main2, text="Confirm Password",bg="#f2f2f2", font="ariel 12", justify="left")

        Manager_Id.grid(row=1, padx=45, pady=10)
        Username.grid(row=2,padx=45, pady=10)
        Password.grid(row=3, padx=45, pady=10)
        Confirm_Password.grid(row=4, padx=45, pady=10)

        self.usernameval=tk.StringVar()
        self.passwordval=tk.StringVar()
        self.confirmpasswordval=tk.StringVar()

        username_entry=tk.Entry(frame_main2, textvariable=self.usernameval)
        password_entry=tk.Entry(frame_main2, textvariable=self.passwordval)
        Confirm_password_entry=tk.Entry(frame_main2, textvariable=self.confirmpasswordval)

        username_entry.grid(row=2,column=1, pady=10, padx=10)
        password_entry.grid(row=3, column=1 , pady=10, padx=10)
        Confirm_password_entry.grid(row=4, column=1, pady=10)

        Login_button=tk.Button(frame_main2,text="Sign up", fg="white", bg="#1DB74E", font="ariel 15 bold", activebackground="#79F7A1", command=self.new_manager_login)
        Login_button.grid(row=5, column=1, pady=10)


# ======================================================================================================================
# ======================================== FAQ frame ===================================================================
# ======================================================================================================================


        frame_FAQ=tk.Frame(self,bg="#545454")
        frame_FAQ.pack(side="right", fill="both")
        FAQ=tk.Label(frame_FAQ,bg="#545454",fg="white", text='''        This hotel management system 
        keep tracks of the hotel bookings 
        and has the following features:

        1. Gives you insights on the 
        profits and sales for a 
        particular duration.

        2. Make changes in the rooms 
        and their status accordingly.

        3. Has a flexible user-
        friendly GUI support.

        4. Helps to manage and view 
        the booking history and other 
        records easily. 

        5. Contains logs of all 
        logins and bookings.

        6. hashing passwords from MD5 for 
        security.

        ''',font="ariel 11", justify = "left" )
        FAQ.pack(padx=7, pady=7 ,fill="both")


# ====================================================================================================================
# ======================================== class login frame functions (backend) ======================================
# =====================================================================================================================

    def new_manager_login(self):
        ''' this function of the login frame help to register a new manager into the system by updating the details
        into the database and it keeps the passwrod encrypyted using md5 hashinh security'''
    
        if self.passwordval.get()!= self.confirmpasswordval.get():
            messagebox.showerror("Incorrect password!","The passwords you enetered did not match.")

        elif self.usernameval.get()=="" or self.passwordval.get()=="":
            messagebox.showwarning("empty fields", "enter all the details.")

        else:
            new_login_query= f"INSERT INTO managers VALUES({self.auto_manager_id},'{self.usernameval.get()}', md5('{self.passwordval.get()}'))"

            cursor.execute(new_login_query)
            connection.commit()

            logs_query=f"INSERT INTO manager_logins VALUES({self.auto_manager_id},'{self.usernameval.get()}','{dt.datetime.now().time()}', '{dt.date.today()}' )"
            # print(f"{auto_manager_id},{usernameval.get()}, {dt.datetime.now().strftime('%H:%M:%S')}, {dt.date.today()}")
            cursor.execute(logs_query)
            connection.commit()

            # opens the next window after this

            self.controller.show_frame("frame_main")
    
    def manager_login(self):

        ''' this class function helpes the already existing managers to login, it tallies the entered details with
        the details of the database and logs the user in while at the same time enters the logs in the login table '''

        # add try except

        query_managers="SELECT manager_id from managers"
        cursor.execute(query_managers)
        managers=cursor.fetchall()
        data_manager=[]

        for i in range(len(managers)):
            data_manager.append(managers[i][0])
    #    print(data_manager)

        query_password=f"select password from managers where manager_id={self.manager_idval.get()} and password = md5('{self.existingpasswordval.get()}')"
        cursor.execute(query_password)
        data_password=cursor.fetchone()
        # print(manager_idval.get(), passwordval.get())
        # print(data_password)
        
        if self.manager_idval.get() not in data_manager:
            messagebox.showerror("invalid user", "User does not exist!")

        elif data_password==None:
            messagebox.showerror("invalid password", "Enter the correct password")

        else:
            
            logs_query=f"INSERT INTO manager_logins VALUES({self.manager_idval.get()},'{self.existingusernameval.get()}', '{dt.datetime.now().strftime('%H:%M:%S')}', '{dt.date.today()}')"
            cursor.execute(logs_query)
            connection.commit()

            # connects to the main frame using the controller class function show_frame()
            
            self.controller.show_frame("frame_main")
        

#====================================================================================================================
#=================================================== main frame for operations ======================================
#==================================================================================================================== 


class frame_main(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

        frame_heading_main= tk.Frame(self, bg="#0e6fed")
        frame_heading_main.pack(side="top", fill="x")

        heading=tk.Label(frame_heading_main, text="Hotel Management System", fg="white", bg="#0e6fed", font="ariel 30 bold")
        heading.pack(pady=10)
        subheading=tk.Label(frame_heading_main, text="Manage your Hotel with ease...", fg="white", bg="#0e6fed", font="ariel 23 bold")
        subheading.pack(pady=10)

#====================================================================================================================
#=================================================== date time frame bottom =========================================
#==================================================================================================================== 

        frame_main_datetime=tk.Frame(self , bg="#1DB74E")
        frame_main_datetime.pack(side='bottom', fill="both")

        self.label_date=tk.Label(frame_main_datetime,text=f"Date : {dt.date.today()}", fg="white", bg="#1DB74E", font="ariel 11")
        self.label_date.pack(side="right" ,fill="both", padx=20)

        created_by=tk.Label(frame_main_datetime, text=''' MADE BY : REVA BHARARA      CONTACT INFO: revabharara@gmail.com''', fg="white", bg="#1DB74E", font="ariel 9 bold")
        created_by.pack(side= "left",pady=2)


#===========================================================================================================================
#===================================================== frame buttons side ==================================================
#===========================================================================================================================

        frame_buttons_main=tk.Frame(self,bg="#545454")
        frame_buttons_main.pack(side="left", fill="y")

        # configuring the rows and columns of the grid

        frame_buttons_main.grid_rowconfigure(0,weight=1)
        frame_buttons_main.grid_rowconfigure(0,weight=2)
        frame_buttons_main.grid_rowconfigure(0,weight=3)
        frame_buttons_main.grid_rowconfigure(0,weight=4)
        frame_buttons_main.grid_rowconfigure(0,weight=5)
        frame_buttons_main.grid_rowconfigure(0,weight=6)
        frame_buttons_main.grid_rowconfigure(0,weight=7)
        frame_buttons_main.grid_rowconfigure(0,weight=8)
        frame_buttons_main.grid_rowconfigure(0,weight=9)
        frame_buttons_main.grid_rowconfigure(0,weight=10)
        frame_buttons_main.grid_rowconfigure(0,weight=11)

        # creating and packing the buttons

        button_home=tk.Button(frame_buttons_main ,text="Home Page", bg="#545454",fg="white", justify="left",font="ariel 9", width=25, height=2, activebackground="dark grey", command= lambda: self.show_subframe("homepage"))
        button_home.grid()

        button_check_in=tk.Button(frame_buttons_main ,text="Check In", bg="#545454",fg="white", justify="left",font="ariel 9", width=25, height=2, activebackground="dark grey", command= lambda: self.show_subframe("check_in"))
        button_check_in.grid(row=1)

        button_check_out=tk.Button(frame_buttons_main ,text="Check Out", bg="#545454",fg="white", justify="left",font="ariel 9", width=25, height=2, activebackground="dark grey", command= lambda: self.show_subframe("check_out"))
        button_check_out.grid(row=2)

        button_check_rooms=tk.Button(frame_buttons_main ,text="Check Room Status", bg="#545454",fg="white", justify="left",font="ariel 9", width=25, height=2, activebackground="dark grey", command= lambda: self.show_subframe("check_room_status"))
        button_check_rooms.grid(row=3)

        button_add_rooms=tk.Button(frame_buttons_main ,text="Add Rooms", bg="#545454",fg="white", justify="left",font="ariel 9", width=25, height=2, activebackground="dark grey", command= lambda: self.show_subframe("add_rooms"))
        button_add_rooms.grid(row=4)

        button_update_rooms=tk.Button(frame_buttons_main ,text="Update Rooms", bg="#545454",fg="white", justify="left",font="ariel 9", width=25, height=2, activebackground="dark grey", command= lambda: self.show_subframe("update_rooms"))
        button_update_rooms.grid(row=5)

        button_delete_rooms=tk.Button(frame_buttons_main ,text="Delete Rooms", bg="#545454",fg="white", justify="left",font="ariel 9", width=25, height=2, activebackground="dark grey", command= lambda: self.show_subframe("delete_rooms"))
        button_delete_rooms.grid(row=6)

        button_booking_details=tk.Button(frame_buttons_main ,text="Booking Details", bg="#545454",fg="white", justify="left",font="ariel 9", width=25, height=2, activebackground="dark grey", command= lambda: self.show_subframe("booking_details"))
        button_booking_details.grid(row=7)

        button_customer_details=tk.Button(frame_buttons_main ,text="Customer Details", bg="#545454",fg="white", justify="left",font="ariel 9", width=25, height=2, activebackground="dark grey", command= lambda: self.show_subframe("customer_details"))
        button_customer_details.grid(row=8)

        button_employee=tk.Button(frame_buttons_main ,text="Employee Info", bg="#545454",fg="white", justify="left",font="ariel 9", width=25, height=2, activebackground="dark grey", command= lambda: self.show_subframe("employee_info"))
        button_employee.grid(row=9)

        button_employee_logins=tk.Button(frame_buttons_main ,text="Employee Login Info", bg="#545454",fg="white", justify="left",font="ariel 9", width=25, height=2, activebackground="dark grey", command= lambda: self.show_subframe("employee_login_info"))
        button_employee_logins.grid(row=10)

        button_sign_out=tk.Button(frame_buttons_main ,text="Sign Out", bg="#545454",fg="white", justify="left",font="ariel 9", width=25, height=2, activebackground="dark grey", command=self.sign_out)
        button_sign_out.grid(row=11)

# =====================================================================================================================
# ================================================ frame picture ======================================================
# =====================================================================================================================

        frame_bg_image=tk.Frame(self,bg="#f2f2f2")
        frame_bg_image.pack(side="right", fill="both", expand=True)

        self.image_bg=tk.PhotoImage(file="main_bg_image.png")
        image_label=tk.Label(frame_bg_image,image=self.image_bg)
        image_label.grid(row=0,column=1, sticky="NSEW")


# =====================================================================================================================
# ================================================ frame main activity ================================================
# =====================================================================================================================

        # this frame in a container for the subframes to switch that switch when the buttons are pressed

        self.frame_main_activity=tk.Frame(self, bg="#f2f2f2")
        self.frame_main_activity.pack(side="right",fill="both", expand=True)

        # initializing the subframe object distionary

        self.sub_frames={}

        # populating the subframe oject dictionary

        for sf in {homepage, check_in,check_out, check_room_status, add_rooms, update_rooms ,delete_rooms ,booking_details, customer_details, employee_info, employee_login_info}:
            sf_name=sf.__name__
            sub_frame=sf(parent_frame=self.frame_main_activity, controller=self)
            sub_frame.grid(row=0,column=0, sticky="NSEW")
            self.sub_frames[sf_name]=sub_frame

        self.show_subframe("homepage")

        # this functions helps to show the subframes by lifting them up and making them visible as the buttions are pressed

    def show_subframe(self,subframe_name):
        sub_frame=self.sub_frames[subframe_name]
        sub_frame.tkraise()

        # funcion for signing out and going back to login page

    def sign_out(self):
        self.controller.show_frame("frame_login")

        # this function basically helps to update the table contents in the treeview as changes are made into the database
    
    def refresh(self, frame):

        ''' this function helps to reflect the changes in treeview that are made in the database, this happenes
        by destroying the current frame and initializing it again while adding it to the object dictionary 
        with the new changes in place
        '''

        # destroy old frame 

        to_destroy=self.sub_frames[frame.__name__]
        to_destroy.destroy()

        # create new updated frame

        refreshed_frame=frame(parent_frame=self.frame_main_activity, controller=self)
        refreshed_frame.grid(row=0,column=0, sticky="NSEW")
        self.sub_frames[frame.__name__]=refreshed_frame


# =====================================================================================================================
# ================================================ homepage subframe ==================================================
# =====================================================================================================================


class homepage(tk.Frame):
    def __init__(self, parent_frame, controller):
        tk.Frame.__init__(self,parent_frame)

        homepage_label=tk.Label(self, text="Profit report", bg="#f2f2f2", font="ariel 15 bold")
        homepage_label.grid(row=0, column=0, sticky="w", padx=30, pady=7)

        # calling in the refresh function from frame_main (controller) to update the details

        refresh_button=tk.Button(self,text="Refresh", fg="white", bg="#FF4040", command= lambda:controller.refresh(homepage))
        refresh_button.grid(row=0, column=0, padx=(200,0))
 
        label_info=tk.Label(self,text='''
        This hotel management system 
        keep tracks of the hotel bookings 
        and has the following features:

        1. Make changes in the rooms 
        and their status accordingly.

        2. Has a flexible user-
        friendly GUI support.

        3. Helps to manage and view 
        the booking history and other 
        records easily. 

        4. Contains logs of all 
        logins and bookings.

        5. hashing passwords from MD5 for 
        security.''',font="ariel 12", justify = "left" )

        label_info.grid(row=1, column=0)

        # adding pie chart for data visualization

        pie_chart_label=tk.Label(self, text="Current Hotel Room Status", bg="#f2f2f2", font="ariel 14 bold")
        pie_chart_label.grid(row=0, column=1, sticky="w", padx=(95, 50), pady=7)

        # adding the matplotlib figure

        fig=Figure(figsize=(4,4), dpi=100)

        # adding the subplot 
        a=fig.add_subplot(111)

        # plotting the data

        query_filled_rooms="SELECT COUNT(*) FROM room where availability=0"

        query_empty_rooms="SELECT COUNT(*) FROM room where availability=1"

        cursor.execute(query_filled_rooms)
        self.rooms_filled_tuple=cursor.fetchone()
        self.rooms_filled=self.rooms_filled_tuple[0]

        cursor.execute(query_empty_rooms)
        self.rooms_empty_tuple=cursor.fetchone()
        self.rooms_empty=self.rooms_empty_tuple[0]


        pie_labels=[f"occupied: {self.rooms_filled}", f"available: {self.rooms_empty}"]
        a.pie([self.rooms_filled, self.rooms_empty], labels=pie_labels)

        # creating the canvas to show the plot in

        canvas=FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=1, sticky="NSEW", padx=(95, 50))

        
# =====================================================================================================================
# ================================================ check in subframe ==================================================
# =====================================================================================================================


class check_in(tk.Frame):
    def __init__(self, parent_frame, controller):
        tk.Frame.__init__(self,parent_frame)

        check_in_label=tk.Label(self, text="Check In", bg="#f2f2f2", font="ariel 15 bold")
        check_in_label.grid(row=0, column=0, sticky="w", padx=30, pady=7)

        # bringing in the required data from the database

        customer_id_query="SELECT COUNT(*) FROM customer "
        cursor.execute(customer_id_query)
        ids=cursor.fetchone()
        self.auto_customer_id=(ids[0]+1)

        bill_id_query="SELECT COUNT(*) FROM booking_details "
        cursor.execute(bill_id_query)
        ids=cursor.fetchone()
        self.auto_bill_id=(ids[0]+1)

        customer_Id=tk.Label(self, text=f"Your auto generated Customer Id is: {self.auto_customer_id} ", bg="#f2f2f2",font="ariel 11", justify="left")
        customer_Id.grid(row=1, column=0, pady=10, padx=10)

        customer_Id=tk.Label(self, text=f"Your auto generated Bill Id is: {self.auto_bill_id} ", bg="#f2f2f2",font="ariel 11", justify="left")
        customer_Id.grid(row=1, column=2, pady=10, padx=10)

        cust_name=tk.Label(self, text="Name", bg="#f2f2f2", font="ariel, 11", justify="left")
        cust_name.grid(row=2, column=0, pady=15, padx=10)

        cust_age=tk.Label(self, text="Age", bg="#f2f2f2", font="ariel, 11")
        cust_age.grid(row=2, column=2, pady=15, padx=10)

        cust_phone_no=tk.Label(self, text="Phone number", bg="#f2f2f2", font="ariel, 11")
        cust_phone_no.grid(row=3, column=0, pady=15, padx=10)

        cust_gender=tk.Label(self, text="Gender", bg="#f2f2f2", font="ariel, 11")
        cust_gender.grid(row=3, column=2, pady=15, padx=10)

        cust_address=tk.Label(self, text="Address", bg="#f2f2f2", font="ariel, 11")
        cust_address.grid(row=4, column=0, pady=15, padx=10)

        cust_adhaar_no=tk.Label(self, text="Adhaar number", bg="#f2f2f2", font="ariel, 11")
        cust_adhaar_no.grid(row=4, column=2, pady=15, padx=10)

        cust_no_people=tk.Label(self, text="Number of people", bg="#f2f2f2", font="ariel, 11")
        cust_no_people.grid(row=5, column=0, pady=15, padx=10)
        
        cust_room_no=tk.Label(self, text="Room number", bg="#f2f2f2", font="ariel, 11")
        cust_room_no.grid(row=5, column=2, pady=15, padx=10)

        self.breakfast_var=tk.IntVar()

        cust_breakfast=tk.Checkbutton(self, text="Do you want complementary breakfast?", bg="#f2f2f2", font="ariel, 11", variable=self.breakfast_var)
        cust_breakfast.grid(row=6, column=0, pady=15, padx=10)

        cust_check_out=tk.Label(self, text="Check out date\n (YYYY-MM-DD)", bg="#f2f2f2", font="ariel, 11")
        cust_check_out.grid(row=6, column=2, pady=15, padx=10)

        cust_payment_amount=tk.Label(self, text="Payment amount", bg="#f2f2f2", font="ariel, 11")
        cust_payment_amount.grid(row=7, column=0, pady=15, padx=10)

        cust_payment_method=tk.Label(self, text="Payment method", bg="#f2f2f2", font="ariel, 11")
        cust_payment_method.grid(row=7, column=2, pady=15, padx=10)

        self.cust_name_var=tk.StringVar()
        self.cust_age_var=tk.IntVar()
        self.cust_phone_no_var=tk.IntVar()
        self.cust_gender_var=tk.StringVar()
        self.cust_address_var=tk.StringVar()
        self.cust_adhaar_no_var=tk.IntVar()
        self.cust_no_people_var=tk.IntVar()
        self.cust_room_no_var=tk.StringVar()
        self.cust_check_out_var=tk.StringVar()
        self.cust_payment_amount_var=tk.IntVar()
        self.cust_payment_method_var=tk.StringVar()

        cust_name_entry=tk.Entry(self, textvariable=self.cust_name_var)
        cust_age_entry=tk.Entry(self, textvariable=self.cust_age_var)
        cust_phone_no_entry=tk.Entry(self, textvariable=self.cust_phone_no_var)
        cust_gender_entry=tk.Entry(self, textvariable=self.cust_gender_var)
        cust_address_entry=tk.Entry(self, textvariable=self.cust_address_var)
        cust_adhaar_no_entry=tk.Entry(self, textvariable=self.cust_adhaar_no_var)
        cust_no_people_entry=tk.Entry(self, textvariable=self.cust_no_people_var)
        cust_room_no_entry=tk.Entry(self, textvariable=self.cust_room_no_var)
        cust_check_out_entry=tk.Entry(self, textvariable=self.cust_check_out_var)
        cust_payment_amount_entry=tk.Entry(self, textvariable=self.cust_payment_amount_var)
        cust_payment_method_entry=tk.Entry(self, textvariable=self.cust_payment_method_var)
        
        cust_name_entry.grid(row=2, column=1, pady=10)
        cust_age_entry.grid(row=2, column=3, pady=10)
        cust_phone_no_entry.grid(row=3, column=1, pady=10)
        cust_gender_entry.grid(row=3, column=3, pady=10)
        cust_address_entry.grid(row=4, column=1, pady=10)
        cust_adhaar_no_entry.grid(row=4, column=3, pady=10)
        cust_no_people_entry.grid(row=5, column=1, pady=10)
        cust_room_no_entry.grid(row=5, column=3, pady=10)
        cust_check_out_entry.grid(row=6, column=3, pady=10)
        cust_payment_amount_entry.grid(row=7, column=1, pady=10)
        cust_payment_method_entry.grid(row=7, column=3, pady=10)

        button_check_in=tk.Button(self,text="Check In", bg="#FF4040", fg="white", font="ariel 15 bold", activebackground="#E26868", command=self.check_in)
        button_check_in.grid(row=8, column=2, pady=10)


    def check_in(self):

        details_list=[self.cust_name_var.get(), self.cust_age_var.get(), self.cust_phone_no_var.get(), self.cust_gender_var.get(), self.cust_address_var.get(), self.cust_adhaar_no_var.get(), self.cust_no_people_var.get(), self.cust_room_no_var.get(), self.cust_check_out_var.get(), self.cust_payment_amount_var.get(), self.cust_payment_method_var.get()]

        # error handling for empty fields

        if "" in details_list:
            messagebox.showerror("Invaild entry", "Some fields were left empty")

        # error handling for room doesn't exists

        query_room=f"SELECT room_number,room_rate, availability from room where room_number='{self.cust_room_no_var.get()}'"
        cursor.execute(query_room)
        data=cursor.fetchall()
        rows=cursor.rowcount

        if rows==0:
            messagebox.showerror("Invaild entry", "No such room exists, check the room number again")

        # error handling for room that is already occupied

        elif data[0][2]==0:
            messagebox.showerror("Room Occupied", "The room number entered has already been occupied")

        # error handling for invalid price

        elif data[0][1]!=self.cust_payment_amount_var.get():
            messagebox.showerror("Price mismatch", "The amount paid by the user does not correspond to the respective room rate")
    
        else:
            try:
                query_insert_customer=f"INSERT INTO `customer` VALUES ('{self.auto_customer_id}','{self.cust_name_var.get()}','{self.cust_phone_no_var.get()}','{self.cust_age_var.get()}','{self.cust_gender_var.get()}','{self.cust_address_var.get()}','{self.cust_adhaar_no_var.get()}','{self.cust_room_no_var.get()}','{self.auto_bill_id}')"
                cursor.execute(query_insert_customer)

                query_insert_booking_details=f"INSERT INTO `booking_details` VALUES ('{self.auto_bill_id}','{self.cust_room_no_var.get()}','{dt.date.today()}','{dt.datetime.now().strftime('%H:%M:%S')}','{self.cust_payment_amount_var.get()}','{self.cust_payment_method_var.get()}','{self.cust_no_people_var.get()}','{self.auto_customer_id}','{self.breakfast_var.get()}','{self.cust_check_out_var.get()}')"
                cursor.execute(query_insert_booking_details)

                query_room_status =f"UPDATE `room` SET `availability`='0',`occupant`='{self.auto_customer_id}' WHERE `room_number`='{self.cust_room_no_var.get()}'"
                cursor.execute(query_room_status)

                connection.commit()

                messagebox.showinfo("Task successful", "The details have been added to the database successfully")
            
            except:
                messagebox.showerror("Error occured", "There was an error please try again")

    
# =====================================================================================================================
# ================================================ check out subframe ==================================================
# =====================================================================================================================


class check_out(tk.Frame):
    def __init__(self, parent_frame, controller):
        tk.Frame.__init__(self,parent_frame)

        check_out_label=tk.Label(self, text="Check Out", bg="#f2f2f2", font="ariel 15 bold")
        check_out_label.grid(row=0, column=0, sticky="w", padx=30, pady=30)

        cust_Id=tk.Label(self, text="Enter the Customer Id", bg="#f2f2f2", font="ariel, 13")
        cust_Id.grid(row=1, column=0, pady=10, padx=30)

        self.cust_Id_var=tk.IntVar()

        cust_Id_entry=tk.Entry(self, textvariable=self.cust_Id_var)

        cust_Id_entry.grid(row=2, column=0, padx=30, pady=10)

        check_out_button=tk.Button(self,text="Check Out", bg="#FF4040", fg="white", font="ariel 15 bold", activebackground="#E26868", command=self.check_out)
        check_out_button.grid(row=3, column=0, pady=20)

    def check_out(self):
        try:
            query_check_out=f"UPDATE `room` SET `availability`='1',`occupant`='NULL' WHERE occupant='{self.cust_Id_var.get()}'"
            cursor.execute(query_check_out)

            connection.commit()

            if cursor.rowcount>0:
                messagebox.showinfo("task completed", "Checked out successfully!")
            else:
                messagebox.showerror("task failed", '''Couldn't check out, please try again.
    (If the rooms table is empty or some error occured you cannot heck out)''')
        except:
            messagebox.showerror("Error occured", "Some of the fields were either left empty or there was some database issue")


# =====================================================================================================================
# ================================================ check room status subframe =========================================
# =====================================================================================================================


class check_room_status(tk.Frame):
    def __init__(self, parent_frame, controller):
        tk.Frame.__init__(self,parent_frame)

        check_room_status_query="SELECT * from room"

        cursor.execute(check_room_status_query)

        self.data=cursor.fetchall()

        # print(self.data)

        check_room_status_label=tk.Label(self, text="Current room status", bg="#f2f2f2", font="ariel 15 bold")
        check_room_status_label.grid(row=0, column=0, sticky="w", padx=30, pady=30)

        # refreshes the window to show the updated data in thetreeview

        refresh_button=tk.Button(self,text="Refresh", fg="white", bg="#FF4040", command= lambda:controller.refresh(check_room_status))
        refresh_button.grid(row=0, column=1)

        # styling the treeview

        style=ttk.Style()
        style.configure("Treeview", rowheight=50)

        style.map("Treeview")

        # we make a column ka tuple i.e. columns define kr diye

        col=("room No", "room type", "room rate", "availability", "occupant")

        self.room_table=ttk.Treeview(self, height=7, columns=col, show="headings")

        self.room_table.column("room No", anchor="w", width=140, minwidth=100)
        self.room_table.column("room type", anchor="w", width=140, minwidth=100)
        self.room_table.column("room rate", anchor="w", width=140, minwidth=100)
        self.room_table.column("availability", anchor="w", width=140, minwidth=100)
        self.room_table.column("occupant", anchor="w", width=140, minwidth=100)

        self.room_table.heading("room No", text="Room No", anchor='w')
        self.room_table.heading("room type", text="Room Type", anchor='w')
        self.room_table.heading("room rate", text="Room Rate", anchor='w')
        self.room_table.heading("availability", text="Availability", anchor='w')
        self.room_table.heading("occupant", text="Occupant", anchor='w')
        
        # populating the tree

        for entry in self.data:

            self.room_table.insert('', index="end", values=entry)


        self.room_table.grid(row=1, column=0, sticky='nsew', padx=(50,0))

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.room_table.yview)
        self.room_table.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=1, sticky='nsw')

        
# =====================================================================================================================
# ================================================ add rooms subframe =================================================
# =====================================================================================================================


class add_rooms(tk.Frame):
    def __init__(self, parent_frame, controller):
        tk.Frame.__init__(self,parent_frame)

        add_rooms_label=tk.Label(self, text="Add Rooms", bg="#f2f2f2", font="ariel 15 bold")
        add_rooms_label.grid(row=0, column=0, sticky="w", padx=30, pady=30)

        room_no=tk.Label(self, text="Room number", bg="#f2f2f2", font="ariel, 13")
        room_no.grid(row=1, column=0, sticky="w", padx=30, pady=30)

        room_type=tk.Label(self, text="Room type", bg="#f2f2f2", font="ariel, 13")
        room_type.grid(row=1, column=1, sticky="w", padx=30, pady=30)

        room_rate=tk.Label(self, text="Room rate", bg="#f2f2f2", font="ariel, 13")
        room_rate.grid(row=1, column=2, sticky="w", padx=30, pady=30)

        self.room_no_var=tk.StringVar()
        self.room_type_var=tk.StringVar()
        self.room_rate_var=tk.IntVar()

        room_no_entry=tk.Entry(self,textvariable=self.room_no_var)
        room_no_entry.grid(row=2, column=0, padx=30)

        room_type_entry=tk.Entry(self,textvariable=self.room_type_var)
        room_type_entry.grid(row=2, column=1, padx=30)

        room_no_entry=tk.Entry(self,textvariable=self.room_rate_var)
        room_no_entry.grid(row=2, column=2, padx=30)

        add_room_button=tk.Button(self,text="Add room", bg="#FF4040", fg="white", font="ariel 15 bold", activebackground="#E26868", command= self.add_room)
        add_room_button.grid(row=3, column=1, pady=20)

    def add_room(self):

        ''' this method executes the sql queries to insert data into the table room as well as handle errors'''

        try:
            query_add_room=f"INSERT INTO room VALUES ('{self.room_no_var.get()}','{self.room_type_var.get()}',{self.room_rate_var.get()},'','')"
            cursor.execute(query_add_room)

            connection.commit()

            if cursor.rowcount>0:
                messagebox.showinfo("task completed", "room added successfully!")

            else:
                messagebox.showerror("task failed", "Couldn't add rows, please try again.")
        except:
            messagebox.showerror("Error occured", "Some of the fields were either left empty or there was some database issue")


# =====================================================================================================================
# ================================================ update rooms subframe =================================================
# =====================================================================================================================


class update_rooms(tk.Frame):

    def __init__(self, parent_frame, controller):
        tk.Frame.__init__(self,parent_frame)

        update_rooms_label=tk.Label(self, text="Update Rooms", bg="#f2f2f2", font="ariel 15 bold")
        update_rooms_label.grid(row=0, column=0, sticky="w", padx=30, pady=30)

        room_no=tk.Label(self, text="Room number", bg="#f2f2f2", font="ariel, 13")
        room_no.grid(row=1, column=0, sticky="w", padx=30, pady=30)

        room_type=tk.Label(self, text="New Room type", bg="#f2f2f2", font="ariel, 13")
        room_type.grid(row=1, column=1, sticky="w", padx=30, pady=30)

        room_rate=tk.Label(self, text="New Room rate", bg="#f2f2f2", font="ariel, 13")
        room_rate.grid(row=1, column=2, sticky="w", padx=30, pady=30)

        self.room_no_var=tk.StringVar()
        self.room_type_var=tk.StringVar()
        self.room_rate_var=tk.IntVar()

        room_no_entry=tk.Entry(self,textvariable=self.room_no_var)
        room_no_entry.grid(row=2, column=0, padx=20)

        room_type_entry=tk.Entry(self,textvariable=self.room_type_var)
        room_type_entry.grid(row=2, column=1, padx=20)

        room_no_entry=tk.Entry(self,textvariable=self.room_rate_var)
        room_no_entry.grid(row=2, column=2, padx=20)

        add_room_button=tk.Button(self,text="Update room", bg="#FF4040", fg="white", font="ariel 15 bold", activebackground="#E26868", command=self.update_room)
        add_room_button.grid(row=3, column=1, pady=20)


    def update_room(self):

        ''' this method executes the sql queries to update data values into the table room as well as handle errors'''

        try:
            query_update_room=f"UPDATE room SET `room_number`='{self.room_no_var.get()}',`room_type`='{self.room_type_var.get()}',`room_rate`='{self.room_rate_var.get()}',`availability`='',`occupant`='' WHERE room_number={self.room_no_var.get()}"
            cursor.execute(query_update_room)

            connection.commit()
        
            if cursor.rowcount>0:
                messagebox.showinfo("task completed", "room updated successfully!")
            else:
                messagebox.showerror("task failed", "Couldn't update rooms, please try again.")
        except:
            messagebox.showerror("Error occured", "Some of the fields were either left empty or there was some database issue")


# =====================================================================================================================
# ================================================ delete rooms subframe =================================================
# =====================================================================================================================


class delete_rooms(tk.Frame):
    def __init__(self, parent_frame, controller):
        tk.Frame.__init__(self,parent_frame)

        delete_rooms_label=tk.Label(self, text="Delete Rooms", bg="#f2f2f2", font="ariel 15 bold")
        delete_rooms_label.grid(row=0, column=0, sticky="w", padx=30, pady=30)

        room_no=tk.Label(self, text=" Enter the Room number you want to delete", bg="#f2f2f2", font="ariel, 13")
        room_no.grid(row=1, column=0, sticky="w", padx=30, pady=30)

        self.room_no_var=tk.StringVar()

        room_no_entry=tk.Entry(self,textvariable=self.room_no_var)
        room_no_entry.grid(row=2, column=0, padx=30)

        delete_room_button=tk.Button(self,text="Delete room", bg="#FF4040", fg="white", font="ariel 15 bold", activebackground="#E26868", command=self.delete_room)
        delete_room_button.grid(row=3, column=0, pady=20)


    def delete_room(self):

        ''' this method executes the sql queries to delete data into the table room as well as handle errors'''

        try:
            
            query_delete_room=f"DELETE FROM `room` WHERE room_number='{self.room_no_var.get()}'"
            cursor.execute(query_delete_room)

            connection.commit()

            if cursor.rowcount>0:
                messagebox.showinfo("task completed", "room deleted successfully!")
            else:
                messagebox.showerror("task failed", '''Couldn't delete rooms, please try again.
    (If the rooms table is empty or some error occured you cannot delete rooms)''')
        except:
            
            messagebox.showerror("Error occured", "Some of the fields were either left empty or there was some database issue")


# =====================================================================================================================
# ================================================ booking details subframe ===========================================
# =====================================================================================================================


class booking_details(tk.Frame):
    def __init__(self, parent_frame, controller):
        tk.Frame.__init__(self,parent_frame)

        booking_details_label=tk.Label(self, text="Booking details", bg="#f2f2f2", font="ariel 15 bold")
        booking_details_label.grid(row=0, column=0, sticky="w", padx=30, pady=30)

        refresh_button=tk.Button(self,text="Refresh", fg="white", bg="#FF4040", command= lambda:controller.refresh(booking_details))
        refresh_button.grid(row=0, column=0, padx=100)

        # Getting the data from the database

        query_booking_details="SELECT * FROM booking_details"
        cursor.execute(query_booking_details)

        # fetches a list of tuples
        data=cursor.fetchall()

        # styling the treeview table
        
        style=ttk.Style()
        style.configure("Treeview", rowheight=50)
        style.map("Treeview")

        # creating columns

        self.col=("bill_id", "room_number", "book_date", "book_time", "payment_amount", "payment_method", "number_of_people", "customer_id", "Complimentary_breakfast", "check_out_date")

        # creating the treeview table

        bk_details_table=ttk.Treeview(self, height=7, columns=self.col, show="headings")

        bk_details_table.column("bill_id", anchor="w", width=40)
        bk_details_table.column("room_number", anchor="w", width=60)
        bk_details_table.column("book_date", anchor="w", width=80)
        bk_details_table.column("book_time", anchor="w", width=80)
        bk_details_table.column("payment_amount", anchor="w", width=100)
        bk_details_table.column("payment_method", anchor="w", width=100)
        bk_details_table.column("number_of_people", anchor="w", width=110)
        bk_details_table.column("customer_id", anchor="w", width=80)
        bk_details_table.column("Complimentary_breakfast", anchor="w", width=60)
        bk_details_table.column("check_out_date", anchor="w", width=65)


        bk_details_table.heading("bill_id", text="Bill Id", anchor='w')
        bk_details_table.heading("room_number", text="Room No", anchor='w')
        bk_details_table.heading("book_date", text="Booking date", anchor='w')
        bk_details_table.heading("book_time", text="Booking time", anchor='w')
        bk_details_table.heading("payment_amount", text="Payment amount", anchor='w')
        bk_details_table.heading("payment_method", text="Payment method", anchor='w')
        bk_details_table.heading("number_of_people", text="Number of people", anchor='w')
        bk_details_table.heading("customer_id", text="Customer Id", anchor='w')
        bk_details_table.heading("Complimentary_breakfast", text="Breakfast", anchor='w')
        bk_details_table.heading("check_out_date", text="Check out", anchor='w')

        # populating the treeview
       
        for entry in data:
            bk_details_table.insert('', index="end", values=entry)

        bk_details_table.grid(row=1, column=0, sticky='nsew', padx=(18,0))

        # add a scrollbar
        scrollbary = ttk.Scrollbar(self, orient=tk.VERTICAL, command=bk_details_table.yview)
        bk_details_table.configure(yscroll=scrollbary.set)
        scrollbary.grid(row=1, column=1, sticky='nsw')


# =====================================================================================================================
# ================================================ customer details subframe ==========================================
# =====================================================================================================================


class customer_details(tk.Frame):
    def __init__(self, parent_frame, controller):
        tk.Frame.__init__(self,parent_frame)

        cust_details_label=tk.Label(self, text="Customer details", bg="#f2f2f2", font="ariel 15 bold")
        cust_details_label.grid(row=0, column=0, sticky="w", padx=30, pady=30)

        refresh_button=tk.Button(self,text="Refresh", fg="white", bg="#FF4040", command= lambda:controller.refresh(customer_details))
        refresh_button.grid(row=0, column=1)

        # Getting the data from the database

        query_cust_details="SELECT * FROM customer"
        cursor.execute(query_cust_details)

        # fetches a list of tuples
        data=cursor.fetchall()

        # styling the treeview table
        
        style=ttk.Style()
        style.configure("Treeview", rowheight=50)
        style.map("Treeview")

        # creating columns

        self.col=("customer_id", "name", "phone", "age", "gender", "address", "adhaar_number", "room_number", "bill_id")

        # creating the treeview table

        cust_details_table=ttk.Treeview(self, height=7, columns=self.col, show="headings")

        cust_details_table.column("customer_id", anchor="w", width=90)
        cust_details_table.column("name", anchor="w", width=130)
        cust_details_table.column("phone", anchor="w", width=80)
        cust_details_table.column("age", anchor="w", width=30)
        cust_details_table.column("gender", anchor="w", width=60)
        cust_details_table.column("address", anchor="w", width=130)
        cust_details_table.column("adhaar_number", anchor="w", width=80)
        cust_details_table.column("room_number", anchor="w", width=60)
        cust_details_table.column("bill_id", anchor="w", width=60)

        cust_details_table.heading("customer_id", text="Customer Id", anchor='w')
        cust_details_table.heading("name", text="Name", anchor='w')
        cust_details_table.heading("phone", text="Phone", anchor='w')
        cust_details_table.heading("age", text="Age", anchor='w')
        cust_details_table.heading("gender", text="Gender", anchor='w')
        cust_details_table.heading("address", text="Address", anchor='w')
        cust_details_table.heading("adhaar_number", text="Adhaar No", anchor='w')
        cust_details_table.heading("room_number", text="Room No", anchor='w')
        cust_details_table.heading("bill_id", text="Bill Id", anchor='w')

        # populating the treeview

        for entry in data:
            cust_details_table.insert('', index="end", values=entry)

        cust_details_table.grid(row=1, column=0, sticky='nsew', padx=(40,0))

        # add a scrollbar
        scrollbary = ttk.Scrollbar(self, orient=tk.VERTICAL, command=cust_details_table.yview)
        cust_details_table.configure(yscroll=scrollbary.set)
        scrollbary.grid(row=1, column=1, sticky='nsw')

    
# =====================================================================================================================
# ================================================ employee info subframe =============================================
# =====================================================================================================================


class employee_info(tk.Frame):
    def __init__(self, parent_frame, controller):
        tk.Frame.__init__(self,parent_frame)

        emp_info_label=tk.Label(self, text="Employee Information", bg="#f2f2f2", font="ariel 15 bold")
        emp_info_label.grid(row=0, column=0, sticky="w", padx=30, pady=30)

        refresh_button=tk.Button(self,text="Refresh", fg="white", bg="#FF4040", command= lambda:controller.refresh(employee_info))
        refresh_button.grid(row=0, column=1)

        # Getting the data from the database

        query_emp_info="SELECT `manager_id`, `username` FROM managers"
        cursor.execute(query_emp_info)

        # fetches a list of tuples
        data=cursor.fetchall()

        # styling the treeview table
        
        style=ttk.Style()
        style.configure("Treeview", rowheight=50)
        style.map("Treeview")

        # creating columns

        self.col=("manager_id", "username")

        # creating the treeview table

        emp_info_table=ttk.Treeview(self, height=7, columns=self.col, show="headings")

        emp_info_table.column("manager_id", anchor="w", width=130)
        emp_info_table.column("username", anchor="w", width=130)
        
        emp_info_table.heading("manager_id", text="Manager Id", anchor='w')
        emp_info_table.heading("username", text="Name", anchor='w')

        # populating the treeview
       
        for entry in data:
            emp_info_table.insert('', index="end", values=entry)

        emp_info_table.grid(row=1, column=0, sticky='nsew', padx=(60,0))

        # add a scrollbar
        scrollbary = ttk.Scrollbar(self, orient=tk.VERTICAL, command=emp_info_table.yview)
        emp_info_table.configure(yscroll=scrollbary.set)
        scrollbary.grid(row=1, column=1, sticky='nsw')


# =====================================================================================================================
# ================================================ employee ogin info subframe ========================================
# =====================================================================================================================


class employee_login_info(tk.Frame):
    def __init__(self, parent_frame, controller):
        tk.Frame.__init__(self,parent_frame)

        emp_login_info_label=tk.Label(self, text="Employee Login Information", bg="#f2f2f2", font="ariel 15 bold")
        emp_login_info_label.grid(row=0, column=0, sticky="w", padx=30, pady=30)

        refresh_button=tk.Button(self,text="Refresh", fg="white", bg="#FF4040", command= lambda:controller.refresh(employee_login_info))
        refresh_button.grid(row=0, column=1)

        # Getting the data from the database

        query_emp_login_info="SELECT * FROM `manager_logins`"
        cursor.execute(query_emp_login_info)

        # fetches a list of tuples
        data=cursor.fetchall()

        # styling the treeview table
        
        style=ttk.Style()
        style.configure("Treeview", rowheight=50)
        style.map("Treeview")

        # creating columns

        self.col=("manager_id", "username", "time_of_login", "date_of_login")

        # creating the treeview table

        emp_login_info_table=ttk.Treeview(self, height=7, columns=self.col, show="headings")

        emp_login_info_table.column("manager_id", anchor="w", width=130)
        emp_login_info_table.column("username", anchor="w", width=130)
        emp_login_info_table.column("time_of_login", anchor="w", width=130)
        emp_login_info_table.column("date_of_login", anchor="w", width=130)
        
        emp_login_info_table.heading("manager_id", text="Manager Id", anchor='w')
        emp_login_info_table.heading("username", text="Name", anchor='w')
        emp_login_info_table.heading("time_of_login", text="Login Time", anchor='w')
        emp_login_info_table.heading("date_of_login", text="Login Date", anchor='w')

        # populating the treeview
       
        for entry in data:
            emp_login_info_table.insert('', index="end", values=entry)

        emp_login_info_table.grid(row=1, column=0, sticky='nsew', padx=(60,0))

        # add a scrollbar
        scrollbary = ttk.Scrollbar(self, orient=tk.VERTICAL, command=emp_login_info_table.yview)
        emp_login_info_table.configure(yscroll=scrollbary.set)
        scrollbary.grid(row=1, column=1, sticky='nsw')


# =====================================================================================================================
# ================================================ main ===============================================================
# =====================================================================================================================
    

if __name__=="__main__":

    # database connection error handling

    try:

    # connecting the data base

        connection=c.connect(host="localhost", user="root", passwd="", database="hotel_management")

        cursor=connection.cursor()

    # creating the object    

        hotel=App()
        hotel.mainloop()

    except:
        messagebox.showerror("Connection failed", "Failed to connect to database")

                   
    

       
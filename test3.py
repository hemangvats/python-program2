#Hemang Vats 
#Velocity bus booking (Front end [GUI]). Refer to X link 
#for discord interface and commands. 
#The Database is centralised and the whole app is based on the idea 
#of being decentralised and transparent

# importing libaries
import os
import csv
import tkinter as tk
from tkinter import messagebox

# Background Image
BACKGROUND_IMAGE = "trial.png"   

def apply_background(window, width=800, height=500):
    """Attach background image safely to a window and return a frame where you can put widgets."""
    try:
        bg_img = tk.PhotoImage(file=BACKGROUND_IMAGE)
        window.bg_img = bg_img  # prevent garbage collection
        bg_label = tk.Label(window, image=bg_img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # all widgets go inside this frame (on top of background)
        content_frame = tk.Frame(window, bg="black")
        content_frame.place(relx=0.5, rely=0.5, anchor="s")
        return content_frame
    except Exception as e:
        print("Background load error:", e)
        return window

# importaant data
ADMIN_PASSWORD = "Hem@ng&cyph3r"
USERDATA_FILE = "userdata.csv"
LOCATION_FILE = "locationdata.csv"
BUSTYPE_FILE = "Bustypedata.csv"
BOOKING_FILE = "bookingrecords.csv"

# Ensure CSV files exist
def ensure_files_exist():
    for fname in (USERDATA_FILE, LOCATION_FILE, BUSTYPE_FILE, BOOKING_FILE):
        if not os.path.exists(fname):
            with open(fname, "w", newline="") as f:
                pass

def read_csv_rows(file):
    if not os.path.exists(file):
        return []
    with open(file, "r", newline="") as f:
        return list(csv.reader(f))

def append_csv_row(file, row):
    with open(file, "a", newline="") as f:
        csv.writer(f).writerow(row)

def write_csv_rows(file, rows):
    with open(file, "w", newline="") as f:
        csv.writer(f).writerows(rows)

def is_int(s):
    try:
        int(s)
        return True
    except:
        return False

# Main Application 
class VBBApp:
    def __init__(self, root):
        self.root = root
        self.root.title("VBB Home")
        self.root.geometry("800x500")
        ensure_files_exist()
        self.build_main_screen()

    def build_main_screen(self):
        for w in self.root.winfo_children():
            w.destroy()

        frame = apply_background(self.root)

        header = tk.Label(frame, text="Welcome to Velocity Bus Booking",
                          font=("Helvetica", 40, "italic"),
                          fg="yellow", bg="black")
        header.pack(pady=10)

        sub = tk.Label(frame, text="Please select",
                       font=("Helvetica", 24, "italic"),
                       fg="yellow", bg="black")
        sub.pack(pady=5)

        btn_frame = tk.Frame(frame, bg="black")
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="Admin Panel", width=24, command=self.open_admin_login).grid(row=0, column=0, padx=6, pady=6)
        tk.Button(btn_frame, text="Customer Login", width=24, command=self.open_login).grid(row=0, column=1, padx=6, pady=6)
        tk.Button(btn_frame, text="Customer Sign-Up", width=24, command=self.open_signup).grid(row=0, column=2, padx=6, pady=6)
        tk.Button(btn_frame, text="About Us", width=24, command=self.open_about).grid(row=0, column=3, padx=6, pady=6)
        tk.Button(btn_frame, text="Chat Bot", width=24, command=self.open_chat_bot).grid(row=0, column=4, padx=6, pady=6)

    # About
    def open_about(self):
        top = tk.Toplevel(self.root)
        top.title("About VBB")
        top.geometry("600x350")
        frame = apply_background(top, 600, 350)

        tk.Label(frame, text="About Us", font=("Helvetica", 40, "italic"),
                 fg="yellow", bg="black").pack(pady=10)
        about_txt = (
            "Stuck where to contact for a bus?\nCan't go on holidays with family because of logistics issues?\n"
            "We are your solution. Providing quality buses at affordable prices.\nPlan your perfect holiday trip with us.\n"
            "Travel hassle free with Velocity.\nContact us at bizwithcyph3r@gmail.com"
        )
        tk.Label(frame, text=about_txt, justify="left", wraplength=560,
                 fg="yellow", bg="black").pack(padx=10, pady=10)
    
    # Chat Bot
    def open_chat_bot(self):
        chat_win = tk.Toplevel(self.root)
        chat_win.title("VBB Chatbot Assistant")
        chat_win.geometry("400x500")
        frame = apply_background(chat_win, 400, 500)
        chat_window = tk.Text(frame, bd=1, fg="yellow", bg="black", width=50, height=20)
        chat_window.pack(pady=10)
        input_frame = tk.Frame(frame, bg="black")
        input_frame.pack(pady=5)
        entry = tk.Entry(input_frame, width=30)
        entry.pack(side=tk.LEFT, padx=5)
        def send_message(event=None):
            user_input = entry.get()
            if not user_input.strip():
                return
            chat_window.insert(tk.END, "You: " + user_input + "\n")
            entry.delete(0, tk.END)
            response = "I didn’t understand that."
            if "hello" in user_input.lower() or "hi" in user_input.lower():
                response = "Hi there! How can I help you?"
            elif "problem" in user_input.lower():
                response = "Please describe your problem in detail."
            elif "bus" in user_input.lower():
                response = "You can view bus types in the booking section."
            elif "book" in user_input.lower():
                response = "To book a bus, go to the booking page and select a route and bus type."
            elif "bye" in user_input.lower():
                response = "Goodbye! Have a nice day 😊"
                chat_window.insert(tk.END, "Bot: " + response + "\n")
        send_button = tk.Button(input_frame, text="Send", command=send_message)
        send_button.pack(side=tk.LEFT)
        entry.bind("<Return>", send_message)

    # Signup
    def open_signup(self):
        top = tk.Toplevel(self.root)
        top.title("VBB Sign-Up")
        top.geometry("600x400")
        frame = apply_background(top, 600, 400)

        labels = ["First name", "Second name", "Email", "Username", "Password", "Confirm Password"]
        entries = []
        for i, text in enumerate(labels):
            tk.Label(frame, text=f"{text}:", fg="yellow", bg="black").grid(row=i, column=0, padx=10, pady=6, sticky="e")
            ent = tk.Entry(frame, show="*" if "Password" in text else "")
            ent.grid(row=i, column=1, padx=10, pady=6, sticky="w")
            entries.append(ent)

        def do_signup():
            firstname, secondname, email, username, pwd, pwdc = [e.get().strip() for e in entries]
            if not (firstname and username and pwd and pwdc):
                messagebox.showwarning("Missing", "Please fill required fields.")
                return
            if pwd != pwdc:
                messagebox.showerror("Password", "Passwords do not match.")
                return
            for u in read_csv_rows(USERDATA_FILE):
                if len(u) >= 4 and u[3] == username:
                    messagebox.showerror("Username", "Username already taken.")
                    return
            append_csv_row(USERDATA_FILE, [firstname, secondname, email, username, pwd])
            messagebox.showinfo("Success", "Sign-up successful. You can now log in.")
            top.destroy()

        tk.Button(frame, text="Sign Up", command=do_signup).grid(row=len(labels), column=1, pady=12, sticky="e")

    # Login
    def open_login(self):
        top = tk.Toplevel(self.root)
        top.title("VBB User Login")
        top.geometry("500x250")
        frame = apply_background(top, 500, 250)

        tk.Label(frame, text="Username:", fg="yellow", bg="black").grid(row=0, column=0, padx=10, pady=8, sticky="e")
        username_ent = tk.Entry(frame)
        username_ent.grid(row=0, column=1, padx=10, pady=8, sticky="w")

        tk.Label(frame, text="Password:", fg="yellow", bg="black").grid(row=1, column=0, padx=10, pady=8, sticky="e")
        pwd_ent = tk.Entry(frame, show="*")
        pwd_ent.grid(row=1, column=1, padx=10, pady=8, sticky="w")

        def do_login():
            uname, pwd = username_ent.get().strip(), pwd_ent.get()
            for row in read_csv_rows(USERDATA_FILE):
                if len(row) >= 5 and row[3] == uname and row[4] == pwd:
                    messagebox.showinfo("Login", f"Welcome {row[0]} {row[1]}")
                    top.destroy()
                    self.open_booking_page(username=uname, display_name=f"{row[0]} {row[1]}")
                    return
            messagebox.showerror("Login Failed", "Incorrect username or password.")

        tk.Button(frame, text="Login", command=do_login).grid(row=2, column=1, pady=12, sticky="e")

    # Admin
    def open_admin_login(self):
        top = tk.Toplevel(self.root)
        top.title("Admin Login")
        top.geometry("400x200")
        frame = apply_background(top, 400, 200)

        tk.Label(frame, text="Enter admin password:", fg="yellow", bg="black").pack(pady=10)
        pwd = tk.Entry(frame, show="*")
        pwd.pack(pady=5)

        def do_admin_login():
            if pwd.get() == ADMIN_PASSWORD:
                top.destroy()
                self.open_admin_panel()
            else:
                messagebox.showerror("Access Denied", "Incorrect admin password.")

        tk.Button(frame, text="Login", command=do_admin_login).pack(pady=10)

    def open_admin_panel(self):
        top = tk.Toplevel(self.root)
        top.title("Admin Panel")
        top.geometry("800x450")
        frame = apply_background(top, 800, 450)

        tk.Label(frame, text="Admin Controls", font=("Helvetica", 16),
                 fg="yellow", bg="black").pack(pady=8)

        btn_frame = tk.Frame(frame, bg="black")
        btn_frame.pack(pady=8)

        tk.Button(btn_frame, text="Add Location", width=20, command=lambda: self.admin_add_entry(LOCATION_FILE, "Location")).grid(row=0, column=0, padx=8, pady=6)
        tk.Button(btn_frame, text="Add Bus Type", width=20, command=lambda: self.admin_add_entry(BUSTYPE_FILE, "Bus Type")).grid(row=0, column=1, padx=8, pady=6)
        tk.Button(btn_frame, text="Modify Location", width=20, command=lambda: self.admin_modify_entry(LOCATION_FILE, "Location")).grid(row=1, column=0, padx=8, pady=6)
        tk.Button(btn_frame, text="Modify Bus Type", width=20, command=lambda: self.admin_modify_entry(BUSTYPE_FILE, "Bus Type")).grid(row=1, column=1, padx=8, pady=6)
        tk.Button(btn_frame, text="Delete Location", width=20, command=lambda: self.admin_delete_entry(LOCATION_FILE, "Location")).grid(row=2, column=0, padx=8, pady=6)
        tk.Button(btn_frame, text="Delete Bus Type", width=20, command=lambda: self.admin_delete_entry(BUSTYPE_FILE, "Bus Type")).grid(row=2, column=1, padx=8, pady=6)

    # Booking Page
    def open_booking_page(self, username, display_name=None):
        top = tk.Toplevel(self.root)
        top.title("VBB Booking")
        top.geometry("800x600")
        frame = apply_background(top, 800, 600)

        locations = read_csv_rows(LOCATION_FILE)
        bustypes = read_csv_rows(BUSTYPE_FILE)

        disp = display_name or username
        tk.Label(frame, text=f"Welcome {disp}", font=("Helvetica", 20, "bold"),
                 fg="yellow", bg="black").pack(pady=10)

        # Locations
        tk.Label(frame, text="Available Locations:", fg="yellow", bg="black").pack()
        for idx, r in enumerate(locations):
            tk.Label(frame, text=f"{idx} : {r[0]}  -  {r[1]}",
                     fg="yellow", bg="black").pack(anchor="w")

        tk.Label(frame, text="Enter location choice number:", fg="yellow", bg="black").pack(pady=4)
        loc_choice_ent = tk.Entry(frame)
        loc_choice_ent.pack(pady=4)

        # Bustypes
        tk.Label(frame, text="Available Bus Types:", fg="yellow", bg="black").pack()
        for idx, r in enumerate(bustypes):
            tk.Label(frame, text=f"{idx} : {r[0]}  -  {r[1]}",
                     fg="yellow", bg="black").pack(anchor="w")

        tk.Label(frame, text="Enter bus type choice number:", fg="yellow", bg="black").pack(pady=4)
        bt_choice_ent = tk.Entry(frame)
        bt_choice_ent.pack(pady=4)

        tk.Label(frame, text="Number of people travelling:", fg="yellow", bg="black").pack(pady=4)
        num_ent = tk.Entry(frame)
        num_ent.pack(pady=4)

        def show_bill_and_save():
            if not (loc_choice_ent.get().strip() and bt_choice_ent.get().strip() and num_ent.get().strip()):
                messagebox.showwarning("Missing", "Please fill all booking fields.")
                return
            if not (is_int(loc_choice_ent.get()) and is_int(bt_choice_ent.get()) and is_int(num_ent.get())):
                messagebox.showerror("Invalid", "Choices and passengers must be integers.")
                return
            loc_idx, bt_idx, cnt = int(loc_choice_ent.get()), int(bt_choice_ent.get()), int(num_ent.get())
            if loc_idx < 0 or loc_idx >= len(locations) or bt_idx < 0 or bt_idx >= len(bustypes) or cnt <= 0:
                messagebox.showerror("Invalid", "Invalid selection or passenger count.")
                return

            loc_row, bt_row = locations[loc_idx], bustypes[bt_idx]
            total = (int(loc_row[1]) + int(bt_row[1])) * cnt
            append_csv_row(BOOKING_FILE, [username, loc_row[0], bt_row[0], str(cnt), str(total)])

            bill = tk.Toplevel(top)
            bill.title("Billing Window")
            bill.geometry("400x300")
            f2 = apply_background(bill, 400, 300)
            tk.Label(f2, text="Your choice is as follows:", font=("Helvetica", 14, "bold"),
                     fg="yellow", bg="black").pack(pady=8)
            tk.Label(f2, text=f"Location: {loc_row[0]}", fg="yellow", bg="black").pack()
            tk.Label(f2, text=f"Bus Choice: {bt_row[0]}", fg="yellow", bg="black").pack()
            tk.Label(f2, text=f"Travellers: {cnt}", fg="yellow", bg="black").pack()
            tk.Label(f2, text=f"Total Price: {total}", fg="yellow", bg="black").pack()
            tk.Button(f2, text="OK", command=bill.destroy).pack(pady=8)

        def show_previous_bookings():
            rows = read_csv_rows(BOOKING_FILE)
            user_rows = [r for r in rows if len(r) >= 1 and r[0] == username]
            if not user_rows:
                messagebox.showinfo("No Records", "No previous bookings found.")
                return
            rec_win = tk.Toplevel(top)
            rec_win.title("Previous Records")
            rec_win.geometry("500x400")
            f3 = apply_background(rec_win, 500, 400)
            tk.Label(f3, text=f"Previous bookings for {username}:",
                     font=("Helvetica", 12, "bold"), fg="yellow", bg="black").pack(pady=6)
            for r in user_rows:
                text = f"Destination: {r[1]} | Bus: {r[2]} | Passengers: {r[3]} | Fare: {r[4]}"
                tk.Label(f3, text=text, fg="yellow", bg="black",
                         anchor="w", justify="left", wraplength=460).pack(padx=8, pady=4)

        tk.Button(frame, text="Confirm and Proceed", command=show_bill_and_save).pack(pady=10)
        tk.Button(frame, text="Previous Bookings", command=show_previous_bookings).pack(pady=4)

# run app
if __name__ == "__main__":
    root = tk.Tk()
    app = VBBApp(root)
    root.mainloop()

# main.py
# Debugged & refactored Velocity Bus Booking (VBB) front-end (Tkinter)
# Author: adapted for Hemang Vats
import os
import csv
import tkinter as tk
from tkinter import messagebox

# --- Background Helper ---
BACKGROUND_IMAGE = "trial.png"   

def apply_background(window, width=800, height=500):
    """
    Attach background image safely to a window
    and return a frame where you can put widgets.
    """
    try:
        bg_img = tk.PhotoImage(file=BACKGROUND_IMAGE)
        window.bg_img = bg_img  # prevent garbage collection
        bg_label = tk.Label(window, image=bg_img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # all widgets go inside this frame (on top of background)
        content_frame = tk.Frame(window, bg="black")
        content_frame.place(relx=0.5, rely=0.5, anchor="center")
        return content_frame
    except Exception as e:
        print("Background load error:", e)
        return window


# Config
ADMIN_PASSWORD = "Hem@ng&cyph3r"
USERDATA_FILE = "userdata.csv"
LOCATION_FILE = "locationdata.csv"
BUSTYPE_FILE = "Bustypedata.csv"
BOOKING_FILE = "bookingrecords.csv"

# Ensure CSV files exist with proper headers if desired (not required)
def ensure_files_exist():
    for fname in (USERDATA_FILE, LOCATION_FILE, BUSTYPE_FILE, BOOKING_FILE):
        if not os.path.exists(fname):
            with open(fname, "w", newline="") as f:
                pass

def read_csv_rows(file):
    rows = []
    if not os.path.exists(file):
        return rows
    with open(file, "r", newline="") as f:
        reader = csv.reader(f)
        rows = [r for r in reader]
    return rows

def append_csv_row(file, row):
    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(row)

def write_csv_rows(file, rows):
    with open(file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

# Utility validators
def is_int(s):
    try:
        int(s)
        return True
    except:
        return False

# ---------- Main Application ----------
class VBBApp:
    def __init__(self, root):
        self.root = root
        self.root.title("VBB Home")
        self.root.geometry("800x500")
        ensure_files_exist()
        
        # Main UI
        self.build_main_screen()

    def build_main_screen(self):
        # Clear root
        for w in self.root.winfo_children():
            w.destroy()

        # Header
        header = tk.Label(self.root, text="Welcome to Velocity Bus Booking", font=("Helvetica", 24, "italic"))
        header.pack(pady=10)

        sub = tk.Label(self.root, text="Please select", font=("Helvetica", 16, "italic"))
        sub.pack(pady=5)

        # Buttons frame (use grid inside this frame)
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="Admin Panel", width=18, command=self.open_admin_login).grid(row=0, column=0, padx=6, pady=6)
        tk.Button(btn_frame, text="Customer Login", width=18, command=self.open_login).grid(row=0, column=1, padx=6, pady=6)
        tk.Button(btn_frame, text="Customer Sign-Up", width=18, command=self.open_signup).grid(row=0, column=2, padx=6, pady=6)
        tk.Button(btn_frame, text="About Us", width=18, command=self.open_about).grid(row=0, column=3, padx=6, pady=6)

    # ----------------- About -----------------
    def open_about(self):
        top = tk.Toplevel(self.root)
        top.title("About VBB")
        top.geometry("600x350")
        tk.Label(top, text="About Us", font=("Helvetica", 20, "italic")).pack(pady=10)
        about_txt = (
            "Stuck where to contact for a bus?\nCan't go on holidays with family because of logistics issues?\n"
            "We are your solution. Providing quality buses at affordable prices.\nPlan your perfect holiday trip with us.\n"
            "Travel hassle free with Velocity.\nContact us at bizwithcyph3r@gmail.com"
        )
        tk.Label(top, text=about_txt, justify="left", wraplength=560).pack(padx=10, pady=10)

    # ----------------- Signup -----------------
    def open_signup(self):
        top = tk.Toplevel(self.root)
        top.title("VBB Sign-Up")
        top.geometry("600x400")

        labels = ["First name", "Second name", "Email", "Username", "Password", "Confirm Password"]
        entries = []
        for i, text in enumerate(labels):
            lbl = tk.Label(top, text=f"Enter your {text}:")
            lbl.grid(row=i, column=0, padx=10, pady=6, sticky="e")
            ent = tk.Entry(top, show="*" if "Password" in text else "")
            ent.grid(row=i, column=1, padx=10, pady=6, sticky="w")
            entries.append(ent)

        def do_signup():
            firstname = entries[0].get().strip()
            secondname = entries[1].get().strip()
            email = entries[2].get().strip()
            username = entries[3].get().strip()
            pwd = entries[4].get()
            pwdc = entries[5].get()

            if not (firstname and username and pwd and pwdc):
                messagebox.showwarning("Missing", "Please fill required fields (first name, username and passwords).")
                return
            if pwd != pwdc:
                messagebox.showerror("Password", "Passwords do not match.")
                return

            # check username uniqueness
            users = read_csv_rows(USERDATA_FILE)
            for u in users:
                if len(u) >= 4 and u[3] == username:
                    messagebox.showerror("Username", "Username already taken.")
                    return

            append_csv_row(USERDATA_FILE, [firstname, secondname, email, username, pwd])
            messagebox.showinfo("Success", "Sign-up successful. You can now log in.")
            top.destroy()

        tk.Button(top, text="Sign Up", command=do_signup).grid(row=len(labels), column=1, pady=12, sticky="e")

    # ----------------- Login -----------------
    def open_login(self):
        top = tk.Toplevel(self.root)
        top.title("VBB User Login")
        top.geometry("500x250")

        tk.Label(top, text="Enter your username:").grid(row=0, column=0, padx=10, pady=8, sticky="e")
        username_ent = tk.Entry(top)
        username_ent.grid(row=0, column=1, padx=10, pady=8, sticky="w")

        tk.Label(top, text="Enter your password:").grid(row=1, column=0, padx=10, pady=8, sticky="e")
        pwd_ent = tk.Entry(top, show="*")
        pwd_ent.grid(row=1, column=1, padx=10, pady=8, sticky="w")

        def do_login():
            uname = username_ent.get().strip()
            pwd = pwd_ent.get()
            users = read_csv_rows(USERDATA_FILE)
            for row in users:
                if len(row) >= 5 and row[3] == uname and row[4] == pwd:
                    messagebox.showinfo("Login", f"Welcome {row[0]} {row[1]}")
                    top.destroy()
                    self.open_booking_page(username=uname, display_name=f"{row[0]} {row[1]}")
                    return
            messagebox.showerror("Login Failed", "Incorrect username or password.")

        tk.Button(top, text="Login", command=do_login).grid(row=2, column=1, pady=12, sticky="e")

    # ----------------- Admin -----------------
    def open_admin_login(self):
        top = tk.Toplevel(self.root)
        top.title("Admin Login")
        top.geometry("400x200")

        tk.Label(top, text="Enter admin password:").pack(pady=10)
        pwd = tk.Entry(top, show="*")
        pwd.pack(pady=5)

        def do_admin_login():
            if pwd.get() == ADMIN_PASSWORD:
                top.destroy()
                self.open_admin_panel()
            else:
                messagebox.showerror("Access Denied", "Incorrect admin password.")

        tk.Button(top, text="Login", command=do_admin_login).pack(pady=10)

    def open_admin_panel(self):
        top = tk.Toplevel(self.root)
        top.title("Admin Panel")
        top.geometry("800x450")

        tk.Label(top, text="Admin Controls", font=("Helvetica", 16)).pack(pady=8)

        frame = tk.Frame(top)
        frame.pack(pady=8)

        tk.Button(frame, text="Add Location", width=20, command=lambda: self.admin_add_entry(LOCATION_FILE, "Location")).grid(row=0, column=0, padx=8, pady=6)
        tk.Button(frame, text="Add Bus Type", width=20, command=lambda: self.admin_add_entry(BUSTYPE_FILE, "Bus Type")).grid(row=0, column=1, padx=8, pady=6)
        tk.Button(frame, text="Modify Location", width=20, command=lambda: self.admin_modify_entry(LOCATION_FILE, "Location")).grid(row=1, column=0, padx=8, pady=6)
        tk.Button(frame, text="Modify Bus Type", width=20, command=lambda: self.admin_modify_entry(BUSTYPE_FILE, "Bus Type")).grid(row=1, column=1, padx=8, pady=6)
        tk.Button(frame, text="Delete Location", width=20, command=lambda: self.admin_delete_entry(LOCATION_FILE, "Location")).grid(row=2, column=0, padx=8, pady=6)
        tk.Button(frame, text="Delete Bus Type", width=20, command=lambda: self.admin_delete_entry(BUSTYPE_FILE, "Bus Type")).grid(row=2, column=1, padx=8, pady=6)

    def admin_add_entry(self, file, label):
        top = tk.Toplevel(self.root)
        top.title(f"Add {label}")
        top.geometry("450x200")
        tk.Label(top, text=f"Add {label} Name:").grid(row=0, column=0, padx=8, pady=8, sticky="e")
        name_ent = tk.Entry(top)
        name_ent.grid(row=0, column=1, padx=8, pady=8, sticky="w")
        tk.Label(top, text="Price:").grid(row=1, column=0, padx=8, pady=8, sticky="e")
        price_ent = tk.Entry(top)
        price_ent.grid(row=1, column=1, padx=8, pady=8, sticky="w")

        def do_add():
            name = name_ent.get().strip()
            price = price_ent.get().strip()
            if not name or not price:
                messagebox.showwarning("Missing", "Please fill both fields.")
                return
            if not price.isdigit():
                messagebox.showerror("Invalid", "Price must be numeric.")
                return
            append_csv_row(file, [name, price])
            messagebox.showinfo("Added", f"{label} added.")
            top.destroy()

        tk.Button(top, text="Add", command=do_add).grid(row=2, column=1, pady=10, sticky="e")

    def admin_modify_entry(self, file, label):
        rows = read_csv_rows(file)
        if not rows:
            messagebox.showinfo("No Data", f"No {label} entries to modify.")
            return
        top = tk.Toplevel(self.root)
        top.title(f"Modify {label}")
        top.geometry("600x400")

        tk.Label(top, text=f"Select {label} to modify:").pack(pady=6)
        listbox = tk.Listbox(top, width=60, height=8)
        for r in rows:
            listbox.insert(tk.END, f"{r[0]}  -  Price: {r[1]}")
        listbox.pack(pady=8)

        # edit area
        edit_frame = tk.Frame(top)
        edit_frame.pack(pady=8)
        tk.Label(edit_frame, text=f"New {label} name:").grid(row=0, column=0, padx=8, pady=4)
        name_ent = tk.Entry(edit_frame)
        name_ent.grid(row=0, column=1, padx=8, pady=4)
        tk.Label(edit_frame, text="New Price:").grid(row=1, column=0, padx=8, pady=4)
        price_ent = tk.Entry(edit_frame)
        price_ent.grid(row=1, column=1, padx=8, pady=4)

        def do_modify():
            sel = listbox.curselection()
            if not sel:
                messagebox.showwarning("Select", "Please select an entry to modify.")
                return
            idx = sel[0]
            new_name = name_ent.get().strip() or rows[idx][0]
            new_price = price_ent.get().strip() or rows[idx][1]
            if not new_price.isdigit():
                messagebox.showerror("Invalid", "Price must be numeric.")
                return
            rows[idx] = [new_name, new_price]
            write_csv_rows(file, rows)
            messagebox.showinfo("Modified", f"{label} modified.")
            top.destroy()

        tk.Button(top, text="Confirm Edit", command=do_modify).pack(pady=10)

    def admin_delete_entry(self, file, label):
        rows = read_csv_rows(file)
        if not rows:
            messagebox.showinfo("No Data", f"No {label} entries to delete.")
            return
        top = tk.Toplevel(self.root)
        top.title(f"Delete {label}")
        top.geometry("600x400")

        tk.Label(top, text=f"Select {label} to delete:").pack(pady=6)
        listbox = tk.Listbox(top, width=60, height=8)
        for r in rows:
            listbox.insert(tk.END, f"{r[0]}  -  Price: {r[1]}")
        listbox.pack(pady=8)

        def do_delete():
            sel = listbox.curselection()
            if not sel:
                messagebox.showwarning("Select", "Please select an entry to delete.")
                return
            idx = sel[0]
            del rows[idx]
            write_csv_rows(file, rows)
            messagebox.showinfo("Deleted", f"{label} deleted.")
            top.destroy()

        tk.Button(top, text="Delete Selected", command=do_delete).pack(pady=10)

    # ----------------- Booking Page -----------------
    def open_booking_page(self, username, display_name=None):
        top = tk.Toplevel(self.root)
        top.title("VBB Booking")
        top.geometry("800x600")

        # Read data
        locations = read_csv_rows(LOCATION_FILE)
        bustypes = read_csv_rows(BUSTYPE_FILE)

        # Header
        disp = display_name or username
        tk.Label(top, text=f"Welcome {disp}", font=("Helvetica", 20, "bold")).pack(pady=10)

        # Locations list
        loc_frame = tk.Frame(top, bd=1, relief="sunken")
        loc_frame.pack(fill="x", padx=12, pady=6)
        tk.Label(loc_frame, text="Available Locations (Choice number : Name - Price)").pack(anchor="w")
        for idx, r in enumerate(locations):
            tk.Label(loc_frame, text=f"{idx} : {r[0]}  -  {r[1]}").pack(anchor="w")

        tk.Label(top, text="Enter location choice number:").pack(pady=4)
        loc_choice_ent = tk.Entry(top)
        loc_choice_ent.pack(pady=4)

        # Bus types
        bt_frame = tk.Frame(top, bd=1, relief="sunken")
        bt_frame.pack(fill="x", padx=12, pady=6)
        tk.Label(bt_frame, text="Available Bus Types (Choice number : Type - Price)").pack(anchor="w")
        for idx, r in enumerate(bustypes):
            tk.Label(bt_frame, text=f"{idx} : {r[0]}  -  {r[1]}").pack(anchor="w")

        tk.Label(top, text="Enter bus type choice number:").pack(pady=4)
        bt_choice_ent = tk.Entry(top)
        bt_choice_ent.pack(pady=4)

        tk.Label(top, text="Number of people travelling:").pack(pady=4)
        num_ent = tk.Entry(top)
        num_ent.pack(pady=4)

        def show_bill_and_save():
            # validation
            if not (loc_choice_ent.get().strip() and bt_choice_ent.get().strip() and num_ent.get().strip()):
                messagebox.showwarning("Missing", "Please fill all booking fields.")
                return
            if not (is_int(loc_choice_ent.get()) and is_int(bt_choice_ent.get()) and is_int(num_ent.get())):
                messagebox.showerror("Invalid", "Choice numbers and passenger count must be integers.")
                return
            loc_idx = int(loc_choice_ent.get())
            bt_idx = int(bt_choice_ent.get())
            cnt = int(num_ent.get())

            if loc_idx < 0 or loc_idx >= len(locations):
                messagebox.showerror("Invalid", "Location choice out of range.")
                return
            if bt_idx < 0 or bt_idx >= len(bustypes):
                messagebox.showerror("Invalid", "Bus type choice out of range.")
                return
            if cnt <= 0:
                messagebox.showerror("Invalid", "Passenger count must be positive.")
                return

            loc_row = locations[loc_idx]
            bt_row = bustypes[bt_idx]
            total = (int(loc_row[1]) + int(bt_row[1])) * cnt

            # Save booking record: [username, location_name, bustype, passengers, total]
            append_csv_row(BOOKING_FILE, [username, loc_row[0], bt_row[0], str(cnt), str(total)])
            # Show bill window
            bill = tk.Toplevel(top)
            bill.title("Billing Window")
            bill.geometry("400x300")
            tk.Label(bill, text="Your choice is as follows:", font=("Helvetica", 14, "bold")).pack(pady=8)
            tk.Label(bill, text=f"Location: {loc_row[0]}").pack(pady=4)
            tk.Label(bill, text=f"Bus Choice: {bt_row[0]}").pack(pady=4)
            tk.Label(bill, text=f"Number of people travelling: {cnt}").pack(pady=4)
            tk.Label(bill, text=f"Total Price: {total}").pack(pady=8)
            tk.Button(bill, text="OK", command=bill.destroy).pack(pady=8)

        def show_previous_bookings():
            rows = read_csv_rows(BOOKING_FILE)
            user_rows = [r for r in rows if len(r) >= 1 and r[0] == username]
            if not user_rows:
                messagebox.showinfo("No Records", "No previous bookings found for you.")
                return
            rec_win = tk.Toplevel(top)
            rec_win.title("Previous Records")
            rec_win.geometry("500x400")
            tk.Label(rec_win, text=f"Previous bookings for {username}:", font=("Helvetica", 12, "bold")).pack(pady=6)
            for r in user_rows:
                # r = [username, location, bus, passengers, total]
                text = f"Destination: {r[1]} | Bus: {r[2]} | Passengers: {r[3]} | Fare: {r[4]}"
                tk.Label(rec_win, text=text, anchor="w", justify="left", wraplength=460).pack(padx=8, pady=4)

        tk.Button(top, text="Confirm and Proceed", command=show_bill_and_save).pack(pady=10)
        tk.Button(top, text="Previous Bookings", command=show_previous_bookings).pack(pady=4)

# run app
if __name__ == "__main__":
    root = tk.Tk()
    app = VBBApp(root)
    root.mainloop()

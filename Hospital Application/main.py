import json
import tkinter as tk
from tkinter import messagebox, simpledialog
from admin import Admin
from doctor import Doctor
from patient import Patient

# Initialize admin, doctors, and patients
admin = Admin('admin', '1234', 'Admin Street')
doctors = [Doctor("John", "Doe", "Cardiology")]
patients = admin.load_patients_from_file()  # Automatically load patients on startup
discharged_patients = []

def attempt_login():
    # Handle login attempt
    username = username_entry.get()
    password = password_entry.get()
    if admin.login(username, password):
        messagebox.showinfo("Login", "Login successful!")
        login_frame.pack_forget()
        show_main_menu()
    else:
        messagebox.showerror("Login", "Incorrect username or password.")

def show_main_menu():
    # Display the main menu
    title_label.pack(pady=20)
    btn_manage_doctors.pack(pady=10)
    btn_manage_patients.pack(pady=10)
    btn_discharge_patient.pack(pady=10)
    btn_view_discharged_patients.pack(pady=10)
    btn_relocate_patient.pack(pady=10)
    btn_generate_report.pack(pady=10)
    btn_add_patient.pack(pady=10)
    btn_remove_patient.pack(pady=10)
    btn_update_username.pack(pady=10)
    btn_update_password.pack(pady=10)
    btn_update_address.pack(pady=10)
    text_widget.pack(pady=20)

def manage_doctors():
    # Manage doctors
    admin.doctor_management(doctors, text_widget)

def manage_patients():
    # Manage patients
    admin.assign_doctor_to_patient(patients, doctors, text_widget)

def discharge_patient():
    # Discharge a patient
    text_widget.insert(tk.END, "----- Discharge Patient -----\n")
    for patient in patients:
        text_widget.insert(tk.END, f"ID: {patient.get_id()} | Name: {patient.full_name()}\n")
    patient_id = simpledialog.askinteger("Discharge Patient", "Enter patient ID:")
    if patient_id is not None:
        admin.discharge_patient(patients, discharged_patients, patient_id, text_widget)
    else:
        text_widget.insert(tk.END, "Operation cancelled.\n")

def view_discharged_patients():
    # View discharged patients
    admin.view_discharged_patients(discharged_patients, text_widget)

def relocate_patient():
    # Relocate a patient to a new doctor
    try:
        patient_id = simpledialog.askinteger("Relocate Patient", "Enter patient ID:")
        new_doctor_id = simpledialog.askinteger("Relocate Patient", "Enter new doctor ID:")
        if patient_id is not None and new_doctor_id is not None:
            admin.relocate_patient(patients, doctors, patient_id, new_doctor_id, text_widget)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid IDs for patient and new doctor.")

def generate_report():
    # Generate a report
    admin.generate_report(doctors, patients, text_widget)

def add_patient():
    # Add a new patient
    try:
        first_name = simpledialog.askstring("Add Patient", "Enter first name:")
        surname = simpledialog.askstring("Add Patient", "Enter surname:")
        age = simpledialog.askinteger("Add Patient", "Enter age:")
        mobile = simpledialog.askstring("Add Patient", "Enter mobile number:")
        postcode = simpledialog.askstring("Add Patient", "Enter postcode:")
        symptoms_input = simpledialog.askstring("Add Patient", "Enter symptoms (comma separated):")
        symptoms = symptoms_input.split(',') if symptoms_input else []
        address = simpledialog.askstring("Add Patient", "Enter address:")
        family_id = simpledialog.askinteger("Add Patient", "Enter family ID:")
        if address is None:
            address = ""
        new_patient = Patient(first_name, surname, age, mobile, postcode, symptoms, address, family_id)
        patients.append(new_patient)
        text_widget.insert(tk.END, f"Patient {new_patient.full_name()} added.\n")
        admin.save_patients_to_file(patients)  # Automatically save patients after adding
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid patient details.")

def remove_patient():
    # Remove a patient
    try:
        patient_id = simpledialog.askinteger("Remove Patient", "Enter patient ID:")
        if patient_id is not None:
            patient_to_remove = next((p for p in patients if p.get_id() == patient_id), None)
            if patient_to_remove:
                patients.remove(patient_to_remove)
                text_widget.insert(tk.END, f"Patient {patient_to_remove.full_name()} removed.\n")
                admin.save_patients_to_file(patients)  # Automatically save patients after removing
            else:
                text_widget.insert(tk.END, f"Patient with ID {patient_id} not found.\n")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid patient ID.")

def update_admin_username():
    new_username = simpledialog.askstring("Update Username", "Enter new username:")
    if new_username:
        admin.update_username(new_username)
        messagebox.showinfo("Update", "Username updated successfully.")

def update_admin_password():
    new_password = simpledialog.askstring("Update Password", "Enter new password:", show='*')
    if new_password:
        admin.update_password(new_password)
        messagebox.showinfo("Update", "Password updated successfully.")

def update_admin_address():
    new_address = simpledialog.askstring("Update Address", "Enter new address:")
    if new_address:
        admin.update_address(new_address)
        messagebox.showinfo("Update", "Address updated successfully.")

# Initialize the main window
root = tk.Tk()
root.title("Hospital Management System")
root.geometry("900x900")
root.configure(bg="#005EB8")  # NHS Blue

# Create and configure widgets
title_label = tk.Label(root, text="Hospital Management System", font=("Arial", 16), bg="#005EB8", fg="white")

btn_style = {"bg": "#0072CE", "fg": "white", "font": ("Arial", 12), "activebackground": "#003087", "activeforeground": "white"}

btn_manage_doctors = tk.Button(root, text="Manage Doctors", command=manage_doctors, **btn_style)
btn_manage_patients = tk.Button(root, text="Manage Patients", command=manage_patients, **btn_style)
btn_discharge_patient = tk.Button(root, text="Discharge Patient", command=discharge_patient, **btn_style)
btn_view_discharged_patients = tk.Button(root, text="View Discharged Patients", command=view_discharged_patients, **btn_style)
btn_relocate_patient = tk.Button(root, text="Relocate Patient", command=relocate_patient, **btn_style)
btn_generate_report = tk.Button(root, text="Generate Report", command=generate_report, **btn_style)
btn_add_patient = tk.Button(root, text="Add Patient", command=add_patient, **btn_style)
btn_remove_patient = tk.Button(root, text="Remove Patient", command=remove_patient, **btn_style)
btn_update_username = tk.Button(root, text="Update Username", command=update_admin_username, **btn_style)
btn_update_password = tk.Button(root, text="Update Password", command=update_admin_password, **btn_style)
btn_update_address = tk.Button(root, text="Update Address", command=update_admin_address, **btn_style)

text_widget = tk.Text(root, height=15, width=70, bg="white", fg="black", font=("Arial", 12))

login_frame = tk.Frame(root, bg="#005EB8")
tk.Label(login_frame, text="Login", font=("Arial", 16), bg="#005EB8", fg="white").pack(pady=10)
tk.Label(login_frame, text="Username:", bg="#005EB8", fg="white").pack(pady=5)
username_entry = tk.Entry(login_frame)
username_entry.pack(pady=5)
tk.Label(login_frame, text="Password:", bg="#005EB8", fg="white").pack(pady=5)
password_entry = tk.Entry(login_frame, show='*')
password_entry.pack(pady=5)
tk.Button(login_frame, text="Login", command=attempt_login, **btn_style).pack(pady=10)

login_frame.pack(pady=20)
root.mainloop()

#   __           ___ __ 
#  /__)/  ///| )(_  /__)
# / ( (__/(/ |/ /__/ (

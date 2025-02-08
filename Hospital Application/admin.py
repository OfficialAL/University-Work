import json
import tkinter as tk
from doctor import Doctor
from patient import Patient
from tkinter import simpledialog

class Admin:
    """A class that handles Admin operations."""

    def __init__(self, username, password, address=''):
        self.__username = username
        self.__password = password
        self.__address = address

    def login(self, username, password):
        # Validate admin login credentials
        if username == self.__username and password == self.__password:
            return True
        else:
            return False

    def view(self, items, text_widget):
        # Display a list of items in the text widget
        for idx, item in enumerate(items):
            text_widget.insert(tk.END, f"{idx + 1:3} | {item}\n")

    def doctor_management(self, doctors, text_widget):
        # Manage doctors
        text_widget.insert(tk.END, "----- Doctor Management -----\n")
        text_widget.insert(tk.END, "1 - Register\n")
        text_widget.insert(tk.END, "2 - View\n")
        text_widget.insert(tk.END, "3 - Update\n")
        text_widget.insert(tk.END, "4 - Delete\n")
        choice = simpledialog.askinteger("Doctor Management", "Choose an option:")

        if choice == 1:
            first_name = simpledialog.askstring("Register Doctor", "Enter first name:")
            surname = simpledialog.askstring("Register Doctor", "Enter surname:")
            speciality = simpledialog.askstring("Register Doctor", "Enter speciality:")
            doctors.append(Doctor(first_name, surname, speciality))
            text_widget.insert(tk.END, "Doctor registered.\n")
        elif choice == 2:
            text_widget.insert(tk.END, "----- Doctors List -----\n")
            self.view(doctors, text_widget)
        elif choice == 3:
            self.view(doctors, text_widget)
            idx = simpledialog.askinteger("Update Doctor", "Choose a doctor to update (ID):")
            if idx is not None:
                idx -= 1
            else:
                text_widget.insert(tk.END, "Operation cancelled.\n")
                return
            if 0 <= idx < len(doctors):
                doctor = doctors[idx]
                text_widget.insert(tk.END, "1 - Update First Name\n")
                text_widget.insert(tk.END, "2 - Update Surname\n")
                text_widget.insert(tk.END, "3 - Update Speciality\n")
                field = simpledialog.askinteger("Update Doctor", "Choose a field:")
                if field == 1:
                    doctor.set_first_name(simpledialog.askstring("Update First Name", "Enter new first name:"))
                elif field == 2:
                    doctor.set_surname(simpledialog.askstring("Update Surname", "Enter new surname:"))
                elif field == 3:
                    doctor.set_speciality(simpledialog.askstring("Update Speciality", "Enter new speciality:"))
                text_widget.insert(tk.END, "Doctor details updated.\n")
            else:
                text_widget.insert(tk.END, "Invalid ID.\n")
        elif choice == 4:
            self.view(doctors, text_widget)
            idx = simpledialog.askinteger("Delete Doctor", "Choose a doctor to delete (ID):")
            if idx is not None:
                idx -= 1
            else:
                text_widget.insert(tk.END, "Operation cancelled.\n")
                return
            if 0 <= idx < len(doctors):
                del doctors[idx]
                text_widget.insert(tk.END, "Doctor deleted.\n")
            else:
                text_widget.insert(tk.END, "Invalid ID.\n")
        else:
            text_widget.insert(tk.END, "Invalid option.\n")

    def discharge_patient(self, patients, discharged_patients, patient_id, text_widget):
        # Discharge a patient
        for patient in patients:
            if patient.get_id() == patient_id:
                discharged_patients.append(patient)
                patients.remove(patient)
                text_widget.insert(tk.END, f"Patient with ID {patient_id} discharged.\n")
                return
        text_widget.insert(tk.END, f"Patient with ID {patient_id} not found.\n")

    def view_discharged_patients(self, discharged_patients, text_widget):
        # View discharged patients
        text_widget.insert(tk.END, "----- Discharged Patients -----\n")
        for patient in discharged_patients:
            text_widget.insert(tk.END, f"{patient}\n")

    def update_name(self, new_name):
        # Update admin username
        self.__username = new_name
        print("Name updated.")

    def update_address(self, new_address):
        self.__address = new_address

    def get_address(self):
        # Return the admin address
        return self.__address

    def save_patients_to_file(self, patients, filename="patients.json"):
        # Save patients to a file
        with open(filename, 'w') as file:
            json.dump([p.to_dict() for p in patients], file)
        print(f"Patients saved to {filename}.")

    def load_patients_from_file(self, filename="patients.json"):
        # Load patients from a file
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                return [Patient.from_dict(p) for p in data]
        except FileNotFoundError:
            print(f"{filename} not found.")
            return []

    def assign_doctor_to_patient(self, patients, doctors, text_widget):
        # Assign a doctor to a patient
        text_widget.insert(tk.END, "----- Assign Doctor to Patient -----\n")
        self.view(patients, text_widget)
        patient_idx = simpledialog.askinteger("Assign Doctor", "Choose a patient ID:")
        if patient_idx is not None:
            patient_idx -= 1
        else:
            text_widget.insert(tk.END, "Operation cancelled.\n")
            return
        self.view(doctors, text_widget)
        doctor_idx = simpledialog.askinteger("Assign Doctor", "Choose a doctor ID:")
        if doctor_idx is not None:
            doctor_idx -= 1
        else:
            text_widget.insert(tk.END, "Operation cancelled.\n")
            return
        if 0 <= patient_idx < len(patients) and 0 <= doctor_idx < len(doctors):
            doctors[doctor_idx].add_patient(patients[patient_idx])
            patients[patient_idx].link(doctors[doctor_idx])
            text_widget.insert(tk.END, "Doctor assigned.\n")
        else:
            text_widget.insert(tk.END, "Invalid ID.\n")

    def relocate_patient(self, patients, doctors, patient_id, new_doctor_id, text_widget):
        # Relocate a patient to a new doctor
        patient = next((p for p in patients if p.get_id() == patient_id), None)
        new_doctor = next((d for d in doctors if d.get_id() == new_doctor_id), None)

        if patient and new_doctor:
            # Remove patient from current doctor's list
            current_doctor_name = patient.get_doctor()
            current_doctor = next((d for d in doctors if d.full_name() == current_doctor_name), None)
            if current_doctor:
                current_doctor.remove_patient(patient)

            # Assign patient to new doctor
            patient.link(new_doctor)
            new_doctor.add_patient(patient)
            text_widget.insert(tk.END, f"Patient {patient_id} relocated to Dr. {new_doctor.full_name()}.\n")
        else:
            text_widget.insert(tk.END, "Patient or doctor not found.\n")

    def generate_report(self, doctors, patients, text_widget):
        # Generate a management report
        patients_from_file = self.load_patients_from_file()
        all_patients = patients + patients_from_file

        text_widget.insert(tk.END, "----- Management Report -----\n")
        text_widget.insert(tk.END, f"Total Doctors: {len(doctors)}\n")
        text_widget.insert(tk.END, f"Total Patients: {len(all_patients)}\n")
        for doctor in doctors:
            text_widget.insert(tk.END, f"Doctor: {doctor.full_name()}\n")
            text_widget.insert(tk.END, f"  Total Patients: {len(doctor.get_patients())}\n")
            # Assuming appointments and illness type data are available
            # text_widget.insert(tk.END, f"  Total Appointments per Month: {doctor.get_appointments_per_month()}\n")
            # text_widget.insert(tk.END, f"  Total Patients by Illness Type: {doctor.get_patients_by_illness_type()}\n")

    def update_username(self, new_username):
        self.__username = new_username

    def update_password(self, new_password):
        self.__password = new_password

#   __           ___ __ 
#  /__)/  ///| )(_  /__)
# / ( (__/(/ |/ /__/  (
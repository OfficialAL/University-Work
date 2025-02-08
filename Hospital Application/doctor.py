import random
import string

class Doctor:
    """A class that deals with Doctor operations"""

    _id_counter = 1

    def __init__(self, first_name, surname, speciality):
        self.__first_name = first_name
        self.__surname = surname
        self.__speciality = speciality
        self.__patients = []
        self.__id = self.generate_id()

    def generate_id(self):
        # Generate a unique integer ID for the doctor
        id = Doctor._id_counter
        Doctor._id_counter += 1
        return id

    def full_name(self):
        # Return the full name of the doctor
        return f"{self.__first_name} {self.__surname}"

    def get_first_name(self):
        # Return the first name of the doctor
        return self.__first_name

    def set_first_name(self, new_first_name):
        # Set a new first name for the doctor
        self.__first_name = new_first_name

    def get_surname(self):
        # Return the surname of the doctor
        return self.__surname

    def set_surname(self, new_surname):
        # Set a new surname for the doctor
        self.__surname = new_surname

    def get_speciality(self):
        # Return the speciality of the doctor
        return self.__speciality

    def set_speciality(self, new_speciality):
        # Set a new speciality for the doctor
        self.__speciality = new_speciality

    def add_patient(self, patient):
        # Add a patient to the doctor's list
        self.__patients.append(patient)

    def remove_patient(self, patient):
        # Remove a patient from the doctor's list
        if patient in self.__patients:
            self.__patients.remove(patient)

    def get_patients(self):
        # Return the list of patients assigned to the doctor
        return self.__patients

    def get_appointments_per_month(self):
        # Placeholder for actual implementation
        return 0

    def get_patients_by_illness_type(self):
        # Placeholder for actual implementation
        return {}

    def get_id(self):
        # Return the doctor's ID
        return self.__id

    def __str__(self):
        # Return a string representation of the doctor
        return f"{self.full_name():^30}|{self.__speciality:^15}"

#   __           ___ __ 
#  /__)/  ///| )(_  /__)
# / ( (__/(/ |/ /__/ (
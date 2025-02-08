import random
import string

class Patient:
    """A class that represents a Patient."""

    _id_counter = 1

    def __init__(self, first_name, surname, age, mobile, postcode, symptoms=[], address='', family_id=None, patient_id=None):
        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__symptoms = symptoms
        self.__doctor = None
        self.__address = address
        self.__family_id = family_id
        self.__id = patient_id if patient_id is not None else self.generate_id()

    def generate_id(self):
        # Generate a unique integer ID for the patient
        id = Patient._id_counter
        Patient._id_counter += 1
        return id

    def full_name(self):
        # Return the full name of the patient
        return f"{self.__first_name} {self.__surname}"

    def get_doctor(self):
        # Return the name of the doctor assigned to the patient
        return self.__doctor

    def link(self, doctor):
        # Link a doctor to the patient
        self.__doctor = doctor.full_name()

    def get_id(self):
        # Return the patient's ID
        return self.__id

    def get_family_id(self):
        # Return the family ID of the patient
        return self.__family_id

    def to_dict(self):
        # Convert the patient object to a dictionary
        return {
            "first_name": self.__first_name,
            "surname": self.__surname,
            "age": self.__age,
            "mobile": self.__mobile,
            "postcode": self.__postcode,
            "symptoms": self.__symptoms,
            "doctor": self.__doctor,
            "address": self.__address,
            "family_id": self.__family_id,
            "id": self.__id
        }

    @staticmethod
    def from_dict(data):
        # Create a patient object from a dictionary
        return Patient(
            data["first_name"],
            data["surname"],
            data["age"],
            data["mobile"],
            data["postcode"],
            data["symptoms"],
            data.get("address", ''),
            data.get("family_id", None),
            data.get("id", None)
        )

    def __str__(self):
        # Return a string representation of the patient
        return f"{self.full_name():^30}|{self.__doctor or 'None':^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}"

#   __           ___ __ 
#  /__)/  ///| )(_  /__)
# / ( (__/(/ |/ /__/ (
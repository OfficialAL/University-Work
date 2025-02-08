import unittest
from unittest.mock import Mock
from admin import Admin
from doctor import Doctor
from patient import Patient

class TestHospitalManagementSystem(unittest.TestCase):

    def setUp(self):
        # Initialize the admin, doctor, patient, and other necessary objects
        self.admin = Admin('admin', '1234', 'Admin Street')
        self.doctor = Doctor("John", "Doe", "Cardiology")
        self.patient = Patient("Alice", "Smith", 30, "1234567890", "AB1 2CD", ["Fever"])
        self.discharged_patients = []
        self.text_widget = Mock()

    def test_admin_login_success(self):
        # Test successful admin login
        self.assertTrue(self.admin.login('admin', '1234'))

    def test_admin_login_failure(self):
        # Test admin login failure
        self.assertFalse(self.admin.login('admin', 'wrongpassword'))

    def test_doctor_full_name(self):
        # Test getting the full name of a doctor
        self.assertEqual(self.doctor.full_name(), "John Doe")

    def test_patient_full_name(self):
        # Test getting the full name of a patient
        self.assertEqual(self.patient.full_name(), "Alice Smith")

    def test_link_doctor_to_patient(self):
        # Test linking a doctor to a patient
        self.patient.link(self.doctor)
        self.assertEqual(self.patient.get_doctor(), "John Doe")

    def test_discharge_patient(self):
        # Test discharging a patient
        patients = [self.patient]
        self.admin.discharge_patient(patients, self.discharged_patients, self.patient.get_id(), self.text_widget)
        self.assertIn(self.patient, self.discharged_patients)
        self.assertNotIn(self.patient, patients)

    def test_save_and_load_patients(self):
        # Test saving and loading patients to/from a file
        patients = [self.patient]
        self.admin.save_patients_to_file(patients, "test_patients.json")
        loaded_patients = self.admin.load_patients_from_file("test_patients.json")
        self.assertEqual(len(loaded_patients), 1)
        self.assertEqual(loaded_patients[0].full_name(), "Alice Smith")

    def test_assign_doctor_to_patient(self):
        # Test assigning a doctor to a patient
        patients = [self.patient]
        doctors = [self.doctor]
        self.admin.assign_doctor_to_patient(patients, doctors, self.text_widget)
        self.assertEqual(self.patient.get_doctor(), "John Doe")
        self.assertIn(self.patient, self.doctor.get_patients())

    def test_relocate_patient(self):
        # Test relocating a patient to a new doctor
        new_doctor = Doctor("Jane", "Doe", "Neurology")
        doctors = [self.doctor, new_doctor]
        patients = [self.patient]
        self.patient.link(self.doctor)
        self.doctor.add_patient(self.patient)
        self.admin.relocate_patient(patients, doctors, self.patient.get_id(), new_doctor.get_id(), self.text_widget)
        self.assertEqual(self.patient.get_doctor(), "Jane Doe")
        self.assertIn(self.patient, new_doctor.get_patients())
        self.assertNotIn(self.patient, self.doctor.get_patients())

    def test_update_admin_username(self):
        # Test updating admin username
        self.admin.update_name("new_admin")
        self.assertTrue(self.admin.login("new_admin", "1234"))

    def test_update_admin_password(self):
        # Test updating admin password
        self.admin.update_password("new_password")
        self.assertTrue(self.admin.login("admin", "new_password"))

    def test_update_admin_address(self):
        # Test updating admin address
        self.admin.update_address("New Admin Street")
        self.assertEqual(self.admin.get_address(), "New Admin Street")

    def test_patient_to_dict(self):
        # Test converting patient to dictionary
        patient_dict = self.patient.to_dict()
        self.assertEqual(patient_dict["first_name"], "Alice")
        self.assertEqual(patient_dict["surname"], "Smith")

    def test_patient_from_dict(self):
        # Test creating patient from dictionary
        patient_dict = self.patient.to_dict()
        new_patient = Patient.from_dict(patient_dict)
        self.assertEqual(new_patient.full_name(), "Alice Smith")

if __name__ == '__main__':
    unittest.main()

#   __           ___ __ 
#  /__)/  ///| )(_  /__)
# / ( (__/(/ |/ /__/  (

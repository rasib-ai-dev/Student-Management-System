class Student:
    def __init__(self, student_id, full_name, father_name, age, gender, student_class, 
                 section, roll_number, phone, email, address, date_of_birth, admission_date):
        self.student_id = student_id
        self.full_name = full_name
        self.father_name = father_name
        self.age = age
        self.gender = gender
        self.student_class = student_class
        self.section = section
        self.roll_number = roll_number
        self.phone = phone
        self.email = email
        self.address = address
        self.date_of_birth = date_of_birth
        self.admission_date = admission_date


    def to_dict(self):
        return {
            "Student_ID": self.student_id,
            "Full_Name": self.full_name,
            "Father_Name": self.father_name,
            "Age": self.age,
            "Gender": self.gender,
            "Class": self.student_class,
            "Section": self.section,
            "Roll_Number": self.roll_number,
            "Phone": self.phone,
            "Email": self.email,
            "Address": self.address,
            "Date_Of_Birth": self.date_of_birth,
            "Admission_Date": self.admission_date
        }


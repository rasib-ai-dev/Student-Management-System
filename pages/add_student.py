from utils import add_student, load_students, normalize_name, normalize_email, generate_student_id
from student import Student
import streamlit as st
import datetime

generated_id = generate_student_id()

def show_add_student_page():
    st.title("➕ Add New Student Form")

    with st.form("Add New Student Form"):
        
        col1, col2, col3 = st.columns(3)
        with col1:
            student_id = st.text_input("Student ID", value=generated_id, disabled=True)
        with col2:
            full_name = st.text_input("Full Name", placeholder="Enter Student's Full Name")
        with col3:
            father_name = st.text_input("Father's Name", placeholder="Enter Father's Full Name")

        col4, col5, col6 = st.columns(3)
        with col4:
            std_class = st.selectbox("Class", options=["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th"], placeholder="e.g., 5th")
        with col5:
            section = st.selectbox("Section", options=["A", "B", "C", "D"], placeholder="e.g., A")
        with col6:
            roll_number = st.number_input("Roll Number", min_value=1, step=1, placeholder="e.g., 1")

        col7, col8, col9 = st.columns(3)
        with col7:
            gender = st.selectbox("Gender", options=["Male", "Female"], placeholder="Select Gender")
        with col8:
            age = st.number_input("Age", min_value=5, max_value=30, step=1, placeholder="Enter Student's Age")
        with col9:
            phone = st.text_input("Phone Number", max_chars=11 ,placeholder="e.g., 03001234567")

        email = st.text_input("Email", placeholder="e.g., student@example.com")
        address = st.text_area("Address", placeholder="Enter Student's Address")

        col12, col13 = st.columns(2)
        with col12:
            date_of_birth = st.date_input(
                "Date of Birth",
                value=datetime.date(2010, 1, 1),
                max_value=datetime.date.today()
            )
        with col13:
            admission_date = st.date_input(
                "Admission Date",
                value=datetime.date.today()
            )

        submitted = st.form_submit_button("➕ Add Student")
        
        if submitted:
            if not student_id.strip():
                st.error("Student ID is required.")
                st.stop()
            elif not full_name.strip():
                st.error("Full Name is required.")
                st.stop()
            elif not father_name.strip():
                st.error("Father's Name is required.")
                st.stop()
            elif not email.strip():
                st.error("Email is required.")
                st.stop()
            elif not address.strip():
                st.error("Address is required.")
                st.stop()
            elif not phone.strip():
                st.error("Phone Number is required.")
                st.stop()
            elif not phone.isdigit() or len(phone) != 11:
                st.error("Invalid phone number! It must be exactly 11 digits and contain only numbers.")
                st.stop()
            elif ("@" not in email) or ("." not in email):
                st.error("Invalid email address.")
                st.stop()
            else:
                student = Student(
                student_id=student_id.strip().upper(),
                full_name=normalize_name(full_name),
                father_name=normalize_name(father_name),
                age=age,
                gender=gender,
                student_class=std_class,
                section=section,
                roll_number=roll_number,
                phone=phone,
                email=normalize_email(email),
                address=normalize_name(address),
                date_of_birth=date_of_birth,
                admission_date=admission_date
            )
                if add_student(student):
                    st.success(f"{full_name} Student record added successfully!")
                else:
                    st.error("Failed to save data. Please check the information provided.")
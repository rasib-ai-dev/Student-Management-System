import streamlit as st
from datetime import datetime, date
from utils import load_students, update_student, normalize_name, normalize_email
from student import Student

def update_student_page():
    st.title("✏️ Update Student")
    students_df = load_students()

    if students_df.empty:
        st.info("No student records found.")
        return

    st.write("Update an existing student record in the system.")
    student_id_input = st.text_input("Enter Student ID to update", placeholder="e.g. STD-1001")

    if st.button("Search"):
        if not student_id_input.strip():
            st.warning("Please enter a Student ID to search.")
            st.session_state.pop("update_target_id", None)
        else:
            filtered_df = students_df[students_df["Student_ID"].str.upper() ==student_id_input.strip().upper()]
            if filtered_df.empty:
                st.warning(f"❌ No matching Student ID ({student_id_input}) records found.")
                st.session_state.pop("update_target_id", None)
            else:
                st.session_state.update_target_id = filtered_df.iloc[0]["Student_ID"]

    if "update_target_id" in st.session_state:
        target_id = st.session_state.update_target_id

        row_df = students_df[
            students_df["Student_ID"] == target_id]

        if row_df.empty:
            st.error("Student record no longer exists.")
            st.session_state.pop("update_target_id", None)
            st.rerun()

        row = row_df.iloc[0]
        phone_number = str(row["Phone"]).zfill(11)

        st.success("✅ Access Granted: Student record retrieved successfully from the database.")
        st.write(f"Found Matching Student: {target_id}")

        st.subheader("📄 Student Profile Overview")

        st.table({
            "Profile Field": [
                "Student ID",
                "Full Name",
                "Father Name",
                "Class",
                "Section",
                "Roll Number",
                "Age",
                "Gender",
                "Phone",
                "Email",
                "Address",
                "Date of Birth",
                "Admission Date"
            ],
            "Student Data": [
                row["Student_ID"],
                row["Full_Name"],
                row["Father_Name"],
                row["Class"],
                row["Section"],
                row["Roll_Number"],
                row["Age"],
                row["Gender"],
                phone_number,
                row["Email"],
                row["Address"],
                row["Date_Of_Birth"],
                row["Admission_Date"]
            ]
        })
        
        st.write("Click the 'Update Student' button below to update the student's details.")

        with st.form("🔄 Update Student Form"):
            col1, col2 = st.columns(2)
            with col1:
                full_name = st.text_input("Full Name", value=row["Full_Name"])
            with col2:
                father_name = st.text_input("Father's Name", value=row["Father_Name"])

            col3, col4, col5 = st.columns(3)
            with col3:
                std_class = st.selectbox("Class", options=["1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th"],
                                          index=["1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th"].index(row["Class"]))
            with col4:
                section = st.selectbox("Section", options=["A","B","C","D"], index=["A","B","C","D"].index(row["Section"]))
            with col5:
                roll_number = st.number_input("Roll Number", min_value=1, step=1, value=int(row["Roll_Number"]))

            col6, col7, col8 = st.columns(3)
            with col6:
                gender = st.selectbox("Gender", options=["Male","Female"], index=["Male","Female"].index(row["Gender"]))
            with col7:
                age = st.number_input("Age", min_value=5, max_value=30, step=1, value=int(row["Age"]))
            with col8:
                phone = st.text_input("Phone Number", max_chars=11, value=str(row["Phone"]).zfill(11))

            email = st.text_input("Email", value=row["Email"])
            address = st.text_area("Address", value=row["Address"])

            col11, col12 = st.columns(2)
            with col11:
                date_obj = datetime.strptime(row["Date_Of_Birth"], "%Y-%m-%d").date()
                date_of_birth = st.date_input("Date of Birth", max_value=date.today(), value=date_obj)
            with col12:
                admission_obj = datetime.strptime(row["Admission_Date"], "%Y-%m-%d").date()
                admission_date = st.date_input("Admission Date", value=admission_obj)

            submitted = st.form_submit_button("🔄 Update Student")

            if submitted:
                if not full_name.strip():
                    st.error("❌ Full Name is required.")
                elif not father_name.strip():
                    st.error("❌ Father's Name is required.")
                elif not email.strip():
                    st.error("❌ Email is required.")
                elif not address.strip():
                    st.error("❌ Address is required.")
                elif not phone.strip():
                    st.error("❌ Phone Number is required.")
                elif not phone.isdigit() or len(phone) != 11:
                    st.error("❌ Invalid phone number! It must be exactly 11 digits and contain only numbers.")
                elif ("@" not in email) or ("." not in email):
                    st.error("❌ Invalid email address.")
                else:
                    success = update_student(target_id, Student(
                        student_id=target_id,
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
                    ))

                    if success:
                        st.success(f"✅ Student {full_name} updated successfully!")
                        del st.session_state["update_target_id"]
                        st.rerun()
                    else:
                        st.error("❌ Update failed — possibly a duplicate roll number in the same class/section.")

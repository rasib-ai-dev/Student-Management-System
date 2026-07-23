import streamlit as st
from utils import load_students, delete_student

def delete_student_page():
    st.title("🗑️ Delete Student")
    students_df = load_students()

    if students_df.empty:
        st.info("No student records found.")
        return

    st.write("Delete an existing student record from the system.")
    student_id_input = st.text_input("Enter Student ID to delete: ", placeholder="e.g. STD-1001")

    if st.button("Search"):
        if not student_id_input.strip():
            st.warning("Please enter a Student ID to search.")
            st.session_state.pop("delete_target_id", None)
        else:
            filtered_df = students_df[students_df["Student_ID"].str.upper() == student_id_input.strip().upper()]
            if filtered_df.empty:
                st.warning(f"❌ No matching Student ID ({student_id_input}) records found.")
                st.session_state.pop("delete_target_id", None)
            else:
                st.session_state.delete_target_id = filtered_df.iloc[0]["Student_ID"]

    if "delete_target_id" in st.session_state:
        target_id = st.session_state.delete_target_id
        row_df = students_df[students_df["Student_ID"] == target_id]
        if row_df.empty:
            st.error("Student record no longer exists.")
            st.session_state.pop("delete_target_id", None)
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

        st.write("Click the 'Delete Student' button below to delete the student's record.")
        st.warning("⚠ This action cannot be undone.")

        confirm = st.checkbox("I understand that this action cannot be undone.")
        if st.button("🗑 Delete Student", use_container_width=True):
            if not confirm:
                st.warning("Please confirm before deleting the student.")
            else:
                success = delete_student(target_id)
                if success:
                    st.success(f"✅ {row['Full_Name']} has been deleted successfully.")
                    st.session_state.pop("delete_target_id", None)
                    st.rerun()
                else:
                    st.error(f"Failed to delete student with ID {target_id}. Please try again.")
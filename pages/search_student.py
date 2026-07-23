import streamlit as st
from utils import load_students

def show_search_student_page():
    st.title("🔍 Search Student")
    students_df = load_students()

    if students_df.empty:
        st.info("No student records found.")
    else:
        st.write("Search a Student by ID, Name, or Roll Number.")
        search_query = st.text_input("Enter Student ID, Full Name, or Roll Number to search: ")

        if st.button("Search"):
            if not search_query.strip():
                st.warning("Please enter a value to search.")
            elif search_query:
                filtered_df = students_df[
                    (students_df["Student_ID"].str.contains(search_query, case=False, na=False)) |
                    (students_df["Full_Name"].str.contains(search_query, case=False, na=False)) |
                    (students_df["Roll_Number"].astype(str).str.contains(search_query, na=False))
                ]
                
                if filtered_df.empty:
                    st.warning(f"No matching Student ({search_query}) records found.")
                else:
                    st.success("✅ Access Granted: Student record retrieved successfully from the database.")
                    st.write(f"The **(Student: {search_query})** you searched for exists in the system.")

                    row = filtered_df.iloc[0]
                    phone = str(row["Phone"]).zfill(11)

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
                            phone,
                            row["Email"],
                            row["Address"],
                            row["Date_Of_Birth"],
                            row["Admission_Date"]
                        ]
                    })
                    row_index = filtered_df.index[0]
                    st.write("📍 Record Position")
                    st.write(f"This student's record is located at **Row Number: {row_index}** (Index: {row_index+1}) in the View Students table.")
import os
import pandas as pd


FILE_PATH = "data/students.csv"

COLUMNS = [
    "Student_ID",
    "Full_Name",
    "Father_Name",
    "Age",
    "Gender",
    "Class",
    "Section",
    "Roll_Number",
    "Phone",
    "Email",
    "Address",
    "Date_Of_Birth",
    "Admission_Date"
]


def create_students_csv():
    """
    Create students.csv file if it does not exist.
    """

    if not os.path.exists(FILE_PATH):
        df = pd.DataFrame(columns=COLUMNS)
        df.to_csv(FILE_PATH, index=False)
        print("✅ students.csv created successfully.")

    else:
        print("ℹ️ students.csv already exists.")

def load_students():
    """
    Load all student records from students.csv.
    Returns an empty DataFrame if the file does not exist.
    """
    if os.path.exists(FILE_PATH):
        return pd.read_csv(
            FILE_PATH,
            dtype={
                "Student_ID": str,
                "Roll_Number": int,
                "Phone": str,
                "Age": int
            }
        )
    return pd.DataFrame(columns=COLUMNS)


def add_student(student):
    """
    Add a new student record to students.csv.
    """
    student_data = student.to_dict()
    students_df = load_students()

    duplicate_roll = students_df[
        (students_df["Class"] == student_data["Class"]) &
        (students_df["Section"] == student_data["Section"]) &
        (students_df["Roll_Number"].astype(int) == int(student_data["Roll_Number"]))
    ]

    if student_data["Student_ID"] in students_df["Student_ID"].values:
        return False
    elif not duplicate_roll.empty:
        return False
    else:
        pd.concat([students_df, pd.DataFrame([student_data])], ignore_index=True).to_csv(FILE_PATH, index=False)
        return True
    


def update_student(student_id, updated_student):
    """
    Update an existing student record in students.csv.
    """
    updated_data = updated_student.to_dict()
    students_df = load_students()

    if student_id not in students_df["Student_ID"].values:
        return False

    duplicate_roll = students_df[
        (students_df["Class"] == updated_data["Class"]) &
        (students_df["Section"] == updated_data["Section"]) &
        (students_df["Roll_Number"].astype(int) == int(updated_data["Roll_Number"])) &
        (students_df["Student_ID"] != student_id)
    ]

    if not duplicate_roll.empty:
        return False

    students_df.loc[students_df["Student_ID"] == student_id, COLUMNS] = list(updated_data.values())
    students_df.to_csv(FILE_PATH, index=False)
    return True


def normalize_name(text):
    """
    Convert to title case: 'muhammad rasib' -> 'Muhammad Rasib'
    """
    return text.strip().title()

def normalize_email(text):
    """
    Convert to lowercase: 'ABCDEF@GMAIL.COM' -> 'abcdef@gmail.com'
    """
    return text.strip().lower()

def delete_student(student_id):
    """
    Delete a student record from students.csv.
    """
    students_df = load_students()

    if student_id not in students_df["Student_ID"].values:
        return False

    students_df = students_df[students_df["Student_ID"] != student_id]
    students_df.to_csv(FILE_PATH, index=False)
    return True


def generate_student_id():
    FILE_NAME = "data/students.csv"
    if not os.path.exists(FILE_NAME):
        return "STD-1001"

    df = pd.read_csv(FILE_NAME)

    if df.empty or "Student_ID" not in df.columns:
        return "STD-1001"

    last_id = df["Student_ID"].iloc[-1]

    last_number = int(last_id.split("-")[1])

    new_number = last_number + 1

    return f"STD-{new_number:04d}"




def view_student_per_selected_classes_and_selected_section(df):
    """
    View Students By Selected Class & Section
    """

    import streamlit as st
    df["Phone"] = df["Phone"].astype(str).str.zfill(11)

    col1, col2 = st.columns(2)
    with col1:
        clas = st.selectbox("Class", ["-- Select Class --", "1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th"])
    with col2:
        section = st.selectbox("Section", ["-- Select Section --", "A", "B", "C", "D", "All Sections"])
        
    if clas == "-- Select Class --":
        return None
        
    if section == "-- Select Section --":
        return None
        
    if section == "All Sections":
        filtered_students = df[df["Class"] == clas]
        if filtered_students.empty:
            st.info(f"❌ No student records found for Class {clas}")
        else:
            st.write(f"View all student records for Class {clas}")
            st.success(f"Total Students: {len(filtered_students)}")
            st.dataframe(filtered_students, use_container_width=True)
            
    else:
        filtered_students = df[(df["Class"] == clas) & (df["Section"] == section)]
        if filtered_students.empty:
            st.info(f"❌ No student records found for Class {clas} - Section {section}.")
        else:
            st.write(f"View all student records for Class {clas} - Section {section}.")
            st.success(f"Total Students: {len(filtered_students)}")
            st.dataframe(filtered_students, use_container_width=True)
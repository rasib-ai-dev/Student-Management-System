import streamlit as st
from utils import load_students, view_student_per_selected_classes_and_selected_section

def show_view_students_page():
    st.title("👨‍🎓 View Students")
    students_df = load_students()

    if students_df.empty:
        st.info("❌ No student records were found.")
    else:
        st.write("View student records by selecting one of the available options below.")
        action = st.selectbox("Choose an action to proceed:", ["-- Select an Option --", "View All Students", "View Students by Class & Section"])
        
        if action == "View All Students":
            st.write("View all student records available in the system.")
            st.success(f"Total Students: {len(students_df)}")
            students_df["Phone"] = students_df["Phone"].astype(str).str.zfill(11)
            st.dataframe(students_df, use_container_width=True)
        elif action == "View Students by Class & Section":
            st.write("Select the class & Section whose students you want to view.")
            view_student_per_selected_classes_and_selected_section(students_df)


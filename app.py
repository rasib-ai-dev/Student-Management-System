from utils import add_student, load_students, create_students_csv, delete_student, update_student
from pages.add_student import show_add_student_page
from pages.search_student import show_search_student_page
from pages.update_student import update_student_page
from pages.delete_student import delete_student_page
from pages.view_students import show_view_students_page
from pages.dashboard import show_dashboard_page
from pages.about import show_about_page
from student import Student
import streamlit as st
import pandas as pd


create_students_csv()

st.set_page_config(page_title="Student Management System", layout="wide")

st.sidebar.title("📌 Main Menu")
page = st.sidebar.radio("Go to Page:", ["🏠 Dashboard", "➕ Add Student", "👨‍🎓 View Students", 
                                        "🔍 Search Student", "✏️ Update Student", "🗑 Delete Student", "ℹ️ About"])

if page == "🏠 Dashboard":
    show_dashboard_page()

elif page == "➕ Add Student":
    show_add_student_page()

elif page == "👨‍🎓 View Students":
    show_view_students_page()

elif page == "🔍 Search Student":
    show_search_student_page()

elif page == "✏️ Update Student":
    update_student_page()

elif page == "🗑 Delete Student":
    delete_student_page()

elif page == "ℹ️ About":
    show_about_page()
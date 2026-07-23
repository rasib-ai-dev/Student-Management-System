import streamlit as st
from utils import load_students
import datetime
import os


def show_dashboard_page():

    st.title("🏫 Student Management System")

    st.write(
        """
        Welcome to the **Student Management System**.

        Manage student records efficiently using the options available in the sidebar.
        """
    )

    st.info(
        "This dashboard provides an overview of student records and system statistics."
    )

    st.divider()

    students_df = load_students()

    if students_df.empty:
        st.warning("❌ No student records found.")
        st.info("Please add student records to view dashboard statistics.")
        return

    # ===========================
    # Statistics
    # ===========================

    total_students = len(students_df)

    male_students = (
        students_df["Gender"]
        .astype(str)
        .str.strip()
        .str.lower()
        .eq("male")
        .sum()
    )

    female_students = (
        students_df["Gender"]
        .astype(str)
        .str.strip()
        .str.lower()
        .eq("female")
        .sum()
    )

    total_classes = students_df["Class"].nunique()
    total_sections = students_df["Section"].nunique()

    st.subheader("📊 Dashboard Statistics")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            label="👨‍🎓 Total Students",
            value=total_students
        )

    with col2:
        st.metric(
            label="👦 Male Students",
            value=male_students
        )

    with col3:
        st.metric(
            label="👧 Female Students",
            value=female_students
        )

    with col4:
        st.metric(
            label="🏫 Total Classes",
            value=total_classes
        )

    with col5:
        st.metric(
            label="🏷 Total Sections",
            value=total_sections
        )

    st.divider()

    # ===========================
    # Students by Class
    # ===========================

    col6, col7 = st.columns(2)

    with col6:

        st.subheader("📚 Students by Class")

        class_summary = (
            students_df["Class"]
            .value_counts()
            .rename_axis("Class")
            .reset_index(name="Students")
        )

        st.dataframe(
            class_summary,
            use_container_width=True,
            hide_index=True
        )

    # ===========================
    # Students by Section
    # ===========================

    with col7:

        st.subheader("🏷 Students by Section")

        section_summary = (
            students_df["Section"]
            .value_counts()
            .rename_axis("Section")
            .reset_index(name="Students")
        )

        st.dataframe(
            section_summary,
            use_container_width=True,
            hide_index=True
        )

    st.divider()

    # ===========================
    # Quick Information
    # ===========================

    st.subheader("⚡ Quick Information")

    col8, col9, col10 = st.columns(3)

    with col8:
        st.info(f"📅 Today's Date\n\n{datetime.date.today().strftime('%d %B %Y')}")

    with col9:
        st.info(f"🕒 Current Time\n\n{datetime.datetime.now().strftime('%I:%M:%S %p')}")

    with col10:
        if os.path.exists("data/students.csv"):
            st.success("💾 Database Status\n\nConnected")
        else:
            st.error("💾 Database Status\n\nDisconnected")

    st.divider()


    # ===========================
    # Available Features
    # ===========================

    st.subheader("🚀 Available Features")

    col11, col12 = st.columns(2)

    with col11:

        st.success("➕ Add Student")
        st.write("Register a new student in the system.")

        st.success("👨‍🎓 View Students")
        st.write("View all student records.")

        st.success("🔍 Search Student")
        st.write("Search a student using Student ID.")

    with col12:
            
        st.success("✏️ Update Student")
        st.write("Modify existing student information.")

        st.success("🗑 Delete Student")
        st.write("Delete a student record permanently.")

        st.success("🏠 Dashboard")
        st.write("View overall student statistics.")


    st.divider()

    st.caption(
        "Student Management System | Developed by Muhammad Rasib Saeed | Version 1.0"
    )
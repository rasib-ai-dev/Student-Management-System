import streamlit as st


def show_about_page():
    st.title("ℹ️ About Student Management System")

    st.info("A simple, secure, and user-friendly application for managing student records efficiently.")

    st.write(
        """
        Welcome to the **Student Management System**, a simple and user-friendly
        application developed to efficiently manage student records.

        This system allows schools and educational institutions to securely
        maintain student information using an organized and easy-to-use interface.
        """
    )

    st.divider()

    st.subheader("📖 Project Overview")

    st.write(
        """
        The Student Management System is designed to simplify the process of
        managing student information. It provides an efficient way to add,
        search, update, delete, and view student records while ensuring data
        accuracy through built-in validation.

        All student data is stored locally in a CSV file, making the system
        lightweight, fast, and easy to maintain.
        """
    )

    st.divider()

    st.subheader("🚀 Features")

    features = [
        "Add New Student",
        "Automatic Student ID Generation",
        "View All Students",
        "View Students by Class & Section",
        "Search Student by Student ID",
        "Update Student Information",
        "Delete Student Records",
        "Duplicate Roll Number Protection",
        "Phone Number Validation",
        "Email Validation",
        "Automatic Name Formatting",
        "Automatic Email Formatting",
        "User-Friendly Interface"
    ]

    for feature in features:
        st.write(f"✅ {feature}")

        st.divider()

        st.subheader("🛠 Technologies Used")

        st.markdown("""
    - Python
    - Streamlit
    - Pandas
    - CSV File Storage
    - Object-Oriented Programming (OOP)
    """)

    st.divider()

    st.subheader("📂 Data Management")

    st.write(
        """
        Student records are stored in a **students.csv** file.

        The application automatically loads, updates, and saves student
        information whenever changes are made. No external database is required.
        """
    )

    st.divider()

    st.subheader("🔒 Data Validation")

    st.markdown("""
- ✔ Unique Student ID
- ✔ Duplicate Roll Number Prevention
- ✔ Required Field Validation
- ✔ Phone Number Validation
- ✔ Email Validation
- ✔ Automatic Name Formatting
- ✔ Automatic Email Formatting
""")

    st.divider()

    st.subheader("📌 Project Information")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Project Name**")
        st.write("Student Management System")

        st.write("**Version**")
        st.write("1.0")

        st.write("**Application Type**")
        st.write("Desktop Web Application")

    with col2:
        st.write("**Programming Language**")
        st.write("Python")

        st.write("**Framework**")
        st.write("Streamlit")

        st.write("**Database**")
        st.write("CSV File")

    st.divider()

    st.subheader("👨‍💻 Developer")

    st.write("**Muhammad Rasib Saeed**")


    st.divider()

    st.caption("© 2026 Student Management System")
    st.caption("Version 1.0")
    st.caption("All Rights Reserved.")
    st.caption("Thank you for using the Student Management System.")
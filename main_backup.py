import streamlit as st

st.title("Career Twin AI")

st.write("Build your career with AI")
st.write("Discover your skills, identify your career path and prepare for your dream job.")

name = st.text_input("Enter your name")

if name:
    st.success("Hello " + name + "! Welcome to Career Twin AI.")

    st.subheader("Choose what you want to explore")

    option = st.selectbox(
        "Select an option",
        [
            "Discover your skills",
            "Identify your career path",
            "Prepare for your dream job"
        ]
    )

    if option == "Discover your skills":
        st.write("### Skills Discovery")

        programming = st.checkbox("I enjoy programming")
        problem_solving = st.checkbox("I enjoy solving problems")
        designing = st.checkbox("I enjoy designing")

        if st.button("Discover My Career"):
            if programming and problem_solving:
                st.success("Recommended Career: Software Developer")
            elif designing:
                st.success("Recommended Career: UI/UX Designer")
            elif problem_solving:
                st.success("Recommended Career: Data Analyst")
            else:
                st.info("Explore different technology careers.")

    elif option == "Identify your career path":
        interest = st.text_input("What do you enjoy most?")

        if st.button("Find My Career"):
            if "coding" in interest.lower() or "programming" in interest.lower():
                st.success("Recommended Career: Software Developer")
            elif "design" in interest.lower():
                st.success("Recommended Career: UI/UX Designer")
            elif "data" in interest.lower():
                st.success("Recommended Career: Data Analyst")
            else:
                st.info("Explore Software, Data, and Design fields.")

    elif option == "Prepare for your dream job":
        job = st.text_input("What is your dream job?")

        if st.button("Create Preparation Plan"):
            st.success("Your Dream Job: " + job)
            st.write("### Preparation Plan")
            st.write("1. Learn the required technical skills")
            st.write("2. Build practical projects")
            st.write("3. Improve communication skills")
            st.write("4. Prepare for interviews")
            st.write("5. Create a good resume")
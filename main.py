import streamlit as st
from PyPDF2 import PdfReader
from docx import Document

# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------

st.set_page_config(
    page_title="Career Twin AI",
    page_icon="🚀",
    layout="wide"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🚀 Career Twin AI")
st.subheader("Build your career with AI")

st.write(
    "Discover your skills • Identify your career path • "
    "Prepare for your dream job"
)

# --------------------------------------------------
# NAME
# --------------------------------------------------

name = st.text_input("Enter your name")

if name:

    st.success(f"Welcome {name}! 👋")

    # ==================================================
    # DASHBOARD
    # ==================================================

    st.header("📊 Career Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Skill Score", "80%")

    with col2:
        st.metric("Resume", "Ready")

    with col3:
        st.metric("Interview", "Ready")

    with col4:
        st.metric("Job Readiness", "92%")

    # --------------------------------------------------
    # CAREER GOAL
    # --------------------------------------------------

    st.subheader("🎯 Career Goal")

    career_goal = st.selectbox(
        "Select your career goal",
        [
            "Software Developer",
            "Data Analyst",
            "UI/UX Designer",
            "Web Developer",
            "AI / ML Engineer"
        ]
    )

    st.info(f"Your selected career goal: {career_goal}")

    # --------------------------------------------------
    # CAREER PREPARATION PROGRESS
    # --------------------------------------------------

    st.subheader("📈 Career Preparation Progress")

    st.write("Technical Skills")
    st.progress(70)

    st.write("Resume Preparation")
    st.progress(100)

    st.write("Interview Preparation")
    st.progress(100)

    st.write("Project Experience")
    st.progress(100)

    # ==================================================
    # FEATURE SELECTION
    # ==================================================

    feature = st.selectbox(
        "Choose a feature",
        [
            "Skills Discovery",
            "Career Recommendation",
            "Dream Job Preparation",
            "Career Report",
            "Resume Analyzer",
            "Interview Preparation",
            "Job Readiness Score",
            "Job Recommendation",
            "AI Career Roadmap",
            "AI Career Progress Tracker",
            "Personalized Skill Gap Analyzer",
            "AI Interview Evaluation",
            "Career Analytics Dashboard",
            "Download Career Report"
        ]
    )

    # ==================================================
    # 1. SKILLS DISCOVERY
    # ==================================================

    if feature == "Skills Discovery":

        st.header("🧠 Skills Discovery")

        programming = st.checkbox(
            "I enjoy programming",
            key="programming"
        )

        problem_solving = st.checkbox(
            "I enjoy solving problems",
            key="problem_solving"
        )

        designing = st.checkbox(
            "I enjoy designing",
            key="designing"
        )

        if st.button("🔍 Discover My Skills"):

            selected_skills = []

            if programming:
                selected_skills.append("Programming")

            if problem_solving:
                selected_skills.append("Problem Solving")

            if designing:
                selected_skills.append("Designing")

            if selected_skills:

                st.success("Skills identified successfully!")

                for skill in selected_skills:
                    st.write("✅", skill)

                selected_scores = []

                if programming:
                    selected_scores.append(80)

                if problem_solving:
                    selected_scores.append(80)

                if designing:
                    selected_scores.append(80)

                overall_score = sum(selected_scores) // len(
                    selected_scores
                )

                st.subheader("📊 Overall Skill Score")

                st.metric(
                    "Your Skill Score",
                    f"{overall_score}%"
                )

            else:

                st.warning(
                    "Please select at least one skill."
                )

    # ==================================================
    # 2. CAREER RECOMMENDATION
    # ==================================================

    elif feature == "Career Recommendation":

        st.header("🎯 Smart Career Recommendation")

        programming = st.checkbox(
            "I enjoy programming",
            key="career_programming"
        )

        problem_solving = st.checkbox(
            "I enjoy solving problems",
            key="career_problem_solving"
        )

        designing = st.checkbox(
            "I enjoy designing",
            key="career_designing"
        )

        if st.button("🚀 Recommend My Career"):

            if programming and problem_solving:

                career = "Software Developer"

                reason = (
                    "You enjoy programming and problem solving, "
                    "which are important skills for software development."
                )

            elif designing:

                career = "UI/UX Designer"

                reason = (
                    "Your interest in designing matches UI/UX design."
                )

            elif problem_solving:

                career = "Data Analyst"

                reason = (
                    "Problem solving is an important part of data analysis."
                )

            elif programming:

                career = "Software Developer"

                reason = (
                    "Programming is a core skill for software development."
                )

            else:

                career = "Explore More Careers"

                reason = (
                    "Select more interests to get a better recommendation."
                )

            st.success(
                f"Recommended Career: {career}"
            )

            st.info(
                f"💡 Why this career?\n\n{reason}"
            )

    # ==================================================
    # 3. DREAM JOB PREPARATION
    # ==================================================

    elif feature == "Dream Job Preparation":

        st.header("💼 Dream Job Preparation")

        dream_job = st.text_input(
            "Enter your dream job",
            placeholder="Example: Software Developer"
        )

        if st.button("📚 Create Preparation Plan"):

            if dream_job:

                st.success(
                    "Your preparation plan is ready!"
                )

                st.write("### Step 1 — Learn Technical Skills")
                st.write(
                    "Learn the programming languages and technologies "
                    "required for your dream job."
                )

                st.write("### Step 2 — Build Projects")
                st.write(
                    "Create practical projects to demonstrate your skills."
                )

                st.write("### Step 3 — Improve Communication")
                st.write(
                    "Practice explaining your projects and technical concepts."
                )

                st.write("### Step 4 — Prepare for Interviews")
                st.write(
                    "Practice aptitude, technical and HR interview questions."
                )

                st.write("### Step 5 — Apply for Jobs")
                st.write(
                    "Prepare your resume and apply for suitable job opportunities."
                )

            else:

                st.warning(
                    "Please enter your dream job."
                )

    # ==================================================
    # 4. CAREER REPORT
    # ==================================================

    elif feature == "Career Report":

        st.header("📄 Career Report")

        dream_job = st.text_input(
            "Enter your dream job",
            key="report_job"
        )

        if st.button("📊 Generate Career Report"):

            if dream_job:

                st.success(
                    "Your career report has been created successfully!"
                )

                st.write("### 👤 Candidate")
                st.write(name)

                st.write("### 🎯 Dream Job")
                st.write(dream_job)

                st.write("### 💼 Recommended Career")
                st.write(dream_job)

                st.write("### 📈 Skill Score")
                st.write("80%")

                st.write("### 🚀 Job Readiness")
                st.write("92%")

            else:

                st.warning(
                    "Please enter your dream job."
                )

    # ==================================================
    # 5. RESUME ANALYZER
    # ==================================================

    elif feature == "Resume Analyzer":

        st.header("📄 Resume Analyzer")

        st.write(
            "Upload your resume to identify technical skills."
        )

        uploaded_file = st.file_uploader(
            "Upload your Resume",
            type=["pdf", "docx"]
        )

        if uploaded_file:

            st.success(
                "Resume uploaded successfully!"
            )

            if st.button("🔍 Analyze Resume"):

                resume_text = ""

                try:

                    if uploaded_file.name.lower().endswith(".pdf"):

                        reader = PdfReader(uploaded_file)

                        for page in reader.pages:

                            text = page.extract_text()

                            if text:
                                resume_text += text

                    else:

                        document = Document(uploaded_file)

                        for paragraph in document.paragraphs:

                            resume_text += (
                                paragraph.text + " "
                            )

                    resume_text = resume_text.lower()

                    skills = [
                        "python",
                        "java",
                        "c++",
                        "sql",
                        "html",
                        "css",
                        "javascript",
                        "react",
                        "machine learning",
                        "data analysis",
                        "git",
                        "streamlit"
                    ]

                    found_skills = []

                    for skill in skills:

                        if skill in resume_text:
                            found_skills.append(skill)

                    missing_skills = [
                        skill
                        for skill in skills
                        if skill not in found_skills
                    ]

                    score = min(
                        int(
                            (len(found_skills) / len(skills))
                            * 100
                        ),
                        100
                    )

                    st.subheader("🧠 Skills Found")

                    if found_skills:

                        for skill in found_skills:
                            st.write("✅", skill.title())

                    else:

                        st.write(
                            "No technical skills detected."
                        )

                    st.subheader("📚 Skills You Can Add")

                    for skill in missing_skills:
                        st.write("➕", skill.title())

                    st.subheader("📊 Resume Score")

                    st.metric(
                        "Resume Score",
                        f"{score}%"
                    )

                    st.progress(score)

                    if score >= 70:

                        st.success(
                            "Your resume contains a good number "
                            "of technical skills."
                        )

                    elif score >= 40:

                        st.info(
                            "Your resume is good, but you can add "
                            "more relevant technical skills."
                        )

                    else:

                        st.warning(
                            "Consider adding more technical skills "
                            "and projects."
                        )

                    st.caption(
                        "Note: This is a basic demo resume analysis "
                        "based on detected technical skills."
                    )

                except Exception as e:

                    st.error(
                        f"Unable to analyze the resume: {e}"
                    )

    # ==================================================
    # 6. INTERVIEW PREPARATION
    # ==================================================

    elif feature == "Interview Preparation":

        st.header("🎤 Interview Question Generator")

        target_job = st.selectbox(
            "Select your target job",
            [
                "Software Developer",
                "Data Analyst",
                "UI/UX Designer"
            ],
            key="interview_target_job"
        )

        if st.button("🔍 Generate Interview Questions"):

            st.subheader("💻 Technical Questions")

            if target_job == "Software Developer":

                questions = [
                    (
                        "What is OOP?",
                        "OOP stands for Object-Oriented Programming. "
                        "It is a programming approach based on objects and classes."
                    ),
                    (
                        "What is a variable?",
                        "A variable is a named memory location used to store data."
                    ),
                    (
                        "What is a database?",
                        "A database is an organized collection of data."
                    ),
                    (
                        "What is SQL?",
                        "SQL is used to store, retrieve and manage data in databases."
                    ),
                    (
                        "What is Git?",
                        "Git is a version control system used to track code changes."
                    )
                ]

            elif target_job == "Data Analyst":

                questions = [
                    (
                        "What is data analysis?",
                        "Data analysis is the process of examining data to find useful information."
                    ),
                    (
                        "What is SQL?",
                        "SQL is used to query and manage data in databases."
                    ),
                    (
                        "What is a dataset?",
                        "A dataset is a collection of related data."
                    ),
                    (
                        "What is data visualization?",
                        "Data visualization represents data using charts and graphs."
                    ),
                    (
                        "What is Python used for in data analysis?",
                        "Python can be used for data processing, analysis and visualization."
                    )
                ]

            else:

                questions = [
                    (
                        "What is UI?",
                        "UI means User Interface. It refers to the visual elements of an application."
                    ),
                    (
                        "What is UX?",
                        "UX means User Experience. It focuses on how users interact with a product."
                    ),
                    (
                        "What is a wireframe?",
                        "A wireframe is a basic visual structure of a webpage or application."
                    ),
                    (
                        "Why is user research important?",
                        "It helps designers understand user needs and problems."
                    ),
                    (
                        "What is usability?",
                        "Usability refers to how easily users can use a product."
                    )
                ]

            for question, answer in questions:

                with st.expander(question):

                    st.write("**Answer:**")
                    st.write(answer)

            st.subheader("🤝 HR Questions")

            hr_questions = [
                (
                    "Tell me about yourself.",
                    "I am a CSE student interested in software development and technology. "
                    "I enjoy solving problems and building practical projects."
                ),
                (
                    "What are your strengths?",
                    "My strengths are problem solving, learning new technologies and teamwork."
                ),
                (
                    "Why should we hire you?",
                    "I am willing to learn, improve my skills and contribute to the organization."
                ),
                (
                    "Where do you see yourself in five years?",
                    "I want to become a skilled professional and take more responsibility in my career."
                )
            ]

            for question, answer in hr_questions:

                with st.expander(question):

                    st.write("**Answer:**")
                    st.write(answer)

    # ==================================================
    # 7. JOB READINESS SCORE
    # ==================================================

    elif feature == "Job Readiness Score":

        st.header("🚀 Job Readiness Score")

        st.write(
            "Check how prepared you are for your target job."
        )

        technical_score = st.slider(
            "💻 Technical Skills",
            0,
            100,
            70,
            key="readiness_technical"
        )

        resume_ready = st.radio(
            "📄 Is your resume ready?",
            ["Yes", "Needs Improvement"],
            key="readiness_resume"
        )

        interview_ready = st.radio(
            "🎤 Are you prepared for interviews?",
            ["Yes", "Not Yet"],
            key="readiness_interview"
        )

        project_ready = st.radio(
            "🛠️ Do you have project experience?",
            ["Yes", "Not Yet"],
            key="readiness_project"
        )

        if st.button("🚀 Calculate Job Readiness"):

            resume_score = 100 if resume_ready == "Yes" else 50
            interview_score = 100 if interview_ready == "Yes" else 40
            project_score = 100 if project_ready == "Yes" else 40

            job_readiness_score = int(
                (
                    technical_score
                    + resume_score
                    + interview_score
                    + project_score
                ) / 4
            )

            st.subheader("📊 Overall Job Readiness")

            st.metric(
                "Job Readiness Score",
                f"{job_readiness_score}%"
            )

            st.progress(job_readiness_score)

            st.write("### 📋 Readiness Breakdown")

            st.write(f"💻 Technical Skills: {technical_score}%")
            st.write(f"📄 Resume: {resume_score}%")
            st.write(f"🎤 Interview Preparation: {interview_score}%")
            st.write(f"🛠️ Project Experience: {project_score}%")

            st.success(
                "Career Twin AI has generated your personal "
                "Job Readiness Report."
            )

    # ==================================================
    # 8. JOB RECOMMENDATION
    # ==================================================

    elif feature == "Job Recommendation":

        st.header("💼 Job Recommendation")

        interest = st.selectbox(
            "Select your area of interest",
            [
                "Software Development",
                "Data Analytics",
                "UI/UX Design",
                "Web Development",
                "Artificial Intelligence"
            ],
            key="job_interest"
        )

        if st.button("🔎 Find Suitable Jobs"):

            if interest == "Software Development":

                role = "Software Developer"

                companies = ["TCS", "Infosys", "Wipro", "Accenture"]

                required_skills = [
                    "Python / Java",
                    "SQL",
                    "Data Structures",
                    "Git"
                ]

                improve = [
                    "Advanced DSA",
                    "Problem Solving",
                    "System Design"
                ]

            elif interest == "Data Analytics":

                role = "Data Analyst"

                companies = [
                    "TCS",
                    "Infosys",
                    "Accenture",
                    "Deloitte"
                ]

                required_skills = [
                    "Python",
                    "SQL",
                    "Excel",
                    "Data Visualization"
                ]

                improve = [
                    "Statistics",
                    "Power BI",
                    "Advanced SQL"
                ]

            elif interest == "UI/UX Design":

                role = "UI/UX Designer"

                companies = [
                    "Accenture",
                    "TCS",
                    "Infosys",
                    "IBM"
                ]

                required_skills = [
                    "Figma",
                    "Wireframing",
                    "Prototyping",
                    "User Research"
                ]

                improve = [
                    "Design Thinking",
                    "UX Research",
                    "Portfolio"
                ]

            elif interest == "Web Development":

                role = "Web Developer"

                companies = [
                    "TCS",
                    "Wipro",
                    "Infosys",
                    "HCLTech"
                ]

                required_skills = [
                    "HTML",
                    "CSS",
                    "JavaScript",
                    "React"
                ]

                improve = [
                    "React",
                    "APIs",
                    "Web Security"
                ]

            else:

                role = "AI / ML Engineer"

                companies = [
                    "TCS",
                    "Infosys",
                    "Accenture",
                    "IBM"
                ]

                required_skills = [
                    "Python",
                    "Machine Learning",
                    "Data Science",
                    "SQL"
                ]

                improve = [
                    "Deep Learning",
                    "Machine Learning",
                    "AI Projects"
                ]

            st.success(
                f"Recommended Job Role: {role}"
            )

            st.subheader("🏢 Example Companies")

            for company in companies:
                st.write("•", company)

            st.subheader("🧠 Required Skills")

            for skill in required_skills:
                st.write("✅", skill)

            st.subheader("📚 Skills to Improve")

            for skill in improve:
                st.write("📌", skill)

    # ==================================================
    # 9. AI CAREER ROADMAP
    # ==================================================

    elif feature == "AI Career Roadmap":

        st.header("🗺️ AI Career Roadmap")

        roadmap_career = st.selectbox(
            "Select your target career",
            [
                "Software Developer",
                "Data Analyst",
                "UI/UX Designer",
                "Web Developer",
                "AI / ML Engineer"
            ],
            key="roadmap_career"
        )

        if st.button("🚀 Generate My Career Roadmap"):

            st.success(
                f"AI Career Roadmap generated for {roadmap_career}!"
            )

            if roadmap_career == "Software Developer":

                st.subheader("🟢 Level 1 — Beginner")
                st.write("1️⃣ Learn Python or Java basics")
                st.write("2️⃣ Understand variables, loops and functions")
                st.write("3️⃣ Learn Object-Oriented Programming")
                st.progress(25)

                st.subheader("🟡 Level 2 — Intermediate")
                st.write("4️⃣ Learn SQL and databases")
                st.write("5️⃣ Learn Data Structures and Algorithms")
                st.write("6️⃣ Learn Git and GitHub")
                st.progress(50)

                st.subheader("🟠 Level 3 — Advanced")
                st.write("7️⃣ Build practical software projects")
                st.write("8️⃣ Learn APIs and basic system design")
                st.write("9️⃣ Improve problem-solving skills")
                st.progress(75)

                st.subheader("🔵 Level 4 — Job Ready")
                st.write("🔟 Prepare your resume")
                st.write("1️⃣1️⃣ Practice technical interviews")
                st.write("1️⃣2️⃣ Practice HR interviews")
                st.write("1️⃣3️⃣ Apply for suitable jobs")
                st.progress(100)

            elif roadmap_career == "Data Analyst":

                st.subheader("🟢 Level 1 — Beginner")
                st.write("1️⃣ Learn Excel")
                st.write("2️⃣ Learn basic statistics")
                st.write("3️⃣ Learn SQL")
                st.progress(25)

                st.subheader("🟡 Level 2 — Intermediate")
                st.write("4️⃣ Learn Python")
                st.write("5️⃣ Learn Pandas")
                st.write("6️⃣ Learn data visualization")
                st.progress(50)

                st.subheader("🟠 Level 3 — Advanced")
                st.write("7️⃣ Learn Power BI")
                st.write("8️⃣ Work with real datasets")
                st.write("9️⃣ Build data analysis projects")
                st.progress(75)

                st.subheader("🔵 Level 4 — Job Ready")
                st.write("🔟 Prepare your resume")
                st.write("1️⃣1️⃣ Build a portfolio")
                st.write("1️⃣2️⃣ Practice interviews")
                st.write("1️⃣3️⃣ Apply for jobs")
                st.progress(100)

            elif roadmap_career == "UI/UX Designer":

                st.subheader("🟢 Level 1 — Beginner")
                st.write("1️⃣ Learn UI/UX fundamentals")
                st.write("2️⃣ Learn design principles")
                st.write("3️⃣ Learn user research")
                st.progress(25)

                st.subheader("🟡 Level 2 — Intermediate")
                st.write("4️⃣ Learn Figma")
                st.write("5️⃣ Create wireframes")
                st.write("6️⃣ Create prototypes")
                st.progress(50)

                st.subheader("🟠 Level 3 — Advanced")
                st.write("7️⃣ Work on real design projects")
                st.write("8️⃣ Improve usability knowledge")
                st.write("9️⃣ Build a design portfolio")
                st.progress(75)

                st.subheader("🔵 Level 4 — Job Ready")
                st.write("🔟 Prepare your resume")
                st.write("1️⃣1️⃣ Prepare your portfolio")
                st.write("1️⃣2️⃣ Practice interviews")
                st.write("1️⃣3️⃣ Apply for jobs")
                st.progress(100)

            elif roadmap_career == "Web Developer":

                st.subheader("🟢 Level 1 — Beginner")
                st.write("1️⃣ Learn HTML")
                st.write("2️⃣ Learn CSS")
                st.write("3️⃣ Learn JavaScript")
                st.progress(25)

                st.subheader("🟡 Level 2 — Intermediate")
                st.write("4️⃣ Learn responsive web design")
                st.write("5️⃣ Learn Git and GitHub")
                st.write("6️⃣ Learn APIs")
                st.progress(50)

                st.subheader("🟠 Level 3 — Advanced")
                st.write("7️⃣ Learn React")
                st.write("8️⃣ Build full web projects")
                st.write("9️⃣ Learn basic web security")
                st.progress(75)

                st.subheader("🔵 Level 4 — Job Ready")
                st.write("🔟 Prepare your resume")
                st.write("1️⃣1️⃣ Create a project portfolio")
                st.write("1️⃣2️⃣ Practice interviews")
                st.write("1️⃣3️⃣ Apply for jobs")
                st.progress(100)

            else:

                st.subheader("🟢 Level 1 — Beginner")
                st.write("1️⃣ Learn Python")
                st.write("2️⃣ Learn mathematics and statistics")
                st.write("3️⃣ Learn SQL")
                st.progress(25)

                st.subheader("🟡 Level 2 — Intermediate")
                st.write("4️⃣ Learn NumPy and Pandas")
                st.write("5️⃣ Learn Machine Learning basics")
                st.write("6️⃣ Practice with datasets")
                st.progress(50)

                st.subheader("🟠 Level 3 — Advanced")
                st.write("7️⃣ Learn Deep Learning basics")
                st.write("8️⃣ Build AI/ML projects")
                st.write("9️⃣ Learn model evaluation")
                st.progress(75)

                st.subheader("🔵 Level 4 — Job Ready")
                st.write("🔟 Prepare your resume")
                st.write("1️⃣1️⃣ Build an AI project portfolio")
                st.write("1️⃣2️⃣ Practice technical interviews")
                st.write("1️⃣3️⃣ Apply for suitable jobs")
                st.progress(100)

    # ==================================================
    # 10. AI CAREER PROGRESS TRACKER
    # ==================================================

    elif feature == "AI Career Progress Tracker":

        st.header("📊 AI Career Progress Tracker")

        tracker_career = st.selectbox(
            "Target Career",
            [
                "Software Developer",
                "Data Analyst",
                "UI/UX Designer",
                "Web Developer",
                "AI / ML Engineer"
            ],
            key="tracker_career"
        )

        st.info(
            f"Tracking progress for: {tracker_career}"
        )

        technical_progress = st.slider(
            "💻 Technical Skills Progress",
            0,
            100,
            70,
            key="technical_progress"
        )

        resume_progress = st.slider(
            "📄 Resume Preparation",
            0,
            100,
            80,
            key="resume_progress"
        )

        interview_progress = st.slider(
            "🎤 Interview Preparation",
            0,
            100,
            60,
            key="interview_progress"
        )

        project_progress = st.slider(
            "🛠️ Project Experience",
            0,
            100,
            70,
            key="project_progress"
        )

        if st.button("📈 Calculate My Overall Progress"):

            overall_progress = int(
                (
                    technical_progress
                    + resume_progress
                    + interview_progress
                    + project_progress
                ) / 4
            )

            st.subheader("🌟 Overall Career Progress")

            st.metric(
                "Overall Progress",
                f"{overall_progress}%"
            )

            st.progress(overall_progress)

            progress_values = {
                "Technical Skills": technical_progress,
                "Resume Preparation": resume_progress,
                "Interview Preparation": interview_progress,
                "Project Experience": project_progress
            }

            weakest_area = min(
                progress_values,
                key=progress_values.get
            )

            weakest_score = progress_values[weakest_area]

            st.subheader("📋 Progress Breakdown")

            for area, score in progress_values.items():

                st.write(
                    f"📌 {area}: {score}%"
                )

                st.progress(score)

            st.subheader("🚀 Suggested Next Steps")

            st.info(
                f"💡 Your current focus area is "
                f"{weakest_area} ({weakest_score}%)."
            )

    # ==================================================
    # 11. PERSONALIZED SKILL GAP ANALYZER
    # ==================================================

    elif feature == "Personalized Skill Gap Analyzer":

        st.header("📋 Personalized Skill Gap Analyzer")

        gap_career = st.selectbox(
            "🎯 Select your target career",
            [
                "Software Developer",
                "Data Analyst",
                "UI/UX Designer",
                "Web Developer",
                "AI / ML Engineer"
            ],
            key="gap_career"
        )

        st.subheader("🧠 Select Your Current Skills")

        if gap_career == "Software Developer":

            skill1 = st.checkbox("Python", key="gap_python")
            skill2 = st.checkbox("Java", key="gap_java")
            skill3 = st.checkbox("SQL", key="gap_sql")
            skill4 = st.checkbox("Data Structures", key="gap_dsa")
            skill5 = st.checkbox("Git", key="gap_git")

            current_skills = []

            if skill1:
                current_skills.append("Python")
            if skill2:
                current_skills.append("Java")
            if skill3:
                current_skills.append("SQL")
            if skill4:
                current_skills.append("Data Structures")
            if skill5:
                current_skills.append("Git")

            required_skills = [
                "Python",
                "Java",
                "SQL",
                "Data Structures",
                "Git"
            ]

        elif gap_career == "Data Analyst":

            skill1 = st.checkbox("Python", key="gap_da_python")
            skill2 = st.checkbox("SQL", key="gap_da_sql")
            skill3 = st.checkbox("Excel", key="gap_excel")
            skill4 = st.checkbox("Statistics", key="gap_statistics")
            skill5 = st.checkbox("Power BI", key="gap_powerbi")

            current_skills = []

            if skill1:
                current_skills.append("Python")
            if skill2:
                current_skills.append("SQL")
            if skill3:
                current_skills.append("Excel")
            if skill4:
                current_skills.append("Statistics")
            if skill5:
                current_skills.append("Power BI")

            required_skills = [
                "Python",
                "SQL",
                "Excel",
                "Statistics",
                "Power BI"
            ]

        elif gap_career == "UI/UX Designer":

            skill1 = st.checkbox("Figma", key="gap_figma")
            skill2 = st.checkbox("Wireframing", key="gap_wireframe")
            skill3 = st.checkbox("Prototyping", key="gap_prototype")
            skill4 = st.checkbox("User Research", key="gap_research")
            skill5 = st.checkbox("Design Thinking", key="gap_design")

            current_skills = []

            if skill1:
                current_skills.append("Figma")
            if skill2:
                current_skills.append("Wireframing")
            if skill3:
                current_skills.append("Prototyping")
            if skill4:
                current_skills.append("User Research")
            if skill5:
                current_skills.append("Design Thinking")

            required_skills = [
                "Figma",
                "Wireframing",
                "Prototyping",
                "User Research",
                "Design Thinking"
            ]

        elif gap_career == "Web Developer":

            skill1 = st.checkbox("HTML", key="gap_html")
            skill2 = st.checkbox("CSS", key="gap_css")
            skill3 = st.checkbox("JavaScript", key="gap_javascript")
            skill4 = st.checkbox("React", key="gap_react")
            skill5 = st.checkbox("Git", key="gap_web_git")

            current_skills = []

            if skill1:
                current_skills.append("HTML")
            if skill2:
                current_skills.append("CSS")
            if skill3:
                current_skills.append("JavaScript")
            if skill4:
                current_skills.append("React")
            if skill5:
                current_skills.append("Git")

            required_skills = [
                "HTML",
                "CSS",
                "JavaScript",
                "React",
                "Git"
            ]

        else:

            skill1 = st.checkbox("Python", key="gap_ai_python")
            skill2 = st.checkbox("Machine Learning", key="gap_ml")
            skill3 = st.checkbox("SQL", key="gap_ai_sql")
            skill4 = st.checkbox("Statistics", key="gap_ai_statistics")
            skill5 = st.checkbox("Deep Learning", key="gap_dl")

            current_skills = []

            if skill1:
                current_skills.append("Python")
            if skill2:
                current_skills.append("Machine Learning")
            if skill3:
                current_skills.append("SQL")
            if skill4:
                current_skills.append("Statistics")
            if skill5:
                current_skills.append("Deep Learning")

            required_skills = [
                "Python",
                "Machine Learning",
                "SQL",
                "Statistics",
                "Deep Learning"
            ]

        if st.button("🔍 Analyze My Skill Gap"):

            missing_skills = [
                skill
                for skill in required_skills
                if skill not in current_skills
            ]

            skill_match = int(
                (len(current_skills) / len(required_skills)) * 100
            )

            st.subheader("📊 Skill Match")

            st.metric(
                "Current Skill Match",
                f"{skill_match}%"
            )

            st.progress(skill_match)

            st.subheader("📚 Skill Gap — Skills to Learn")

            if missing_skills:

                for skill in missing_skills:
                    st.write("🔴", skill)

            else:

                st.success(
                    "🎉 You have selected all the required skills!"
                )

            st.subheader("🛣️ Personalized Learning Path")

            for number, skill in enumerate(
                missing_skills,
                start=1
            ):

                st.write(
                    f"**Step {number}:** Learn {skill}"
                )

                st.write(
                    f"Practice {skill} with a small project."
                )

            st.subheader("💡 AI Recommendation")

            if skill_match >= 80:

                st.success(
                    "You have a strong skill match. "
                    "Focus on projects and interview preparation."
                )

            elif skill_match >= 60:

                st.info(
                    "You have a good foundation. "
                    "Learn the missing skills and build projects."
                )

            else:

                st.warning(
                    "Focus on the missing skills one by one."
                )

    # ==================================================
    # 12. AI INTERVIEW EVALUATION
    # ==================================================

    elif feature == "AI Interview Evaluation":

        st.header("🤖 AI Interview Evaluation")

        interview_role = st.selectbox(
            "🎯 Select your interview role",
            [
                "Software Developer",
                "Data Analyst",
                "Web Developer"
            ],
            key="evaluation_role"
        )

        if interview_role == "Software Developer":

            question = (
                "Tell me about yourself and your technical skills."
            )

        elif interview_role == "Data Analyst":

            question = (
                "Tell me about yourself and your interest "
                "in data analysis."
            )

        else:

            question = (
                "Tell me about yourself and your web "
                "development skills."
            )

        st.subheader("🎤 Interview Question")
        st.info(question)

        answer = st.text_area(
            "✍️ Type your answer",
            placeholder=(
                "Example: I am a CSE student interested "
                "in software development. I enjoy solving "
                "problems and building practical projects."
            ),
            height=180,
            key="evaluation_answer"
        )

        if st.button("🤖 Evaluate My Answer"):

            if answer.strip():

                words = answer.strip().split()
                answer_length = len(words)

                score = 40

                if answer_length >= 15:
                    score += 15

                if answer_length >= 30:
                    score += 10

                if answer_length >= 50:
                    score += 10

                answer_lower = answer.lower()

                technical_keywords = [
                    "python",
                    "java",
                    "sql",
                    "programming",
                    "coding",
                    "project",
                    "database",
                    "software",
                    "developer",
                    "problem solving",
                    "data",
                    "web",
                    "javascript",
                    "react"
                ]

                keyword_count = 0

                for keyword in technical_keywords:

                    if keyword in answer_lower:
                        keyword_count += 1

                if keyword_count >= 1:
                    score += 5

                if keyword_count >= 2:
                    score += 5

                score = min(score, 100)

                st.subheader(
                    "📊 Interview Evaluation Result"
                )

                st.metric(
                    "Answer Score",
                    f"{score}%"
                )

                st.progress(score)

                st.subheader("✅ What You Did Well")

                st.write(
                    "✅ Your answer was analyzed for "
                    "detail and technical relevance."
                )

                st.subheader("⚠️ Areas to Improve")

                if answer_length < 30:

                    st.write(
                        "🔸 Add more details about your "
                        "skills, projects and experience."
                    )

                if keyword_count == 0:

                    st.write(
                        "🔸 Mention one or two relevant "
                        "technical skills."
                    )

                st.write(
                    "🔸 Try to answer in a clear and structured way."
                )

                st.subheader("💡 Suggested Better Answer")

                if interview_role == "Software Developer":

                    better_answer = (
                        "I am a CSE student interested in "
                        "software development. I enjoy "
                        "programming and solving problems. "
                        "I have been learning technical skills "
                        "such as Python, SQL and programming "
                        "fundamentals. I am also interested in "
                        "building practical projects and "
                        "improving my problem-solving skills."
                    )

                elif interview_role == "Data Analyst":

                    better_answer = (
                        "I am a CSE student interested in "
                        "data analysis. I enjoy working with "
                        "data and solving problems. I am "
                        "learning skills such as Python, SQL "
                        "and data analysis concepts."
                    )

                else:

                    better_answer = (
                        "I am a CSE student interested in "
                        "web development. I enjoy creating "
                        "web applications and solving "
                        "programming problems. I am learning "
                        "HTML, CSS and JavaScript."
                    )

                st.success(better_answer)

            else:

                st.warning(
                    "Please type your answer before evaluating."
                )

    # ==================================================
    # 13. CAREER ANALYTICS DASHBOARD
    # ==================================================

    elif feature == "Career Analytics Dashboard":

        st.header("📊 Career Analytics Dashboard")

        technical_score = 70
        resume_score = 100
        interview_score = 100
        project_score = 100

        overall_score = int(
            (
                technical_score
                + resume_score
                + interview_score
                + project_score
            ) / 4
        )

        st.subheader("🌟 Overall Career Progress")

        st.metric(
            "Overall Progress",
            f"{overall_score}%"
        )

        st.progress(overall_score)

        st.subheader("📈 Career Preparation Analytics")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "💻 Technical Skills",
                f"{technical_score}%"
            )

        with col2:
            st.metric(
                "📄 Resume",
                f"{resume_score}%"
            )

        with col3:
            st.metric(
                "🎤 Interview",
                f"{interview_score}%"
            )

        with col4:
            st.metric(
                "🛠️ Projects",
                f"{project_score}%"
            )

        st.subheader("📊 Progress Breakdown")

        scores = {
            "Technical Skills": technical_score,
            "Resume Preparation": resume_score,
            "Interview Preparation": interview_score,
            "Project Experience": project_score
        }

        for area, score in scores.items():

            st.write(
                f"📌 {area}: {score}%"
            )

            st.progress(score)

        st.subheader("💪 Strong Areas")

        for area, score in scores.items():

            if score >= 80:

                st.write(
                    f"✅ {area}: {score}%"
                )

        st.subheader("🎯 Area to Improve")

        weakest_area = min(
            scores,
            key=scores.get
        )

        weakest_score = scores[weakest_area]

        st.warning(
            f"{weakest_area} needs more attention "
            f"({weakest_score}%)."
        )

        st.subheader("🤖 AI Recommendation")

        st.info(
            "Focus on improving your technical skills "
            "through coding practice, SQL, DSA and projects."
        )

        st.success(
            "Career Twin AI has generated your "
            "Career Analytics Dashboard successfully!"
        )

    # ==================================================
    # 14. DOWNLOAD CAREER REPORT
    # ==================================================

    elif feature == "Download Career Report":

        st.header("📥 Download Career Report")

        st.write(
            "Generate a simple career report containing "
            "your career preparation details."
        )

        # --------------------------------------------------
        # REPORT DATA
        # --------------------------------------------------

        technical_score = 70
        resume_score = 100
        interview_score = 100
        project_score = 100

        overall_score = int(
            (
                technical_score
                + resume_score
                + interview_score
                + project_score
            ) / 4
        )

        report = f"""
==================================================
             CAREER TWIN AI
              CAREER REPORT
==================================================

Candidate Name:
{name}

Career Goal:
{career_goal}

--------------------------------------------------
CAREER PREPARATION SUMMARY
--------------------------------------------------

Technical Skills       : {technical_score}%
Resume Preparation     : {resume_score}%
Interview Preparation  : {interview_score}%
Project Experience     : {project_score}%

Overall Career Progress: {overall_score}%

Job Readiness Score    : 92%
Skill Score            : 80%

--------------------------------------------------
CAREER FEATURES
--------------------------------------------------

1. Skills Discovery
2. Career Recommendation
3. Dream Job Preparation
4. Career Report
5. Resume Analyzer
6. Interview Preparation
7. Job Readiness Score
8. Job Recommendation
9. AI Career Roadmap
10. AI Career Progress Tracker
11. Personalized Skill Gap Analyzer
12. AI Interview Evaluation
13. Career Analytics Dashboard

--------------------------------------------------
AI RECOMMENDATION
--------------------------------------------------

Focus on improving your technical skills through
programming practice, SQL, Data Structures,
problem-solving and practical projects.

Continue practicing technical and HR interview
questions and keep improving your resume.

--------------------------------------------------
END OF REPORT
--------------------------------------------------

Generated by Career Twin AI
"""

        st.subheader("📄 Report Preview")

        st.text_area(
            "Career Report",
            report,
            height=500
        )

        st.download_button(
            label="📥 Download Career Report",
            data=report,
            file_name="Career_Twin_AI_Report.txt",
            mime="text/plain"
        )

        st.success(
            "Your Career Report is ready to download! 🚀"
        )
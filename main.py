import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
from datetime import date

st.set_page_config(
    page_title="Career Twin AI",
    page_icon="🚀",
    layout="wide"
)

# CAREER DATABASE

CAREERS = {
    "software developer": {
        "category": "Technology",
        "skills": ["Python", "Java", "SQL", "OOP", "Problem Solving", "Git"],
        "improve": ["DSA", "API Development", "Project Development"],
        "steps": [
            "Learn Python or Java fundamentals",
            "Practice variables, loops and functions",
            "Learn SQL and databases",
            "Study data structures and algorithms",
            "Build practical projects",
            "Learn Git and GitHub",
            "Prepare for interviews"
        ],
        "questions": [
            ("What is OOP?", "OOP is a programming approach based on classes and objects."),
            ("What is Python?", "Python is a high-level programming language."),
            ("What is SQL?", "SQL is used to manage and query databases."),
            ("What is Git?", "Git is a version control system.")
        ],
        "companies": ["TCS", "Infosys", "Wipro", "IBM", "Accenture"]
    },

    "data analyst": {
        "category": "Technology and Analytics",
        "skills": ["Excel", "SQL", "Python", "Statistics", "Power BI", "Data Visualization"],
        "improve": ["Advanced SQL", "Dashboard Development", "Communication"],
        "steps": [
            "Learn Excel",
            "Study basic statistics",
            "Learn SQL",
            "Learn Python and Pandas",
            "Practice data analysis",
            "Create Power BI dashboards",
            "Build a portfolio"
        ],
        "questions": [
            ("What is data analysis?", "It is the process of examining data to find useful information."),
            ("What is SQL?", "SQL is used to retrieve and manage database information."),
            ("What is data visualization?", "It represents data using charts and graphs.")
        ],
        "companies": ["TCS", "Infosys", "IBM", "Deloitte", "Accenture"]
    },

    "software tester": {
        "category": "Technology and Quality Assurance",
        "skills": ["Manual Testing", "SDLC", "STLC", "Test Cases", "Bug Reporting", "SQL", "Jira"],
        "improve": ["API Testing", "Automation Testing", "Agile"],
        "steps": [
            "Understand SDLC",
            "Understand STLC",
            "Learn software testing types",
            "Write test cases",
            "Practice bug reporting",
            "Learn SQL",
            "Practice API testing using Postman",
            "Prepare for testing interviews"
        ],
        "questions": [
            ("What is software testing?", "Software testing checks whether an application works as expected."),
            ("What is a test case?", "A test case contains steps and expected results."),
            ("What is a bug?", "A bug is an error in software."),
            ("What is regression testing?", "It checks whether new changes affect existing features.")
        ],
        "companies": ["TCS", "Wipro", "Infosys", "Accenture", "Capgemini"]
    },

    "web developer": {
        "category": "Technology",
        "skills": ["HTML", "CSS", "JavaScript", "Python", "Git", "APIs"],
        "improve": ["React", "Backend Development", "Web Security"],
        "steps": [
            "Learn HTML",
            "Learn CSS",
            "Practice JavaScript",
            "Build responsive websites",
            "Learn Git and GitHub",
            "Understand APIs",
            "Build and deploy projects"
        ],
        "questions": [
            ("What is HTML?", "HTML creates the structure of a webpage."),
            ("What is CSS?", "CSS controls the design of a webpage."),
            ("What is JavaScript?", "JavaScript adds interactivity to webpages.")
        ],
        "companies": ["TCS", "Wipro", "Infosys", "IBM"]
    },

    "doctor": {
        "category": "Healthcare",
        "skills": ["Medical Knowledge", "Biology", "Patient Care", "Communication", "Clinical Reasoning"],
        "improve": ["Clinical Experience", "Patient Communication", "Medical Research"],
        "steps": [
            "Complete required science education",
            "Qualify for the required medical entrance examination",
            "Complete an accredited medical degree",
            "Complete clinical training",
            "Meet professional registration requirements",
            "Continue medical education"
        ],
        "questions": [
            ("Why is patient confidentiality important?", "It protects patient privacy and builds trust."),
            ("What is diagnosis?", "Diagnosis is identifying a disease or condition."),
            ("Why is communication important?", "It helps patients understand their treatment.")
        ],
        "companies": ["Hospitals", "Clinics", "Medical Research Institutions"]
    },

    "teacher": {
        "category": "Education",
        "skills": ["Subject Knowledge", "Communication", "Lesson Planning", "Classroom Management", "Patience"],
        "improve": ["Digital Teaching", "Classroom Skills", "Assessment Methods"],
        "steps": [
            "Choose your teaching subject",
            "Complete the required degree",
            "Complete required teacher training",
            "Practice lesson planning",
            "Develop communication skills",
            "Gain teaching experience",
            "Prepare a teaching portfolio",
            "Apply to schools or colleges"
        ],
        "questions": [
            ("Why do you want to become a teacher?", "I enjoy sharing knowledge and helping students learn."),
            ("What is lesson planning?", "It is preparing the topics and activities for a class."),
            ("How do you manage a classroom?", "By setting clear rules and encouraging students.")
        ],
        "companies": ["Schools", "Colleges", "Training Institutes", "Education Organizations"]
    },

    "nurse": {
        "category": "Healthcare",
        "skills": ["Patient Care", "Communication", "Medical Knowledge", "First Aid", "Teamwork"],
        "improve": ["Clinical Practice", "Emergency Care", "Patient Education"],
        "steps": [
            "Research approved nursing courses",
            "Complete the required nursing education",
            "Complete supervised clinical training",
            "Meet registration requirements",
            "Develop patient care skills",
            "Apply to hospitals and clinics"
        ],
        "questions": [
            ("What is patient care?", "It is providing support and care to patients."),
            ("Why is hygiene important?", "It helps prevent infections."),
            ("What is first aid?", "It is immediate basic care given to an injured person.")
        ],
        "companies": ["Hospitals", "Clinics", "Healthcare Centers"]
    },

    "lawyer": {
        "category": "Law",
        "skills": ["Legal Knowledge", "Research", "Communication", "Critical Thinking", "Argumentation"],
        "improve": ["Legal Drafting", "Court Practice", "Case Analysis"],
        "steps": [
            "Complete the required law education",
            "Study important laws",
            "Develop legal research skills",
            "Practice legal drafting",
            "Gain supervised legal experience",
            "Meet professional enrollment requirements"
        ],
        "questions": [
            ("What is a law?", "A law is a rule established by an authority."),
            ("What is a contract?", "A contract is a legally enforceable agreement."),
            ("Why is legal research important?", "It helps identify relevant laws and previous judgments.")
        ],
        "companies": ["Law Firms", "Legal Departments", "Courts", "Corporate Organizations"]
    },

    "ui/ux designer": {
        "category": "Design",
        "skills": ["Figma", "Wireframing", "Prototyping", "Design Principles", "User Research"],
        "improve": ["Usability Testing", "Portfolio", "Design Systems"],
        "steps": [
            "Learn UI and UX fundamentals",
            "Learn design principles",
            "Practice Figma",
            "Create wireframes",
            "Build prototypes",
            "Create design projects",
            "Build a portfolio"
        ],
        "questions": [
            ("What is UI?", "UI means User Interface."),
            ("What is UX?", "UX means User Experience."),
            ("What is a wireframe?", "A wireframe is a basic layout of a design.")
        ],
        "companies": ["Accenture", "IBM", "TCS", "Infosys"]
    },

    "ai / ml engineer": {
        "category": "Technology",
        "skills": ["Python", "Statistics", "Machine Learning", "SQL", "Data Analysis"],
        "improve": ["Deep Learning", "Model Evaluation", "Deployment"],
        "steps": [
            "Learn Python",
            "Study statistics",
            "Learn data analysis",
            "Understand machine learning",
            "Practice model building",
            "Build projects",
            "Learn model deployment"
        ],
        "questions": [
            ("What is AI?", "AI is technology that performs tasks requiring human-like intelligence."),
            ("What is machine learning?", "It enables computers to learn patterns from data.")
        ],
        "companies": ["IBM", "Google", "TCS", "Infosys"]
    }
}

GENERAL_SKILLS = [
    "Communication",
    "Problem Solving",
    "Time Management",
    "Teamwork",
    "Adaptability",
    "Computer Knowledge"
]

# GENERAL PROFILE FOR ANY OTHER CAREER

def create_profile(career):
    name = career.strip().title()

    return {
        "category": "General Career",
        "skills": [
            "Basic knowledge of " + name,
            "Communication",
            "Problem Solving",
            "Time Management",
            "Teamwork",
            "Professional Knowledge"
        ],
        "improve": [
            "Practical Experience",
            "Professional Communication",
            "Technical Knowledge",
            "Interview Preparation"
        ],
        "steps": [
            "Understand the responsibilities of a " + name,
            "Research the required qualifications",
            "Learn the basic skills for this career",
            "Attend relevant training or courses",
            "Gain practical experience",
            "Build a portfolio or work profile",
            "Prepare for interviews",
            "Apply for suitable opportunities"
        ],
        "questions": [
            ("Why do you want to become a " + name + "?",
             "Explain your interest and motivation for choosing this career."),
            ("What skills are important for this career?",
             "Explain the professional and practical skills required."),
            ("How will you improve your knowledge?",
             "Explain your learning plan and practical experience.")
        ],
        "companies": [
            "Relevant Companies",
            "Organizations",
            "Professional Institutions"
        ]
    }


# PAGE HEADER

st.title("🚀 Career Twin AI")
st.subheader("Explore your future, one step at a time")
st.write("Discover your career skills, learning roadmap and job preparation plan.")

st.divider()

name = st.text_input(
    "Enter your name",
    placeholder="Your name"
)

# IMPORTANT: FREE TEXT CAREER INPUT

career_goal = st.text_input(
    "Enter any career you are interested in",
    placeholder="Example: Teacher, Doctor, Nurse, Lawyer, Software Tester"
)

if not career_goal.strip():
    st.info("Please enter a career name to explore your career guidance.")
    st.stop()

career_key = career_goal.strip().lower()

if career_key in CAREERS:
    profile = CAREERS[career_key]
else:
    profile = create_profile(career_goal)

st.success("Career selected: " + career_goal.title())

st.divider()

FEATURES = [
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

feature = st.selectbox(
    "Choose a Feature",
    FEATURES
)


def show_list(title, items, icon="✅"):
    st.subheader(title)

    for item in items:
        st.write(icon, item)


# 1. SKILLS DISCOVERY

if feature == "Skills Discovery":
    st.header("🔍 Skills Discovery")

    show_list("Skills required for " + career_goal, profile["skills"])
    show_list("Skills to improve", profile["improve"], "🎯")


# 2. CAREER RECOMMENDATION

elif feature == "Career Recommendation":
    st.header("💡 Career Recommendation")

    st.write("Career selected: **" + career_goal.title() + "**")
    st.write("Career category: " + profile["category"])

    show_list("Recommended skills", profile["skills"])
    show_list("Suggested improvement areas", profile["improve"])


# 3. DREAM JOB PREPARATION

elif feature == "Dream Job Preparation":
    st.header("🎯 Dream Job Preparation")

    st.write("Preparation plan for: **" + career_goal.title() + "**")

    for i, step in enumerate(profile["steps"], 1):
        st.write(str(i) + ". " + step)


# 4. CAREER REPORT

elif feature == "Career Report":
    st.header("📄 Career Report")

    st.write("Candidate:", name if name else "Not entered")
    st.write("Career:", career_goal.title())
    st.write("Category:", profile["category"])

    show_list("Core Skills", profile["skills"])
    show_list("Skills to Improve", profile["improve"])
    show_list("Preparation Roadmap", profile["steps"], "➡️")


# 5. RESUME ANALYZER

elif feature == "Resume Analyzer":
    st.header("📑 Resume Analyzer")

    uploaded = st.file_uploader(
        "Upload your resume",
        type=["pdf", "docx"]
    )

    if uploaded is not None:
        try:
            resume_text = ""

            if uploaded.name.lower().endswith(".pdf"):
                reader = PdfReader(uploaded)

                for page in reader.pages:
                    resume_text += (page.extract_text() or "") + " "

            else:
                doc = Document(uploaded)
                resume_text = " ".join(
                    paragraph.text for paragraph in doc.paragraphs
                )

            text_lower = resume_text.lower()

            all_skills = list(
                dict.fromkeys(profile["skills"] + GENERAL_SKILLS)
            )

            found = [
                skill for skill in all_skills
                if skill.lower() in text_lower
            ]

            missing = [
                skill for skill in profile["skills"]
                if skill.lower() not in text_lower
            ]

            score = int(
                100 * len(found) / max(1, len(all_skills))
            )

            show_list("Skills Found", found or ["No matching skills detected"])
            show_list("Skills to Improve", missing, "➕")

            st.metric("Resume Keyword Match", str(score) + "%")
            st.progress(score)

            st.caption(
                "This is a basic keyword check, not a prediction of hiring chances."
            )

        except Exception as error:
            st.error("Unable to read the resume: " + str(error))


# 6. INTERVIEW PREPARATION

elif feature == "Interview Preparation":
    st.header("🎤 Interview Preparation")

    st.write("Practice questions for " + career_goal.title())

    for question, answer in profile["questions"]:
        with st.expander(question):
            st.write("Sample Answer:")
            st.write(answer)

    st.subheader("HR Questions")

    hr_questions = [
        "Tell me about yourself.",
        "Why are you interested in this career?",
        "What are your strengths?",
        "How do you handle challenges?"
    ]

    for question in hr_questions:
        with st.expander(question):
            st.write(
                "Prepare an honest answer using your education, skills and experience."
            )


# 7. JOB READINESS SCORE

elif feature == "Job Readiness Score":
    st.header("🚀 Job Readiness Score")

    technical = st.slider(
        "Rate your career-related skills",
        0, 100, 50
    )

    resume = st.radio(
        "Is your resume ready?",
        ["Yes", "Needs Improvement"],
        horizontal=True
    )

    interview = st.radio(
        "Are you interview-ready?",
        ["Yes", "Not Yet"],
        horizontal=True
    )

    experience = st.radio(
        "Do you have practical experience?",
        ["Yes", "Not Yet"],
        horizontal=True
    )

    if st.button("Calculate Readiness"):
        resume_score = 100 if resume == "Yes" else 40
        interview_score = 100 if interview == "Yes" else 40
        experience_score = 100 if experience == "Yes" else 40

        total = int(
            (technical + resume_score + interview_score + experience_score) / 4
        )

        st.metric("Estimated Job Readiness", str(total) + "%")
        st.progress(total)

        if total >= 75:
            st.success("Good progress! Continue practicing.")
        elif total >= 50:
            st.info("You are building your foundation. Keep improving.")
        else:
            st.warning("Focus on basic skills and practical learning first.")


# 8. JOB RECOMMENDATION

elif feature == "Job Recommendation":
    st.header("💼 Job Recommendation")

    show_list("Career-related skills", profile["skills"])
    show_list("Possible workplaces", profile["companies"], "🏢")

    st.info(
        "Check official company websites for current vacancies and eligibility."
    )


# 9. AI CAREER ROADMAP

elif feature == "AI Career Roadmap":
    st.header("🗺️ AI Career Roadmap")

    for i, step in enumerate(profile["steps"], 1):
        st.write("Level " + str(i) + ": " + step)


# 10. CAREER PROGRESS TRACKER

elif feature == "AI Career Progress Tracker":
    st.header("📈 Career Progress Tracker")

    completed = []

    for i, step in enumerate(profile["steps"]):
        if st.checkbox(step, key="progress_" + str(i)):
            completed.append(step)

    total_steps = len(profile["steps"])
    percentage = int(100 * len(completed) / max(1, total_steps))

    st.metric(
        "Completed Steps",
        str(len(completed)) + " / " + str(total_steps)
    )

    st.progress(percentage)


# 11. SKILL GAP ANALYZER

elif feature == "Personalized Skill Gap Analyzer":
    st.header("🧩 Personalized Skill Gap Analyzer")

    known = []

    for i, skill in enumerate(profile["skills"]):
        if st.checkbox(skill, key="skill_" + str(i)):
            known.append(skill)

    if st.button("Analyze My Skill Gap"):
        missing = [
            skill for skill in profile["skills"]
            if skill not in known
        ]

        show_list("Skills You Know", known or ["No skills selected"])
        show_list("Skills to Learn", missing, "📌")
        show_list("Additional Improvement Areas", profile["improve"], "🎯")


# 12. AI INTERVIEW EVALUATION

elif feature == "AI Interview Evaluation":
    st.header("📝 AI Interview Evaluation")

    questions = [
        question for question, answer in profile["questions"]
    ]

    questions += [
        "Tell me about yourself.",
        "Why should we select you?"
    ]

    question = st.selectbox(
        "Choose an interview question",
        questions
    )

    answer = st.text_area(
        "Type your answer",
        height=150
    )

    if st.button("Evaluate My Answer"):
        words = len(answer.split())

        if words == 0:
            st.warning("Please type your answer first.")
        else:
            st.metric("Answer Word Count", words)

            if words < 20:
                st.info("Add more detail and one example.")
            elif words <= 120:
                st.success("Good answer length. Check clarity and relevance.")
            else:
                st.info("Try making your answer shorter and more focused.")

            st.write("Self-review:")
            st.write("- Did you answer the question?")
            st.write("- Did you give an example?")
            st.write("- Was your answer clear?")


# 13. CAREER ANALYTICS DASHBOARD

elif feature == "Career Analytics Dashboard":
    st.header("📊 Career Analytics Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Core Skills", len(profile["skills"]))
    col2.metric("Roadmap Steps", len(profile["steps"]))
    col3.metric("Interview Questions", len(profile["questions"]))

    show_list("Focus Areas", profile["improve"], "🎯")


# 14. DOWNLOAD CAREER REPORT

elif feature == "Download Career Report":
    st.header("⬇️ Download Career Report")

    report_lines = [
        "CAREER TWIN AI - CAREER REPORT",
        "Candidate: " + (name if name else "Not entered"),
        "Date: " + date.today().isoformat(),
        "Career Goal: " + career_goal.title(),
        "Category: " + profile["category"],
        "",
        "CORE SKILLS:"
    ]

    report_lines += [
        "- " + item for item in profile["skills"]
    ]

    report_lines += ["", "SKILLS TO IMPROVE:"]

    report_lines += [
        "- " + item for item in profile["improve"]
    ]

    report_lines += ["", "CAREER ROADMAP:"]

    report_lines += [
        str(i) + ". " + step
        for i, step in enumerate(profile["steps"], 1)
    ]

    report_lines += ["", "INTERVIEW QUESTIONS:"]

    report_lines += [
        "- " + question
        for question, answer in profile["questions"]
    ]

    report_text = "\n".join(report_lines)

    st.text_area(
        "Report Preview",
        report_text,
        height=350
    )

    st.download_button(
        "📥 Download Career Report",
        data=report_text,
        file_name="career_twin_report.txt",
        mime="text/plain"
    )


st.divider()

st.caption(
    "Career Twin AI 🚀 | Explore your future, one step at a time"
)

import streamlit as st

try:
    from PyPDF2 import PdfReader
except ImportError:
    PdfReader = None

try:
    from docx import Document
except ImportError:
    Document = None

st.set_page_config(page_title="CareerTwin AI", page_icon="🎯", layout="wide")

CAREER_OPTIONS = [
    "Software Developer", "Data Analyst", "UI/UX Designer", "Web Developer",
    "AI / ML Engineer", "Software Tester", "Doctor", "Teacher", "Nurse"
]

CAREER_SKILLS = {
    "Software Developer": ["Python", "Java", "SQL", "Data Structures", "Problem Solving", "Git"],
    "Data Analyst": ["Python", "SQL", "Excel", "Power BI", "Statistics", "Data Visualization"],
    "UI/UX Designer": ["Figma", "Wireframing", "Prototyping", "User Research", "Typography"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "React", "Python", "Git"],
    "AI / ML Engineer": ["Python", "Statistics", "Machine Learning", "Pandas", "NumPy", "Deep Learning"],
    "Software Tester": ["Manual Testing", "Test Cases", "Bug Reporting", "SDLC", "STLC", "SQL", "Selenium"],
    "Doctor": ["Biology", "Anatomy", "Physiology", "Clinical Skills", "Communication", "Patient Care"],
    "Teacher": ["Subject Knowledge", "Lesson Planning", "Communication", "Classroom Management", "Assessment"],
    "Nurse": ["Patient Care", "Anatomy", "First Aid", "Communication", "Clinical Skills", "Medical Terminology"],
}

ROADMAPS = {
    "Software Developer": ["Learn Python or Java fundamentals", "Practise problem solving and data structures", "Learn SQL, Git and APIs", "Build 2–3 projects", "Prepare for technical interviews"],
    "Data Analyst": ["Learn Excel and data cleaning", "Learn SQL", "Practise Python with Pandas", "Create Power BI dashboards", "Build a portfolio using datasets"],
    "UI/UX Designer": ["Learn design principles", "Practise Figma", "Create wireframes and prototypes", "Study user research", "Build a case-study portfolio"],
    "Web Developer": ["Learn HTML and CSS", "Learn JavaScript", "Build responsive pages", "Learn React and APIs", "Deploy projects"],
    "AI / ML Engineer": ["Strengthen Python", "Learn statistics and linear algebra basics", "Practise Pandas and NumPy", "Study machine learning", "Build ML projects"],
    "Software Tester": ["Understand SDLC and STLC", "Learn test scenarios and test cases", "Practise functional and regression testing", "Learn SQL and API testing basics", "Explore Selenium"],
    "Doctor": ["Complete the required science education", "Prepare for and qualify the relevant medical entrance examination", "Complete an approved medical degree", "Complete required clinical training and registration", "Pursue a medical specialty"],
    "Teacher": ["Choose your subject and education level", "Complete the required degree", "Complete required teacher training or eligibility exams", "Practise lesson planning", "Build teaching experience"],
    "Nurse": ["Complete an approved nursing qualification", "Build anatomy and patient-care knowledge", "Complete supervised clinical practice", "Meet registration and licensing requirements", "Develop specialty-care skills"],
}

INTERVIEW_QA = {
    "Software Developer": [("What is a variable?", "A variable is a named place used to store a value."), ("What is OOP?", "Object-Oriented Programming organizes code using classes and objects."), ("What is SQL?", "SQL is used to manage data in relational databases.")],
    "Data Analyst": [("What does a data analyst do?", "A data analyst studies data to support decisions."), ("What is data cleaning?", "It is correcting missing, duplicate or incorrect data."), ("What is a dashboard?", "A dashboard presents information using visuals and metrics.")],
    "UI/UX Designer": [("What is UI?", "UI means User Interface, the visual parts a person interacts with."), ("What is UX?", "UX means User Experience, how easy and useful a product is."), ("What is a wireframe?", "A wireframe is a basic layout of a screen.")],
    "Web Developer": [("What is HTML?", "HTML gives structure to a web page."), ("What is CSS?", "CSS controls a web page's appearance."), ("What is JavaScript?", "JavaScript adds interactivity to web pages.")],
    "AI / ML Engineer": [("What is AI?", "AI enables computer systems to perform tasks that normally need human intelligence."), ("What is machine learning?", "Machine learning helps systems learn patterns from data."), ("What is a dataset?", "A dataset is a collection of related data.")],
    "Software Tester": [("What is software testing?", "Testing checks whether software works as expected and helps find defects."), ("What is a test case?", "A test case contains steps, input and expected results."), ("What is regression testing?", "It checks that changes have not broken existing features.")],
    "Doctor": [("Why is communication important in healthcare?", "It helps doctors understand patients and explain care clearly."), ("What is preventive healthcare?", "It means preventing illness or detecting it early."), ("Why is patient confidentiality important?", "It protects private medical information.")],
    "Teacher": [("What makes an effective teacher?", "Clear communication, subject knowledge, patience and student engagement."), ("What is a lesson plan?", "It outlines learning goals, activities and assessment."), ("How can you support different learners?", "Use varied explanations and activities, and check understanding.")],
    "Nurse": [("What is patient-centred care?", "It respects each patient's needs, preferences and dignity."), ("Why is hand hygiene important?", "It helps prevent the spread of infection."), ("Why are observation skills important?", "They help identify changes in a patient's condition.")],
}

def extract_resume_text(uploaded_file):
    if uploaded_file is None:
        return ""
    try:
        if uploaded_file.name.lower().endswith(".pdf"):
            if PdfReader is None:
                return "PyPDF2 package is not installed."
            reader = PdfReader(uploaded_file)
            return "\\n".join(page.extract_text() or "" for page in reader.pages)
        if uploaded_file.name.lower().endswith(".docx"):
            if Document is None:
                return "python-docx package is not installed."
            doc = Document(uploaded_file)
            return "\\n".join(p.text for p in doc.paragraphs)
        return "Please upload a PDF or DOCX file."
    except Exception as error:
        return f"Could not read the file: {error}"

st.title("🎯 CareerTwin AI")
st.caption("Developed by Avantika S | Final Year B.E. Computer Science Engineering")
st.subheader("Your AI-powered career planning companion")
st.write("Explore careers, discover skills, prepare for interviews and create your learning roadmap.")

name = st.text_input("Enter your name")

if not name.strip():
    st.info("Please enter your name to open your CareerTwin AI dashboard.")
else:
    st.success(f"Welcome, {name.strip()}!")
    st.markdown("### 📊 Your Career Dashboard")
    col1, col2, col3 = st.columns(3)
    col1.metric("Career paths", len(CAREER_OPTIONS))
    col2.metric("Career tools", "14")
    col3.metric("Your status", "Getting started")

    career_goal = st.selectbox("Choose your Career Goal", CAREER_OPTIONS)
    st.caption("Choose from technology, healthcare or education careers.")

    features = [
        "1. Skills Discovery", "2. Career Recommendation", "3. Dream Job Preparation",
        "4. Career Report", "5. Resume Analyzer", "6. Interview Preparation",
        "7. Job Readiness Score", "8. Job Recommendation", "9. AI Career Roadmap",
        "10. AI Career Progress Tracker", "11. Personalized Skill Gap Analyzer",
        "12. AI Interview Evaluation", "13. Career Analytics Dashboard",
        "14. Download Career Report"
    ]
    feature = st.selectbox("Select a Feature", features)
    st.divider()

    if feature == features[0]:
        st.header("🧠 Skills Discovery")
        selected = st.multiselect("Select the skills you already have", CAREER_SKILLS[career_goal])
        score = round(len(selected) / len(CAREER_SKILLS[career_goal]) * 100)
        st.metric("Skills match", f"{score}%")
        st.progress(score / 100)
        st.write("Skills to explore:", ", ".join(s for s in CAREER_SKILLS[career_goal] if s not in selected) or "You selected all listed skills.")

    elif feature == features[1]:
        st.header("💡 Career Recommendation")
        related = {
            "Software Developer": ["Backend Developer", "Application Developer", "Python Developer"],
            "Data Analyst": ["Business Analyst", "BI Analyst", "Data Associate"],
            "UI/UX Designer": ["UI Designer", "UX Researcher", "Product Designer"],
            "Web Developer": ["Frontend Developer", "Backend Developer", "Full Stack Developer"],
            "AI / ML Engineer": ["Machine Learning Engineer", "AI Associate", "Data Scientist"],
            "Software Tester": ["Manual Tester", "QA Analyst", "Automation Tester"],
            "Doctor": ["General Physician", "Paediatrician", "Medical Specialist"],
            "Teacher": ["School Teacher", "Online Tutor", "Subject Educator"],
            "Nurse": ["Staff Nurse", "Community Health Nurse", "Specialty Nurse"]
        }
        st.write(f"Related paths for **{career_goal}**:")
        for role in related[career_goal]:
            st.write("•", role)

    elif feature == features[2]:
        st.header("🌟 Dream Job Preparation")
        st.write(f"Preparation plan for **{career_goal}**:")
        for step in ["Understand the required qualifications and skills", "Learn the fundamentals through a structured course", "Practise and complete projects or supervised training", "Prepare your resume and practise explaining your skills", "Apply for suitable entry-level opportunities"]:
            st.write("•", step)
        st.info("For regulated professions such as Doctor and Nurse, follow approved qualification, registration and licensing requirements.")

    elif feature == features[3]:
        st.header("📄 Career Report")
        st.write("Name:", name)
        st.write("Career goal:", career_goal)
        st.write("Important skills:")
        for skill in CAREER_SKILLS[career_goal]:
            st.write("•", skill)

    elif feature == features[4]:
        st.header("📑 Resume Analyzer")
        resume = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
        if resume:
            resume_text = extract_resume_text(resume)
            st.text_area("Extracted resume text", resume_text, height=180)
            found = [s for s in CAREER_SKILLS[career_goal] if s.lower() in resume_text.lower()]
            missing = [s for s in CAREER_SKILLS[career_goal] if s not in found]
            st.write(f"Relevant skills found: {len(found)} / {len(CAREER_SKILLS[career_goal])}")
            st.write("Found:", ", ".join(found) if found else "No matching skills found.")
            st.write("Consider adding only skills you genuinely have:", ", ".join(missing) if missing else "No listed skill gaps.")

    elif feature == features[5]:
        st.header("🎤 Interview Preparation")
        selected_career = st.selectbox("Choose interview area", CAREER_OPTIONS, index=CAREER_OPTIONS.index(career_goal), key="interview")
        for question, answer in INTERVIEW_QA[selected_career]:
            with st.expander(question):
                st.write(answer)

    elif feature == features[6]:
        st.header("📈 Job Readiness Score")
        selected = st.multiselect("Skills you know", CAREER_SKILLS[career_goal], key="readiness")
        resume_ready = st.checkbox("I have an updated resume")
        project_ready = st.checkbox("I have completed a relevant project or practical training")
        interview_ready = st.checkbox("I have practised interview questions")
        total = round(len(selected) / len(CAREER_SKILLS[career_goal]) * 70) + (10 if resume_ready else 0) + (10 if project_ready else 0) + (10 if interview_ready else 0)
        st.metric("Your readiness score", f"{total}/100")
        st.progress(total / 100)
        st.caption("This is a self-assessment guide, not a hiring result.")

    elif feature == features[7]:
        st.header("💼 Job Recommendation")
        interest = st.selectbox("Select your interest", ["Software Development", "Data Analytics", "UI/UX Design", "Web Development", "Artificial Intelligence", "Software Testing", "Healthcare", "Education"])
        jobs = {
            "Software Development": ["Junior Software Developer", "Python Developer"],
            "Data Analytics": ["Junior Data Analyst", "BI Trainee"],
            "UI/UX Design": ["UI/UX Design Intern", "Junior UI Designer"],
            "Web Development": ["Frontend Developer Trainee", "Web Developer"],
            "Artificial Intelligence": ["AI/ML Intern", "Junior Data Associate"],
            "Software Testing": ["Manual Testing Trainee", "QA Analyst Trainee"],
            "Healthcare": ["Explore approved Doctor or Nurse qualification pathways"],
            "Education": ["Teaching Assistant", "Tutor", "Teacher (with required qualifications)"]
        }
        st.write("Suggested roles:")
        for job in jobs[interest]:
            st.write("•", job)
        st.caption("Check employer eligibility and official qualification requirements.")

    elif feature == features[8]:
        st.header("🗺️ AI Career Roadmap")
        selected_career = st.selectbox("Choose a career", CAREER_OPTIONS, index=CAREER_OPTIONS.index(career_goal), key="roadmap")
        for i, step in enumerate(ROADMAPS[selected_career], 1):
            st.write(f"**Step {i}:** {step}")

    elif feature == features[9]:
        st.header("📍 AI Career Progress Tracker")
        selected_career = st.selectbox("Career to track", CAREER_OPTIONS, index=CAREER_OPTIONS.index(career_goal), key="tracker")
        progress = st.slider("How much of your learning plan have you completed?", 0, 100, 0)
        st.progress(progress / 100)
        st.metric(f"{selected_career} progress", f"{progress}%")

    elif feature == features[10]:
        st.header("🔍 Personalized Skill Gap Analyzer")
        selected_career = st.selectbox("Choose a career", CAREER_OPTIONS, index=CAREER_OPTIONS.index(career_goal), key="gapcareer")
        known = st.multiselect("Select skills you already know", CAREER_SKILLS[selected_career], key="gapskills")
        gaps = [s for s in CAREER_SKILLS[selected_career] if s not in known]
        st.write("Your strengths:", ", ".join(known) if known else "Select the skills you know.")
        st.write("Skills to develop:", ", ".join(gaps) if gaps else "You selected all listed skills.")

    elif feature == features[11]:
        st.header("📝 AI Interview Evaluation")
        selected_career = st.selectbox("Choose interview area", CAREER_OPTIONS, index=CAREER_OPTIONS.index(career_goal), key="evaluation")
        question, sample = INTERVIEW_QA[selected_career][0]
        st.write("**Question:**", question)
        answer = st.text_area("Type your answer")
        if st.button("Evaluate my answer"):
            if len(answer.strip()) < 20:
                st.warning("Please write a little more so you can review your answer.")
            else:
                st.success("Answer submitted for self-review.")
                st.write("Compare your answer with these key points:")
                st.info(sample)
                st.caption("This is a basic practice aid, not a professional interview score.")

    elif feature == features[12]:
        st.header("📊 Career Analytics Dashboard")
        st.write("Your selected career:", career_goal)
        st.metric("Skills listed", len(CAREER_SKILLS[career_goal]))
        st.metric("Roadmap steps", len(ROADMAPS[career_goal]))
        st.write("Use Skills Discovery, Skill Gap Analyzer and Progress Tracker to monitor your preparation.")

    elif feature == features[13]:
        st.header("⬇️ Download Career Report")
        report = f"""CAREERTWIN AI - CAREER REPORT
Name: {name}
Career Goal: {career_goal}

Suggested Skills:
{chr(10).join('- ' + skill for skill in CAREER_SKILLS[career_goal])}

Career Roadmap:
{chr(10).join(str(i + 1) + '. ' + step for i, step in enumerate(ROADMAPS[career_goal]))}

Note: This report is for learning guidance. Follow official qualification and licensing rules for regulated professions.
"""
        st.download_button("Download Career Report", data=report, file_name="CareerTwin_AI_Report.txt", mime="text/plain")
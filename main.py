import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
from datetime import date

# =========================================================
# CAREER TWIN AI - UNIVERSAL CAREER GUIDANCE
# =========================================================

st.set_page_config(page_title="Career Twin AI", page_icon="🚀", layout="wide")

CAREERS = {
    "software developer": {
        "category": "Technology",
        "skills": ["Python or Java", "Problem solving", "Data structures", "SQL", "Git and GitHub", "OOP"],
        "improve": ["DSA practice", "APIs", "Project development"],
        "steps": [
            "Learn Python or Java fundamentals",
            "Practice variables, loops, functions and OOP",
            "Learn SQL and database basics",
            "Study data structures and algorithms",
            "Build 2-3 practical applications",
            "Use Git and GitHub",
            "Prepare resume and interview"
        ],
        "questions": [
            ("What is OOP?", "OOP is a programming approach based on classes and objects."),
            ("What is a variable?", "A variable is a named place used to store a value."),
            ("What is SQL?", "SQL is a language used to manage and query relational databases."),
            ("What is Git?", "Git is a version control system used to track code changes."),
            ("What is an API?", "An API allows different software applications to communicate.")
        ],
        "companies": ["TCS", "Infosys", "Wipro", "Accenture", "IBM"]
    },

    "data analyst": {
        "category": "Technology and Analytics",
        "skills": ["Excel", "SQL", "Python", "Statistics", "Power BI or Tableau", "Data visualization"],
        "improve": ["Advanced SQL", "Dashboard building", "Business communication"],
        "steps": [
            "Learn Excel and spreadsheets",
            "Study basic statistics",
            "Learn SQL",
            "Learn Python basics and Pandas",
            "Create dashboards using Power BI or Tableau",
            "Practice with real datasets",
            "Build a portfolio and prepare for interviews"
        ],
        "questions": [
            ("What is data analysis?", "It is the process of examining data to find useful information."),
            ("What is a dataset?", "A dataset is an organized collection of related data."),
            ("What is data visualization?", "It presents information through charts, graphs and dashboards."),
            ("What is SQL used for?", "SQL is used to retrieve and manage data in databases.")
        ],
        "companies": ["TCS", "Infosys", "Accenture", "Deloitte", "IBM"]
    },

    "ui/ux designer": {
        "category": "Design",
        "skills": ["Design principles", "Figma", "Wireframing", "Prototyping", "User research", "Communication"],
        "improve": ["Usability testing", "Portfolio", "Design systems"],
        "steps": [
            "Understand UI and UX fundamentals",
            "Learn layout, color and typography",
            "Learn Figma",
            "Create wireframes and prototypes",
            "Conduct basic user research",
            "Redesign an existing app as a case study",
            "Build a portfolio and prepare for interviews"
        ],
        "questions": [
            ("What is UI?", "UI means User Interface: the visual parts of a digital product."),
            ("What is UX?", "UX means User Experience: how people feel when using a product."),
            ("What is a wireframe?", "A wireframe is a simple layout showing a page structure."),
            ("What is usability?", "Usability describes how easily people can use a product.")
        ],
        "companies": ["Accenture", "TCS", "Infosys", "IBM"]
    },

    "web developer": {
        "category": "Technology",
        "skills": ["HTML", "CSS", "JavaScript", "Responsive design", "Git", "APIs"],
        "improve": ["React", "Backend basics", "Web security"],
        "steps": [
            "Learn HTML structure",
            "Style pages using CSS",
            "Learn JavaScript",
            "Build responsive webpages",
            "Learn Git and GitHub",
            "Understand APIs and a backend framework",
            "Build and deploy projects",
            "Prepare your portfolio and interview"
        ],
        "questions": [
            ("What is HTML?", "HTML defines the structure of a webpage."),
            ("What is CSS?", "CSS controls the presentation and layout of webpages."),
            ("What is JavaScript?", "JavaScript adds logic and interactivity to webpages."),
            ("What is responsive design?", "It makes a website adapt to different screen sizes.")
        ],
        "companies": ["TCS", "Wipro", "Infosys", "HCLTech", "Accenture"]
    },

    "ai / ml engineer": {
        "category": "Technology",
        "skills": ["Python", "Statistics", "Linear algebra", "SQL", "Machine learning", "Data preparation"],
        "improve": ["Deep learning", "Model evaluation", "Deployment"],
        "steps": [
            "Strengthen Python",
            "Learn statistics and basic linear algebra",
            "Practice data cleaning with Pandas",
            "Study machine-learning fundamentals",
            "Train and evaluate simple models",
            "Build end-to-end projects",
            "Learn model deployment and prepare for interviews"
        ],
        "questions": [
            ("What is AI?", "AI is the field of creating systems that perform tasks requiring human-like intelligence."),
            ("What is machine learning?", "Machine learning enables systems to learn patterns from data."),
            ("What is a dataset?", "A dataset is a collection of examples used for analysis or model training.")
        ],
        "companies": ["IBM", "TCS", "Infosys", "Accenture"]
    },

    "software tester": {
        "category": "Technology and Quality Assurance",
        "skills": ["Manual testing", "SDLC", "STLC", "Test cases", "Bug reporting", "SQL", "Jira"],
        "improve": ["API testing", "Automation basics", "Agile methodology"],
        "steps": [
            "Understand SDLC and STLC",
            "Learn testing types and testing levels",
            "Write test scenarios and test cases",
            "Practice reporting bugs with clear steps",
            "Learn basic SQL",
            "Try API testing with Postman",
            "Understand Agile and Jira",
            "Practice interviews and build a testing portfolio"
        ],
        "questions": [
            ("What is software testing?", "It is the process of checking software to find defects and verify requirements."),
            ("What is a test case?", "A test case contains steps, test data and expected results for checking a feature."),
            ("What is a bug?", "A bug is a defect where actual software behavior differs from expected behavior."),
            ("What is regression testing?", "It checks that changes have not broken existing functionality."),
            ("What is the difference between verification and validation?", "Verification checks whether the product is built correctly; validation checks whether the right product is built.")
        ],
        "companies": ["TCS", "Wipro", "Infosys", "Accenture", "Capgemini"]
    },
    "doctor": {
        "category": "Healthcare",
        "skills": ["Biology and medical knowledge", "Clinical reasoning", "Patient communication",
                   "Ethics", "Decision making", "Teamwork"],
        "improve": ["Clinical experience", "Communication", "Continuing medical education"],
        "steps": ["Complete the required school science subjects", "Qualify for the relevant medical entrance process in your country",
                  "Complete an accredited medical degree", "Complete required clinical rotations and supervised training",
                  "Meet licensing or registration requirements", "Consider specialization and ongoing professional development"],
        "questions": [("Why is patient confidentiality important?", "It protects patient privacy and helps maintain trust."),
                      ("What is a differential diagnosis?", "It is a list of possible conditions that could explain a patient's symptoms."),
                      ("Why is communication important in healthcare?", "It helps patients understand care and supports safe decisions.")],
        "companies": ["Hospitals", "Clinics", "Public health organizations", "Medical research institutions"]
    },
    "teacher": {
        "category": "Education",
        "skills": ["Subject knowledge", "Lesson planning", "Classroom management",
                   "Communication", "Assessment", "Patience"],
        "improve": ["Digital teaching tools", "Inclusive teaching", "Assessment design"],
        "steps": ["Choose the subject and age group you want to teach", "Complete the required degree",
                  "Complete teacher training or certification required in your region",
                  "Practice lesson planning and classroom communication", "Gain supervised teaching experience",
                  "Prepare a teaching portfolio and apply to schools"],
        "questions": [("How do you support a student who is struggling?", "Identify the learning difficulty, explain in different ways and monitor progress."),
                      ("Why is lesson planning important?", "It gives a clear learning goal, sequence and way to assess understanding."),
                      ("How do you manage a classroom?", "Set clear expectations, build respect and respond consistently.")],
        "companies": ["Schools", "Colleges", "Training institutes", "Education organizations"]
    },
    "nurse": {
        "category": "Healthcare",
        "skills": ["Patient care", "Clinical observation", "Communication", "Medical documentation",
                   "Infection control", "Teamwork"],
        "improve": ["Clinical practice", "Emergency response", "Patient education"],
        "steps": ["Research accredited nursing courses in your region", "Complete the required nursing education",
                  "Complete supervised clinical placements", "Meet registration or licensing requirements",
                  "Develop patient-care and communication skills", "Apply to hospitals or healthcare providers"],
        "questions": [("Why is hand hygiene important?", "It reduces the spread of infection."),
                      ("What are vital signs?", "Common vital signs include temperature, pulse, respiration and blood pressure."),
                      ("How do you communicate with an anxious patient?", "Listen calmly, explain procedures clearly and show empathy.")],
        "companies": ["Hospitals", "Clinics", "Community health services", "Care organizations"]
    },
    "lawyer": {
        "category": "Law",
        "skills": ["Legal research", "Reading and writing", "Critical thinking", "Public speaking",
                   "Negotiation", "Ethics"],
        "improve": ["Courtroom advocacy", "Drafting", "Specialized legal knowledge"],
        "steps": ["Understand the legal education route in your country", "Complete an accredited law degree",
                  "Develop legal research and drafting skills", "Gain internships or supervised practical experience",
                  "Meet bar admission or licensing requirements", "Build expertise in an area of law"],
        "questions": [("Why is legal ethics important?", "It protects clients, the justice system and public trust."),
                      ("What is a legal precedent?", "It is an earlier court decision that may guide later cases."),
                      ("Why is legal research important?", "It helps identify applicable laws, rules and prior decisions.")],
        "companies": ["Law firms", "Corporate legal departments", "Courts and public legal services", "Legal aid organizations"]
    }
}

GENERAL_SKILLS = ["Communication", "Problem solving", "Time management", "Teamwork",
                  "Domain knowledge", "Digital literacy", "Critical thinking", "Adaptability"]

def get_profile(career):
    key = career.strip().lower()
    if key in CAREERS:
        return CAREERS[key]
    return {
        "category": "Career-specific field",
        "skills": ["Core subject knowledge in " + career, "Communication",
                   "Problem solving", "Digital literacy", "Teamwork", "Time management"],
        "improve": ["Practical experience in " + career, "Professional certification where required",
                    "Portfolio or evidence of relevant work"],
        "steps": ["Research the education and entry requirements for " + career,
                  "Learn the core knowledge and skills required in this field",
                  "Choose a recognized course, degree or training route where needed",
                  "Gain practical experience through projects, volunteering, placements or supervised work",
                  "Build evidence of your skills and seek feedback from professionals",
                  "Prepare a role-specific resume and practice interviews",
                  "Apply to suitable entry-level opportunities and continue learning"],
        "questions": [
            ("Why are you interested in " + career + "?", "Explain your genuine interest and connect it to the work this career involves."),
            ("What skills are important in " + career + "?", "Mention relevant subject knowledge, communication, problem solving and practical skills."),
            ("How do you handle a difficult situation?", "Explain the situation, the action you took and the result."),
            ("How do you keep learning?", "Describe courses, practice, feedback and how you stay updated.")
        ],
        "companies": ["Relevant employers in the " + career + " field",
                      "Organizations offering entry-level roles or training in " + career]
    }

def show_list(title, items, icon="✅"):
    st.subheader(title)
    for item in items:
        st.write(f"{icon} {item}")

# HEADER AND PROFILE
st.title("🚀 Career Twin AI")
st.subheader("Explore your skills • Plan your career • Prepare for opportunities")
st.caption("A beginner-friendly career guidance demo. Guidance is general and should be checked against official course, licensing and job requirements.")

name = st.text_input("Enter your name", placeholder="Your name")
if not name.strip():
    st.info("Enter your name to open your Career Twin dashboard.")
    st.stop()

st.success(f"Welcome {name}! 👋")
st.header("📊 Career Dashboard")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Skill Score", "80%")
c2.metric("Resume", "Ready to review")
c3.metric("Interview", "Practice available")
c4.metric("Job Readiness", "Starter estimate")

st.subheader("🎯 Your Dream Career")
career_goal = st.text_input(
    "Enter any career you are interested in",
    value=st.session_state.get("career_goal", "Software Tester"),
    placeholder="Example: Doctor, Teacher, Nurse, Lawyer, Software Tester"
)
st.session_state["career_goal"] = career_goal
if not career_goal.strip():
    st.warning("Enter a career name to personalize the guidance.")
    st.stop()

profile = get_profile(career_goal)
st.info(f"Your selected career: **{career_goal}**  |  Field: **{profile['category']}**")

st.subheader("📈 Career Preparation Progress")
p1, p2, p3, p4 = st.columns(4)
p1.write("Skills"); p1.progress(70)
p2.write("Resume"); p2.progress(50)
p3.write("Interview"); p3.progress(40)
p4.write("Practical experience"); p4.progress(30)

feature = st.selectbox("Choose a feature", [
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
])

# 1. SKILLS DISCOVERY
if feature == "Skills Discovery":
    st.header("🧠 Skills Discovery")
    st.write(f"Select the skills you already have for **{career_goal}**.")
    selected = []
    cols = st.columns(2)
    for i, skill in enumerate(profile["skills"] + GENERAL_SKILLS[:4]):
        with cols[i % 2]:
            if st.checkbox(skill, key="discover_" + str(i)):
                selected.append(skill)
    if st.button("🔍 Discover My Skills"):
        score = int(100 * len(selected) / max(1, len(profile["skills"] + GENERAL_SKILLS[:4])))
        st.success("Your skills have been recorded.")
        show_list("Your selected skills", selected or ["No skills selected yet. Start learning one skill at a time."])
        st.metric("Self-reported skill coverage", f"{score}%")

# 2. CAREER RECOMMENDATION
elif feature == "Career Recommendation":
    st.header("🎯 Career Recommendation")
    interests = st.multiselect("What activities do you enjoy?", [
        "Helping people", "Teaching", "Solving problems", "Working with technology",
        "Analyzing information", "Designing", "Research", "Communication",
        "Working with children", "Healthcare", "Law and justice"
    ])
    if st.button("🚀 Recommend My Career"):
        mapping = {
            "Helping people": "Healthcare, education or community services",
            "Teaching": "Teaching and education",
            "Solving problems": "Technology, analytics, engineering or law",
            "Working with technology": "Software development, testing or IT",
            "Analyzing information": "Data analysis, research or finance",
            "Designing": "UI/UX, graphic or product design",
            "Research": "Research, science or analytics",
            "Communication": "Teaching, law, sales or public relations",
            "Working with children": "Teaching or child development",
            "Healthcare": "Healthcare and medical professions",
            "Law and justice": "Law and legal services"
        }
        if interests:
            st.success("Career areas to explore")
            for item in interests:
                st.write("•", mapping[item])
            st.caption("These are exploration ideas, not a formal aptitude assessment.")

# 3. DREAM JOB PREPARATION
elif feature == "Dream Job Preparation":
    st.header("💼 Dream Job Preparation")
    st.write(f"Your preparation plan for **{career_goal}**")
    show_list("Preparation Steps", profile["steps"], "📌")
    show_list("Important Skills", profile["skills"], "⭐")

# 4. CAREER REPORT
elif feature == "Career Report":
    st.header("📄 Career Report")
    st.write(f"Career report for **{career_goal}**")
    show_list("Required Skills", profile["skills"])
    show_list("Skills to Improve", profile["improve"], "🎯")
    # 5. RESUME ANALYZER
elif feature == "Resume Analyzer":
    st.header("📄 Resume Analyzer")
    uploaded_resume = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
    if uploaded_resume:
        resume_text = ""
        try:
            if uploaded_resume.name.endswith(".pdf"):
                reader = PdfReader(uploaded_resume)
                resume_text = "\n".join(page.extract_text() or "" for page in reader.pages)
            else:
                doc = Document(uploaded_resume)
                resume_text = "\n".join(p.text for p in doc.paragraphs)
            if resume_text.strip():
                st.success("Resume uploaded and text extracted.")
                st.write("Characters found:", len(resume_text))
                keywords = profile["skills"]
                found = [s for s in keywords if s.lower() in resume_text.lower()]
                missing = [s for s in keywords if s.lower() not in resume_text.lower()]
                show_list("Relevant skills found", found)
                show_list("Skills not found (consider adding only if you have them)", missing, "⚠️")
                st.info("Keep your resume truthful. Add only skills and experience you can explain.")
            else:
                st.warning("No readable text found. This may be a scanned PDF.")
        except Exception as e:
            st.error(f"Could not read the resume: {e}")

# 6. INTERVIEW PREPARATION
elif feature == "Interview Preparation":
    st.header("🎤 Interview Preparation")
    st.write(f"Practice questions for **{career_goal}**")
    for i, (question, answer) in enumerate(profile["questions"], 1):
        with st.expander(f"Question {i}: {question}"):
            st.write("**Sample answer:**", answer)
    st.subheader("Your practice answer")
    practice = st.text_area("Write your answer to an interview question")
    if st.button("Review My Answer"):
        if practice.strip():
            st.write("Your answer has been saved for this practice session.")
            st.write("Tip: Use a clear structure, give a specific example and keep your answer relevant.")
        else:
            st.warning("Please write an answer first.")

# 7. JOB READINESS SCORE
elif feature == "Job Readiness Score":
    st.header("📊 Job Readiness Score")
    st.write("Rate your current preparation honestly.")
    skill_rating = st.slider("Knowledge of required skills", 0, 10, 5)
    practical_rating = st.slider("Practical experience or projects", 0, 10, 3)
    communication_rating = st.slider("Communication skills", 0, 10, 5)
    resume_rating = st.slider("Resume preparation", 0, 10, 4)
    interview_rating = st.slider("Interview preparation", 0, 10, 3)
    if st.button("Calculate Readiness"):
        score = int((skill_rating + practical_rating + communication_rating + resume_rating + interview_rating) * 2)
        st.metric("Your self-assessed readiness", f"{score}/100")
        if score >= 75:
            st.success("Good preparation. Continue practicing and apply for suitable roles.")
        elif score >= 45:
            st.info("You are making progress. Focus on the areas with lower ratings.")
        else:
            st.warning("Start with fundamentals and build practical experience step by step.")

# 8. JOB RECOMMENDATION
elif feature == "Job Recommendation":
    st.header("💼 Job Recommendation")
    st.write(f"Explore entry-level opportunities related to **{career_goal}**.")
    show_list("Possible job titles", [
        f"Junior {career_goal}",
        f"{career_goal} Trainee",
        f"Entry-Level {career_goal}",
        f"{career_goal} Intern"
    ], "🔎")
    show_list("Organizations or employer types to research", profile["companies"], "🏢")
    st.info("Check official employer career pages for current vacancies, eligibility and location.")

# 9. AI CAREER ROADMAP
elif feature == "AI Career Roadmap":
    st.header("🗺️ Career Roadmap")
    st.write(f"Your learning roadmap for **{career_goal}**")
    for i, step in enumerate(profile["steps"], 1):
        st.write(f"**Step {i}:** {step}")
    st.subheader("Weekly learning target")
    weekly_hours = st.slider("Hours you can spend each week", 1, 30, 7)
    st.write(f"Your weekly learning target: **{weekly_hours} hours**")
    st.caption("Adjust the pace according to your studies and responsibilities.")

# 10. CAREER PROGRESS TRACKER
elif feature == "AI Career Progress Tracker":
    st.header("📈 Career Progress Tracker")
    st.write(f"Track your learning progress for **{career_goal}**.")
    completed = []
    for i, step in enumerate(profile["steps"]):
        if st.checkbox(step, key="progress_" + str(i)):
            completed.append(step)
    progress = len(completed) / max(1, len(profile["steps"]))
    st.progress(progress)
    st.metric("Completed roadmap steps", f"{len(completed)}/{len(profile['steps'])}")
    if progress == 1:
        st.success("Excellent! You marked every roadmap step complete.")
    else:
        st.info("Keep learning and update the checkboxes as you complete each step.")

# 11. PERSONALIZED SKILL GAP ANALYZER
elif feature == "Personalized Skill Gap Analyzer":
    st.header("🔍 Personalized Skill Gap Analyzer")
    st.write(f"Compare your current skills with skills suggested for **{career_goal}**.")
    current_skills = st.multiselect("Select the skills you already know", profile["skills"])
    gaps = [skill for skill in profile["skills"] if skill not in current_skills]
    if st.button("Analyze Skill Gaps"):
        show_list("Skills you already have", current_skills or ["No skills selected yet."])
        show_list("Skills to learn or improve", gaps, "🎯")
        if not gaps:
            st.success("You selected all the suggested skills. Continue practicing them.")

# 12. AI INTERVIEW EVALUATION
elif feature == "AI Interview Evaluation":
    st.header("📝 Interview Answer Evaluation")
    st.write(f"Practice an interview answer for **{career_goal}**.")
    question = st.text_input("Enter your interview question")
    answer = st.text_area("Enter your answer")
    if st.button("Evaluate Answer"):
        if answer.strip():
            score = min(100, 30 + len(answer.split()) * 2)
            st.metric("Basic answer-length score", f"{score}/100")
            st.write("**Improvement tips:**")
            st.write("- Answer the exact question.")
            st.write("- Include a relevant example.")
            st.write("- Explain your contribution or reasoning.")
            st.write("- Use simple and professional language.")
            st.caption("This is a simple rule-based practice score, not an AI assessment of answer quality.")
        else:
            st.warning("Please enter your answer.")

# 13. CAREER ANALYTICS DASHBOARD
elif feature == "Career Analytics Dashboard":
    st.header("📊 Career Analytics Dashboard")
    st.write(f"Preparation overview for **{career_goal}**.")
    st.metric("Suggested core skills", len(profile["skills"]))
    st.metric("Suggested roadmap steps", len(profile["steps"]))
    st.metric("Practice interview questions", len(profile["questions"]))
    st.subheader("Your preparation areas")
    areas = ["Skills", "Projects", "Resume", "Communication", "Interview"]
    values = [70, 40, 50, 60, 35]
    st.bar_chart({"Preparation (%)": values}, x=areas)
    st.caption("Illustrative dashboard values. They are not measured performance results.")

# 14. DOWNLOAD CAREER REPORT
elif feature == "Download Career Report":
    st.header("📥 Download Career Report")
    report = f"""
CAREER TWIN AI - CAREER REPORT

Name: {name}
Career Goal: {career_goal}
Career Field: {profile['category']}
Date: {date.today()}

REQUIRED SKILLS
{chr(10).join('- ' + s for s in profile['skills'])}

SKILLS TO IMPROVE
{chr(10).join('- ' + s for s in profile['improve'])}

CAREER ROADMAP
{chr(10).join(str(i + 1) + '. ' + s for i, s in enumerate(profile['steps']))}

INTERVIEW QUESTIONS
{chr(10).join(str(i + 1) + '. ' + q for i, (q, a) in enumerate(profile['questions']))}

POSSIBLE EMPLOYERS / ORGANIZATIONS
{chr(10).join('- ' + c for c in profile['companies'])}

Note: This is general career guidance. Verify official education,
licensing and job requirements for your location.
"""
    st.download_button(
        "⬇️ Download My Career Report",
        data=report,
        file_name="Career_Twin_Report.txt",
        mime="text/plain"
    )

st.divider()
st.caption("Career Twin AI | Explore your future, one step at a time.")

import streamlit as st
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Mujeeb Ahmed", layout="wide")

# ---------------- DETECT THEME ----------------
current_theme = st.get_option("theme.base")  # "light" or "dark"

if current_theme == "dark":
    TEXT_COLOR = "white"
    SUBTEXT_COLOR = "#94a3b8"
    CARD_BG = "rgba(255, 255, 255, 0.08)"
    BTN_TEXT = "white"
else:
    TEXT_COLOR = "black"
    SUBTEXT_COLOR = "#475569"
    CARD_BG = "rgba(0, 0, 0, 0.05)"
    BTN_TEXT = "black"

# ---------------- CUSTOM CSS ----------------
st.markdown(f"""
<style>
/* Page Width Control */
.block-container {{
    max-width: 1100px;
    padding-top: 3rem;
    padding-left: 2rem;
    padding-right: 2rem;
    margin: auto;
}}

/* Section spacing */
.section {{
    margin-top: 40px;
}}

/* Card Design */
.card {{
    background: {CARD_BG};
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0px 8px 30px rgba(0,0,0,0.3);
    transition: 0.3s;
    color: {TEXT_COLOR};
    margin-bottom: 25px;
}}

.card:hover {{
    transform: translateY(-8px);
}}

/* Titles */
.title {{
    font-size: 45px;
    font-weight: 700;
    color: {TEXT_COLOR};
}}

.subtitle {{
    font-size: 18px;
    color: {SUBTEXT_COLOR};
}}

/* Buttons */
.stButton>button {{
    background: linear-gradient(90deg, #22c55e, #4ade80);
    border-radius: 10px;
    padding: 10px 20px;
    border: none;
    color: {BTN_TEXT};
}}
</style>
""", unsafe_allow_html=True)

# ---------------- NAVIGATION ----------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("", ["Home", "About", "Skills", "Projects", "Teaching", "Contact"])

# ---------------- HOME ----------------
if page == "Home":
    st.markdown('<div class="section">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        st.image("profile.jpeg", width=250)

    with col2:
        st.markdown('<p class="title">Mujeeb Ahmed</p>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle">Python Developer | Data Science Graduate | Teacher</p>', unsafe_allow_html=True)
        st.write("""
        I am a passionate developer and educator specializing in Python and modern web technologies.
        I have completed my journey in Data Science and now focus on building high-quality applications
        and training students with real-world skills.
        """)
        st.success("Turning ideas into real-world applications")

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("---")

    # Cards Section
    st.markdown('<div class="section">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.markdown(f'<div class="card"><h3>💻 Development</h3><p>Building scalable apps using Flask & Streamlit.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="card"><h3>📊 Data Science</h3><p>Strong analytical and problem-solving skills.</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="card"><h3>👨‍🏫 Teaching</h3><p>Practical teaching approach for students.</p></div>', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- ABOUT ----------------
elif page == "About":
    st.markdown(f'<div class="section card">', unsafe_allow_html=True)
    st.title("About Me")
    st.write(f"""
    I am **Mujeeb Ahmed**, a passionate Python Developer, Data Science graduate, and Programming Instructor with a strong focus on building practical, real-world solutions.

    🎓 **Degree:** Data Science from **Sukkur IBA University**  
    💼 **Profession:** Programming Teacher & Developer

    My journey in technology began with curiosity and quickly turned into a mission to simplify programming for others. I specialize in Python development, data analysis, and web application design. My goal is to combine **practical development skills** with **teaching expertise** to make students industry-ready.

    **Key Highlights:**
    - ✅ Real-world project experience with Python and web technologies  
    - ✅ Strong foundation in Data Science and analytics  
    - ✅ Practical, project-based teaching methodology  
    - ✅ Expertise in Flask, Streamlit, and SQLite for scalable applications

    **Hobbies & Interests:**
    - Solving programming challenges and puzzles  
    - Exploring AI & Machine Learning trends  
    - Mentoring students and sharing knowledge  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- SKILLS ----------------
elif page == "Skills":
    st.title("Skills")
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Programming")
        st.write("Python"); st.progress(90)
        st.write("C++"); st.progress(75)
        st.write("JavaScript"); st.progress(70)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Web & Tools")
        st.write("HTML"); st.progress(85)
        st.write("CSS"); st.progress(75)
        st.write("Flask"); st.progress(85)
        st.write("Streamlit"); st.progress(90)
        st.write("SQLite"); st.progress(80)
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- PROJECTS ----------------
elif page == "Projects":
    st.title("Projects")
    st.markdown('<div class="section">', unsafe_allow_html=True)

    projects = [
        {
            "title": "Quiz System",
            "desc": "Complete quiz platform with admin panel, tracking results in Excel or database.",
            "tech": "Python, Flask, SQLite",
            "features": "Full CRUD, responsive UI, question sequencing, result tracking"
        },
        {
            "title": "AI Chatbot",
            "desc": "AI-powered chatbot with voice input and chat history using OpenAI APIs.",
            "tech": "Python, APIs",
            "features": "Voice input/output, persistent chat history, conversational AI"
        },
        {
            "title": "Portfolio Website",
            "desc": "Modern portfolio UI built with Streamlit, showcasing projects and teaching experience.",
            "tech": "Python, Streamlit, CSS",
            "features": "Responsive layout, interactive cards, internal CSS styling"
        },
        {
            "title": "Student Mini Projects",
            "desc": "Guided students to create calculators, web scrapers, and basic games.",
            "tech": "Python, C++, HTML/CSS, JavaScript",
            "features": "Hands-on learning, practical coding exercises, project mentorship"
        }
    ]

    for p in projects:
        st.markdown(f"""
        <div class="card">
            <h3>{p['title']}</h3>
            <p>{p['desc']}</p>
            <p><b>Tech Stack:</b> {p['tech']}</p>
            <p><b>Features:</b> {p['features']}</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- TEACHING ----------------
elif page == "Teaching":
    st.markdown('<div class="section card">', unsafe_allow_html=True)
    st.title("Teaching Experience")
    st.write("""
    I teach programming with a **practical and project-based approach**.

    **Subjects I Teach:**
    - Python Programming
    - C++ Programming
    - HTML & CSS
    - JavaScript
    - Data Science Fundamentals

    **My Teaching Approach:**
    - 🔹 Hands-on coding exercises  
    - 🔹 Project-based learning  
    - 🔹 Logical thinking & problem-solving focus  
    - 🔹 Mentorship on real projects
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- CONTACT ----------------
elif page == "Contact":
    st.title("Contact Me")
    st.markdown('<div class="section card">', unsafe_allow_html=True)

    st.write("📧 Email: ahmedalixy149@gmail.com")
    st.write("📱 Phone: +92 3180307822")
    st.write("🔗 LinkedIn: www.linkedin.com/in/mujeeb-ullah-a16555321")

    st.markdown("### Send Me a Message")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Send Message")

        if submit_button:
            if name.strip() == "" or email.strip() == "" or message.strip() == "":
                st.warning("Please fill in all fields before sending.")
            else:
                try:
                    import smtplib
                    from email.message import EmailMessage

                    # Create email
                    msg = EmailMessage()
                    msg['Subject'] = f"Portfolio Contact Form Message from {name}"
                    msg['From'] = os.environ.get("EMAIL_USER")
                    msg['To'] = os.environ.get("EMAIL_USER")
                    msg.set_content(f"Name: {name}\nEmail: {email}\nMessage:\n{message}")

                    # Send email
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                        smtp.login(os.environ.get("EMAIL_USER"), os.environ.get("EMAIL_PASSWORD"))
                        smtp.send_message(msg)

                    st.success("✅ Your message has been sent! I will contact you soon.")

                except Exception as e:
                    st.error(f"❌ Failed to send message. Error: {e}")

    st.markdown('</div>', unsafe_allow_html=True)

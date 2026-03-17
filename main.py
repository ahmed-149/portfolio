import streamlit as st
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Mujeeb Ahmed", layout="wide")

st.markdown("""
<style>

/* Layout */
.block-container {
    max-width: 1100px;
    padding-top: 3rem;
    padding-left: 2rem;
    padding-right: 2rem;
    margin: auto;
}

.section {
    margin-top: 40px;
}

/* ---------------- LIGHT MODE (DEFAULT) ---------------- */
.card {
    background: rgba(0, 0, 0, 0.05);
    color: black;
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0px 8px 30px rgba(0,0,0,0.1);
    margin-bottom: 25px;
    transition: 0.3s;
}

.title {
    font-size: 45px;
    font-weight: 700;
    color: black;
}

.subtitle {
    font-size: 18px;
    color: #475569;
}

/* ---------------- DARK MODE ---------------- */
@media (prefers-color-scheme: dark) {

    .card {
        background: rgba(255, 255, 255, 0.08);
        color: white;
        box-shadow: 0px 8px 30px rgba(0,0,0,0.5);
    }

    .title {
        color: white;
    }

    .subtitle {
        color: #94a3b8;
    }
}

/* Hover */
.card:hover {
    transform: translateY(-8px);
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #22c55e, #4ade80);
    border-radius: 10px;
    padding: 10px 20px;
    border: none;
}

</style>
""", unsafe_allow_html=True)

# ---------------- NAVIGATION ----------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("", ["Home", "About", "Skills", "Projects", "Teaching", "Contact"])

# ---------------- HOME ----------------
if page == "Home":
    col1, col2 = st.columns([1,2])

    with col1:
        st.image("profile.jpeg", width=250)

    with col2:
        st.markdown('<p class="title">Mujeeb Ahmed</p>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle">Python Developer | Data Science Graduate | Teacher</p>', unsafe_allow_html=True)

        st.write("""
        I am a passionate developer and educator specializing in Python and modern technologies.
        I focus on building real-world applications and training students with practical skills.
        """)

        st.success("Turning ideas into real-world applications")

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card"><h3>💻 Development</h3><p>Building apps using Flask & Streamlit.</p></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card"><h3>📊 Data Science</h3><p>Strong analytical & problem-solving skills.</p></div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card"><h3>👨‍🏫 Teaching</h3><p>Project-based learning approach.</p></div>', unsafe_allow_html=True)

# ---------------- ABOUT ----------------
elif page == "About":
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.title("About Me")
    st.write("""
    I am **Mujeeb Ahmed**, a passionate Python Developer and Programming Instructor.

    🎓 **Degree:** Data Science from **Sukkur IBA University**  
    💼 **Profession:** Teacher & Developer  

    I specialize in building practical applications and teaching students real-world skills.

    **Highlights:**
    - Real-world project experience  
    - Strong Data Science foundation  
    - Project-based teaching  
    - Flask & Streamlit expertise  
    """)

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- SKILLS ----------------
elif page == "Skills":
    col1, col2 = st.columns(2)

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
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- PROJECTS ----------------
elif page == "Projects":
    projects = [
        {
            "title": "Quiz System",
            "desc": "Complete quiz platform with admin panel and result tracking.",
        },
        {
            "title": "AI Chatbot",
            "desc": "Chatbot with voice input and intelligent responses.",
        },
        {
            "title": "Portfolio Website",
            "desc": "Modern UI portfolio built with Streamlit.",
        },
    ]

    for p in projects:
        st.markdown(f"""
        <div class="card">
            <h3>{p['title']}</h3>
            <p>{p['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------- TEACHING ----------------
elif page == "Teaching":
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.title("Teaching Experience")
    st.write("""
    I follow a **practical teaching approach**.

    **Subjects:**
    - Python
    - C++
    - Web Development
    - Data Science Basics

    **Method:**
    - Hands-on practice  
    - Real projects  
    - Problem-solving focus  
    """)

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- CONTACT ----------------
elif page == "Contact":
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.title("Contact Me")
    st.write("📧 Email: ahmedalixy149@gmail.com")
    st.write("📱 Phone: +92 3180307822")

    st.markdown("### Send Message")

    with st.form("form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        msg = st.text_area("Message")
        submit = st.form_submit_button("Send")

        if submit:
            try:
                import smtplib
                from email.message import EmailMessage

                email_msg = EmailMessage()
                email_msg['Subject'] = f"Message from {name}"
                email_msg['From'] = os.environ.get("EMAIL_USER")
                email_msg['To'] = os.environ.get("EMAIL_USER")
                email_msg.set_content(msg)

                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(os.environ.get("EMAIL_USER"), os.environ.get("EMAIL_PASSWORD"))
                    smtp.send_message(email_msg)

                st.success("Message Sent Successfully!")

            except Exception as e:
                st.error("Error sending message")

    st.markdown('</div>', unsafe_allow_html=True)

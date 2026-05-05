import streamlit as st
import os
import smtplib
from email.message import EmailMessage

# ─────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────
st.set_page_config(page_title="Mujeeb Ahmed", page_icon="⚡", layout="wide")

# ─────────────────────────────────────────
#  GLOBAL CSS  –  fully theme-aware
#  Uses Streamlit's own CSS variables so
#  text / backgrounds adapt to light & dark
# ─────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500;600;700&display=swap');

/* ── reset & base ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

/* force body font */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

/* hide default Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }

.block-container {
    max-width: 1080px;
    padding: 2.5rem 2rem 4rem;
    margin: auto;
}

/* ── colour tokens – auto light / dark ── */
:root {
    --accent: #22c55e;
    --accent2: #16a34a;
    --mono: 'Space Mono', monospace;
}

/* light defaults */
[data-theme="light"], .stApp {
    --bg-card: rgba(0,0,0,0.04);
    --border: rgba(0,0,0,0.10);
    --text-main: #0f172a;
    --text-muted: #475569;
    --tag-bg: #dcfce7;
    --tag-text: #15803d;
    --shadow: 0 4px 24px rgba(0,0,0,0.08);
    --shadow-hover: 0 12px 40px rgba(0,0,0,0.14);
    --progress-bg: #e2e8f0;
}

/* dark overrides */
@media (prefers-color-scheme: dark) {
    .stApp {
        --bg-card: rgba(255,255,255,0.06);
        --border: rgba(255,255,255,0.10);
        --text-main: #f1f5f9;
        --text-muted: #94a3b8;
        --tag-bg: rgba(34,197,94,0.15);
        --tag-text: #4ade80;
        --shadow: 0 4px 24px rgba(0,0,0,0.4);
        --shadow-hover: 0 12px 40px rgba(0,0,0,0.6);
        --progress-bg: #1e293b;
    }
}

/* Streamlit injects data-theme on <html> – catch it too */
[data-theme="dark"] .stApp,
.stApp[data-theme="dark"] {
    --bg-card: rgba(255,255,255,0.06);
    --border: rgba(255,255,255,0.10);
    --text-main: #f1f5f9;
    --text-muted: #94a3b8;
    --tag-bg: rgba(34,197,94,0.15);
    --tag-text: #4ade80;
    --shadow: 0 4px 24px rgba(0,0,0,0.4);
    --shadow-hover: 0 12px 40px rgba(0,0,0,0.6);
    --progress-bg: #1e293b;
}

/* ── card ── */
.card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 28px 32px;
    margin-bottom: 24px;
    box-shadow: var(--shadow);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.card:hover { transform: translateY(-6px); box-shadow: var(--shadow-hover); }

/* ── typography ── */
.hero-name {
    font-family: var(--mono);
    font-size: clamp(2.2rem, 5vw, 3.6rem);
    font-weight: 700;
    color: var(--text-main) !important;
    letter-spacing: -1px;
    line-height: 1.1;
}
.hero-role {
    font-size: 1.05rem;
    color: var(--accent);
    font-family: var(--mono);
    margin: 6px 0 14px;
    letter-spacing: 0.5px;
}
.hero-bio {
    font-size: 1rem;
    color: var(--text-muted) !important;
    line-height: 1.7;
    max-width: 480px;
}
.section-label {
    font-family: var(--mono);
    font-size: 0.72rem;
    letter-spacing: 3px;
    color: var(--accent);
    text-transform: uppercase;
    margin-bottom: 6px;
}
.section-title {
    font-size: 2rem;
    font-weight: 700;
    color: var(--text-main) !important;
    margin-bottom: 24px;
}
.card h3 {
    font-size: 1.15rem;
    font-weight: 600;
    color: var(--text-main) !important;
    margin-bottom: 8px;
}
.card p, .card li {
    color: var(--text-muted) !important;
    font-size: 0.95rem;
    line-height: 1.65;
}
.card ul { padding-left: 18px; }

/* ── accent badge ── */
.badge {
    display: inline-block;
    background: var(--tag-bg);
    color: var(--tag-text) !important;
    font-family: var(--mono);
    font-size: 0.72rem;
    padding: 3px 10px;
    border-radius: 99px;
    margin: 4px 3px 4px 0;
    font-weight: 700;
    letter-spacing: 0.5px;
}

/* ── skill bar ── */
.skill-wrap { margin-bottom: 14px; }
.skill-label {
    display: flex;
    justify-content: space-between;
    font-size: 0.88rem;
    color: var(--text-main) !important;
    margin-bottom: 5px;
}
.skill-bar-bg {
    background: var(--progress-bg);
    border-radius: 99px;
    height: 8px;
    overflow: hidden;
}
.skill-bar-fill {
    height: 8px;
    border-radius: 99px;
    background: linear-gradient(90deg, var(--accent), #4ade80);
    transition: width 0.6s ease;
}

/* ── stat pill ── */
.stat-grid { display: flex; gap: 16px; flex-wrap: wrap; margin-top: 18px; }
.stat-pill {
    background: var(--tag-bg);
    border-radius: 14px;
    padding: 14px 22px;
    text-align: center;
    flex: 1;
    min-width: 110px;
}
.stat-num {
    font-family: var(--mono);
    font-size: 1.6rem;
    font-weight: 700;
    color: var(--accent);
}
.stat-desc { font-size: 0.78rem; color: var(--text-muted) !important; margin-top: 2px; }

/* ── contact info ── */
.contact-row {
    display: flex;
    align-items: center;
    gap: 12px;
    color: var(--text-main) !important;
    font-size: 0.97rem;
    margin-bottom: 10px;
}
.contact-icon {
    width: 38px; height: 38px;
    background: var(--tag-bg);
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.1rem;
    flex-shrink: 0;
}

/* ── inputs (override Streamlit) ── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.95rem !important;
}

/* ── button ── */
.stButton > button {
    background: linear-gradient(90deg, #22c55e, #4ade80) !important;
    color: #0f172a !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 10px 26px !important;
    font-family: var(--mono) !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.5px !important;
    transition: opacity 0.2s !important;
}
.stButton > button:hover { opacity: 0.85 !important; }

/* ── sidebar ── */
section[data-testid="stSidebar"] {
    border-right: 1px solid var(--border);
}
section[data-testid="stSidebar"] .stRadio label {
    font-family: var(--mono) !important;
    font-size: 0.88rem !important;
    color: var(--text-main) !important;
}

/* ── divider ── */
.divider {
    border: none;
    border-top: 1px solid var(--border);
    margin: 32px 0;
}

/* project number */
.proj-num {
    font-family: var(--mono);
    font-size: 2.5rem;
    font-weight: 700;
    color: var(--accent);
    opacity: 0.3;
    line-height: 1;
    margin-bottom: 6px;
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────
#  SIDEBAR NAV
# ─────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='padding:10px 0 24px'>
        <div style='font-family:Space Mono,monospace;font-size:1.1rem;font-weight:700;
                    color:var(--text-main)'>mujeeb.dev</div>
        <div style='font-size:0.75rem;color:var(--accent);font-family:Space Mono,monospace'>
            v2025
        </div>
    </div>
    """, unsafe_allow_html=True)
    page = st.radio("", ["🏠  Home", "👤  About", "🛠  Skills", "📁  Projects", "🎓  Teaching", "📬  Contact"])
    page = page.split("  ")[1]   # strip emoji prefix


# ─────────────────────────────────────────
#  HOME
# ─────────────────────────────────────────
if page == "Home":
    col1, col2 = st.columns([1, 1.6], gap="large")

    with col1:
        try:
            st.image("profile.jpeg", width=260, use_container_width=False)
        except Exception:
            st.markdown("""
            <div style='width:220px;height:220px;border-radius:20px;
                        background:linear-gradient(135deg,#22c55e,#4ade80);
                        display:flex;align-items:center;justify-content:center;
                        font-size:5rem;'>👨‍💻</div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="hero-name">Mujeeb<br>Ahmed</div>', unsafe_allow_html=True)
        st.markdown('<div class="hero-role">// Python Developer · Data Scientist · Educator</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="hero-bio">
        I build real-world Python applications and train the next generation of developers
        with hands-on, project-based teaching. Based in Sukkur, Pakistan.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        badges = ["Python", "Flask", "Streamlit", "Data Science", "Teaching"]
        badge_html = "".join(f'<span class="badge">{b}</span>' for b in badges)
        st.markdown(badge_html, unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    cards = [
        ("💻", "Development", "Full-stack Python apps using Flask & Streamlit with clean, maintainable code."),
        ("📊", "Data Science", "Analytical problem-solving — from raw data to actionable insights."),
        ("👨‍🏫", "Teaching", "Project-based learning with a focus on real industry skills."),
    ]
    for col, (icon, title, desc) in zip([c1, c2, c3], cards):
        with col:
            st.markdown(f"""
            <div class="card">
                <div style="font-size:2rem;margin-bottom:10px">{icon}</div>
                <h3>{title}</h3>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    # stats
    st.markdown("""
    <div class="stat-grid">
        <div class="stat-pill"><div class="stat-num">3+</div><div class="stat-desc">Years Coding</div></div>
        <div class="stat-pill"><div class="stat-num">10+</div><div class="stat-desc">Projects Built</div></div>
        <div class="stat-pill"><div class="stat-num">50+</div><div class="stat-desc">Students Trained</div></div>
        <div class="stat-pill"><div class="stat-num">4</div><div class="stat-desc">Core Tech Stacks</div></div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────
#  ABOUT
# ─────────────────────────────────────────
elif page == "About":
    st.markdown('<div class="section-label">Who I am</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">About Me</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1.4, 1], gap="large")

    with col1:
        st.markdown("""
        <div class="card">
            <h3>Background</h3>
            <p>
            I'm <strong style="color:var(--text-main)">Mujeeb Ahmed</strong>, a Python Developer
            and Programming Instructor from Sukkur, Pakistan.
            I completed my degree in <strong style="color:var(--text-main)">Data Science
            from Sukkur IBA University</strong> and have since focused on bridging the gap
            between theory and real-world application — both in the software I build
            and in the students I teach.
            </p>
            <br>
            <p>
            My philosophy is simple: the best way to learn is by building things that
            actually work. I apply this to every classroom session and every project I ship.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <h3>What I do</h3>
            <ul>
                <li>Build web applications with Flask & Streamlit</li>
                <li>Analyse data and create visual insights</li>
                <li>Design and deliver Python & C++ courses</li>
                <li>Mentor students through project-based learning</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>Quick Facts</h3>
            <p>🎓 &nbsp;<strong style="color:var(--text-main)">Degree</strong><br>
               <span style="margin-left:24px">B.Sc Data Science</span></p>
            <br>
            <p>🏫 &nbsp;<strong style="color:var(--text-main)">University</strong><br>
               <span style="margin-left:24px">Sukkur IBA University</span></p>
            <br>
            <p>💼 &nbsp;<strong style="color:var(--text-main)">Role</strong><br>
               <span style="margin-left:24px">Developer & Instructor</span></p>
            <br>
            <p>📍 &nbsp;<strong style="color:var(--text-main)">Location</strong><br>
               <span style="margin-left:24px">Sukkur, Pakistan</span></p>
        </div>
        """, unsafe_allow_html=True)


# ─────────────────────────────────────────
#  SKILLS  –  pure HTML, no widget injection
# ─────────────────────────────────────────
elif page == "Skills":
    st.markdown('<div class="section-label">What I know</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Skills</div>', unsafe_allow_html=True)

    def skill_bar(name, pct):
        return f"""
        <div class="skill-wrap">
            <div class="skill-label"><span>{name}</span><span>{pct}%</span></div>
            <div class="skill-bar-bg">
                <div class="skill-bar-fill" style="width:{pct}%"></div>
            </div>
        </div>
        """

    col1, col2 = st.columns(2, gap="large")

    with col1:
        bars = [("Python", 90), ("C++", 75), ("JavaScript", 70)]
        bars_html = "".join(skill_bar(n, p) for n, p in bars)
        st.markdown(f"""
        <div class="card">
            <h3>Programming Languages</h3><br>
            {bars_html}
        </div>
        """, unsafe_allow_html=True)

    with col2:
        bars2 = [("HTML & CSS", 85), ("Flask", 85), ("Streamlit", 90)]
        bars2_html = "".join(skill_bar(n, p) for n, p in bars2)
        st.markdown(f"""
        <div class="card">
            <h3>Web & Frameworks</h3><br>
            {bars2_html}
        </div>
        """, unsafe_allow_html=True)

    # tools row
    tools = ["VS Code", "Git", "Jupyter", "Pandas", "NumPy", "Matplotlib", "MySQL", "Linux"]
    badges_html = "".join(f'<span class="badge">{t}</span>' for t in tools)
    st.markdown(f"""
    <div class="card">
        <h3>Tools & Libraries</h3>
        <div style="margin-top:12px">{badges_html}</div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────
#  PROJECTS
# ─────────────────────────────────────────
elif page == "Projects":
    st.markdown('<div class="section-label">What I built</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Projects</div>', unsafe_allow_html=True)

    projects = [
        {
            "title": "Quiz System",
            "desc": "Full-featured quiz platform with an admin panel, result tracking, and student leaderboard. Built with Flask and SQLite.",
            "tags": ["Flask", "SQLite", "HTML/CSS"],
        },
        {
            "title": "AI Chatbot",
            "desc": "Conversational chatbot with voice input, speech-to-text integration, and intelligent context-aware responses.",
            "tags": ["Python", "OpenAI API", "SpeechRecognition"],
        },
        {
            "title": "Portfolio Website",
            "desc": "This very portfolio — a modern, fully responsive Streamlit app with dark/light mode support and a working contact form.",
            "tags": ["Streamlit", "CSS", "Python"],
        },
        {
            "title": "Data Dashboard",
            "desc": "Interactive analytics dashboard for visualising CSV datasets with dynamic charts and export support.",
            "tags": ["Pandas", "Plotly", "Streamlit"],
        },
    ]

    for i, p in enumerate(projects):
        tags_html = "".join(f'<span class="badge">{t}</span>' for t in p["tags"])
        st.markdown(f"""
        <div class="card">
            <div class="proj-num">0{i+1}</div>
            <h3>{p['title']}</h3>
            <p style="margin:6px 0 14px">{p['desc']}</p>
            {tags_html}
        </div>
        """, unsafe_allow_html=True)


# ─────────────────────────────────────────
#  TEACHING
# ─────────────────────────────────────────
elif page == "Teaching":
    st.markdown('<div class="section-label">Education & Mentorship</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Teaching</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div class="card">
            <h3>Subjects I Teach</h3>
            <ul style="margin-top:10px">
                <li>Python (beginner → advanced)</li>
                <li>C++ & OOP concepts</li>
                <li>Web Development (HTML, CSS, Flask)</li>
                <li>Data Science fundamentals</li>
                <li>Streamlit application development</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>My Teaching Method</h3>
            <ul style="margin-top:10px">
                <li>100% hands-on, project-based learning</li>
                <li>Real-world assignments from day one</li>
                <li>1-on-1 code review sessions</li>
                <li>Problem-solving over memorisation</li>
                <li>Industry-relevant tech stack focus</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>My belief as an educator</h3>
        <p>
        Theory without practice is just trivia. Every concept I teach is immediately
        applied to something real — a mini project, a coding challenge, or a piece of
        a larger system the student is building. That's how skills stick.
        </p>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────
#  CONTACT  –  fixed email logic
# ─────────────────────────────────────────
elif page == "Contact":
    st.markdown('<div class="section-label">Get in touch</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Contact Me</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.3], gap="large")

    with col1:
        st.markdown("""
        <div class="card">
            <h3>Reach me directly</h3>
            <br>
            <div class="contact-row">
                <div class="contact-icon">📧</div>
                <span>ahmedalixy149@gmail.com</span>
            </div>
            <div class="contact-row">
                <div class="contact-icon">📱</div>
                <span>+92 318 030 7822</span>
            </div>
            <div class="contact-row">
                <div class="contact-icon">📍</div>
                <span>Sukkur, Sindh, Pakistan</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("**Send me a message**")
        st.markdown("<br>", unsafe_allow_html=True)

        name  = st.text_input("Your Name",        placeholder="Ali Khan")
        email = st.text_input("Your Email",        placeholder="ali@example.com")
        msg   = st.text_area("Message",            placeholder="Hello Mujeeb, I'd like to ...", height=140)

        if st.button("Send Message ↗"):
            # ── validation ──
            if not name.strip():
                st.error("Please enter your name.")
            elif not email.strip() or "@" not in email:
                st.error("Please enter a valid email address.")
            elif not msg.strip():
                st.error("Please write a message.")
            else:
                # ── send email ──
                EMAIL_USER = os.environ.get("EMAIL_USER", "")
                EMAIL_PASS = os.environ.get("EMAIL_PASSWORD", "")

                if not EMAIL_USER or not EMAIL_PASS:
                    st.warning(
                        "⚠️ Email credentials are not configured. "
                        "Set the **EMAIL_USER** and **EMAIL_PASSWORD** environment variables "
                        "to enable sending."
                    )
                else:
                    try:
                        em = EmailMessage()
                        em["Subject"] = f"Portfolio message from {name}"
                        em["From"]    = EMAIL_USER          # must be authenticated sender
                        em["To"]      = EMAIL_USER          # deliver to yourself
                        em["Reply-To"] = email              # so you can reply to visitor

                        em.set_content(
                            f"Name:    {name}\n"
                            f"Email:   {email}\n\n"
                            f"Message:\n{msg}"
                        )

                        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                            smtp.login(EMAIL_USER, EMAIL_PASS)
                            smtp.send_message(em)

                        st.success("✅ Message sent! I'll get back to you soon.")

                    except smtplib.SMTPAuthenticationError:
                        st.error(
                            "Authentication failed. Make sure you are using a "
                            "**Gmail App Password** (not your regular Gmail password). "
                            "Generate one at myaccount.google.com › Security › App Passwords."
                        )
                    except Exception as e:
                        st.error(f"Could not send message: {e}")

        st.markdown("</div>", unsafe_allow_html=True)

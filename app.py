
import streamlit as st
import pandas as pd
from pathlib import Path

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="AI Career Guidance System",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = BASE_DIR / "data" / "essential_skills.csv"

if not DATA_PATH.exists():
    DATA_PATH = BASE_DIR / "essential_skills.csv"

# ----------------  DESIGN ----------------
st.markdown("""

<style>
.stApp {
    background:
        radial-gradient(ellipse at 10% 0%, #252052 0%, transparent 38%),
        radial-gradient(ellipse at 90% 10%, #103c55 0%, transparent 35%),
        #090b16;
    color: #f4f5ff;
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #15112c, #080d1b);
    border-right: 1px solid #6d42bd;
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1 {
    background: linear-gradient(90deg, #ffffff, #c4a7ff, #67e8f9);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

h2, h3 {
    color: #f3efff !important;
}

p, label, li {
    color: #cbd5f5;
}

.hero, .glass-card, .career-card {
    background: linear-gradient(135deg, #17172f, #111a30);
    border: 1px solid #55408d;
    border-radius: 20px;
    padding: 22px;
    box-shadow: 0 12px 35px #00000045;
}

.hero {
    background: linear-gradient(115deg, #24164b, #17274b 60%, #10394b);
    border: 1px solid #8957e5;
}

.metric-card {
    background: linear-gradient(140deg, #251b47, #112b42);
    border: 1px solid #554d99;
    border-radius: 17px;
    padding: 20px;
    min-height: 110px;
}

.metric-number {
    font-size: 1.9rem;
    font-weight: 800;
    color: #67e8f9;
}

.metric-label {
    color: #c9c8f5;
    font-size: 0.9rem;
}

.career-card {
    margin: 12px 0;
    border-left: 4px solid #a78bfa;
}

.tag {
    background: #123c40;
    color: #67e8f9;
    padding: 5px 10px;
    border-radius: 20px;
}

div.stButton > button,
div.stFormSubmitButton > button {
    background: linear-gradient(100deg, #9333ea, #6366f1, #0891b2);
    color: white;
    border: 1px solid #9b8cff;
    border-radius: 12px;
    font-weight: 700;
    min-height: 45px;
    transition: all 0.2s ease;
}

div.stButton > button:hover,
div.stFormSubmitButton > button:hover {
    border-color: #67e8f9;
    box-shadow: 0 0 22px #7c3aed55;
    transform: translateY(-1px);
}

.stTextInput input,
.stNumberInput input {
    background: #10182b;
    color: white;
    border: 1px solid #454c7a;
    border-radius: 10px;
}

div[data-baseweb="select"] > div {
    background: #10182b;
    border-color: #454c7a;
    border-radius: 10px;
}

div[data-testid="stMetric"] {
    background: linear-gradient(135deg, #21183e, #11283c);
    border: 1px solid #574a91;
    border-radius: 15px;
    padding: 16px;
}

div[data-testid="stProgressBar"] > div {
    background: #202742;
}

div[data-testid="stProgressBar"] div[role="progressbar"] {
    background: linear-gradient(90deg, #a855f7, #6366f1, #22d3ee);
}

hr {
    border-color: #373459;
}

[data-testid="stExpander"] {
    background: #11182a;
    border: 1px solid #4d467d;
    border-radius: 12px;
}

footer {
    visibility: hidden;
}
</style>

""", unsafe_allow_html=True)


# ---------------- DATASET ----------------
@st.cache_data
def load_onet_data():
    if not DATA_PATH.exists():
        return None
    data = pd.read_csv(DATA_PATH, low_memory=False)
    data.columns = data.columns.str.strip()
    return data


# ---------------- CAREER KNOWLEDGE BASE ----------------
CAREERS = {
    "Data Scientist": {
        "skills": ["Python", "SQL", "Statistics", "Excel"],
        "description": "Analyze data and discover useful patterns.",
        "icon": "📊",
        "roadmap": [
            "Learn Python fundamentals",
            "Practice SQL and data cleaning",
            "Study statistics and probability",
            "Learn Pandas and data visualization",
            "Build real-world data projects"
        ]
    },
    "AI / ML Engineer": {
        "skills": ["Python", "Machine Learning", "Statistics", "Problem Solving"],
        "description": "Build intelligent systems and machine-learning models.",
        "icon": "🤖",
        "roadmap": [
            "Strengthen Python and mathematics",
            "Learn NumPy and Pandas",
            "Study machine-learning algorithms",
            "Practice model evaluation",
            "Build and deploy an ML project"
        ]
    },
    "Web Developer": {
        "skills": ["HTML", "CSS", "JavaScript"],
        "description": "Create modern and interactive websites.",
        "icon": "🌐",
        "roadmap": [
            "Learn HTML page structure",
            "Practice CSS and responsive layouts",
            "Learn JavaScript",
            "Build interactive projects",
            "Publish a portfolio website"
        ]
    },
    "Software Engineer": {
        "skills": ["Python", "SQL", "Problem Solving"],
        "description": "Design, develop and maintain software applications.",
        "icon": "💻",
        "roadmap": [
            "Master one programming language",
            "Practice data structures and algorithms",
            "Learn Git and GitHub",
            "Understand databases and testing",
            "Build and document software projects"
        ]
    },
    "Business Analyst": {
        "skills": ["Excel", "SQL", "Communication", "Statistics"],
        "description": "Turn business data into useful decisions.",
        "icon": "📈",
        "roadmap": [
            "Improve Excel and spreadsheet skills",
            "Learn SQL queries",
            "Practice charts and dashboards",
            "Develop communication skills",
            "Complete a business analytics project"
        ]
    }
}


# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown(
        "<div style='text-align:center; padding:12px 0 18px;'>"
        "<div style='font-size:3rem;'>🎯</div>"
        "<h2 style='margin:0;'>AI Career</h2>"
        "<h3 style='margin:0; color:#a5b4fc !important;'>Guidance System</h3>"
        "<p style='font-size:0.85rem;'>By Vishal, Prince & Kangna</p>"
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown("---")
    page = st.radio(
        "NAVIGATION",
        [
            "🏠 Home",
            "🎯 Career Predictor",
            "📊 Skill Analysis",
            "🧭 Career Roadmap",
            "📚 About Project"
        ],
        label_visibility="visible"
    )

    st.markdown("---")
    st.caption("✨ Discover your next step.")
    st.caption("Dataset: O*NET Essential Skills")


# ---------------- LOAD DATA ----------------
df = load_onet_data()

# ---------------- HERO ----------------
st.markdown("""
<div class="hero">
    <div style="color:#a5b4fc;font-weight:700;letter-spacing:2px;">
        YOUR FUTURE STARTS HERE
    </div>
    <h1>AI Career Guidance System 🚀</h1>
    <p>Discover career paths that match your skills, interests and goals.</p>
    <p>Developed by <b>Vishal, Prince & Kangna</b></p>
</div>
""", unsafe_allow_html=True)

if df is not None:
    st.success("O*NET skills dataset loaded successfully!")
else:
    st.error(
        "O*NET CSV not found. Check that data/essential_skills.csv "
        "exists inside your project folder."
    )

if df is not None:
    with st.expander("📁 View dataset information"):
        st.write(f"**Rows:** {len(df):,}")
        st.write(f"**Columns:** {len(df.columns)}")
        st.write(", ".join(df.columns.astype(str)))

# ---------------- HOME ----------------
if page == "🏠 Home":
    st.subheader("✨ Your Career Dashboard")

    a, b, c = st.columns(3)
    with a:
        st.markdown(
            '<div class="metric-card"><div class="metric-number">5</div>'
            '<div class="metric-label">Career paths to explore</div></div>',
            unsafe_allow_html=True
        )
    with b:
        st.markdown(
            '<div class="metric-card"><div class="metric-number">10</div>'
            '<div class="metric-label">Selectable skills</div></div>',
            unsafe_allow_html=True
        )
    with c:
        st.markdown(
            '<div class="metric-card"><div class="metric-number">O*NET</div>'
            '<div class="metric-label">Occupational skills dataset</div></div>',
            unsafe_allow_html=True
        )

    st.markdown("")
    left, right = st.columns([1.2, 1])

    with left:
        st.markdown("""
        <div class="glass-card">
            <h3>🌟 Find your direction</h3>
            <p>Discover careers based on your current skills, interests,
            and academic profile.</p>
            <p>✓ Compare your skills with career requirements</p>
            <p>✓ Identify skills you can develop next</p>
            <p>✓ Explore a step-by-step learning roadmap</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🎯 Start Career Prediction", use_container_width=True):
            st.session_state["page_request"] = "🎯 Career Predictor"
            st.rerun()

    with right:
        st.markdown("""
        <div class="glass-card">
            <h3>💡 A better next step</h3>
            <p>Career guidance is a starting point—not a guarantee.
            Use recommendations to plan projects, learning and exploration.</p>
            <p class="small-note">Tip: Select skills you can actually demonstrate.</p>
        </div>
        """, unsafe_allow_html=True)

# Handle home-page navigation button
if "page_request" in st.session_state:
    st.info("Use the Career Predictor page in the sidebar to enter your details.")

# ---------------- CAREER PREDICTOR ----------------
if page == "🎯 Career Predictor":
    st.subheader("👨‍🎓 Tell Us About Yourself")
    st.write("Complete your profile to compare your skills with career paths.")

    with st.form("career_form"):
        name = st.text_input("Your name", placeholder="Enter your name")
        marks = st.slider("Academic performance (%)", 0, 100, 70)

        skill_options = [
            "Python", "SQL", "Statistics", "HTML", "CSS",
            "JavaScript", "Communication", "Excel",
            "Problem Solving", "Machine Learning"
        ]
        skills = st.multiselect(
            "Select the skills you have",
            skill_options,
            help="Choose only the skills you know or have practised."
        )

        interest = st.selectbox(
            "Career interest",
            ["No preference"] + list(CAREERS.keys())
        )

        submitted = st.form_submit_button(
            "✨ Generate My Recommendations",
            use_container_width=True
        )

    if submitted:
        if not name.strip():
            st.warning("Please enter your name.")
        elif not skills:
            st.warning("Please select at least one skill.")
        else:
            st.session_state["student_result"] = {
                "name": name.strip(),
                "marks": marks,
                "skills": skills,
                "interest": interest
            }

    result = st.session_state.get("student_result")

    if result:
        st.markdown("---")
        st.subheader(f"🎉 Career Results for {result['name']}")

        ranked = []
        for career, details in CAREERS.items():
            required = details["skills"]
            matched = [
                s for s in required
                if s.strip().casefold()
                in {x.strip().casefold() for x in result["skills"]}
            ]
            missing = [s for s in required if s not in matched]
            score = round(len(matched) / len(required) * 100)

            # Preference is a small ranking boost, not a skill match.
            rank_score = score
            if result["interest"] == career:
                rank_score += 5

            ranked.append({
                "career": career,
                "details": details,
                "matched": matched,
                "missing": missing,
                "score": score,
                "rank_score": rank_score
            })

        ranked.sort(key=lambda item: item["rank_score"], reverse=True)

        top_career = next(
            (item for item in ranked if item["career"] == result["interest"]),
            ranked[0]
        ) if result["interest"] != "No preference" else ranked[0]

        m1, m2, m3 = st.columns(3)
        m1.metric("Top career match", top_career["career"])
        m2.metric("Skill match", f"{top_career['score']}%")
        m3.metric("Academic performance", f"{result['marks']}%")

        st.progress(top_career["score"] / 100)
        st.markdown(
            f"**Matching skills:** {', '.join(top_career['matched']) or 'None yet'}"
        )
        st.markdown(
            f"**Skills to develop:** {', '.join(top_career['missing']) or 'None from this list'}"
        )

        st.subheader("🏆 Your Top Career Matches")
        for number, item in enumerate(ranked[:3], start=1):
            details = item["details"]
            st.markdown(f"""
            <div class="career-card">
                <h3>{number}. {details['icon']} {item['career']}
                    <span class="tag">{item['score']}% skill match</span>
                </h3>
                <p>{details['description']}</p>
                <p><b>Skills you have:</b>
                {', '.join(item['matched']) or 'No matching skills yet'}</p>
                <p><b>Next skills to learn:</b>
                {', '.join(item['missing']) or 'Continue practising and building projects'}</p>
            </div>
            """, unsafe_allow_html=True)
            st.progress(item["score"] / 100)

        st.info(
            "This is a rule-based prototype. Match percentages compare your "
            "selected skills with the skills listed for each career in this app; "
            "they are not validated AI predictions or job-success probabilities."
        )

# ---------------- SKILL ANALYSIS ----------------
if page == "📊 Skill Analysis":
    st.subheader("📊 Skill Gap Analysis")
    result = st.session_state.get("student_result")

    if not result:
        st.info("First visit Career Predictor and submit your profile.")
    else:
        st.write(f"Analysis for **{result['name']}**")
        selected = {s.casefold() for s in result["skills"]}

        for career, details in CAREERS.items():
            required = details["skills"]
            count = sum(1 for s in required if s.casefold() in selected)
            score = count / len(required)
            with st.container(border=True):
                st.markdown(f"**{details['icon']} {career}**")
                st.progress(score)
                st.caption(f"{round(score * 100)}% of this app's listed skills selected")

        st.markdown("""
        <div class="glass-card">
            <h3>💡 Improve your profile</h3>
            <p>Choose one missing skill, practise it, and demonstrate it in a
            small project. Reassess your profile as your abilities grow.</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------- CAREER ROADMAP ----------------
if page == "🧭 Career Roadmap":
    st.subheader("🧭 Your Learning Roadmap")
    result = st.session_state.get("student_result")

    if not result:
        st.info("Submit your profile on Career Predictor to personalise this page.")
        chosen_career = st.selectbox("Explore a career", list(CAREERS.keys()))
    else:
        chosen_career = st.selectbox(
            "Choose a career roadmap",
            list(CAREERS.keys()),
            index=(
                list(CAREERS.keys()).index(result["interest"])
                if result["interest"] in CAREERS else 0
            )
        )

    details = CAREERS[chosen_career]
    st.markdown(
        f'<div class="glass-card"><h2>{details["icon"]} {chosen_career}</h2>'
        f'<p>{details["description"]}</p></div>',
        unsafe_allow_html=True
    )

    for index, step in enumerate(details["roadmap"], start=1):
        st.markdown(f"**Step {index}**")
        st.checkbox(step, key=f"roadmap_{chosen_career}_{index}")

# ---------------- ABOUT PROJECT ----------------
if page == "📚 About Project":
    st.subheader("📚 About This Project")
    st.markdown("""
    <div class="glass-card">
        <h2>🎯 AI Career Guidance System</h2>
        <p><b>Developed by:</b> Vishal, Prince & Kangna</p>
        <p>This student project demonstrates how skills and career interests
        can be used to explore career paths and identify learning needs.</p>
        <p><b>Technology:</b> Python, Streamlit and Pandas</p>
        <p><b>Dataset:</b> O*NET Essential Skills CSV</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📌 Dataset information")
    st.write(
        "O*NET is used as an occupational skills reference. "
        "The app's initial match percentages are calculated from its own "
        "career-skill lists and are not calculated from O*NET ratings."
    )
    st.caption(
        "Data attribution: O*NET 31.0 Database, U.S. Department of Labor, "
        "Employment and Training Administration. Verify the applicable "
        "license and attribution terms when distributing this project."
    )

# ---------------- O*NET OCCUPATION SKILLS ----------------
if df is not None:
    with st.expander("🔎 Explore O*NET occupational skills"):
        title_col = next(
            (c for c in df.columns if c.casefold() == "title"), None
        )
        element_col = next(
            (c for c in df.columns if c.casefold() == "element name"), None
        )
        scale_col = next(
            (c for c in df.columns if c.casefold() == "scale name"), None
        )
        value_col = next(
            (c for c in df.columns if c.casefold() == "data value"), None
        )

        if title_col and element_col:
            titles = sorted(df[title_col].dropna().astype(str).unique())
            selected_title = st.selectbox(
                "Select an occupation from the O*NET dataset",
                titles
            )
            occupation_df = df[
                df[title_col].astype(str) == selected_title
            ].copy()

            if scale_col:
                importance = occupation_df[
                    occupation_df[scale_col].astype(str).str.contains(
                        "importance", case=False, na=False
                    )
                ]
                if not importance.empty:
                    occupation_df = importance

            columns_to_show = [element_col]
            if scale_col:
                columns_to_show.append(scale_col)
            if value_col:
                columns_to_show.append(value_col)

            st.write(f"**Occupation:** {selected_title}")
            st.dataframe(
                occupation_df[columns_to_show].drop_duplicates().head(40),
                hide_index=True,
                width="stretch"
            )
        else:
            st.warning(
                "The CSV does not contain the expected Title and Element Name columns."
            )

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:#9eafd7; padding:10px;'>"
    "🎯 AI Career Guidance System · Developed by Vishal, Prince & Kangna"
    "</div>",
    unsafe_allow_html=True
)


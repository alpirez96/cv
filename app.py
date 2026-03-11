"""
Alp İrez — Personal Portfolio Web App
Built with Streamlit | Cross-browser compatible (Safari, Chrome, Firefox)
Run: streamlit run app.py
"""

import streamlit as st
import base64
from pathlib import Path

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Alp İrez · Data & BI Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",  # Sidebar kapalı — navigasyon tabs ile
)

# ─────────────────────────────────────────────
# CUSTOM CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    background-color: #0d0f14 !important;
    color: #e8e3d8;
    font-family: 'DM Sans', sans-serif;
}
[data-testid="stAppViewContainer"] > .main { background-color: #0d0f14 !important; }
[data-testid="stHeader"] { background-color: #0d0f14 !important; }

/* Hide sidebar entirely — all browsers */
[data-testid="collapsedControl"] { display: none !important; }
section[data-testid="stSidebar"]  { display: none !important; }

/* ── Tab bar ── */
.stTabs [data-baseweb="tab-list"] {
    background-color: #111318 !important;
    border-bottom: 1px solid #1f2330 !important;
    gap: 0 !important;
    padding: 0 0.5rem !important;
    flex-wrap: wrap !important;
}
.stTabs [data-baseweb="tab"] {
    background-color: transparent !important;
    color: #a09e9a !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.85rem !important;
    font-weight: 400 !important;
    padding: 0.8rem 1rem !important;
    border: none !important;
    border-bottom: 2px solid transparent !important;
    white-space: nowrap !important;
}
.stTabs [aria-selected="true"] {
    background-color: transparent !important;
    color: #f0c27a !important;
    border-bottom: 2px solid #f0c27a !important;
}
.stTabs [data-baseweb="tab"]:hover { color: #f0c27a !important; background: transparent !important; }
.stTabs [data-baseweb="tab-highlight"] { background-color: transparent !important; }
.stTabs [data-baseweb="tab-border"]    { display: none !important; }
.stTabs [data-baseweb="tab-panel"]     { background-color: #0d0f14 !important; padding: 2rem 0 !important; }

/* ── Typography ── */
h1,h2,h3,h4 { font-family: 'Syne', sans-serif; letter-spacing: -0.02em; }

/* ── Portfolio header strip ── */
.portfolio-header {
    display: flex; align-items: center; gap: 1rem;
    padding: 1.1rem 1.5rem;
    background: #111318; border-bottom: 1px solid #1f2330;
}
.header-avatar {
    width: 42px; height: 42px; border-radius: 50%;
    background: linear-gradient(135deg,#f0c27a,#c97f3a);
    display:flex; align-items:center; justify-content:center;
    font-family:'Syne',sans-serif; font-weight:800; font-size:0.95rem;
    color:#0d0f14; flex-shrink:0;
}
.header-name { font-family:'Syne',sans-serif; font-weight:700; font-size:1rem; color:#f0f0ec; }
.header-role { font-size:0.68rem; color:#f0c27a; letter-spacing:0.12em; text-transform:uppercase; }

/* ── Section headers ── */
.section-label {
    font-size:0.7rem; font-weight:500; letter-spacing:0.22em;
    text-transform:uppercase; color:#f0c27a; margin-bottom:0.25rem;
}
.section-title {
    font-family:'Syne',sans-serif; font-size:2rem; font-weight:700;
    color:#f0f0ec; margin-top:0; margin-bottom:1.5rem; letter-spacing:-0.03em;
}

/* ── Hero ── */
.hero-name {
    font-family:'Syne',sans-serif;
    font-size: clamp(2.4rem,5vw,4rem);
    font-weight:800; line-height:1.05; letter-spacing:-0.04em; color:#f0f0ec;
}
.hero-title {
    font-size:0.95rem; font-weight:300; color:#f0c27a;
    letter-spacing:0.14em; text-transform:uppercase; margin:0.5rem 0 1.5rem;
}
.hero-summary { font-size:1rem; line-height:1.78; color:#b8b4ac; max-width:640px; font-weight:300; }

.thin-divider { border:none; border-top:1px solid #1f2330; margin:2rem 0; }

/* ── Cards ── */
.card {
    background:#14171f; border:1px solid #1f2330; border-radius:12px;
    padding:1.5rem 1.75rem; margin-bottom:1rem;
    transition:border-color .25s, transform .2s;
}
.card:hover { border-color:#f0c27a44; transform:translateY(-2px); }
.card-title  { font-family:'Syne',sans-serif; font-size:1.05rem; font-weight:700; color:#f0f0ec; margin-bottom:0.15rem; }
.card-subtitle { font-size:0.85rem; color:#f0c27a; font-weight:400; margin-bottom:0.5rem; }
.card-meta   { font-size:0.75rem; color:#6b6a66; margin-bottom:0.75rem; }
.card-body   { font-size:0.92rem; color:#a09e9a; line-height:1.65; }

/* ── Stats ── */
.stat-box { background:#14171f; border:1px solid #1f2330; border-radius:12px; padding:1.25rem; text-align:center; transition:border-color .2s; }
.stat-box:hover { border-color:#f0c27a44; }
.stat-number { font-family:'Syne',sans-serif; font-size:2rem; font-weight:800; color:#f0c27a; line-height:1; }
.stat-label  { font-size:0.7rem; color:#6b6a66; text-transform:uppercase; letter-spacing:0.1em; margin-top:0.35rem; }

/* ── Skills ── */
.skill-grid  { display:flex; flex-wrap:wrap; gap:0.5rem; margin-top:0.5rem; }
.skill-pill  {
    background:#1a1e28; border:1px solid #2a2f3e; border-radius:50px;
    padding:0.35rem 0.9rem; font-size:0.82rem; color:#c8c4bc;
    font-family:'DM Sans',sans-serif; font-weight:400; transition:all .2s; display:inline-block;
}
.skill-pill:hover { border-color:#f0c27a88; color:#f0c27a; }
.skill-pill-accent { background:#f0c27a18; border-color:#f0c27a55; color:#f0c27a; }

/* ── Contact ── */
.contact-item {
    display:flex; align-items:center; gap:0.75rem; padding:0.85rem 1rem;
    background:#14171f; border:1px solid #1f2330; border-radius:10px; margin-bottom:0.75rem;
    font-size:0.92rem; color:#c8c4bc;
}
.contact-icon { font-size:1.1rem; width:1.5rem; text-align:center; }

/* ── Certs ── */
.cert-badge {
    background:#14171f; border:1px solid #1f2330; border-left:3px solid #f0c27a;
    border-radius:8px; padding:0.9rem 1.2rem; margin-bottom:0.75rem;
}
.cert-name { font-family:'Syne',sans-serif; font-size:0.95rem; font-weight:600; color:#e8e3d8; }
.cert-org  { font-size:0.78rem; color:#6b6a66; margin-top:0.2rem; }

/* ── Download button ── */
.download-btn {
    display:inline-flex; align-items:center; gap:0.5rem;
    background:#f0c27a; color:#0d0f14; font-family:'Syne',sans-serif; font-weight:700;
    font-size:0.88rem; letter-spacing:0.04em; padding:0.65rem 1.4rem; border-radius:8px;
    text-decoration:none; border:none; cursor:pointer; transition:background .2s, transform .15s; margin-top:1rem;
}
.download-btn:hover { background:#f5d18a; transform:translateY(-1px); }

/* ── Misc overrides ── */
.stMarkdown p { margin-bottom:0.5rem; }
footer { visibility:hidden; }
#MainMenu { visibility:hidden; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# DATA
# ─────────────────────────────────────────────
CV_DATA = {
    "name": "Alp İrez",
    "title": "Data & BI Analyst",
    "location": "Ataşehir, İstanbul",
    "email": "alpirez96@gmail.com",
    "phone": "+90 (530) 236 11 52",
    "linkedin": "linkedin.com/in/alpirez",
    "linkedin_url": "https://linkedin.com/in/alpirez",
    "summary": (
        "Data & BI Analyst with 4+ years of hands-on experience building "
        "machine learning models, optimising data pipelines, and delivering "
        "actionable business intelligence. Passionate about transforming raw "
        "data into clear insights through SQL, Python, and modern BI tools. "
        "Currently pursuing an MSc in Economics to deepen the analytical "
        "foundation behind every dashboard and model."
    ),
    "experience": [
        {
            "role": "Data Analyst", "company": "Wellbees", "period": "2023 – 2025",
            "bullets": [
                "Developed and deployed machine learning models to personalise user engagement.",
                "Optimised story recommendation algorithms, improving content relevance metrics.",
                "Collaborated cross-functionally with product and engineering teams to translate data findings into product decisions.",
            ],
        },
        {
            "role": "Junior Data Analyst", "company": "Wellbees", "period": "2021 – 2023",
            "bullets": [
                "Managed and maintained SQL databases, ensuring data integrity and query performance.",
                "Supported the Product Owner with data-driven analysis for roadmap prioritisation.",
                "Built dashboards and reports that tracked key product KPIs.",
            ],
        },
        {
            "role": "Sales Assistant", "company": "Wellbees", "period": "2021",
            "bullets": [
                "Managed CRM workflows and sales reporting pipelines.",
                "Provided data support to the sales team using HubSpot.",
            ],
        },
        {
            "role": "Content Editor", "company": "BLB Media", "period": "2016 – 2019",
            "bullets": [
                "Produced translations and project-based editorial content.",
                "Collaborated with creative teams on multimedia projects.",
            ],
        },
    ],
    "education": [
        {"degree": "MSc Economics", "institution": "Çanakkale Onsekiz Mart University", "period": "2024 – Present", "note": ""},
        {"degree": "BSc Tourism Management", "institution": "İstanbul University", "period": "2015 – 2020", "note": "Erasmus+ Exchange — Mid Sweden University, 2017"},
        {"degree": "Associate Degree — HR Management", "institution": "Anadolu University", "period": "", "note": ""},
        {"degree": "Associate Degree — Computer Programming", "institution": "Anadolu University", "period": "", "note": ""},
    ],
    "skills": {
        "Data & Analytics": ["SQL", "Python", "pandas", "numpy", "plotly", "Power BI"],
        "ML & AI": ["Machine Learning", "Prompt Engineering", "Algorithm Optimisation"],
        "Tools & Platforms": ["HubSpot", "MS Office", "Corel Draw"],
        "Languages": ["Turkish (Native)", "English (Advanced)", "German (A2)", "Russian (A2)"],
    },
    "certifications": [
        {"name": "SEGEM Certificate of Technical Personnel Competence", "org": "SEGEM", "year": "2025"},
        {"name": "Data Analytics Bootcamp", "org": "Trendyol", "year": "2022"},
        {"name": "Miul & VBO Bootcamp", "org": "VBO", "year": "2022"},
        {"name": "SQL Programming", "org": "Udemy", "year": "2021"},
    ],
    "projects": [
        {
            "title": "TÜBİTAK Project — History",
            "desc": "Finalist in TÜBİTAK with the research project 'The Biga Rebellion in the National Struggle Years'. Conducted primary-source historical research and presented findings at a national level.",
        },
        {
            "title": "Swedish Cinema Days — IU 7th Art Cinema Club",
            "desc": "Organised and curated Swedish Cinema Days as part of İstanbul University's Faculty of Economics 7th Art Cinema Club, bridging international film culture with the university community.",
        },
    ],
    "hobbies": ["Cinema 🎬", "Rowing 🚣", "Photography 📷", "CrossFit 🏋️", "Art & Culture 🎨", "Traditional Shaving 🪒"],
}

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────

def card(title, subtitle="", meta="", body_lines=None):
    bullets_html = ""
    if body_lines:
        bullets_html = "<ul style='margin:0.5rem 0 0 1rem;padding:0;'>"
        for line in body_lines:
            bullets_html += f"<li style='color:#a09e9a;font-size:0.9rem;line-height:1.6;margin-bottom:0.25rem;'>{line}</li>"
        bullets_html += "</ul>"
    meta_html     = f"<div class='card-meta'>📅 {meta}</div>" if meta else ""
    subtitle_html = f"<div class='card-subtitle'>{subtitle}</div>" if subtitle else ""
    st.markdown(f"<div class='card'><div class='card-title'>{title}</div>{subtitle_html}{meta_html}{bullets_html}</div>", unsafe_allow_html=True)


def section_header(label, title):
    st.markdown(f"<div class='section-label'>{label}</div><div class='section-title'>{title}</div>", unsafe_allow_html=True)


def skills_block(category, items, accent=False):
    pill_class = "skill-pill skill-pill-accent" if accent else "skill-pill"
    pills = "".join([f"<span class='{pill_class}'>{s}</span>" for s in items])
    st.markdown(f"""
    <div style='margin-bottom:1.25rem;'>
        <div style='font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:#6b6a66;margin-bottom:0.5rem;'>{category}</div>
        <div class='skill-grid'>{pills}</div>
    </div>""", unsafe_allow_html=True)


def get_pdf_download_link(label="Download CV (PDF)"):
    pdf_path = Path(__file__).parent / "Alp_I_rez_CV.pdf"
    if not pdf_path.exists():
        return ""
    try:
        with open(pdf_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        return f'<a class="download-btn" href="data:application/pdf;base64,{b64}" download="Alp_Irez_CV.pdf">⬇ {label}</a>'
    except Exception:
        return ""

# ─────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────
st.markdown("""
<div class='portfolio-header'>
    <div class='header-avatar'>AI</div>
    <div>
        <div class='header-name'>Alp İrez</div>
        <div class='header-role'>Data &amp; BI Analyst</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# TABS  ← tüm tarayıcılarda çalışır
# ─────────────────────────────────────────────
tab_home, tab_exp, tab_skills, tab_edu, tab_proj, tab_cert, tab_contact = st.tabs([
    "🏠 Home", "💼 Experience", "🛠 Skills", "🎓 Education",
    "🚀 Projects", "🏅 Certifications", "✉️ Contact",
])

# ── HOME ──────────────────────────────────────
with tab_home:
    col_main, _ = st.columns([3, 1])
    with col_main:
        st.markdown(f"<div class='hero-name'>{CV_DATA['name']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='hero-title'>{CV_DATA['title']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='hero-summary'>{CV_DATA['summary']}</div>", unsafe_allow_html=True)
        dl = get_pdf_download_link("Download CV")
        if dl:
            st.markdown(dl, unsafe_allow_html=True)

    st.markdown("<hr class='thin-divider'>", unsafe_allow_html=True)
    st.markdown("<div class='section-label'>At a glance</div>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    for col, num, lbl in zip([c1,c2,c3,c4], ["4+","3","4","2"], ["Years Experience","Roles at Wellbees","Certifications","Degree Fields"]):
        with col:
            st.markdown(f"<div class='stat-box'><div class='stat-number'>{num}</div><div class='stat-label'>{lbl}</div></div>", unsafe_allow_html=True)

    st.markdown("<hr class='thin-divider'>", unsafe_allow_html=True)
    st.markdown("<div class='section-label'>Highlights</div>", unsafe_allow_html=True)
    h1, h2, h3 = st.columns(3)
    for col, icon, title, desc in zip(
        [h1,h2,h3], ["🤖","🗄️","📊"],
        ["ML Model Development","SQL & Data Engineering","BI & Dashboarding"],
        ["Built and deployed machine learning models at Wellbees to personalise user experience at scale.",
         "Managed production SQL databases and optimised query performance for product analytics.",
         "Delivered Power BI dashboards and reports to translate data into actionable strategy."],
    ):
        with col:
            st.markdown(f"<div class='card' style='text-align:center;'><div style='font-size:1.8rem;margin-bottom:0.5rem;'>{icon}</div><div class='card-title' style='font-size:1rem;'>{title}</div><div class='card-body' style='font-size:0.85rem;margin-top:0.4rem;'>{desc}</div></div>", unsafe_allow_html=True)

    st.markdown("<hr class='thin-divider'>", unsafe_allow_html=True)
    st.markdown("<div class='section-label'>Outside the data</div>", unsafe_allow_html=True)
    pills = "".join([f"<span class='skill-pill'>{h}</span>" for h in CV_DATA["hobbies"]])
    st.markdown(f"<div class='skill-grid' style='margin-top:0.5rem;'>{pills}</div>", unsafe_allow_html=True)

# ── EXPERIENCE ────────────────────────────────
with tab_exp:
    section_header("Career", "Work Experience")
    for exp in CV_DATA["experience"]:
        card(title=exp["role"], subtitle=exp["company"], meta=exp["period"], body_lines=exp["bullets"])

# ── SKILLS ────────────────────────────────────
with tab_skills:
    section_header("Capabilities", "Skills & Tools")
    for i, (cat, items) in enumerate(CV_DATA["skills"].items()):
        skills_block(cat, items, accent=(i == 0))
    st.markdown("<hr class='thin-divider'>", unsafe_allow_html=True)
    st.markdown("<div style='color:#6b6a66;font-size:0.82rem;font-style:italic;'>Skill proficiency is demonstrated through 4+ years of applied professional experience.</div>", unsafe_allow_html=True)

# ── EDUCATION ─────────────────────────────────
with tab_edu:
    section_header("Academic", "Education")
    for edu in CV_DATA["education"]:
        note_html = f"<div style='font-size:0.83rem;color:#f0c27a88;margin-top:0.4rem;'>✈ {edu['note']}</div>" if edu["note"] else ""
        period_html = f'<div class="card-meta">📅 {edu["period"]}</div>' if edu["period"] else ""
        st.markdown(f"<div class='card'><div class='card-title'>{edu['degree']}</div><div class='card-subtitle'>{edu['institution']}</div>{period_html}{note_html}</div>", unsafe_allow_html=True)

# ── PROJECTS ──────────────────────────────────
with tab_proj:
    section_header("Selected Work", "Projects")
    for proj in CV_DATA["projects"]:
        st.markdown(f"<div class='card'><div class='card-title'>{proj['title']}</div><div class='card-body' style='margin-top:0.5rem;'>{proj['desc']}</div></div>", unsafe_allow_html=True)

# ── CERTIFICATIONS ────────────────────────────
with tab_cert:
    section_header("Credentials", "Certifications")
    for cert in CV_DATA["certifications"]:
        st.markdown(f"<div class='cert-badge'><div class='cert-name'>🏅 {cert['name']}</div><div class='cert-org'>{cert['org']} · {cert['year']}</div></div>", unsafe_allow_html=True)

# ── CONTACT ───────────────────────────────────
with tab_contact:
    section_header("Get in Touch", "Contact")
    for icon, lbl, val, href in [
        ("📧","Email",    CV_DATA["email"],    f"mailto:{CV_DATA['email']}"),
        ("📱","Phone",    CV_DATA["phone"],    f"tel:{CV_DATA['phone'].replace(' ','')}"),
        ("🔗","LinkedIn", CV_DATA["linkedin"], CV_DATA["linkedin_url"]),
        ("📍","Location", CV_DATA["location"], None),
    ]:
        ls = f"<a href='{href}' style='color:inherit;text-decoration:none;'>" if href else ""
        le = "</a>" if href else ""
        st.markdown(f"<div class='contact-item'><span class='contact-icon'>{icon}</span><span style='color:#6b6a66;font-size:0.75rem;width:70px;text-transform:uppercase;letter-spacing:0.08em;'>{lbl}</span>{ls}<span style='color:#e8e3d8;'>{val}</span>{le}</div>", unsafe_allow_html=True)

    dl = get_pdf_download_link("Download CV (PDF)")
    if dl:
        st.markdown(dl, unsafe_allow_html=True)

    st.markdown("<hr class='thin-divider'>", unsafe_allow_html=True)
    st.markdown("<div style='color:#6b6a66;font-size:0.88rem;line-height:1.7;'>Open to freelance data projects, full-time opportunities, and interesting collaborations.<br>Feel free to reach out — I typically respond within 24 hours.</div>", unsafe_allow_html=True)

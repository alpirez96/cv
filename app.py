"""
Alp İrez — Personal Portfolio Web App
Built with Streamlit | Senior Python Developer & UX-focused Product Design
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
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# CUSTOM CSS — Refined dark editorial aesthetic
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

/* ── Root & Background ── */
html, body, [data-testid="stAppViewContainer"] {
    background-color: #0d0f14;
    color: #e8e3d8;
    font-family: 'DM Sans', sans-serif;
}

[data-testid="stSidebar"] {
    background-color: #111318;
    border-right: 1px solid #1f2330;
}

/* ── Typography ── */
h1, h2, h3, h4 {
    font-family: 'Syne', sans-serif;
    letter-spacing: -0.02em;
}

/* ── Sidebar nav labels ── */
[data-testid="stSidebar"] .stRadio label {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.9rem;
    color: #a09e9a;
    padding: 2px 0;
    cursor: pointer;
    transition: color 0.2s;
}
[data-testid="stSidebar"] .stRadio label:hover {
    color: #f0c27a;
}

/* ── Hero name ── */
.hero-name {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.8rem, 6vw, 4.5rem);
    font-weight: 800;
    color: #f0f0ec;
    line-height: 1.05;
    letter-spacing: -0.04em;
    margin-bottom: 0;
}

.hero-title {
    font-family: 'DM Sans', sans-serif;
    font-size: 1.05rem;
    font-weight: 300;
    color: #f0c27a;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-top: 0.4rem;
    margin-bottom: 1.5rem;
}

.hero-summary {
    font-size: 1.05rem;
    line-height: 1.75;
    color: #b8b4ac;
    max-width: 620px;
    font-weight: 300;
}

/* ── Section headers ── */
.section-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.72rem;
    font-weight: 500;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #f0c27a;
    margin-bottom: 0.3rem;
}

.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 700;
    color: #f0f0ec;
    margin-top: 0;
    margin-bottom: 1.5rem;
    letter-spacing: -0.03em;
}

/* ── Divider ── */
.thin-divider {
    border: none;
    border-top: 1px solid #1f2330;
    margin: 2rem 0;
}

/* ── Cards ── */
.card {
    background: #14171f;
    border: 1px solid #1f2330;
    border-radius: 12px;
    padding: 1.5rem 1.75rem;
    margin-bottom: 1rem;
    transition: border-color 0.25s, transform 0.2s;
}
.card:hover {
    border-color: #f0c27a44;
    transform: translateY(-2px);
}

.card-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: #f0f0ec;
    margin-bottom: 0.15rem;
}

.card-subtitle {
    font-size: 0.85rem;
    color: #f0c27a;
    font-weight: 400;
    margin-bottom: 0.6rem;
    letter-spacing: 0.03em;
}

.card-meta {
    font-size: 0.78rem;
    color: #6b6a66;
    margin-bottom: 0.75rem;
    font-family: 'DM Sans', sans-serif;
}

.card-body {
    font-size: 0.92rem;
    color: #a09e9a;
    line-height: 1.65;
}

/* ── Skill pills ── */
.skill-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-top: 0.5rem;
}

.skill-pill {
    background: #1a1e28;
    border: 1px solid #2a2f3e;
    border-radius: 50px;
    padding: 0.35rem 0.9rem;
    font-size: 0.82rem;
    color: #c8c4bc;
    font-family: 'DM Sans', sans-serif;
    font-weight: 400;
    transition: all 0.2s;
    display: inline-block;
}
.skill-pill:hover {
    border-color: #f0c27a88;
    color: #f0c27a;
}

.skill-pill-accent {
    background: #f0c27a18;
    border: 1px solid #f0c27a55;
    color: #f0c27a;
}

/* ── Stat boxes ── */
.stat-box {
    background: #14171f;
    border: 1px solid #1f2330;
    border-radius: 12px;
    padding: 1.25rem;
    text-align: center;
}
.stat-number {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    color: #f0c27a;
    line-height: 1;
}
.stat-label {
    font-size: 0.75rem;
    color: #6b6a66;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-top: 0.3rem;
}

/* ── Contact row ── */
.contact-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.85rem 1rem;
    background: #14171f;
    border: 1px solid #1f2330;
    border-radius: 10px;
    margin-bottom: 0.75rem;
    font-size: 0.92rem;
    color: #c8c4bc;
}

.contact-icon {
    font-size: 1.1rem;
    width: 1.5rem;
    text-align: center;
}

/* ── Download button ── */
.download-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: #f0c27a;
    color: #0d0f14;
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 0.88rem;
    letter-spacing: 0.04em;
    padding: 0.65rem 1.4rem;
    border-radius: 8px;
    text-decoration: none;
    border: none;
    cursor: pointer;
    transition: background 0.2s, transform 0.15s;
    margin-top: 1rem;
}
.download-btn:hover {
    background: #f5d18a;
    transform: translateY(-1px);
}

/* ── Cert badge ── */
.cert-badge {
    background: #14171f;
    border: 1px solid #1f2330;
    border-left: 3px solid #f0c27a;
    border-radius: 8px;
    padding: 0.9rem 1.2rem;
    margin-bottom: 0.75rem;
}
.cert-name {
    font-family: 'Syne', sans-serif;
    font-size: 0.95rem;
    font-weight: 600;
    color: #e8e3d8;
}
.cert-org {
    font-size: 0.78rem;
    color: #6b6a66;
    margin-top: 0.2rem;
}

/* ── Streamlit overrides ── */
.stRadio > div { gap: 0 !important; }
[data-testid="stSidebarContent"] { padding-top: 2rem; }
div[data-testid="metric-container"] { display: none; }
.stMarkdown p { margin-bottom: 0.5rem; }
footer { visibility: hidden; }
#MainMenu { visibility: hidden; }
header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# DATA — Structured CV content
# ─────────────────────────────────────────────
CV_DATA = {
    "name": "Alp İrez",
    "title": "Data & BI Analyst",
    "location": "Ataşehir, İstanbul",
    "email": "alpirez96@gmail.com",
    "phone": "+90 (530) 236 11 52",
    "linkedin": "linkedin.com/in/alpirez",
    "linkedin_url": "https://linkedin.com/in/alpirez",
    "dob": "11 September 1996",
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
            "role": "Data Analyst",
            "company": "Wellbees",
            "period": "2023 – 2025",
            "bullets": [
                "Developed and deployed machine learning models to personalise user engagement.",
                "Optimised story recommendation algorithms, improving content relevance metrics.",
                "Collaborated cross-functionally with product and engineering teams to translate data findings into product decisions.",
            ],
        },
        {
            "role": "Junior Data Analyst",
            "company": "Wellbees",
            "period": "2021 – 2023",
            "bullets": [
                "Managed and maintained SQL databases, ensuring data integrity and query performance.",
                "Supported the Product Owner with data-driven analysis for roadmap prioritisation.",
                "Built dashboards and reports that tracked key product KPIs.",
            ],
        },
        {
            "role": "Sales Assistant",
            "company": "Wellbees",
            "period": "2021",
            "bullets": [
                "Managed CRM workflows and sales reporting pipelines.",
                "Provided data support to the sales team using HubSpot.",
            ],
        },
        {
            "role": "Content Editor",
            "company": "BLB Media",
            "period": "2016 – 2019",
            "bullets": [
                "Produced translations and project-based editorial content.",
                "Collaborated with creative teams on multimedia projects.",
            ],
        },
    ],
    "education": [
        {
            "degree": "MSc Economics",
            "institution": "Çanakkale Onsekiz Mart University",
            "period": "2024 – Present",
            "note": "",
        },
        {
            "degree": "BSc Tourism Management",
            "institution": "İstanbul University",
            "period": "2015 – 2020",
            "note": "Erasmus+ Exchange — Mid Sweden University (Mittuniversitetet), 2017",
        },
        {
            "degree": "Associate Degree — HR Management",
            "institution": "Anadolu University",
            "period": "",
            "note": "",
        },
        {
            "degree": "Associate Degree — Computer Programming",
            "institution": "Anadolu University",
            "period": "",
            "note": "",
        },
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
            "desc": (
                "Finalist in TÜBİTAK (Scientific and Technological Research Council of Turkey) "
                "with the research project 'The Biga Rebellion in the National Struggle Years'. "
                "Conducted primary-source historical research and presented findings at a national level."
            ),
        },
        {
            "title": "Swedish Cinema Days — IU 7th Art Cinema Club",
            "desc": (
                "Organised and curated Swedish Cinema Days as part of İstanbul University's "
                "Faculty of Economics 7th Art Cinema Club, bridging international film culture "
                "with the university community."
            ),
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
    meta_html = f"<div class='card-meta'>📅 {meta}</div>" if meta else ""
    subtitle_html = f"<div class='card-subtitle'>{subtitle}</div>" if subtitle else ""
    st.markdown(f"""
    <div class='card'>
        <div class='card-title'>{title}</div>
        {subtitle_html}
        {meta_html}
        {bullets_html}
    </div>
    """, unsafe_allow_html=True)


def section_header(label, title):
    st.markdown(f"<div class='section-label'>{label}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='section-title'>{title}</div>", unsafe_allow_html=True)


def skills_block(category, items, accent=False):
    pill_class = "skill-pill skill-pill-accent" if accent else "skill-pill"
    pills = "".join([f"<span class='{pill_class}'>{s}</span>" for s in items])
    st.markdown(f"""
    <div style='margin-bottom:1.25rem;'>
        <div style='font-size:0.75rem;text-transform:uppercase;letter-spacing:0.15em;
                    color:#6b6a66;margin-bottom:0.5rem;font-family:"DM Sans",sans-serif;'>
            {category}
        </div>
        <div class='skill-grid'>{pills}</div>
    </div>
    """, unsafe_allow_html=True)


def get_pdf_download_link(pdf_path, label="Download CV (PDF)"):
    """Return an HTML anchor tag for downloading the CV PDF."""
    # Also look next to app.py if the given path doesn't exist
    if not Path(pdf_path).exists():
        pdf_path = Path(__file__).parent / "Alp_I_rez_CV.pdf"
    try:
        with open(pdf_path, "rb") as f:
            pdf_bytes = f.read()
        b64 = base64.b64encode(pdf_bytes).decode()
        href = (
            f'<a class="download-btn" href="data:application/pdf;base64,{b64}" '
            f'download="Alp_Irez_CV.pdf">⬇ {label}</a>'
        )
        return href
    except FileNotFoundError:
        return ""

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center;margin-bottom:1.5rem;'>
        <div style='width:72px;height:72px;border-radius:50%;background:linear-gradient(135deg,#f0c27a,#c97f3a);
                    display:flex;align-items:center;justify-content:center;font-size:1.8rem;
                    margin:0 auto 0.75rem;font-family:"Syne",sans-serif;font-weight:800;color:#0d0f14;'>
            AI
        </div>
        <div style='font-family:"Syne",sans-serif;font-weight:700;font-size:1rem;color:#f0f0ec;'>Alp İrez</div>
        <div style='font-size:0.75rem;color:#f0c27a;letter-spacing:0.1em;text-transform:uppercase;margin-top:0.2rem;'>
            Data & BI Analyst
        </div>
    </div>
    """, unsafe_allow_html=True)

    nav = st.radio(
        "Navigate",
        ["🏠  Home", "💼  Experience", "🛠  Skills", "🎓  Education",
         "🚀  Projects", "🏅  Certifications", "✉️  Contact"],
        label_visibility="collapsed",
    )

    st.markdown("<hr class='thin-divider'>", unsafe_allow_html=True)

    # PDF download in sidebar
    pdf_path = Path(__file__).parent / "Alp_I_rez_CV.pdf"
    dl_link = get_pdf_download_link(pdf_path)
    if dl_link:
        st.markdown(dl_link, unsafe_allow_html=True)
    else:
        st.info("Place `Alp_I_rez_CV.pdf` in the same folder as `app.py` to enable download.")

    st.markdown("""
    <div style='margin-top:2rem;font-size:0.72rem;color:#3a3a3a;text-align:center;'>
        © 2025 Alp İrez
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# PAGES
# ─────────────────────────────────────────────
page = nav.split("  ")[1]  # strip emoji prefix

# ── HOME ──────────────────────────────────────
if page == "Home":
    col_main, col_gap = st.columns([3, 1])
    with col_main:
        st.markdown(f"<div class='hero-name'>{CV_DATA['name']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='hero-title'>{CV_DATA['title']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='hero-summary'>{CV_DATA['summary']}</div>", unsafe_allow_html=True)

        # Download button on homepage too
        pdf_path = Path(__file__).parent / "Alp_I_rez_CV.pdf"
        dl_link = get_pdf_download_link(pdf_path, "Download CV")
        if dl_link:
            st.markdown(dl_link, unsafe_allow_html=True)

    st.markdown("<hr class='thin-divider'>", unsafe_allow_html=True)

    # Quick stats
    st.markdown("<div class='section-label'>At a glance</div>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    for col, number, label in zip(
        [c1, c2, c3, c4],
        ["4+", "3", "4", "2"],
        ["Years Experience", "Roles at Wellbees", "Certifications", "Degree Fields"],
    ):
        with col:
            st.markdown(f"""
            <div class='stat-box'>
                <div class='stat-number'>{number}</div>
                <div class='stat-label'>{label}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<hr class='thin-divider'>", unsafe_allow_html=True)

    # Highlights
    st.markdown("<div class='section-label'>Highlights</div>", unsafe_allow_html=True)
    h1, h2, h3 = st.columns(3)
    highlights = [
        ("🤖", "ML Model Development", "Built and deployed machine learning models at Wellbees to personalise user experience at scale."),
        ("🗄️", "SQL & Data Engineering", "Managed production SQL databases and optimised query performance for product analytics."),
        ("📊", "BI & Dashboarding", "Delivered Power BI dashboards and reports to translate data into actionable strategy."),
    ]
    for col, (icon, title, desc) in zip([h1, h2, h3], highlights):
        with col:
            st.markdown(f"""
            <div class='card' style='text-align:center;'>
                <div style='font-size:1.8rem;margin-bottom:0.5rem;'>{icon}</div>
                <div class='card-title' style='font-size:1rem;'>{title}</div>
                <div class='card-body' style='font-size:0.85rem;margin-top:0.4rem;'>{desc}</div>
            </div>""", unsafe_allow_html=True)

    # Hobbies
    st.markdown("<hr class='thin-divider'>", unsafe_allow_html=True)
    st.markdown("<div class='section-label'>Outside the data</div>", unsafe_allow_html=True)
    hobby_pills = "".join([f"<span class='skill-pill'>{h}</span>" for h in CV_DATA["hobbies"]])
    st.markdown(f"<div class='skill-grid'>{hobby_pills}</div>", unsafe_allow_html=True)


# ── EXPERIENCE ────────────────────────────────
elif page == "Experience":
    section_header("Career", "Work Experience")
    for exp in CV_DATA["experience"]:
        card(
            title=exp["role"],
            subtitle=exp["company"],
            meta=exp["period"],
            body_lines=exp["bullets"],
        )


# ── SKILLS ────────────────────────────────────
elif page == "Skills":
    section_header("Capabilities", "Skills & Tools")
    for i, (category, items) in enumerate(CV_DATA["skills"].items()):
        skills_block(category, items, accent=(i == 0))
    st.markdown("<hr class='thin-divider'>", unsafe_allow_html=True)
    st.markdown("""
    <div style='color:#6b6a66;font-size:0.82rem;font-style:italic;'>
        Skill proficiency is demonstrated through 4+ years of applied professional experience.
    </div>
    """, unsafe_allow_html=True)


# ── EDUCATION ─────────────────────────────────
elif page == "Education":
    section_header("Academic", "Education")
    for edu in CV_DATA["education"]:
        note_html = f"<div style='font-size:0.83rem;color:#f0c27a88;margin-top:0.4rem;'>✈ {edu['note']}</div>" if edu["note"] else ""
        st.markdown(f"""
        <div class='card'>
            <div class='card-title'>{edu['degree']}</div>
            <div class='card-subtitle'>{edu['institution']}</div>
            {'<div class="card-meta">📅 ' + edu['period'] + '</div>' if edu['period'] else ''}
            {note_html}
        </div>
        """, unsafe_allow_html=True)


# ── PROJECTS ──────────────────────────────────
elif page == "Projects":
    section_header("Selected Work", "Projects")
    for proj in CV_DATA["projects"]:
        st.markdown(f"""
        <div class='card'>
            <div class='card-title'>{proj['title']}</div>
            <div class='card-body' style='margin-top:0.5rem;'>{proj['desc']}</div>
        </div>
        """, unsafe_allow_html=True)


# ── CERTIFICATIONS ────────────────────────────
elif page == "Certifications":
    section_header("Credentials", "Certifications")
    for cert in CV_DATA["certifications"]:
        st.markdown(f"""
        <div class='cert-badge'>
            <div class='cert-name'>🏅 {cert['name']}</div>
            <div class='cert-org'>{cert['org']} · {cert['year']}</div>
        </div>
        """, unsafe_allow_html=True)


# ── CONTACT ───────────────────────────────────
elif page == "Contact":
    section_header("Get in Touch", "Contact")
    contact_items = [
        ("📧", "Email", CV_DATA["email"], f"mailto:{CV_DATA['email']}"),
        ("📱", "Phone", CV_DATA["phone"], f"tel:{CV_DATA['phone'].replace(' ', '')}"),
        ("🔗", "LinkedIn", CV_DATA["linkedin"], CV_DATA["linkedin_url"]),
        ("📍", "Location", CV_DATA["location"], None),
    ]
    for icon, label, value, href in contact_items:
        link_start = f"<a href='{href}' style='color:inherit;text-decoration:none;'>" if href else ""
        link_end = "</a>" if href else ""
        st.markdown(f"""
        <div class='contact-item'>
            <span class='contact-icon'>{icon}</span>
            <span style='color:#6b6a66;font-size:0.78rem;width:70px;text-transform:uppercase;
                         letter-spacing:0.08em;'>{label}</span>
            {link_start}<span style='color:#e8e3d8;'>{value}</span>{link_end}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr class='thin-divider'>", unsafe_allow_html=True)
    st.markdown("""
    <div style='color:#6b6a66;font-size:0.88rem;line-height:1.6;'>
        Open to freelance data projects, full-time opportunities, and interesting collaborations.<br>
        Feel free to reach out — I typically respond within 24 hours.
    </div>
    """, unsafe_allow_html=True)

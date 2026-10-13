import streamlit as st

# ============================================================
# BANK OF BARODA | APPLICATION PORTAL
# Replace only the placeholders in APP_LINKS below.
# ============================================================

st.set_page_config(
    page_title="Bank of Baroda | Application Portal",
    page_icon="🏦",  # Optional: replace with your preferred browser-tab emoji
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# APP CONFIGURATION — EDIT HERE
# -----------------------------
APP_LINKS = [
    {"name": "Financial Risk Analyzer", "description": "AI-assisted fundamental risk analysis, powered by Gemini + Yahoo Finance", "icon": "📊", "url": "https://financial-risk-bob-dev.streamlit.app"},
    {"name": "Application 02", "description": "Add a short description for this application.", "icon": "📊", "url": "https://REPLACE-WITH-LINK-02"},
    {"name": "Application 03", "description": "Add a short description for this application.", "icon": "🤖", "url": "https://REPLACE-WITH-LINK-03"},
    {"name": "Application 04", "description": "Add a short description for this application.", "icon": "🌐", "url": "https://REPLACE-WITH-LINK-04"},
    {"name": "Application 05", "description": "Add a short description for this application.", "icon": "📈", "url": "https://REPLACE-WITH-LINK-05"},
    {"name": "Application 06", "description": "Add a short description for this application.", "icon": "🛡️", "url": "https://REPLACE-WITH-LINK-06"},
    {"name": "Application 07", "description": "Add a short description for this application.", "icon": "💹", "url": "https://REPLACE-WITH-LINK-07"},
    {"name": "Application 08", "description": "Add a short description for this application.", "icon": "🧠", "url": "https://REPLACE-WITH-LINK-08"},
    {"name": "Application 09", "description": "Add a short description for this application.", "icon": "📑", "url": "https://REPLACE-WITH-LINK-09"},
    {"name": "Application 10", "description": "Add a short description for this application.", "icon": "🌱", "url": "https://REPLACE-WITH-LINK-10"},
    {"name": "Application 11", "description": "Add a short description for this application.", "icon": "🔎", "url": "https://REPLACE-WITH-LINK-11"},
    {"name": "Application 12", "description": "Add a short description for this application.", "icon": "⚙️", "url": "https://REPLACE-WITH-LINK-12"},
    {"name": "Application 13", "description": "Add a short description for this application.", "icon": "💬", "url": "https://REPLACE-WITH-LINK-13"},
    {"name": "Application 14", "description": "Add a short description for this application.", "icon": "📂", "url": "https://REPLACE-WITH-LINK-14"},
    {"name": "Application 15", "description": "Add a short description for this application.", "icon": "⚡", "url": "https://REPLACE-WITH-LINK-15"},
    {"name": "Application 16", "description": "Add a short description for this application.", "icon": "🧩", "url": "https://REPLACE-WITH-LINK-16"},
]

# -----------------------------
# BRAND COLOURS
# -----------------------------
BOB_ORANGE = "#F7941D"
BOB_ORANGE_DEEP = "#E8531B"
BOB_MAROON = "#8E1B3A"
BOB_NAVY = "#12284C"
BOB_BLUE = "#1E3E73"
BOB_CREAM = "#FFF8F1"
BOB_GREY = "#5B6675"

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown(
    f"""
    <style>
    :root {{
        --bob-orange: {BOB_ORANGE};
        --bob-orange-deep: {BOB_ORANGE_DEEP};
        --bob-maroon: {BOB_MAROON};
        --bob-navy: {BOB_NAVY};
        --bob-blue: {BOB_BLUE};
        --bob-cream: {BOB_CREAM};
        --bob-grey: {BOB_GREY};
    }}

    .stApp {{
        background:
            radial-gradient(circle at 5% 0%, rgba(247,148,29,0.08), transparent 27%),
            linear-gradient(180deg, #fffaf5 0%, #f5f7fb 55%, #eef2f8 100%);
    }}

    .block-container {{
        max-width: 1450px;
        padding-top: 1.6rem;
        padding-bottom: 2.5rem;
    }}

    #MainMenu, footer, header {{
        visibility: hidden;
    }}

    .hero {{
        position: relative;
        overflow: hidden;
        padding: 2rem 2.2rem 1.9rem 2.2rem;
        border-radius: 22px;
        color: white;
        background:
            radial-gradient(circle at 90% 5%, rgba(247,148,29,0.45), transparent 28%),
            linear-gradient(115deg, {BOB_NAVY} 0%, {BOB_BLUE} 57%, {BOB_MAROON} 100%);
        box-shadow: 0 14px 35px rgba(18,40,76,0.18);
        border-bottom: 5px solid {BOB_ORANGE};
        margin-bottom: 1.4rem;
    }}

    .hero::after {{
        content: "";
        position: absolute;
        width: 230px;
        height: 230px;
        border: 1px solid rgba(255,255,255,0.16);
        border-radius: 50%;
        right: -65px;
        top: -100px;
        box-shadow: 0 0 0 24px rgba(255,255,255,0.035),
                    0 0 0 48px rgba(255,255,255,0.025);
        pointer-events: none;
    }}

    .brand-kicker {{
        font-size: 0.78rem;
        letter-spacing: 0.19em;
        text-transform: uppercase;
        color: #ffd6a3;
        font-weight: 800;
        margin-bottom: 0.55rem;
    }}

    .hero h1 {{
        color: #ffffff;
        font-size: clamp(1.8rem, 4vw, 2.75rem);
        font-weight: 800;
        letter-spacing: -0.035em;
        line-height: 1.15;
        margin: 0;
    }}

    .hero p {{
        color: rgba(255,255,255,0.86);
        font-size: 1rem;
        margin: 0.75rem 0 0 0;
        max-width: 760px;
        line-height: 1.6;
    }}

    .hero-chip {{
        display: inline-block;
        margin-top: 1.15rem;
        border: 1px solid rgba(255,255,255,0.28);
        border-radius: 999px;
        padding: 0.38rem 0.8rem;
        color: #fff;
        background: rgba(255,255,255,0.09);
        font-size: 0.8rem;
        font-weight: 600;
    }}

    .section-heading {{
        color: {BOB_NAVY};
        font-size: 1.35rem;
        font-weight: 800;
        margin: 0.4rem 0 0.2rem 0;
    }}

    .section-subtitle {{
        color: {BOB_GREY};
        font-size: 0.91rem;
        margin-bottom: 1.1rem;
    }}

    .app-card {{
        display: flex;
        flex-direction: column;
        min-height: 218px;
        height: 100%;
        box-sizing: border-box;
        padding: 1.15rem 1.1rem 1.05rem 1.1rem;
        border: 1px solid #e1e7f0;
        border-top: 4px solid {BOB_ORANGE};
        border-radius: 16px;
        background: rgba(255,255,255,0.96);
        box-shadow: 0 5px 16px rgba(18,40,76,0.055);
        transition: transform 160ms ease, box-shadow 160ms ease, border-color 160ms ease;
        margin-bottom: 0.2rem;
    }}

    .app-card:hover {{
        transform: translateY(-4px);
        border-color: rgba(247,148,29,0.65);
        box-shadow: 0 12px 24px rgba(18,40,76,0.12);
    }}

    .app-card-top {{
        display: flex;
        align-items: center;
        gap: 0.8rem;
        margin-bottom: 0.8rem;
    }}

    .app-icon {{
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        width: 48px;
        height: 48px;
        border-radius: 13px;
        background: linear-gradient(145deg, #fff0dd, #fff8f1);
        border: 1px solid #ffe0b8;
        font-size: 1.55rem;
    }}

    .app-number {{
        color: {BOB_ORANGE_DEEP};
        text-transform: uppercase;
        font-size: 0.68rem;
        font-weight: 800;
        letter-spacing: 0.12em;
        margin-bottom: 0.18rem;
    }}

    .app-title {{
        color: {BOB_NAVY};
        font-size: 1.02rem;
        font-weight: 800;
        line-height: 1.3;
        overflow-wrap: anywhere;
    }}

    .app-description {{
        color: {BOB_GREY};
        font-size: 0.86rem;
        line-height: 1.55;
        min-height: 3.95rem;
        margin-bottom: 1rem;
    }}

    .app-link {{
        display: block;
        margin-top: auto;
        padding: 0.68rem 0.8rem;
        border-radius: 9px;
        text-align: center;
        text-decoration: none !important;
        color: #ffffff !important;
        background: linear-gradient(100deg, {BOB_ORANGE} 0%, {BOB_ORANGE_DEEP} 100%);
        font-weight: 750;
        font-size: 0.88rem;
        box-shadow: 0 4px 10px rgba(232,83,27,0.16);
        transition: filter 150ms ease, transform 150ms ease;
    }}

    .app-link:hover {{
        filter: brightness(1.04);
        transform: translateY(-1px);
    }}

    .portal-footer {{
        margin-top: 2rem;
        padding: 1rem 0 0.2rem 0;
        border-top: 1px solid #dce3ed;
        color: {BOB_GREY};
        font-size: 0.78rem;
        text-align: center;
    }}

    .portal-footer strong {{
        color: {BOB_NAVY};
    }}

    @media (max-width: 700px) {{
        .block-container {{
            padding-left: 1rem;
            padding-right: 1rem;
            padding-top: 1rem;
        }}
        .hero {{
            padding: 1.5rem 1.25rem;
            border-radius: 16px;
        }}
        .app-card {{
            min-height: 205px;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# HEADER / HERO
# -----------------------------
st.markdown(
    """
    <section class="hero">
        <div class="brand-kicker">Bank of Baroda · Digital Workspace</div>
        <h1>Application Portal</h1>
        <p>
            One central place to access applications, AI solutions, analytics
            dashboards and digital resources.
        </p>
        <span class="hero-chip">● &nbsp; Applications &amp; Digital Solutions</span>
    </section>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# SEARCH
# -----------------------------
st.markdown('<div class="section-heading">Explore Applications</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Choose an application below to open it in a new browser tab.</div>',
    unsafe_allow_html=True,
)

search = st.text_input(
    "Search applications",
    placeholder="Type an application name or description...",
    label_visibility="collapsed",
)

filtered_apps = [
    app for app in APP_LINKS
    if search.strip().lower() in (app["name"] + " " + app["description"]).lower()
]

if not filtered_apps:
    st.info("No applications match your search. Try another keyword.")
else:
    # Four cards per row on wide screens; Streamlit adapts on smaller screens.
    for start in range(0, len(filtered_apps), 4):
        row_apps = filtered_apps[start:start + 4]
        cols = st.columns(4, gap="medium")

        for col, app in zip(cols, row_apps):
            with col:
                # Do not render unconfigured placeholder links as working buttons.
                url = app["url"].strip()
                is_configured = (
                    url.startswith("https://") or url.startswith("http://")
                ) and "REPLACE-WITH-LINK" not in url

                link_html = (
                    f'<a class="app-link" href="{url}" target="_blank" '
                    f'rel="noopener noreferrer">Open Application &nbsp; ↗</a>'
                    if is_configured
                    else '<div class="app-link" style="opacity:0.58;cursor:default;">Add Link in APP_LINKS ↑</div>'
                )

                # Escape user-editable text before embedding it in HTML.
                import html
                name = html.escape(str(app["name"]))
                description = html.escape(str(app["description"]))
                icon = html.escape(str(app["icon"]))
                number = APP_LINKS.index(app) + 1

                st.markdown(
                    f"""
                    <div class="app-card">
                        <div class="app-card-top">
                            <div class="app-icon">{icon}</div>
                            <div>
                                <div class="app-number">APPLICATION {number:02d}</div>
                                <div class="app-title">{name}</div>
                            </div>
                        </div>
                        <div class="app-description">{description}</div>
                        {link_html}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

# -----------------------------
# FOOTER
# -----------------------------
st.markdown(
    """
    <div class="portal-footer">
        <strong>Bank of Baroda</strong> &nbsp;|&nbsp; Application Portal
        <br>
        Internal digital workspace · Use only authorised application links
    </div>
    """,
    unsafe_allow_html=True,
)

import streamlit as st


about_page = st.Page(
    page="views/about_me.py",
    title="À propos",
    icon="👀",
    default=True,
)

# project_1_page = st.Page(
#     page="views/SQL_srs.py",
#     title="SQLingo",
#     icon="😎",
# )

interest_1_page = st.Page(
    page="views/Lectures.py",
    title="Livres",
    icon="📖",
)

interest_2_page = st.Page(
    page="views/games.py",
    title="Compétition",
    icon="🎮",
)

pg = st.navigation(
    {
        "Info": [about_page],
        # "Projets": [project_1_page],
        "Intérêts": [interest_1_page, interest_2_page],
    }
)
st.sidebar.markdown("Made with ☕ by [Fabien](https://www.linkedin.com/in/fabien-hos/)")

pg.run()

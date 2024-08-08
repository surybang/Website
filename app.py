import streamlit as st


about_page = st.Page(
    page="views/about_me.py",
    title="À propos",
    icon=":material/account_circle:",
    default=True,
)

project_1_page = st.Page(
    page="views/SQL_srs.py",
    title="SQL srs",
    icon="😎",
)


pg = st.navigation({"Info": [about_page], "Projects": [project_1_page]})


pg.run()

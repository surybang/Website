import streamlit as st
from forms.contact import contact_form


@st.dialog("Contactez moi")
def show_contact_form():
    contact_form()


col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/id.jpg", width=150)

with col2:
    st.title("Fabien HOS", anchor=False)
    st.write("Data scientist")
    if st.button("📩 Contactez moi"):
        show_contact_form()


# Expériences


# Hard skills

# Soft skills

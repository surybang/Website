import streamlit as st

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("Prénom :")
        email = st.text_input("Email :")
        message = st.text_area("Votre message :")
        submit_button = st.form_submit_button("Envoyer")


        if submit_button:
            st.success("C'est dans la boite !")    

# Contact.py

import os
import re
import requests

import streamlit as st
from dotenv import load_dotenv


load_dotenv()
EMAILJS_SERVICE_ID = os.getenv("SERVICE_ID")
EMAILJS_TEMPLATE_ID = os.getenv("TEMPLATE_ID")
EMAILJS_PUBLIC_KEY = os.getenv("PUBLIC_KEY")
EMAILJS_PRIVATE_KEY = os.getenv("PRIVATE_KEY")

EMAILJS_URL = "https://api.emailjs.com/api/v1.0/email/send"


def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None


def contact_form():
    with st.form("contact_form"):
        name = st.text_input("Prénom :")
        email = st.text_input("Email :")
        message = st.text_area("Votre message :")
        submit_button = st.form_submit_button("Envoyer")

        if submit_button:
            if not name:
                st.error("Veuillez saisir votre prénom.", icon="👮‍♂️")
                st.stop()

            if not email or not is_valid_email(email):
                st.error("Veuillez saisir un email valide.", icon="📧")
                st.stop()

            if not message:
                st.error("Veuillez saisir un message.", icon="👀")
                st.stop()

            data = {
                "service_id": EMAILJS_SERVICE_ID,
                "template_id": EMAILJS_TEMPLATE_ID,
                "user_id": EMAILJS_PUBLIC_KEY,
                "accessToken": EMAILJS_PRIVATE_KEY,
                "template_params": {
                    "from_name": name,
                    "from_email": email,
                    "message": message,
                },
            }

            headers = {"Content-Type": "application/json"}
            response = requests.post(EMAILJS_URL, json=data, headers=headers)

            if response.status_code == 200:
                st.success("C'est dans la boite ! 🚀")
            else:
                st.error(
                    "Une erreur s'est produite lors de l'envoi du message", icon="🤔"
                )
                st.write(response.status_code)
                st.write(response.text)

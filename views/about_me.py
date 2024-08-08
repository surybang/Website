import streamlit as st
from forms.contact import contact_form


@st.dialog("Contactez moi")
def show_contact_form():
    contact_form()


col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/pp.jpg", width=250)

with col2:
    st.title("Fabien HOS", anchor=False)
    st.write("Data scientist")
    col3, col4 = st.columns(2, gap='small', vertical_alignment='center')
    with col3:
        if st.button("📩 Contactez moi"):
            show_contact_form()
    with col4:
        if st.button("📜 Mon CV"):
            st.write('cv')


# Expériences
tab1, tab2, tab3 = st.tabs(["Expériences", "Formations", "Projets"])
with tab1:
    st.subheader("Mes expériences professionnelles", anchor=False)
    with st.expander("Professeur vacataire au CNAM"):
        # st.subheader('Mes expériences professionnelles')
        # tab1, tab2, tab3, tab4 = st.tabs(['Professeur vacataire', 'Data scientist', 'Développeur', "Data analyst"])

        # with tab1:
        # st.markdown(
        #     "<h3>Conservatoire nationale des Arts et métiers</h3>",
        #     unsafe_allow_html=True,
        # )
        st.markdown(
            """
        <div style='font-size: 20px; font-family: Arial, sans-serif; line-height: 1.5;'>
            <p><strong>Je commence en septembre 2024 une nouvelle aventure en tant que professeur vacataire au sein de mon ancien <a href='https://https://formation.cnam.fr/rechercher-par-discipline/master-mega-donnees-et-analyse-sociale-medas--1085595.kjsp' target='_blank'>Master MEDAS. </a></strong></p>
            <p>Il y a deux objectifs à cela :</p>
            <ul>
                <li>Continuer de me former en ayant accès à de précieuses ressources et à un réseau de chercheurs 👨‍🎓🔍</li>
                <li>Satisfaire mon envie de transmettre des connaissances 📚📖</li>
            </ul>
            <p> Les domaines enseignés seront Excel et Python 📈🐍 </p>
            <p>Plus d'infos sur le repos Github <a href='https://github.com/surybang/Cours-MEDAS' target='_blank'>ici</a>.</p>
            <p> <p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with st.expander("Data scientist à la CASDEN Banque populaire"):
        st.markdown(
            "<h3>Conservatoire nationale des Arts et métiers</h3>",
            unsafe_allow_html=True,
        )

    with st.expander("Freelance"):
        st.markdown(
            "<h3>Conservatoire nationale des Arts et métiers</h3>",
            unsafe_allow_html=True,
        )

    with st.expander("Data analyst au Crédit Agricole IDF"):
        st.markdown(
            "<h3>Conservatoire nationale des Arts et métiers</h3>",
            unsafe_allow_html=True,
        )

# Formations

# Hard skills

# Soft skills

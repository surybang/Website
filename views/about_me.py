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
        pdf_file_path = "./assets/CV_FABIEN_HOS_DATA_SCIENTIST.pdf"

        with open(pdf_file_path, "rb") as pdf_file:
            pdf_contents = pdf_file.read()

        # Bouton pour dl le CV
        st.download_button(
            label="📜 Mon CV",
            data=pdf_contents,
            file_name="CV_FABIEN_HOS_DATA_SCIENTIST.pdf",
            mime="application/pdf"
        )
        
# -----------
# Expériences
# -----------
tab1, tab2, tab3, tab4 = st.tabs(["Expériences", "Formations", "Projets", "Compétences"])
with tab1:
    st.subheader("Mes expériences professionnelles", anchor=False)
    with st.expander("Professeur vacataire au CNAM"):
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
            """
            <div style='font-size: 20px; font-family: Arial, sans-serif; line-height: 1.5;'>
            <p> Je suis Data Scientist spécialisé dans <strong>la lutte contre la fraude depuis 2021.</p>
            <p> En tant qu'alternant au sein d'une équipe métier, j'ai réussi à démocratiser l'utilisation du Machine Learning pour améliorer l'activité. </p>
            <p> Faits notables : <p>
            <ul>
                <li> Développement d'une application avec Flask pour lire 2D-DOC afin de lutter contre la fraude documentaire. </li>
                <li> J'ai développé un modèle permettant de détecter <strong>100% des cas de fraude</strong> sur un scénario précis avec de <i>l'open data</i>. 
                Ce modèle génère également peu de cas <i>faux-positifs</i>. </li>
                <li> Je pilote un projet à l'échelle de la banque pour créer et harmoniser une piste d'audit concernant les logs applicatives.
                 Cette piste d'audit est developpée dans le cadre de la lutte contre la fraude interne grâce à une interface de recherche. </li>
                <li> J'ai imaginé des scénarios de fraude qui se sont avérés être positifs. </li>
            </ul>
            <p> Technologies utilisées : SAS, Python, SQL, Git </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with st.expander("Freelance"):
        st.markdown(
            """
            <div style='font-size: 20px; font-family: Arial, sans-serif; line-height: 1.5;'>
            <p>Je me suis exercé à la profession de Développeur en freelance pendant la crise du COVID-19.</p>
            <p>J'ai aidé des artisans et commerçants à transitionner vers des solutions numériques pour leurs activités.</p>
            <p>Mes principales missions étaient les suivantes : </p>
            <ul>
                <li>Développement de sites web </li>
                <li>Développement d'applications en VBA (comptabilité, gestion d'inventaire..)</li>
                <li>Maintenance informatique associée </li>
            </ul>
            <p> Technologies utilisées : PHP, HTML&CSS, JS, VBA </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with st.expander("Data analyst au Crédit Agricole IDF"):
        st.markdown(
            """
            <div style='font-size: 20px; font-family: Arial, sans-serif; line-height: 1.5;'>
            <p>En 2018, j'ai rejoins le Crédit Agricole IDF pendant 1 an en tant que Data analyst en alternance.</p>
            <p>J'avais en charge le recueil des besoins métiers et la création des <i>dashboards</i> automatisés.</p>
            <p>J'ai notamment développé une solution de signature électronique avec l'API de YouSign en VBA.</p> 
            <p>Technologies utilisées : VBA, SQL </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    with st.expander("Développeur chez Technema"):
        st.markdown(
        """
        <div style='font-size: 20px; font-family: Arial, sans-serif; line-height: 1.5;'>
        <p>J'ai rejoins l'entreprise Technema en 2016 pendant 2 ans en tant qu'apprenti développeur</p>
        <p>J'avais en charge le recueil des besoins clients et la création de nouvelles fonctionnalités sur notre ERP.</p>
        <p>J'ai notamment développé un service de tracking des commandes en PHP.</p>
        <p>J'utilisais pour cela des webservices pour mettre à jour les statuts des commandes.</p>
    
        <p>Technologies utilisées : Windev, SQL, PHP, HTML&CSS, JS. </p>
        </div>
        """,
        unsafe_allow_html=True,
        )

# -----------
# Formations
# -----------
with tab2:
    st.subheader("Mes formations", anchor=False)
    with st.expander("2022/2024 - Master MÉDAS en alternance - Conservatoire national des Arts et Métiers"):
        st.markdown(
        """
        Module supplémentaire sur le <a href='https://cedric.cnam.fr/vertigo/Cours/ml2/' target='_blank'>Deep Learning</a>
        """,
        unsafe_allow_html=True,
        )

    with st.expander("2021/2022 - L3 Datamining en alternance - Université Gustave Eiffel"):
        st.markdown(
        """

        """,
        unsafe_allow_html=True,
        )
    
    with st.expander("2018/2019 - L3 MIAGE en alternance - Paris Descartes"):
        st.markdown(
        """

        """,
        unsafe_allow_html=True,
        )

    with st.expander("2016/2018 - BTS SIO-SLAM en alternance - Université Paris-Est Marne-la-Vallée"):
        st.markdown(
        """

        """,
        unsafe_allow_html=True,
        )
    

# -----------
# Compétences
# -----------

#expander hard, soft

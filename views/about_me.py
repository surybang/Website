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
    col3, col4 = st.columns(2, gap="small", vertical_alignment="center")
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
            mime="application/pdf",
        )

# -----------
# Expériences
# -----------
tab1, tab2, tab3, tab4 = st.tabs(
    ["Expériences", "Formations", "Projets", "Compétences"]
)
with tab1:
    st.subheader("Mes expériences professionnelles", anchor=False)
    with st.expander("Professeur vacataire au CNAM"):
        st.markdown(
            """
        Je commence en **septembre 2024** une nouvelle aventure en tant que **professeur vacataire** au sein de mon ancien Master MEDAS.

        Il y a **deux objectifs** à cela :

        1. 👨‍🏫 Poursuivre ma formation grâce à un accès à des ressources précieuses et à un réseau de chercheurs
        2. 📚 Satisfaire mon envie de transmettre des connaissances
        
        Les domaines enseignés sont Excel et Python. 🐍

        Plus d'infos sur le repos Github <a href='https://github.com/surybang/Cours-MEDAS' target='_blank'>ici</a>.
        """,
            unsafe_allow_html=True,
        )

    with st.expander("Data scientist à la CASDEN Banque populaire"):
        st.markdown(
            """
            Je suis Data Scientist spécialisé dans la lutte contre la fraude depuis 2021. En tant qu'alternant au sein d'une équipe métier, j'ai réussi à **démocratiser l'utilisation du Machine Learning** pour améliorer l'activité.

            Faits notables :

            - 💻 Développement d'une application avec Flask pour **lire les 2D-DOC** afin de lutter contre la fraude documentaire
            
            - 💸 Mise en place d'un modèle permettant de **détecter 100 % des cas de fraude sur un scénario précis** à l'aide de l'*open data*, générant également peu de *faux positifs*

            - 🏦 Pilotage d'un projet à l'échelle de la banque visant à **créer et harmoniser une piste d'audit pour les logs applicatifs** dans le cadre de la lutte contre la fraude interne

            - 📝 **Conception de scénarios de fraude externe** qui se sont avérés efficaces
            
            ⌨️ <span style="font-variant-caps: small-caps;">langages de programmation utilisés</span> : SAS, Python et SQL
            

            """,
            unsafe_allow_html=True,
        )

    with st.expander("Développeur en Freelance"):
        st.markdown(
            """
            Je me suis exercé à la profession de Développeur en freelance pendant 1 an et demi. J'ai aidé des artisans et commerçants à **transitionner vers des solutions numériques pour leurs activités.**

            Mes principales missions étaient les suivantes :

            - 💻 Développement de sites web
            - 📊 Développement d'applications en VBA (comptabilité, gestion d'inventaire...)
            - 🔧 Maintenances informatiques associées


            ⌨️ <span style="font-variant-caps: small-caps;">langages de programmation utilisés</span> : PHP, HTML & CSS, JS, VBA
            """,
            unsafe_allow_html=True,
        )

    with st.expander("Data analyst au Crédit Agricole IDF"):
        st.markdown(
            """
            En 2018, j'ai rejoint le Crédit Agricole IDF pendant 1 an en tant que Data Analyst en alternance.

            Mes principales missions étaient les suivantes :

            - 📖 Prise en charge du recueil des besoins métiers
            - 📅 Création des dashboards automatisés
            - 💻 Développement d'une solution de signature électronique avec l'API de YouSign en VBA

            ⌨️ <span style="font-variant-caps: small-caps;">langages de programmation utilisés</span>: VBA, SQL
            """,
            unsafe_allow_html=True,
        )

    with st.expander("Développeur chez Technema"):
        st.markdown(
            """
            En 2016, j'ai rejoint l'entreprise Technema pendant 2 ans en tant qu'apprenti développeur.

            Mes principales missions étaient les suivantes :

            - 📖 Prise en charge **du recueil des besoins clients**
            - 🔧 Création de **nouvelles fonctialités** sur notre ERP
            - 🔎 Développement **d'un service de tracking** web des commandes en PHP en utilisant des webservices afin de mettre à jour les status des commandes
            
            ⌨️ <span style="font-variant-caps: small-caps;">langages de programmation utilisés</span> : Windev, SQL, PHP, HTML & CSS, JS
            """,
            unsafe_allow_html=True,
        )

# -----------
# Formations
# -----------
with tab2:
    st.subheader("Mes formations", anchor=False)
    with st.expander(
        "2022/2024 - Master MÉDAS en alternance - Conservatoire national des Arts et Métiers"
    ):
        st.markdown(
            """
        Enseignements : <a href = 'https://formation.cnam.fr/rechercher-par-discipline/master-mega-donnees-et-analyse-sociale-medas--1085595.kjsp' target= '_blank'> Site web du Master </a>

        Module supplémentaire sur le <a href='https://cedric.cnam.fr/vertigo/Cours/ml2/' target='_blank'>Deep Learning</a> en cours du soir.
        
        Mémoire : L'utilisation des données ouvertes dans la lutte contre la fraude bancaire
        
        **Niveau : Très bien**
        """,
            unsafe_allow_html=True,
        )

    with st.expander(
        "2021/2022 - L3 Datamining en alternance - Université Gustave Eiffel"
    ):
        st.markdown(
            """
        Enseignements : <a href = 'https://formations.univ-gustave-eiffel.fr/licence/detail/decision-et-traitement-de-linformation-data-mining-193' target= '_blank'>Site web de la Licence</a>
        
        **Niveau : Très bien**
        """,
            unsafe_allow_html=True,
        )

    with st.expander("2018/2019 - L3 MIAGE en alternance - Paris Descartes"):
        st.markdown(
            """
        Enseignements : <a href = 'https://iutparis-seine.u-paris.fr/informatique/l3-parcours-miage/' target= '_blank'>Site web de la Licence</a>

        Niveau : Bien
        """,
            unsafe_allow_html=True,
        )

    with st.expander(
        "2016/2018 - BTS SIO-SLAM en alternance - Université Paris-Est Marne-la-Vallée"
    ):
        st.markdown(
            """
        Enseignements : <a href = 'https://www.utec77.fr/bts-services-informatiques-aux-organisations-sio-option-solutions-logicielles-et-applications' target= '_blank'>Site web du BTS</a>
        
        **Niveau : Très bien**
        """,
            unsafe_allow_html=True,
        )

# -----------
# Projets
# -----------
with tab3:
    st.subheader("Mes projets", anchor=False)
    st.markdown(
        """
        Tous mes différents projets sont disponibles sur <a href = 'https://github.com/surybang' target= '_blank'>GitHub</a> mais je vous propose de découvrir ici les plus significatifs.
        
        ---
        """,
        unsafe_allow_html=True,
    )
    with st.expander("SQLingo 😎"):
        st.markdown(
            """
            **SQLingo est une application d'apprentissage du langage SQL basé sur le SRS**.

            **C'est quoi le SRS ?** 🤔
            
            Le SRS est le **Spaced Repetition System**, une méthode d'apprentissage basé la répétition sur un laps de temps relatif à chacun.
            
            Les mêmes exercices sont proposés aux utilisateurs et ces derniers peuvent choisir eux même la durée à partir de laquelle ils pourront les revoir.

            Par exemple, si un exercice est trop simple, ils peuvent choisir de le revoir dans 7 jours et si au contraire un exercice est compliqué, ils peuvent le revoir dès le lendemain.

            J'ai également mis en place un système d'authentification avec le package python "bcrypt". 

            <a href='https://github.com/surybang/SQL-srs' target='_blank'>Lien vers le repos GitHub </a>
            
            Langages de programmation utilisées : Python et SQL   
            Frameworks : DuckDB, Streamlit
            """,
            unsafe_allow_html=True,
        )

    with st.expander("Search Operator 📞"):
        st.markdown(
            """
            **Search Operator est une application pour identifier un opérateur téléphonique à partir d'un numéro de téléphone.**
            
            Plusieurs étapes dans ce projet : 

            1. Je recupère les données de l'ARCEP (l'Autorité française de Régulation des Communications Électroniques et des Postes).

            2. À partir des deux csv récupérés, je fabrique un nouveau dataset avec l'identifiant des numéros de téléphone et le nom des attributaires.
            J'enregistre ensuite ce dernier dans une base de données DuckDB.

            3. J'ai developpées différentes fonctions permettant de rechercher un numéro par son idenfiant ou par le nom de l'opérateur.

            4. Une API développée avec FastAPI vient ensuite servir une interface utilisateur développée avec Streamlit.

            **Pourquoi voudriez-vous identifier un opérateur téléphonique ?** 🤔
            
            Si cette question vous intrigue, je serais ravi de vous fournir une réponse détaillée en entretien. 🧐
            
            <a href='https://github.com/surybang/Search-Operator' target='_blank'>Lien vers le repos GitHub</a>

            Langages de programmation utilisées : Python et SQL
            <br>
            Frameworks : DuckDB, FastAPI, Streamlit
            """,
            unsafe_allow_html=True,
        )

    with st.expander("Scanner 2d-Doc 🔎"):
        st.markdown(
            """
            **Scanner 2d-Doc est une application pour lutter contre la fraude documentaire.**
            
            J'ai développé cette application comme un projet personnel avant de l'intégrer à la Casden Banque Populaire.

            En scannant le code, nous pouvons savoir si le document a été falsifié à l'aide de la signature électronique contenue dans le document. 

            La documentation utilisée est disponible sur <a href='https://ants.gouv.fr/nos-missions/les-solutions-numeriques/2d-doc' target='_blank'>le site officiel du gouvernement français</a>

            Langages de programmation utilisées : Python et bash
            <br>
            Framework : Flask
            """,
            unsafe_allow_html=True,
        )
        st.image("./assets/exemple 2ddoc.JPG", width=125)

# -----------
# Compétences
# -----------

# expander hard, soft

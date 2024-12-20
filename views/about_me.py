'''main page of the app'''
import streamlit as st
from forms.contact import contact_form


@st.dialog("Contactez moi")
def show_contact_form():
    '''show contact_form'''
    contact_form()


col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/pp.jpg", width=250)

with col2:
    st.title("Fabien HOS", anchor=False)
    # st.write("Data scientist")
    col3, col4 = st.columns(2, gap="small", vertical_alignment="center")
    with col3:
        if st.button("📩 Contactez moi"):
            show_contact_form()

    with col4:
        PDF_FILE_PATH = "./assets/CV_FabienHOS_DataScientist.pdf"

        with open(PDF_FILE_PATH, "rb") as pdf_file:
            pdf_contents = pdf_file.read()

        # Bouton pour dl le CV
        st.download_button(
            label="📜 Mon CV",
            data=pdf_contents,
            file_name="CV_FabienHOS_DataScientist.pdf",
            mime="application/pdf",
        )

# st.markdown(
#     """
#     Data Scientist avec 3 ans d'expérience, spécialisé dans la modélisation prédictive et l'optimisation de la chaîne de valeur des données du secteur bancaire.
#     <br>
#     Passionné par la résolution de problématiques métiers et le développement d'applications qui améliorent le quotidien de l'entreprise
#     """, unsafe_allow_html=True)

st.markdown(
    """
    Data Scientist avec 3 ans d'expérience, je souhaite me spécialiser dans le déploiement de solutions Data & IA  \
    ainsi que dans l'optimisation de la chaîne de valeur des données.
    
    Ma passion réside dans la résolution de problèmes spécifiques et le \
    développement d'applications qui optimisent les opérations quotidiennes des entreprises.    
        """,
    unsafe_allow_html=True,
)

# 🔎 Je suis actuellement à la recherche d'un poste en CDI où je pourrai non seulement \
# approfondir mes compétences mais aussi apporter une contribution significative à l'entreprise.  
# -----------
# Expériences
# -----------
tab1, tab2, tab3, tab4 = st.tabs(
    ["Expériences", "Formations", "Projets", "Compétences"]
)
with tab1:
    st.subheader("Mes expériences professionnelles", anchor=False)

    with st.expander("Data scientist à la CASDEN Banque populaire"):
        # + de missions, écriture de programmes SAS, traduction SAS -> Python,
        st.markdown(
            """
            Je suis Data Scientist spécialisé dans la lutte contre la fraude et l'optimisation des processus métiers des risques non-financiers depuis 2021. 
            
            En tant qu'alternant au sein d'une équipe métier, j'ai réussi à **démocratiser l'utilisation du Machine Learning** pour améliorer l'activité.
            
            Maintenant que je suis en **CDI** au sein du service data, je me concentre sur le déploiement en production et l'automatisation. 

            Faits notables :

            - 💻 Développement d'une application avec Flask pour **lire les 2D-DOC** afin de lutter contre la fraude documentaire
            
            - 💸 Développement d'un modèle permettant de **détecter 100 % des cas de fraude sur un scénario précis** à l'aide de l'*open data*, générant également peu de *faux positifs*

            - 🏦 Pilotage d'un projet à l'échelle de la banque visant à **créer et harmoniser une piste d'audit pour les logs applicatifs** dans le cadre de la lutte contre la fraude interne

            - 📝 **Conception de scénarios de fraude externe** qui se sont avérés efficaces
            
            ⌨️ <span style="font-variant-caps: small-caps;">langages de programmation utilisés</span> : SAS, Python et SQL
            

            """,
            unsafe_allow_html=True,
        )

    with st.expander("Professeur vacataire au CNAM"):
        st.markdown(
            """
        Je commence en **septembre 2024** une nouvelle aventure en tant que **professeur vacataire** au sein de mon ancien Master MEDAS.

        Il y a **deux objectifs** à cela :

        - 👨‍🎓 Poursuivre ma formation grâce à un accès à des ressources et à un réseau de chercheurs
        - 📚 Satisfaire mon envie de transmettre des connaissances
        
        Les domaines enseignés sont Excel et Python. 🐍

        Plus d'infos sur le repos Github <a href='https://github.com/surybang/Cours-MEDAS' target='_blank'>ici</a>.
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

        **Niveau : Bien**
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
        Vous pouvez consulter l'ensemble de mes projets sur <a href='https://github.com/surybang' target='_blank'>GitHub</a>.
        
        Les projets présentés se concentrent sur le **Data engineering**, domaine dans lequel je souhaite m'améliorer pour devenir un **Data Scientist aussi complet que possible**.
        
        D'autres projets, plus centrés sur la **Data Science**, seront ajoutés ultérieurement. Pour le moment, vous pouvez explorer mes notebooks R sur GitHub.

        ---
        """,
        unsafe_allow_html=True,
    )
    with st.expander("SQLingo 😎"):
        st.markdown(
            """
            **SQLingo est une application d'apprentissage du langage SQL basé sur le SRS**

            **C'est quoi le SRS ?** 🤔

            Le **SRS** ou **Spaced Repetition System** est une méthode d'apprentissage qui utilise la répétition d'exercices à intervalles réguliers adaptés aux besoins de chaque utilisateur. Les exercices sont révisés selon la préférence de l'utilisateur, par exemple, un exercice facile peut être programmé pour une révision dans sept jours, tandis qu'un exercice plus difficile peut être revu dès le lendemain.

            **Accès à l'application**

            L'application dispose également d'un système d'authentification. Pour un accès rapide en mode "invité", utilisez les identifiants suivants : **nom d'utilisateur/mot de passe : guest**.

            <a href='https://github.com/surybang/SQL-srs' target='_blank'>Lien vers le repos GitHub </a>
            
            <a href='https://sqlingo2.streamlit.app/' target='_blank'>Lien vers l'application sur le Community Cloud de Streamlit</a>
            
            <span style="font-variant-caps: small-caps;">langages de programmation utilisés</span> : Python et SQL   
            <span style="font-variant-caps: small-caps;">frameworks</span> : DuckDB, Streamlit
            """,
            unsafe_allow_html=True,
        )

    with st.expander("Search Operator 📞"):
        st.markdown(
            """
            **Search Operator est une application pour identifier un opérateur téléphonique à partir d'un numéro de téléphone.**
            
            Plusieurs étapes dans ce projet : 

            1. J'ai récupéré les données de l'ARCEP (l'Autorité française de Régulation des Communications Électroniques et des Postes).

            2. À partir des deux csv récupérés, je fabrique un nouveau dataset avec l'identifiant des numéros de téléphone et le nom des attributaires.
            J'enregistre ensuite ce dernier dans une base de données DuckDB.

            3. J'ai developpé différentes fonctions permettant de rechercher un numéro par son identifiant ou par le nom de l'opérateur.

            4. Une API développée avec FastAPI vient ensuite servir une interface utilisateur développée avec Streamlit.

            **Pourquoi voudriez-vous identifier un opérateur téléphonique ?** 🤔
            
            Si cette question vous intrigue, je serais ravi de vous fournir une réponse détaillée en entretien. 🧐
            
            <a href='https://github.com/surybang/Search-Operator' target='_blank'>Lien vers le repos GitHub</a>

            <span style="font-variant-caps: small-caps;">langages de programmation utilisés</span> : Python et SQL
            <br>
            <span style="font-variant-caps: small-caps;">frameworks</span> : DuckDB, FastAPI, Streamlit
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

            <span style="font-variant-caps: small-caps;">langages de programmation utilisés</span> : Python et Bash
            <br>
            <span style="font-variant-caps: small-caps;">frameworks</span> : Flask
            """,
            unsafe_allow_html=True,
        )
        st.image("./assets/exemple 2ddoc.JPG", width=125)

# -----------
# Compétences
# -----------

with tab4:
    with st.expander("Hard skills"):
        st.markdown(
            """
        #### Programmation 👨🏼‍💻
        - **Python** : Maitrise des packages Pandas et Seaborn, j'utilise également NumPy et Matplotlib.
        - **SAS** : Maitrise du langage.
        - **SQL** : Maitrise des concepts généraux. (Joins, Windows Functions, Group, CTE ...)
        - **R** : Maitrise du langage, utilisé dans mon parcours universitaire uniquement.
        - **PySpark** : Apprentissage en cours.
        - **PyTorch et TensorFlow** : Connaissance de base pour le deep learning avec des projets universitaires.

        #### Base de données 🛢️
        - **PostgreSQL**
        - **Oracle**
        - **DuckDB & SQLite3**
        - **MongoDB**

        #### Modélisations prédictives 🤖
        - Connaissances fondamentales sur les techniques de **régressions** et de **classifications**.
        - Expérience avec des librairies telles que **SciPy**, **Scikit-learn** et **XGBoost** pour l'implémentation de modèles.
        
        #### Cloud ☁️
        - Bases sur Microsoft Azure.
                     
        #### GenAI 🧠
        - **Ollama et Hugging Face** : Apprentissage en cours, je sais récupérer des modèles et les utiliser localement.
                    
        #### Analyses de données 📊
        - **Compétences en analyses descriptives** : Utilisation de statistiques descriptives , facilitant une compréhension rapide des tendances, des moyennes et de la variabilité au sein des jeux de données.
        - **Nettoyage de données** : Capacité à traiter et à nettoyer les ensembles de données, incluant la gestion des valeurs manquantes, la correction des erreurs de format et l'élimination des doublons, afin de garantir la précision des analyses. 
        - **Manipulation de données** : Utilisation de SQL et Pandas pour effectuer des opérations.
        - **Visualisation de données** : Utilisation de Seaborn, Plotly et Streamlit.
        
        #### Gestion du code source 🧙‍♂️
        - Git : Maitrise des essentiels.
                    
        #### MLOps ⚙️
        - **ML Flow** : Apprentissage en cours.
        - **Docker** : Apprentissage en cours, je sais utiliser une image et écrire un Dockerfile.
        - **CI/CD** : Familiarité avec les pipelines d'intégration et de déploiement continus pour maintenir la qualité du code.
        - **Airflow**
        
        """
        )

    with st.expander("Soft skills"):
        st.markdown(
            """
        ##### Créativité 💡
        Ma créativité se manifeste dans ma capacité à identifier et à intégrer des ressources externes pour résoudre des problèmes complexes.
        <br> 
        Un exemple notable est mon approche lors d'un projet de lutte contre la fraude, où j'ai utilisé des données open data pour développer des indicateurs innovants qui ont significativement amélioré la performance du modèle.

        ##### Esprit critique 🧠
        Doté d'un esprit critique, je ne me contente pas de prendre les observations pour acquis. Je m'engage à analyser en profondeur et à questionner les données pour en extraire les insights les plus pertinents, garantissant ainsi l'intégrité et la précision de nos projets.

        ##### Force de proposition 👊
        En tant qu'unique référent data de mon service pendant mon alternance, j'ai pris l'initiative de proposer et d'implémenter de nouvelles méthodes de travail, conduisant à des améliorations significatives de nos processus.

        ##### Organisation 🟧
        Ma capacité à organiser et planifier le flux de travail se manifeste par une  gestion du temps et une approche méthodique pour segmenter les étapes d'un projet, assurant une exécution efficace.

        ##### Communication 📢
        Je communique efficacement avec les équipes métiers et techniques, facilitant un dialogue constructif et une compréhension mutuelle. 
        <br>
        Mon expérience en tant que professeur vacataire enrichit cette compétence.
        """,
            unsafe_allow_html=True,
        )

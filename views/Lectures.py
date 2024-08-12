import streamlit as st

st.subheader("Mes lectures 📚")
st.write(
    """
        Je suis un lecteur passionné, particulièrement attiré par les ouvrages techniques qui me permettent de constamment approfondir mes connaissances.
         
        J'apprécie de me plonger dans des lectures qui explorent des concepts complexes liés aux statistiques, à l'analyse de données, et à la programmation en général.
        
        Ces lectures m'aident à affiner mes compétences analytiques et à rester au fait des dernières avancées dans mon domaine. 
         
        Elles nourrissent également ma réflexion et mon approche méthodologique, que j'applique avec rigueur dans mes projets professionnels 
        pour trouver des solutions innovantes et efficaces.
         """
)


tab1, tab2, tab3, tab4 = st.tabs(
    ["Data science", "Data engineering", "Poésie", "Autres"]
)
with tab1:
    with st.expander("The elements of Statistical Learning"):
        col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
        with col1:
            st.image("./assets/EOSL.jpeg", use_column_width="auto")

        with col2:
            st.markdown(
                """
                <strong>The Elements of Statistical Learning </strong>
                <p>Ce livre contient toutes les connaissances à acquérir pour un data scientist.</p>
                """,
                unsafe_allow_html=True,
            )

    with st.expander("Data Mining et statistique décisionnelle"):
        col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
        with col1:
            st.image("./assets/DMSD.jpg", use_column_width="auto")

        with col2:
            st.markdown(
                """
                <strong>Data Mining et statistique décisionnelle</strong>
                <p>Ce livre contient toutes les connaissances à acquérir pour un data scientist.</p>
                """,
                unsafe_allow_html=True,
            )

    with st.expander("Big Data, Machine Learning et Apprentissage profond"):
        col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
        with col1:
            st.image("./assets/DMSD.jpg", use_column_width="auto")

        with col2:
            st.markdown(
                """
                <strong>Big Data, Machine Learning et Apprentissage profond</strong>
                <p>Ce livre contient toutes les connaissances à acquérir pour un data scientist.</p>
                """,
                unsafe_allow_html=True,
            )

    with st.expander("Hands on Machine Learning with Scikit-Learn and TensorFlow"):
        col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
        with col1:
            st.image("./assets/DMSD.jpg", use_column_width="auto")

        with col2:
            st.markdown(
                """
                <strong>Hands on Machine Learning with Scikit-Learn and TensorFlow</strong>
                <p>Ce livre contient toutes les connaissances à acquérir pour un data scientist.</p>
                """,
                unsafe_allow_html=True,
            )

    with st.expander("The Hundred-page Machine Learning book"):
        col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
        with col1:
            st.image("./assets/DMSD.jpg", use_column_width="auto")

        with col2:
            st.markdown(
                """
                <strong>Hands on Machine Learning with Scikit-Learn and TensorFlow</strong>
                <p>Ce livre contient toutes les connaissances à acquérir pour un data scientist.</p>
                """,
                unsafe_allow_html=True,
            )

    with tab2:
        with st.expander(
            "Designing Machine learning systems an iterative process for production"
        ):
            col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
            with col1:
                st.image("./assets/DMSD.jpg", use_column_width="auto")

            with col2:
                st.markdown(
                    """
                    <strong>Hands on Machine Learning with Scikit-Learn and TensorFlow</strong>
                    <p>Ce livre contient toutes les connaissances à acquérir pour un data scientist.</p>
                    """,
                    unsafe_allow_html=True,
                )
        with st.expander("Fundamentals of Data Engineering"):
            col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
            with col1:
                st.image("./assets/DMSD.jpg", use_column_width="auto")

            with col2:
                st.markdown(
                    """
                    <strong>Hands on Machine Learning with Scikit-Learn and TensorFlow</strong>
                    <p>Ce livre contient toutes les connaissances à acquérir pour un data scientist.</p>
                    """,
                    unsafe_allow_html=True,
                )

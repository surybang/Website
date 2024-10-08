import streamlit as st

st.subheader("Mes lectures 📚")


tab1, tab2 = st.tabs(["Data science", "Data engineering"])
with tab1:
    with st.expander("The Elements of Statistical Learning"):
        col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
        with col1:
            st.image("./assets/THE_EOS.png", use_column_width="auto")

        with col2:
            st.markdown(
                """
                **The Elements of Statistical Learning**
                
                Auteurs :
                - Trevor Hastie
                - Robert Tibshirani
                - Jerome Friedman
                """,
                unsafe_allow_html=True,
            )

    with st.expander("Data Mining et statistique décisionnelle"):
        col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
        with col1:
            st.image("./assets/Data_mining.png", use_column_width="auto")

        with col2:
            st.markdown(
                """
                **Data Mining et statistique décisionnelle**
                
                Auteur :
                - Stéphane Tufféry

                Les livres associés, qui contiennent des cas pratiques en R et SAS sont également très intéressants. \
                Ils ont été essentiels pour débuter mon apprentissage et continuent de me servir en tant que références.

                """,
                unsafe_allow_html=True,
            )

    with st.expander("Big Data, Machine Learning et Apprentissage profond"):
        col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
        with col1:
            st.image("./assets/BigData.png", use_column_width="auto")

        with col2:
            st.markdown(
                """
                **Big Data, Machine Learning et Apprentissage profond**
                
                Auteur :
                - Stéphane Tufféry
                """,
                unsafe_allow_html=True,
            )

    with st.expander("Hands on Machine Learning with Scikit-Learn and TensorFlow"):
        col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
        with col1:
            st.image("./assets/Hands_on_machine.png", use_column_width="auto")

        with col2:
            st.markdown(
                """
                **Hands on Machine Learning with Scikit-Learn and TensorFlow**
                
                Auteur :
                - Aurélien Géron
                """,
                unsafe_allow_html=True,
            )

    with st.expander("The Hundred-page Machine Learning book"):
        col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
        with col1:
            st.image("./assets/hundred_page.png", use_column_width="auto")

        with col2:
            st.markdown(
                """
                **The Hundred-page Machine Learning book**
                
                Auteur :
                - Andriy Burkov
                """,
                unsafe_allow_html=True,
            )

    with tab2:
        with st.expander(
            "Designing Machine learning systems an iterative process for production"
        ):
            col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
            with col1:
                st.image("./assets/designing_machine.png", use_column_width="auto")

            with col2:
                st.markdown(
                    """
                    **Designing Machine learning systems an iterative process for production**
                    
                    Auteur :
                    - Chip Huyen
                    """,
                    unsafe_allow_html=True,
                )
        with st.expander("Fundamentals of Data Engineering"):
            col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
            with col1:
                st.image("./assets/fundamental_of_data.png", use_column_width="auto")

            with col2:
                st.markdown(
                    """
                    **Fundamentals of Data Engineering**
                    
                    Auteurs :
                    - Joe Reis 
                    - Matt Housley
                    """,
                    unsafe_allow_html=True,
                )

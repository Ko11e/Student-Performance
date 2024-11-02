import streamlit as st
from src.data_management import load_student_data


def page_summary_body():

    df = load_student_data()

    st.write("### Quick Project Summary")

    st.write(
        """
        Something that is important in our society is education. It is of great 
        importance to know how you can influence the outcome of your studies. 
        This is something that both students and educators are interested in. 
        In this project, we show which parameters can have the greatest impact 
        so that all students have as equal conditions as possible to best optimise 
        their results. 

        Below you can read about the three Business Requirements given by the school
        district. Various techniques from Machine Learning have been used to address 
        business concerns. We performed exploratory data analysis, trained 
        classification models, and trained a regression model.
        """
    )

    st.write(
        """
        _For additional information, please visit and **read** the [Project
        README file](https://github.com/Ko11e/Student-Performance/blob/main/README.md)._
        """
    )

    st.success(
        """
        **Dataset Attributes:** 
        
        The dataset contains 20 features, with 'Exam_Score' as the target. 

        **Dataset Observations:** 
        
        The dataset contains a total of 6607 observations.
        """
    )
    if st.checkbox("Inspect dataset"):
        st.write(
            f"Below can the first 10 rows of the dataset."
        )
        st.write(df.head(10))

    st.write("---")

    st.info(
        """
        **The project addresses three key business requirements:**

        _**Business Requirement 1:**_ 

        The client wants to understand which factors have the most significant impact on students' grades. 
        They seek a visual representation and exploration of the correlations between these factors and performance metrics such as grades. This will provide insights for educators and policymakers on elements that may influence student success.

        _**Business Requirement 2:**_

        The client aims to predict students' exam scores based on their resources.

        """
    )


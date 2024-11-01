import streamlit as st


def page_analysis_body():
    st.write(
        """
        ## Exploratory Analysis of Student Prefomence data
        """
    )
    st.info(
        """
        Welcome to the Exploratory Analysis of Student Performance 
        Data. This dataset has been obtained from Kaggle, where it is 
        indicated that it was genarated and created for learning 
        purposes. Since this dataset does not contain real data, 
        many, if not all, of the features are typically normally 
        distributed within the same range.

        However, some features show a correlation with the target 
        variable, Exam_Score. One such feature is Attendance, which 
        represents the percentage of lectures attended by the 
        student. The remaining data has also been analyzed to support
        data-driven decisions, enhancing our understanding and 
        improving treatment strategies
        """ 
    )

    st.write('-----')
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
        distributed within the same range. There is nothing that stands 
        out in the material which affects the ability to predict trends.
        This makes the analysis very narrow and difficult to interpret.

        However, some features show a correlation with the target 
        variable, Exam_Score. One such feature is Attendance, which 
        represents the percentage of lectures attended by the 
        student. The remaining data has also been analyzed to support
        data-driven decisions, enhancing our understanding and 
        improving treatment strategies
        """ 
    )

    st.write('-----')

    st.warning(
        """
        #### Business Requirement 1: Data Visualisation and Correlation Study
        We need to conduct a correlation study to identify which features are 
        most closely related to the target variable. A Pearson correlation
        will help us determine linear relationships between numerical 
        variables. In contrast, a Spearman correlation will assess the 
        monotonic relationships between variables. Additionally, we can use 
        a Predictive Power Score study to explore relationships between 
        attributes, regardless of their data type.
        """
    )

    st.write(
        """
        ###Summary of Correlation Analysis
        The correlations within the dataset were analyzed using both 
        Spearman and Pearson correlation methods, followed by a Predictive 
        Power Score (PPS) analysis. To prepare the data for the Spearman 
        and Pearson correlations. Both methods identified the same 
        correlations between the features and the target variables.
        """
    )
    # Vizualise data

    st.write('----')

    st.info(
        """
        * By studying the correlation between Exam_score, Attendance
        and stuidied houres it can be seen the the student will have 
        a result that will end up in the fourth quantile. Due there are 
        no significat diffrence in the tail of the target.
        * The median value for the students parents education level are close 
        to the same. But a slite diffrence in the placement of the box shows a 
        slite tendens the studets preform better if the parent have a high education level.

        """
    )
    # Vizualisera data
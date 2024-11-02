import streamlit as st
from src.machine_learning.plot_functions import (
    CalculateCorrAndPPS,
    heatmap_corr,
    heatmap_pps
)
from src.data_management import load_student_data


def page_analysis_body():

    df = load_student_data()

    to_plot = [

    ]

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
        ### Business Requirement 1:
        #### Data Visualisation and Correlation Study
        
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
        ### Summary of Correlation Analysis

        The correlations within the dataset were analyzed using both 
        Spearman and Pearson correlation methods, followed by a Predictive 
        Power Score (PPS) analysis. To prepare the data for the Spearman 
        and Pearson correlations. Both methods identified the same 
        correlations between the features and the target variables.
        """
    )

    options = st.selectbox(
        '**Select what you want to display?**',
        ('Pearson correlation', 'Spearman correlation', 'PPS analysis'),
        placeholder="Select the plot here",)

    df_corr_pearson, df_corr_spearman, pps_matrix = CalculateCorrAndPPS(df)  
    if options == "Pearson correlation":
        st.write("-----")
        heatmap_corr(df=df_corr_spearman, threshold=0.2)
    if options == "Spearman correlation":
        st.write("----")
        heatmap_corr(df=df_corr_pearson, threshold=0.2)
    if options == "PPS analysis":
        st.write("-----")
        heatmap_pps(df=pps_matrix, threshold=0.1)

    st.write('----')

    st.info(
        """
        * By studying the correlation between Exam_score, Attendance
        and stuidied houres it can be seen that the student will have 
        a result that will end up in the fourth quantile. Though there are 
        no significat diffrence in the tail of the target.
        * The median value for the students parents education level are close 
        to the same. But a slite diffrence in the placement of the box shows a 
        slite tendens the studets preform better if the parent have a high education level.
        * As disussed before is the majority of the features normal distrubution 
        oven the Exam Score make it hard to find correlation and trends.  

        """
    )
    
    if st.checkbox("Vizualisera data"):
        selected_variable = st.radio(
            "Select a variable to explore:", 
            to_plot,
            index=0
        )

        if selected_variable == "Parallel Plot":
            display_parallel_plot(df_eda)
        else:
            st.write(f"### Plots for: {selected_variable}")
            display_selected_plots(df_eda, selected_variable,
                                   "Live birth occurrence")

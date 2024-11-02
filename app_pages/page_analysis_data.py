import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import ppscore as pps
import plotly.express as px
import matplotlib.patheffects as path_effects
import matplotlib.pyplot as plt

from src.machine_learning.plot_functions import (
    add_median_labels,
    CalculateCorrAndPPS,
    heatmap_corr,
    heatmap_pps
)
from src.data_management import load_student_data


def page_analysis_body():

    df = load_student_data()

    to_plot = [
        "Correlation Studied Houres, Attendance and Exam score ",
        "Distribution Score, Parental education level",
        "Interactive Plot"
    ]

    y_varibels = [
        'Distance_from_Home',
        'School_Type',
        'Teacher_Quality', 
        'Family_Income',
        'Parental_Involvement',
        'Extracurricular_Activities',
        'Exam_Score'
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
    st.write(
        """
        Below are some conclusions that have been made by
        performing a data annalysis and correlation study and dataset. 
        """
    )

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

        if selected_variable == "Interactive Plot":
            dfe = df.filter(y_varibels)

            display_interactive_plot(dfe, y_varibels)

        elif selected_variable == "Correlation Studied Houres, Attendance and Exam score ":
            st.write(
            """
            _**Distrubusion oven Studied Houres, Attendance and Exam score**_
            """
            )
            plt.figure(figsize=(12, 6))
            sns.scatterplot(data=df, x="Exam_Score", y="Hours_Studied", hue="Attendance")
            st.pyplot(plt.gcf())

        elif selected_variable == "Distribution Score, Parental education level":
            st.write("_**Distribution of exam scores based on parental education levels**_")
        
            plt.figure(figsize=(12, 6))
        
            ax = sns.boxplot(data=df, x='Exam_Score', hue='Parental_Education_Level')
            add_median_labels(ax)
            st.pyplot(plt.gcf())
        

def display_interactive_plot(dfe, y):
    try:
        y.remove('Exam_Score')
    except:
        pass
    
    y_axis_val = st.selectbox('Select the Y-axis', options=y )

    plot = px.box(dfe, x='Exam_Score', y=y_axis_val)
    st.plotly_chart(plot, use_container_width=True)
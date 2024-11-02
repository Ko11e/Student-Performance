import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from src.data_management import load_student_data
from src.machine_learning.plot_functions import add_median_labels

def page_hypothesis_o_validation_body():

    df = load_student_data()

    st.write(
        "This is the first page"
    )

    st.success(
        """
        ## Hypothesis 1
        If students have high attendance and spend a significant number of hours studying, they are more likely to achieve a higher grade (over 75).
        """
    )
    st.warning(
        """
        #### Conclusion
        The data indicates that there in a trende that shows of 
        the student having a higher changes of getting a higher Exam
        Score if they a higher attendance and houres stuidied. But 
        there are nothigh that support the statmate the student 
        will have a higher change to get a score that is higher 
        then 75.

        This will conclude that this hypothesis will be rejected
        """
    )
    if st.checkbox("Visualize Graf"):
        st.write("")
        
        plt.figure(figsize=(12, 6))
        
        sns.scatterplot(data=df, x="Exam_Score", y="Hours_Studied", hue="Attendance")
        st.pyplot(plt.gcf())

    st.write("---")

    st.success(
        """
        ## Hypothesis 2
        The education level of the students' parents does not have 
        a significant impact on the students' final exam scores.
        """
    )
    st.warning(
        """
        #### Conclusion
        The median value for the education level of students' parents is 
        relatively similar, but a closer look reveals a slight trend. Students 
        tend to have better Exam score when their parents have 
        higher educational backgrounds. However, the trend is so smale that 
        it have no significat infuance in the students Exam score. There is 
        also shown that Parental_Education_Level is one of the importent features when 
        trying to predict if student can impove theire score.
        This lead to that this hypothersis will be redject since the data shows 
        a smale trend that disproves the hypothesis. 
        """
    )
    if st.checkbox("Visualize Data"):
        st.write("")
        
        plt.figure(figsize=(12, 6))
        
        ax = sns.boxplot(data=df, x='Exam_Score', hue='Parental_Education_Level')
        add_median_labels(ax)
        st.pyplot(plt.gcf())
    
    st.write("---")



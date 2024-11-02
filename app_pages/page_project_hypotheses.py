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
        st.write(
            """
            _**Relationship between hours Studied and Exam scores with
            
        Distrubusion oven Studied Houres, Attendance and Exam score**_
            """
        )
        st.write(
            """
            This graf show a correlation between the Studied Houres, Attendance and the resulte
            from the Student exam score. In the cluster can a distict color diffrence been since 
            indicating a trend that the student result would be higher with a high attendance 
            and number of stuided houres. This visual highlights the combined influence of 
            study time and attendance on student performance.
            """
        )
        
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
        relatively similar and the range and outliers indicate that students' 
        exam performance can vary widely within each parental education category, 
        but a closer look reveals a slight trend. Students tend to have better 
        Exam score when their parents have higher educational backgrounds. However, 
        the trend is so smale that it have no significat infuance in the students 
        Exam score. This lead to that this hypothersis will be redject since the data shows 
        a smale trend that disproves the hypothesis. 
        """
    )
    if st.checkbox("Visualize Data"):
        st.write("_**Distribution of exam scores based on parental education levels**_")
        st.write(
            """
            In the graph belowe shows a boxplot where it can be seen that the media values are
            relatively similar. The box shows the interquartile range (IQR), from the 
            25th percentile (bottom edge) to the 75th percentile (top edge) and in this boxes
            there a smal swift to  higher score  if the parent have a higher education level.
            """
        )
        
        plt.figure(figsize=(12, 6))
        
        ax = sns.boxplot(data=df, x='Exam_Score', hue='Parental_Education_Level')
        add_median_labels(ax)
        st.pyplot(plt.gcf())
    
    st.write("---")



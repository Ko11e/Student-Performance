import streamlit as st

def page_hypothesis_o_validation_body():
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
    st.success(
        """
        ## Hypothesis 3
        For the students to improve their scores, students need to focus on 
        attending lectures, participating in tutoring sessions, 
        and increasing their study hours.
        """
    )
    st.warning(
        """
        #### Conclusion
        In the pipline where the model is train to see if the student can imporve 
        there score it can be seen that the the more important feature for the 
        prediction is the students success is 
        * Attendance
        * Tutoring_Sessions
        * Hours_Studied
        * Sleep_Hours
        * Physical_Activity
        * Parental_Education_Level
        * Parental_Involvement

        Where the first three features are the ones with the highers influance 
        on the training of the model. In conclusion tha data strongly support 
        the hypothesis and will **not** be redjected.

        """
    )



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
        The education level of the students' parents does not have a significant impact on the students' final exam scores.
        """
    )
    st.warning(
        """
        #### Conclusion
        
        """
    )
    st.success(
        """
        ## Hypothesis 3
        For the students to improve their scores, students need to focus on attending lectures, participating in tutoring sessions, and increasing their study hours.
        """
    )
    st.warning(
        """
        #### Conclusion
        """
    )



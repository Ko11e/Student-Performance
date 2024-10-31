import streamlit as st

def page1_body():
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
        """
    )
    st.success(
        """
        ## Hypothesis 2
        he education level of the students' parents does not have a significant impact on the students' final exam scores.
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



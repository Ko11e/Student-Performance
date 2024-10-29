import streamlit as st


def page_summary_body():

    st.write("### Quick Project Summary")

    st.success(
        """
        **The project addresses two key business requirements:**
        """
    )

    st.write(
        """
        * For additional information, please visit and **read** the [Project
        README file](https://github.com/Ko11e/Student-Performance/blob/main/README.md).
        """
    )

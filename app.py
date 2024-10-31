import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_project_hypotheses import page1_body
from app_pages.page_ml_student_exam_score_predictore import page2_body


# Create an instance of the app
app = MultiPage(app_name="Exam Score Predictor")

app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Project Hypothesis and Validation", page1_body)
app.add_page("Exploratory Analysis of the Data", page2_body)
# app.add_page("ML: Predict Success", page_ml_success_predictor_body)
# app.add_page("IVF Success Predictor", page_live_predictor_body)

app.run()
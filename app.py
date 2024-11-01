import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_analysis_data import page_analysis_body
from app_pages.page_project_hypotheses import page_hypothesis_o_validation_body
from app_pages.page_predictore import ML_prediction_exam_score
from app_pages.page_ml_student_exam_score_predictore import page_ML_predict_student_exam_body


# Create an instance of the app
app = MultiPage(app_name="Exam Score Predictor")

app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Project Hypothesis and Validation", page_hypothesis_o_validation_body)
app.add_page("Exploratory Analysis of the Data", page_analysis_body)
app.add_page("Live Predictor", ML_prediction_exam_score)
app.add_page("ML: Predict Exam score and Improv Score", page_ML_predict_student_exam_body)


app.run()
import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_1 import page1_body
from app_pages.page_2 import page2_body


# Create an instance of the app
app = MultiPage(app_name="Exam Score Predictor")

app.add_page("Quick Project Summary", page_summary_body)
app.add_page("The first test page", page1_body)
app.add_page("The second test page", page2_body)
# app.add_page("ML: Predict Success", page_ml_success_predictor_body)
# app.add_page("IVF Success Predictor", page_live_predictor_body)

app.run()
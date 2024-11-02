import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.data_management import (
    load_student_data,
    load_pkl_file
)
# from src.machine_learning.evaluate_regression import regression_performance
from src.machine_learning.prediction_of_score import predict_score

def ML_prediction_exam_score():
    st.write(
        "This is where the prediction wighet goning to be"
    )

    version = 'v1'
    exam_score_pipe_model = load_pkl_file(
        f'outputs/ml_pipeline/predict_exam_score/{version}/clf_pipeline.pkl')
    # sale_price_features = (
    #     pd.read_csv(
    #         f"outputs/ml_pipeline/predict_sale_price/{vsn}/X_train.csv")
    #     .columns
    #     .to_list()
    # )

    st.write("### ")
    # st.info()

    # st.info()

    # st.info()

    # Display plots based on selected variable or Parallel Plot
    st.write("### Exam Score Predictor Tool:")
    X_live = DrawInputsWidgets_Exam()
    if st.button("Run Predictive Analysis"):
        students_score_prediction = predict_score(
            X_live, exam_score_pipe_model)
        exam_score_final_pred = '{:.0f}'.format(students_score_prediction[0])
        st.write("* The model has predicted that the most plausible Exam score result is:")
        st.write(f"**{exam_score_final_pred}**")

    st.write("---")


    st.write("---")


def DrawInputsWidgets_Exam(): # sale_price_features):
    df = load_student_data()
    percentageMin, percentageMax = 0.4, 2.0

    # Specify the four features for user input
    user_input_features = [
        "Parental_Education_Level", "Teacher_Quality", "Distance_from_Home",
        "Hours_Studied", "Attendance", "Gender", "Learning_Disabilities",
        "Physical_Activity", "Peer_Influence", "School_Type", "Family_Income",
        "Tutoring_Sessions", "Internet_Access", "Motivation_Level",
        "Previous_Scores", "Sleep_Hours", "Extracurricular_Activities",
        "Access_to_Resources", "Parental_Involvement"]
    X_live = pd.DataFrame([], index=[0])

    for feature in user_input_features:
        if feature in df.columns:
            if (df[feature].dtype == 'int64' or
                  df[feature].dtype == 'float64'):
                min_value = int(df[feature].min() * percentageMin)
                max_value = int(df[feature].max() * percentageMax)
                median_value = int(df[feature].median())
                st_widget = st.number_input(
                    label=f'{feature}',
                    min_value=min_value,
                    max_value=max_value,
                    value=median_value,
                    step=1
                )
            else:
                unique_values = df[df[feature].notna()][feature].dropna().unique()
                st_widget = st.selectbox(
                    label=f'{feature}',
                    options=unique_values
                )
            X_live[feature] = st_widget

    # Fill the remaining features with default values
    # for feature in sale_price_features:
    #     if feature not in user_input_features:
    #         if feature in df.columns:
    #             if df[feature].dtype in ['int64', 'float64']:
    #                 default_value = df[feature].median()
    #             else:
    #                 default_value = df[feature].mode()[0]
    #         else:
    #             default_value = 0 if feature not in df.columns or \
    #                 df[feature].dtype in ['int64', 'float64'] else 'None'
    #         X_live[feature] = default_value

    return X_live

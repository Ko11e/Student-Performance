import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_management import load_student_data, load_pkl_file
from src.machine_learning.evaluate_reg import regression_performance, regression_evaluation_plots
    
sns.set_style("whitegrid")

def page_ML_predict_student_exam_body():
    
    version = 'v1'
    
    # Upload pipline a train and test set
    exam_score_pipe_model = load_pkl_file(
        f'outputs/ml_pipeline/predict_exam_score/{version}/clf_pipeline.pkl')
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_exam_score/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_exam_score/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_exam_score/{version}/y_train.csv").values
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_exam_score/{version}/y_test.csv").values

    st.write("### ML Pipeline: Predict Exam Score")
    # display pipeline training summary conclusions UTVECKLA
    st.info(
        f"""
        The pipeline was tuned aiming at least 0.70 for a r^{2} on Regression, 

        """
        # since we are interested in this project in detecting a potential churner. \n
        # The pipeline performance on train and test set is 0.90 and 0.85, respectively.
        
    )
 
    # Show pipline
    st.write(
        """
        There are just one pipline both for the cleaning of the data and the feature scaling 
        and modelling
        """
    )
    
    st.write(exam_score_pipe_model)

    
    st.write("---")
    
    st.write(
        """
        ### Pipline performence
        """
    )

    
    regression_evaluation_plots(
        X_train, y_train,
        X_test, y_test,
        exam_score_pipe_model
    )
    regression_performance(
        X_train, y_train,
        X_test, y_test, exam_score_pipe_model
    )

    st.error(
        """
        Quick Summary
        """
    )


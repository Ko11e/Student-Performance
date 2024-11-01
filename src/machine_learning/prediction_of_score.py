import streamlit as st


def predict_score(X_live, score_pipeline):
    # from live data, subset features related to this pipeline
    #X_live_sale_price = X_live.filter(property_features)

    score_prediction = score_pipeline.predict(X_live)

    return score_prediction
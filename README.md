# Student performence

This project aims to help a school district improve student outcomes by analyzing factors that influence student performance. By examining various student-related attributes, the project investigates how different conditions correlate with exam scores and predicts future scores based on student resources. The analysis includes exploring data correlations, testing hypotheses, and building a predictive machine learning model to assist educators in identifying and prioritizing key influences on academic success.

The deployed project can be accessed [here](https://predict-student-performance-1fc4615a3168.herokuapp.com/)

## Table of contents

1. [Dataset Content](#dataset-content)
2. [Business Requirements](#business-requirements)
3. [Hypotheses and Validation](#hypotheses-and-validation)
4. [Rationale Mapping](#the-rationale-to-map-the-business-requirements-to-the-data-visualizations-and-ml-taskshe-rationale)
5. [ML Business Case](#ml-business-case)
6. [Dashboard Design](#dashboard-design)
8. [Validation](#validation)
9. [Bugs](#bugs)
10. [Deployment](#deployment)
11. [Libraries and Technologies](#libraries-and-technologies)
12. [Credits](#credits)

-------------

## Dataset Content

The dataset is obtained from **Kaggle** and includes data on various attributes that can affect student performance. Each entry in the dataset corresponds to an individual student. It is important to emphasize that the dataset has been generated randomly and this only targets students that have a passing grade. According to the sources on the Data Card, the "Student Performance Factors" dataset is a synthetic dataset created for educational and analytical purposes. It is not sourced from any real-world institutions but is designed to simulate realistic scenarios for analyzing factors that affect student performance. 


| Field                     | Data Type | Description                                                                                     |
| ------------------------- | --------- | ----------------------------------------------------------------------------------------------- |
| Hours_Studied             | Number    | Number of hours spent studying per week.                                                |
| Attendance                | Number    | Percentage of classes attended.                                                        |
| Parental_Involvement      | Object    | Level of parental involvement in the student's education (Low, Medium, High)             |
| Access_to_Resources       | Object    | Availability of educational resources (Low, Medium, High).                                        |
| Extracurricular_Activities| Object    | Participation in extracurricular activities (Yes, No).                                      |
| Sleep_Hours               | Number    | number of hours of sleep per night.                                               |
| Previous_Scores           | Number    | Scores from previous exams.                                                               |
| Motivation_Level          | Object    | Student's level of motivation (Low, Medium, High).                                               |
| Internet_Access           | Object    | Availability of internet access (Yes, No). |
| Tutoring_Sessions         | Number    |	Number of tutoring sessions attended per month. |
| Family_Income	          | Object    | Family income level (Low, Medium, High). |
| Teacher_Quality           | Object    | Quality of the teachers (Low, Medium, High). |
| School_Type               | Object    |	Type of school attended (Public, Private). |
| Peer_Influence	          | Object    | Influence of peers on academic performance (Positive, Neutral, Negative). |
| Physical_Activity	       | Number    | Average number of hours of physical activity per week. |
| Learning_Disabilities	    | Object    | Presence of learning disabilities (Yes, No). |
| Parental_Education_Level	 | Object    | Highest education level of parents (High School, College, Postgraduate). |
| Distance_from_Home	       | Object    | Distance from home to school (Near, Moderate, Far). |
| Gender	                   | Object    | Gender of the student (Male, Female). |
| Exam_Score	             | Number    | Final exam score (Procent)|


The dataset can also be seen here on [Kaggle](https://www.kaggle.com/datasets/lainguyn123/student-performance-factors).

-------------

## Business Requirments

he client for this project is a school district that wants to identify the resources schools need to focus on to improve student performance. The client would like to address the following business requirements:

* **Business Requirement 1**: The client wants to understand which factors have the most significant impact on students' grades. They seek a visual representation and exploration of the correlations between these factors and performance metrics such as grades. This will provide insights for educators and policymakers on elements that may influence student success.

* **Business Requirement 2**: The client aims to predict students' exam scores based on their resources.

-------------

## Hypothesis and how to validate?

### Hypothesis

#### Hypothesis 1
If students have high attendance and spend a significant number of hours studying, they are more likely to achieve a higher grade (over 75).


#### Hypothesis 2
The education level of the students' parents does not have a significant impact on the students' final exam scores.

### Validation and Conclusion 

#### Hypothesis 1

This can be confirmed by analyzing the dataset and performing correlation studies, including the use of heatmaps.

**Conclusion**
The data indicates that there in a trende that shows of the student having a higher changes of getting a higher Exam Score if they a higher attendance and houres stuidied. But there are nothigh that support the statmate the student will have a higher change to get a score that is higher then 75.

This will conclude that this hypothesis will be rejected

#### Hypothesis 2

This can be confirmed by analyzing the dataset and performing correlation studies, including the use of heatmaps.

**Conclusion**
The median value for the education level of students' parents is relatively similar, but a closer look reveals a slight trend. Students tend to have better Exam score when their parents have higher educational backgrounds. However, the trend is so smale that it have no significat infuance in the students Exam score. This lead to that this hypothersis will be redject since the data shows a smale trend that disproves the hypothesis. 

-------------

## The rationale to map the business requirements to the Data Visualizations and ML tasks

### Business Requirement 1

To understand the factors associated with higher student scores, we will perform a correlation study. This analysis will utilize different methods to detect various types of relationships. First, Pearson's method will be used to identify linear relationships, while Spearman's method will capture monotonic relationships. Additionally, the Predictive Power Score (PPS) will help us detect more subtle and potentially asymmetric associations.

### Business Requirement 2

In order to accurately predict students' exam scores, we will implement a regression model that will enable us to estimate these scores based on a variety of relevant features. This approach involves constructing a regression model within a structured machine learning pipeline, which will facilitate the identification of relationships between the input features and the target variable. Furthermore, the plan is to conduct hyperparameter optimization to maximize the accuracy of our predictions.

-------------

## ML Business Case
### Predicting Exam score

#### Regression Model

- A machine learning (ML) model was developed to predict the the score a student will get based on historical data. The target variable is numerical and has a value from 50 to 100 which represents the percent of correct answers. The goal is to provide a school district with actionable insights to optimize the teaching or recommendation for the students to succeed.

- Model Success Metrics and Rationale:

  - **R² ≥ 70%**
  - **RMSE ≤ 5**


These metrics ensure that the model not only performs well statistically but also provides meaningful and actionable.

------------

## Dashboard Design

### Page 1: Quick Project Summary

- Introduce the project and its motivation
   - link to README
- Provide an overview of the dataset
   - Display the first ten rows of the dataset
- Outline the business requirements

### Page 2: Project Hypothesis and Validation

This page displays the three hypotheses and utilizes data analysis and visualization to validate or reject each hypothesis.

### Page 3: Exploratory Analysis of the Data
This page provides an interactive dashboard for exploring Student performance data to identify key factors. 

The dashboard includes data visualizations to highlight relationships.


### Page 4: Students Exam Score Predictor

This page will contain the second business requirement which involves implementing a feature for inputting data and generating predictions. This includes creating widget inputs where users can enter the necessary data for the prediction. Additionally, there will be a "Run Prediction" button that, when clicked, runs the inputted data through the machine learning model, producing a prediction. 

### Page 5: ML Predictor preformens 

The document provides a summary of the model's performance and key metrics, detailing the overall effectiveness and accuracy of the model. It also outlines the model pipeline and describes the features used for training, explaining the selection criteria for each feature. Additionally, the document includes comprehensive documentation of the model's performance across both the training and testing datasets, highlighting any differences in accuracy, variance, and potential areas for improvement.

-------

## The Dataset and the Models

Despite extensive efforts to understand the data and identify correlations or insignificant features, the dataset lacks sufficient predictive power to develop a reliable model. Upon examining the data, it is evident that most features follow a normal distribution concerning the exam scores. However, there are no standout elements in the dataset that significantly impact the ability to predict trends, this can also be seen in the section about the cluster model. This limitation makes the analysis narrow and difficult to interpret. In this section the model that is created to predict if the student improves their score or not will not be discussed in detail.

Various pipelines have been tested to evaluate the R² value. The data does not contain many missing values, which makes the cleaning process relatively straightforward. Different approaches were explored to possibly improve the model. The conclusion was to implement three different strategies for handling the missing data. The first strategy involved replacing NaN values with the word "Missing," the second involved filling them with the most frequent value, and the third involved removing rows with NaN values. However, none of the strategies proved to be better than the others, leading to the decision to retain the first strategy.

**Regression**

In the initial attempt to find the best model, we focused on using regression models. Our goal was to achieve an R² accuracy of over 0.70. However, we did not succeed in our first try. The most effective algorithm we found was Linear Regression, which yielded an R² value of 0.64. While trying to optimize the model through hyperparameter tuning, the maximum mean value we achieved remained at 0.64. A detailed comparison of different models and hyperparameters can be found **[here](/MODEL-TEST.md)**.

To help minimize processing time and prevent my computer from crashing during the hyperparameter search, I utilized ChatGPT to optimize the test. However, upon plotting the model evaluation, we noticed a cluster in the right-hand corner, which corresponds to the tail of the target distribution. This clustering is likely responsible for the lower R² value and stile a relatively low RMSE.

**Evaluation plot LinearRegression**

![Evaluation plot with the model LinearRegression](/images/Evu_reg_plot.png)


The next algorithem that was tested was KNeighborsRegressor which is a non-parametric regression method that predicts values based on the k closest training data points. It stores the training data and uses a distance metric, usually Euclidean distance, to make predictions.For each prediction, the average of the target values of the k nearest points is calculated. This can be done with uniform weighting or by considering distance. Choosing the right value for k is crucial: smaller values may result in high variance, while larger values can lead to high bias. Therefore, the function was created to the optimal k-value, along with the mean R² value. The optimail k-value was 19, but the R² value was 0.47 at the maximum.

Forward the pipeline was built using PCA. This however resulted in a lower accarcy and needed all the feature to built the model. This Pipline was not tested  with hyperparameters since the R² value was lower then 0.4. 

**Classification**

Since the previuse models did not succssed in reatching the R² value of 0.70 the next appotch was to us Classification by dividing the taget in to catagorige with the same number of datapoint. Due to the distrubusion of the taget the sizing of the spans was `['<64.0', '64.0 to 66.0', '66.0 to 68.0', '68.0 to 70.0','+70.0']`. Even thoght this model had a high value in the recall the model only predicted <64.0, +70.0 making the accuracy to 0.33.

**Cluster**

A clustering model was also developed, but it revealed that the data does not form well-defined clusters, making it ineffective for identifying correlations between conditions and Exam Score. The Silhouette analysis showed an loser then average Silhouette Score of approximately 0.32, indicating a lack of well-defined clusters, as values close to zero suggest poor clustering structure. 

This lack of separation is clearly evident in the cluster plot, which show that the data points do not form distinct clusters, further demonstrating the challenges in identifying meaningful patterns related to Exam Scores. Leading to no futher investigation in the cluster model.

**Cluster Silhouette Analysis:**

![Cluster Silhouette Analysis](/images/cluster-silhouette.png)

**Cluster plot:**

![Cluster plot](/images/cluster-scatter.png)

### Conclusion

In conclusion, while various approaches were explored to achieve an R² accuracy above 0.70, the analysis faced several limitations. Linear Regression yielded the highest R² score of 0.64, but further tuning failed to improve performance. Alternative methods, including KNeighborsRegressor, PCA, classification, and clustering, were tested, but none provided significant gains. The clustering model particularly showed that the data lacks well-defined patterns, as evidenced by a low Silhouette Score. Ultimately, due to clustering and classification challenges, combined with limited gains from regression and hyperparameter optimization, Linear Regression with NaN values replaced by "Missing" was retained as the optimal model setup.

-----

## Validation

All code in the app_pages and src directories was validated as conforming to PEP8 standards using CodeInstitute's PEP8 Linter.

## Bugs

During the deployment of the project, it was discovered that some of the packages and libraries used were not compatible. This issue was resolved by testing the versions of the packages. Otherwise, no major bugs were encountered during the development of the project.


## Deployment
### Heroku

* The App live link is: [Predict Students Exam Score](https://YOUR_APP_NAME.herokuapp.com/) 
The project have been deployed to heruko folowing the steps below:

1. Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
2. Ensure your requirements.txt file contains all the packages necessary to run the streamlit dashboard.

1. Log in to Heroku and create an  new App ny clicking on **Create app**
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click **Search**. Once it is found, click **Connect**.
4. Select the branch you want to deploy, then click **Deploy Branch**.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


#### Installing Requirements
**WARNING:** The packages listed in the requirements.txt file are limited to those necessary for the deployment of the dashboard to Heroku, due to the limit on the slug size.

In order to ensure all the correct dependencies are installed in your local environment, run the following command in the terminal:
           
       - pip install -r full-requirements.txt


## Main Data Analysis and Machine Learning Libraries
**Libraries Used:**

- **pandas**: For data manipulation, reading, and saving datasets.
- **numpy**: For performing numerical operations.
- **matplotlib.pyplot**: For data visualization, including feature importance plots.
- **seaborn**: Specializes in data visualization, particularly for creating plots and exploring data.
- **scipy.stats**: Contains statistical functions for data analysis.
- **plotly.express**: Used for creating interactive plots for data visualization.
- **plotly.graph_objects**: Allows for detailed customization of Plotly plots.
- **joblib**: Efficiently saves and loads machine learning models.
- **gzip**: Facilitates handling compressed files.
- **feature_engine**: Provides feature engineering capabilities, including encoding, imputation, handling outliers, selection, and transformation.
- **imblearn_learn**: Addresses class imbalance by generating synthetic samples.
- **sklearn**: A comprehensive machine learning toolkit with submodules for various tasks, including data preprocessing, model building, evaluation, and feature selection.
- **ydata_profiling**: Automates data profiling for exploratory data analysis.
- **yellowbrick.cluster**: Offers clustering visualizations, such as KElbowVisualizer and 
-**Streamlit**:Build the web app.

**Other Technologies**

- **Git**: For version control
- **GitHub**: Code repository
- **Heroku**: For application deployment
- **Gitpod**:Cloud IDE used for development
- **Jupyter Notebook**:Interactive Python
- **CI Python Linter**: Style guide for python

## Credits 

- This project was inspired by the walkthrough project 'Churnometer' from Code Institute.
- Hyperparemeters test have been constructed with AI, specifically OpenAI's ChatGPT.
- The function to present the median value in the plot was found on [Stackoverflow](https://stackoverflow.com/questions/38649501/labeling-boxplot-in-seaborn-with-median-value)
- Stockoverflow, W3schools have been used to find solutions to small buges


### Acknowledgements
- My Slackteam and their amazing support and assistance.
- Special thanks to Patricia Halley for pushing me when I don't have any motivation.

- My mentor, Mo Shami, for guiding and supporting me in the right direction.

- My Mum to for being there when a needed to disscuse conclusions.
- My husband for his unwavering support and for handling everything else and our family while I focused on this project.


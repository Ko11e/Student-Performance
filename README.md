# Student performence

Introduction

## Table of contents

1. [Dataset Content](#dataset-content)
2. [Business Requirements](#business-requirements)
   - [Exam Score Improvement Criteria](#exam-score-improvement-criteria)
   - [Features Influencing Student Grades](#features-influencing-student-grades)
   - [Correlation Visualization for Student Performance](#correlation-visualization-for-student-performance)
3. [Hypothesis and Validation](#hypothesis-and-validation)
   - [Hypotheses for Project](#hypotheses-for-project)
   - [Validation Methods](#validation-methods)
4. [Rationale Mapping](#rationale-mapping)
   - [Mapping Business Requirements to Data Visualizations and ML Tasks](#mapping-business-requirements-to-data-visualizations-and-ml-tasks)
5. [ML Business Case](#ml-business-case)
   - [Framing the ML Business Case](#framing-the-ml-business-case)
6. [Dashboard Design](#dashboard-design)
   - [Dashboard Pages and Content](#dashboard-pages-and-content)
   - [Dashboard Feature Updates](#dashboard-feature-updates)
7. [Bugs](#bugs)
   - [Fixed Bugs](#fixed-bugs)
   - [Unfixed Bugs](#unfixed-bugs)
8. [Deployment](#deployment)
   - [Heroku Deployment Steps](#heroku-deployment-steps)
   - [Cloud IDE Reminders](#cloud-ide-reminders)
9. [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
    - [Libraries Used and Usage Examples](#libraries-used-and-usage-examples)
10. [Credits](#credits)
    - [Content References](#content-references)
    - [Media References](#media-references)
11. [Acknowledgements (Optional)](#acknowledgements-optional)

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

* **Business Requirement 3**: The client wants to predict whether a student will improve their score based on their previous scores.

-------------

## Hypothesis and how to validate?

### Hypothesis

#### Hypothesis 1
If students have high attendance and spend a significant number of hours studying, they are more likely to achieve a higher grade (over 75).


#### Hypothesis 2
The education level of the students' parents does not have a significant impact on the students' final exam scores.

#### Hypothesis 3
For the students to improve their scores, students need to focus on attending lectures, participating in tutoring sessions, and increasing their study hours.

### Validation and Conclusion 

#### Hypothesis 1

This can be confirmed by analyzing the dataset and performing correlation studies, including the use of heatmaps.

**Conclusion**

#### Hypothesis 2

This can be confirmed by analyzing the dataset and performing correlation studies, including the use of heatmaps.

**Conclusion**

#### Hypothesis 3
This can been seen in the on the best features for the ML Pipeline that predict in the students will improve there score or not.

**Conclusion**


-------------

## The rationale to map the business requirements to the Data Visualizations and ML tasks

### Business Requirement 1

To understand the factors associated with higher student scores, we will perform a correlation study. This analysis will utilize different methods to detect various types of relationships. First, Pearson's method will be used to identify linear relationships, while Spearman's method will capture monotonic relationships. Additionally, the Predictive Power Score (PPS) will help us detect more subtle and potentially asymmetric associations. Once the classification models are complete, we will also extract similar statistics from the key features identified as important within these models.

### Business Requirement 2

In order to accurately predict students' exam scores, we will implement a regression model that will enable us to estimate these scores based on a variety of relevant features. This approach involves constructing a regression model within a structured machine learning pipeline, which will facilitate the identification of relationships between the input features and the target variable. Furthermore, the plan is to conduct hyperparameter optimization to maximize the accuracy of our predictions.


### Business Requirement 2
To predict if a student's performance has improved, we will that dataset to calculate the difference between studets previous and Exam scores. This analysis will help us develop a binary classification model to predict improvements. By using a structured machine learning pipeline, we can explore the relationships between various factors and the likelihood of score improvement. Additionally, we will conduct thorough hyperparameter optimization to enhance our model's accuracy in predicting student performance.


-------------

## ML Business Case
* In the previous bullet, you potentially visualized an ML task to answer a business requirement. You should frame the business case using the method we covered in the course 

 ------------

## Dashboard Design

* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).

### Page 1: Quick Project Summary
This section of the dashboard provides a concise overview of the project's objectives and functionalities

### Page 2: Exploratory Analysis of the Data
This page provides an interactive dashboard for exploring Student performance data to identify key factors 

The dashboard includes data visualizations to highlight relationships between clinical variables and IVF outcomes, assisting in data-driven decision-making.

#### Introduction and Data Inspection:


### Page 3: Project Hypothesis and Validation

This page explores the hypotheses regarding the Students to improve theire Exam Score, using data analysis and visualization to validate or refute each hypothesis.

### Page 4: Stundens Exam Score Predictor

### Page 5: Predictor of improving the Students score

### Page 6: ML Success Predictor
Evaluates and showcases the performance of a Students prediction models. The page presents the complete machine learning pipelines, including data cleaning, feature engineering, and modeling. It highlights feature importance and provides a detailed summary of the model's predictive performance.

-------

## The Dataset and the Models

-----

## Testing

### Manuel test



### Automated test

No automated tests have been conducted on the code.

### Validation

All code in the app_pages and src directories was validated as conforming to PEP8 standards using CodeInstitute's PEP8 Linter.

## Bugs

### Fixed 

### Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

### Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In the terminal, run `heroku_config`
5. Paste in your API key when asked


You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* Thank the people that provided support through this project.


# Student performence
## Introduction

### Table of contents

1. [Introduction](#introduction)
2. [Dataset Content](#dataset-content)
   - [Dataset Overview](#dataset-overview)
   - [Data Requirements for Model Training](#data-requirements-for-model-training)
3. [Business Requirements](#business-requirements)
   - [Exam Score Improvement Criteria](#exam-score-improvement-criteria)
   - [Features Influencing Student Grades](#features-influencing-student-grades)
   - [Correlation Visualization for Student Performance](#correlation-visualization-for-student-performance)
4. [Hypothesis and Validation](#hypothesis-and-validation)
   - [Hypotheses for Project](#hypotheses-for-project)
   - [Validation Methods](#validation-methods)
5. [Rationale Mapping](#rationale-mapping)
   - [Mapping Business Requirements to Data Visualizations and ML Tasks](#mapping-business-requirements-to-data-visualizations-and-ml-tasks)
6. [ML Business Case](#ml-business-case)
   - [Framing the ML Business Case](#framing-the-ml-business-case)
7. [Dashboard Design](#dashboard-design)
   - [Dashboard Pages and Content](#dashboard-pages-and-content)
   - [Dashboard Feature Updates](#dashboard-feature-updates)
8. [Bugs](#bugs)
   - [Fixed Bugs](#fixed-bugs)
   - [Unfixed Bugs](#unfixed-bugs)
9. [Deployment](#deployment)
   - [Heroku Deployment Steps](#heroku-deployment-steps)
   - [Cloud IDE Reminders](#cloud-ide-reminders)
10. [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
    - [Libraries Used and Usage Examples](#libraries-used-and-usage-examples)
11. [Credits](#credits)
    - [Content References](#content-references)
    - [Media References](#media-references)
12. [Acknowledgements (Optional)](#acknowledgements-optional)


## Dataset Content
* Describe your dataset. Choose a dataset of reasonable size to avoid exceeding the repository's maximum size and to have a shorter model training time. If you are doing an image recognition project, we suggest you consider using an image shape that is 100px × 100px or 50px × 50px, to ensure the model meets the performance requirement but is smaller than 100Mb for a smoother push to GitHub. A reasonably sized image set is ~5000 images, but you can choose ~10000 lines for numeric or textual data. 


## Business Requirments

* What are the requirments for improving you exam scores.

* What are the features that have an effect on the stundent grad.

* The school what to see a visual display on the correlation that effects the score of the students



## Business Requirements
* Describe your business requirements


## Hypothesis and how to validate?
* List here your project hypothesis(es) and how you envision validating it (them) 


## The rationale to map the business requirements to the Data Visualizations and ML tasks
* List your business requirements and a rationale to map them to the Data Visualizations and ML tasks


## ML Business Case
* In the previous bullet, you potentially visualized an ML task to answer a business requirement. You should frame the business case using the method we covered in the course 


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


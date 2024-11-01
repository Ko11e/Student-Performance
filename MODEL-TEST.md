# Hyperparameter testing

## Regression model

In the tabel


| Model                     | Parameters                        | Values                        | Best mean score                                  |
|---------------------------|-----------------------------------|-------------------------------|:------------------------------------------:|
| **LinearRegression**      | `model__positive` <br> `model__n_jobs`   | [True, False] <br> [None, 1, 2]    | 0.64                                           |
| **GradientBoostingRegressor** <br> Balanced performance and speed | `model__n_estimators` <br> `model__learning_rate` <br> `model__max_depth` <br> `model__subsample` <br> `model__max_features` <br> `model__random_state` | [100, 200] <br> [0.1, 0.05] <br> [3, 5] <br> [0.8, 1.0] <br> ["sqrt"] <br> [42] |  0.55 |
| **GradientBoostingRegressor** <br> Minimizing overfitting | `model__n_estimators` <br> `model__learning_rate` <br> `model__max_depth` <br> `model__min_samples_split` <br> `model__min_samples_leaf` <br> `model__subsample` <br> `model__max_features` <br> `model__random_state` | [200, 500] <br> [0.01, 0.05] <br> [3, 5] <br> [10, 20] <br> [5, 10] <br> [0.7, 0.8] <br> [0.5] <br> [42] |  0.55 |
| **GradientBoostingRegressor** <br> Higher complexity and model flexibility | `model__n_estimators` <br> `model__learning_rate` <br> `model__max_depth` <br> `model__subsample` <br> `model__max_features` <br> `model__min_samples_leaf` <br> `model__random_state` | [500, 1000] <br> [0.01, 0.05] <br> [5, 7] <br> [0.8] <br> ["auto", 0.8] <br> [1, 3] <br> [42] |  0.54 |
| **XGBRegressor** <br> Balanced performance and speed | `model__n_estimators` <br> `model__learning_rate` <br> `model__max_depth` <br> `model__subsample` <br> `model__colsample_bytree` <br> `model__random_state` | [100, 200] <br> [0.1, 0.05] <br> [3, 5] <br> [0.8] <br> [0.8, 1.0] <br> [42] |  0.62 | 


## Classification



| Model                     | Parameters                                    | Values                                             | Best mean score                          |
|---------------------------|-----------------------------------------------|----------------------------------------------------|:----------------------------------------:|
| **AdaBoostClassifier** <br> Higher complexity and flexibility | `model__n_estimators` <br> `model__learning_rate` <br> `model__estimator` <br> `model__algorithm` <br> `model__random_state` | [200, 500] <br> [0.01, 0.1] <br> [DecisionTreeClassifier(max_depth=5)] <br> ["SAMME"] <br> [42] |  0.76 |
| **AdaBoostClassifier** <br> Preventing overfitting | `model__n_estimators` <br> `model__learning_rate` <br> `model__estimator` <br> `model__algorithm` <br> `model__random_state` | [100, 200] <br> [0.1, 0.5] <br> [DecisionTreeClassifier(max_depth=3)] <br> ["SAMME.R"] <br> [42] |  0.78 |
| **AdaBoostClassifier** <br> Balanced accuracy and performance | `model__n_estimators` <br> `model__learning_rate` <br> `model__estimator` <br> `model__algorithm` <br> `model__random_state` | [200, 500] <br> [0.01, 0.1] <br> [DecisionTreeClassifier(max_depth=5)] <br> ["SAMME"] <br> [42] | 0.76 |
| **ExtraTreesClassifier** <br>  Preventing overfitting | `model__max_depth` <br> `model__min_samples_split` <br> `model__min_samples_leaf` <br> `model__max_features` <br> `model__max_leaf_nodes` <br> `model__random_state` | [10, 20, 30] <br> [5, 10] <br> [4, 10] <br> [0.5, "sqrt"] <br> [50, 100] <br> [42] | 0.83 |
| **ExtraTreesClassifier** <br> Balanced accuracy and performance | `model__criterion` <br> `model__max_depth` <br> `model__min_samples_split` <br> `model__min_samples_leaf` <br> `model__max_features` <br> `model__random_state` | ["gini", "entropy"] <br> [None, 10, 20] <br> [2, 5] <br> [1, 2, 4] <br> ["sqrt", "log2"] <br> [42] |  0.79 |


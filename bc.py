
"""
pip install
1. numpy
2. pandas
3. matplotlib
4. seaborn
5. sklearn

"""

"""
pip install
1. numpy
2. pandas
3. matplotlib
4. seaborn
5. sklearn

"""

#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix

from sklearn.feature_selection import RFE


# df.isna()

class Data:
    def __init__(self, data_file):
        self.df = pd.read_csv(data_file)
        self.df = df.dropna(axis=1)

    def split(self, test_size=0.25):
        X = self.df.iloc[:, 2:31].values
        encoder = LabelEncoder()
        self.df.iloc[:, 1] = encoder.fit_transform(self.df.iloc[:, 1].values)
        y = self.df.iloc[:, 1].values
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=test_size,
                                                                                random_state=42)
        scaler = MinMaxScaler()
        self.X_train = scaler.fit_transform(self.X_train)
        self.X_test = scaler.transform(self.X_test)


class Model():
    def __init__(self, data, model_name, model):
        print("Initializing model")
        self.name = model_name
        self.m = model
        self.data = data

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.m

    def fit(self):
        print("fit model")
        self.m.fit(self.X_train, self.y_train)

    def cal_score(self):
        # score_percentage and accuracy_percentage နှိုင်းယှဉ်
        print("Calculate model score and percetage")
        self.score = self.m.score(self.X_train, self.y_train)
        self.score_percentage = round(self.score * 100, 2)

    def predict(self):
        print("predict model")
        self.ytest_pred = self.m.predict(self.X_test)
        self.ytrain_pred = self.m.predict(self.X_train)
        self.probability_pred = self.m.predict_proba(self.X_test)

    def cal_scores(self):
        print("Calculate scores . . . ")
        # classification_report, confusion_matrix
        self.test_accuracy_score = accuracy_score(self.y_test, self.ytest_pred)
        self.train_accuracy_score = accuracy_score(self.y_train, self.ytrain_pred)

        self.test_precision_score = precision_score(self.y_test, self.ytest_pred)
        self.train_precision_score = precision_score(self.y_train, self.ytrain_pred)

        self.test_recall_score = recall_score(self.y_test, self.ytest_pred)
        self.train_recall_score = recall_score(self.y_train, self.ytrain_pred)

        self.test_f1_score = f1_score(self.y_test, self.ytest_pred)
        self.train_f1_score = f1_score(self.y_train, self.ytrain_pred)

    def fit_rfe(self):
        print("fit model RFE")
        rfe = RFE(self.m, n_features_to_select=9, verbose=5)
        rfe.fit(self.X_train, self.y_train)
        self.ytest_pred_rfe = rfe.predict(X_test)
        self.ytrain_pred_rfe = rfe.predict(X_train)

    def cal_cf_report_and_accuracy_score(self):
        self.cf_report = classification_report(self.y_test, self.ytest_pred)
        # Another way to get the models accuracy on the test data
        self.accuracy_score = accuracy_score(self.y_test, self.ytest_pred)

    def cal_accuracy(self):
        # heatmap(cm)
        # self.ytest_pred_rfe ?
        self.cm = confusion_matrix(self.y_test, self.ytest_pred)
        TN = cm[0][0]
        TP = cm[1][1]
        FN = cm[1][0]
        FP = cm[0][1]
        print(cm)

        self.accuracy = (TP + TN) / (TP + TN + FN + FP)
        self.accuracy_percentage = round(self.accuracy * 100, 2)


    def auto(self):
        self.fit()
        self.cal_score()
        self.predict()
        self.cal_scores()
        self.fit_rfe()
        self.cal_cf_report_and_accuracy_score()
        self.cal_accuracy()


"""
# Notes

# accuracies = [model.accuracy for model in models]

# max model
for i in models:
        if max(accuracies) == i.accuracy:
            maximum_model = i

# heatmap
for i in models:
        sns.heatmap(i.cm)




model_name = [str(i) for i in models]
model_name_compare = model_name + model_name

scores = [i.score_precentage for i in models]
accuracies = [i.accuracy_precentage for i in models]

accuracy = scores + accuracies

difference = ["normal_accuracy", "normal_accuracy", "normal_accuracy", "normal_accuracy", 
             "accuracy_with_rfe", "accuracy_with_rfe", "accuracy_with_rfe", "accuracy_with_rfe"]

new_df = pd.DataFrame(
                     { "model_name" : model_name_compare,
                      "accuracy"    : accuracy,
                      "difference"  : difference
})





# prediction 
pred = maximum_model.ytest_pred
# actual value
actual = data.ytest

prediction_compare = ["Prediction", "Actual", "Prediction", "Actual"]
result = [list(pred).count(0), list(actual).count(0),
                list(pred).count(1), list(actual).count(1)]
comparison = ["Begnin", "Begnin", "Magnilant", "Magnilant"]

result_df = pd.DataFrame({ 
                     "Prediction" : prediction_compare,
                      "Result"    : result,
                      "Comparison"  : comparison
})







"""

"""

# import libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, \
    confusion_matrix

from sklearn.feature_selection import RFE


class Data:
    def __init__(self, data_file):
        self.df = pd.read_csv(data_file)
        self.df = df.dropna(axis=1)  # < - - -   1 df

    def split(self, test_size=0.25):
        X = self.df.iloc[:, 2:31].values
        encoder = LabelEncoder()
        self.df.iloc[:, 1] = encoder.fit_transform(self.df.iloc[:, 1].values)
        y = self.df.iloc[:, 1].values
        # < - - -   3, 4, 5, 6 
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=test_size,
                                                                                random_state=42)
        scaler = MinMaxScaler()
        self.X_train = scaler.fit_transform(self.X_train)
        self.X_test = scaler.transform(self.X_test)



class Model():
    def __init__(self, name, model,data):
        print("Initializing model")
        self.name = name
        self.m = model
        self.X_train = data.X_train
        self.y_train = data.y_train
        self.X_test = data.X_test
        self.y_test = data.y_test
        
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name

    def fit(self):
        print("fit model")
        self.m.fit(self.X_train, self.y_train)

    def cal_score(self):
        # score_percentage and accuracy_percentage နှိုင်းယှဉ်
        print("Calculate model score and percetage")
        self.score = self.m.score(self.X_train, self.y_train)
        self.score_percentage = round(self.score * 100, 2)

    def predict(self):
        print("predict model")
        self.ytest_pred = self.m.predict(self.X_test)
        self.ytrain_pred = self.m.predict(self.X_train)
        self.probability_pred = self.m.predict_proba(self.X_test)

    def cal_scores(self):
        print("calculate scores . . . ")
        # classification_report, confusion_matrix
        self.test_accuracy_score = accuracy_score(self.y_test, self.ytest_pred)
        self.train_accuracy_score = accuracy_score(self.y_train, self.ytrain_pred)

        self.test_precision_score = precision_score(self.y_test, self.ytest_pred)
        self.train_precision_score = precision_score(self.y_train, self.ytrain_pred)

        self.test_recall_score = recall_score(self.y_test, self.ytest_pred)
        self.train_recall_score = recall_score(self.y_train, self.ytrain_pred)

        self.test_f1_score = f1_score(self.y_test, self.ytest_pred)
        self.train_f1_score = f1_score(self.y_train, self.ytrain_pred)

    def fit_rfe(self):
        print("fit model RFE")
        rfe = RFE(self.m, n_features_to_select=9, verbose=5)
        rfe.fit(self.X_train, self.y_train)
        self.ytest_pred_rfe = rfe.predict(self.X_test)
        self.ytrain_pred_rfe = rfe.predict(self.X_train)

    def cal_cf_report_and_accuracy_score(self):
        print("calculate cf report and accuracy score.")
        self.cf_report = classification_report(self.y_test, self.ytest_pred)
        # Another way to get the models accuracy on the test data
        self.accuracy_score = accuracy_score(self.y_test, self.ytest_pred)

    def cal_accuracy(self):
        print("calculate accuracy.")
        # heatmap(cm)
        # self.ytest_pred_rfe ?
        cm = confusion_matrix(self.y_test, self.ytest_pred)
        TN = cm[0][0]
        TP = cm[1][1]
        FN = cm[1][0]
        FP = cm[0][1]
        self.cm = cm
        self.accuracy = (TP + TN) / (TP + TN + FN + FP)
        self.accuracy_percentage = round(self.accuracy * 100, 2)


    def auto(self):
        print(f"automatic test of {self.name}\n")
        self.fit()
        self.cal_score()
        self.predict()
        self.cal_scores()
        self.fit_rfe()
        self.cal_cf_report_and_accuracy_score()
        self.cal_accuracy()
        print(f"Succesfull test of {self.name}\n")
        print(" -" * 21)




data = Data("C:\\Users\\User\\Documents\\breast_cancer_dataset.csv")
data.df.isna().sum()

sns.pairplot(data.df, hue="diagnosis")

data.df.corr()

plt.figure(figsize=(20,20))  
sns.heatmap(data.df.corr(), annot=True, fmt='.0%')

data.split()
data.df.iloc[:, 1].values




model_list = [("Logistic Regression", LogisticRegression(random_state=0)),
("SVC linear", SVC(kernel="linear", random_state=0, probability=True)),
("Decision Tree Classifier", DecisionTreeClassifier(criterion = 'entropy', random_state = 0)),
("Multinomial Naive Bayes Classifier", MultinomialNB(alpha = 1.0, class_prior = None, fit_prior = True))]

#initialize
models = [Model(name, model, data) for name, model in model_list]

models





# fit, calculate
for model in models:
    model.auto()
    
    
    
    
    
# 0, 1, 2, 3
sns.heatmap(models[0].cm, annot=True)



accuracies = [model.accuracy for model in models]
# max model
for model in models:
        if max(accuracies) == model.accuracy:
            maximum_model = model           
maximum_model



model_names = [str(i) for i in models]
scores = [model.score_percentage for model in models]
accuracies = [model.accuracy_percentage for model in models]
difference = ["normal_accuracy", "normal_accuracy", "normal_accuracy", "normal_accuracy", 
             "accuracy_with_rfe", "accuracy_with_rfe", "accuracy_with_rfe", "accuracy_with_rfe"]

accuracy_df = pd.DataFrame(
                     { "Model name" : model_names + model_names,
                       "Accuracy"    : scores + accuracies,
                       "Difference"  : difference
})
accuracy_df



sns.set(style = 'whitegrid')
ax = sns.barplot (x = "Model name" ,y = "Accuracy", hue="Difference", data= accuracy_df, palette = ["green", "red"])
for i in ax.containers:
    ax.bar_label(i) 
plt.title("Comparsion of accuracy with and without feature selection")
plt.xlabel("Prediction Models")
plt.ylabel("Accuracy")
plt.xticks(rotation = 90)
    
    
    

# prediction 
pred = maximum_model.ytest_pred
# actual value
actual = maximum_model.y_test
# danger <------- check 0 == begnin
result = [list(pred).count(0), list(actual).count(0),
                list(pred).count(1), list(actual).count(1)]
comparison = ["Begnin", "Begnin", "Magnilant", "Magnilant"]
result_df = pd.DataFrame({ 
                     "Prediction" : ["Prediction", "Actual", "Prediction", "Actual"],
                      "Result"    : result,
                      "Comparison"  : comparison
})
result_df




ax = sns.barplot (x = "Prediction" ,y = "Result", hue="Comparison", data= result_df, palette = ["blue", "red"])
for i in ax.containers:
    ax.bar_label(i) 
plt.title("Comparsion of accuracy with and without feature selection")
plt.xlabel("Prediction Models")
plt.ylabel("Accuracy")
plt.xticks(rotation = 90)




"""
import os
import pandas as pd
from sklearn import tree
import pydot
from sklearn import preprocessing
import io

#returns current working directory
os.getcwd()
#changes working directory
os.chdir("C:\\Users\\Algorithmica\\Downloads")

titanic_train = pd.read_csv("train.csv")

#EDA
titanic_train.shape
titanic_train.info()

sum(titanic_train['Pclass'].isnull())
titanic_train.apply(lambda x : sum(x.isnull()))
titanic_train.Embarked[titanic_train['Embarked'].isnull()] = 'S'

titanic_train1 = titanic_train.copy()
le = preprocessing.LabelEncoder()
titanic_train1.Sex = le.fit_transform(titanic_train1.Sex)
titanic_train1.Embarked = le.fit_transform(titanic_train.Embarked)
titanic_train1.Pclass = le.fit_transform(titanic_train1.Pclass)

X_train = titanic_train1[['Fare','Pclass','Sex','Embarked']]
y_train = titanic_train1['Survived']

dt = tree.DecisionTreeClassifier()
dt.fit(X_train,y_train)

#pipeline for test data
titanic_test = pd.read_csv("test.csv")
titanic_test.apply(lambda x : sum(x.isnull()))
titanic_test.Fare[titanic_test['Fare'].isnull()] = titanic_test['Fare'].mean()


titanic_test1 = titanic_test.copy()
titanic_test1.Sex = le.fit_transform(titanic_test1.Sex)
titanic_test1.Embarked = le.fit_transform(titanic_test1.Embarked)
titanic_test1.Pclass = le.fit_transform(titanic_test1.Pclass)

X_test = titanic_test1[['Fare','Pclass','Sex','Embarked']]
titanic_test1['Survived'] = dt.predict_proba(X_test)
titanic_test1.to_csv("submission.csv", columns=['PassengerId','Survived'], index=False)
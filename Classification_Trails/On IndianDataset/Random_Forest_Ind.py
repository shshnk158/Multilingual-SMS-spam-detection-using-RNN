# importing packages
import pandas as pd
import numpy as np
# preprocessing the data
data = pd.ExcelFile('revisedindiandataset.xls')
data = data.parse(0)
data.head()
# encoding Data
data['label'] = pd.factorize(data['label'])[0]


# splitting data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data['msg'], data['label'], test_size = 0.25)

# creating bag of words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 410)
cv.fit(data['msg'])
X_train = cv.transform(X_train)
X_test = cv.transform(X_test)

# Training classifier
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=30, criterion='entropy')
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

#Confusion Matrix                                               [827  15 ]
#                                                               [33  267 ]   95.79
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
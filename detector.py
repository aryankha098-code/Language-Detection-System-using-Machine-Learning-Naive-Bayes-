import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

data = pd.read_csv('new_data.csv')
data.head()

data['Label'].value_counts()

y=np.array(data['Label'])
x=np.array(data['Language'])

cv =CountVectorizer()
X=cv.fit_transform(np.where(x == None, '', x).astype(str))
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.33,random_state=42)

model=MultinomialNB()
model.fit(X_train,y_train)

user=input("Enter some text  ")
d=cv.transform([user]).toarray()
output= model.predict(d)
print(output)

print(model.score(X_test,y_test))
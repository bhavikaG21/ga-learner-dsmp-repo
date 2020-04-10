# --------------
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Code starts here
df=pd.read_csv(path)
print(df.head())

print(df.info())

valRExtraKey = ['HOME_VAL','INCOME','BLUEBOOK','OLDCLAIM','CLM_AMT']

for i in valRExtraKey:
    df[i] = df[i].str.replace(',', '')
    df[i] = df[i].str.replace('$', '') 

X=df.drop("CLAIM_FLAG",axis=1)
y=df['CLAIM_FLAG']

count=y.value_counts()

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,random_state = 6)

# Code ends here


# --------------
# Code starts here

for i in valRExtraKey:
    X_train[i] = X_train[i].astype(float)
    X_test[i] = X_test[i].astype(float)

print(X_train.isnull().sum())
print(X_test.isnull().sum())

# Code ends here


# --------------
# Code starts here
X_train.dropna(subset=['YOJ','OCCUPATION'],inplace=True)
X_test.dropna(subset=['YOJ','OCCUPATION'],inplace=True)

y_train = y_train[X_train.index]
y_test = y_test[X_test.index]


valueForMean = ['AGE','CAR_AGE','INCOME','HOME_VAL']

for i in valueForMean:
    storeVal = X_train[i].mean()
    print(i,storeVal)
    X_train[i].fillna(storeVal,inplace=True)

for i in valueForMean:
    storeVal = X_test[i].mean()
    print(i,storeVal)
    X_test[i].fillna(storeVal,inplace=True)
    
# Code ends here


# --------------
from sklearn.preprocessing import LabelEncoder
columns = ["PARENT1","MSTATUS","GENDER","EDUCATION","OCCUPATION","CAR_USE","CAR_TYPE","RED_CAR","REVOKED"]

# Code starts here

for i in columns:
    le=LabelEncoder()
    #le.fit_transform(X_train[i]).astype(str) 
    #le.transform(X_test[i]).astype(str) 
    
    X_train[i] = le.fit_transform(X_train[i].astype('str'))
    X_test[i] = le.fit_transform(X_test[i].astype('str'))

    #le.fit_transform(X_train[i].astype('str'))
    #le.transform(X_test[i].astype('str'))

# Code ends here



# --------------
from sklearn.metrics import precision_score 
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

# code starts here 

model = LogisticRegression(random_state = 6)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
score= accuracy_score(y_test,y_pred)
print("Accuracy score:",score)

# Code ends here


# --------------
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

# code starts here
smote = SMOTE(random_state = 9)
smote.fit(X_train, y_train)
X_train, y_train = smote.fit_sample(X_train, y_train)
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Code ends here


# --------------
# Code Starts here

model = LogisticRegression()
model.fit(X_train,y_train)
y_pred =model.predict(X_test)
score = accuracy_score(y_test,y_pred)
print('Accuracy score:', score)

# Code ends here



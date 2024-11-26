import pandas as pd
from sklearn.tree import DecisionTreeClassifier,export_text
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = {
    'age': ['<=30', '<=30', '31...40', '>40', '>40', '>40', '31...40', '<=30', '<=30', '>40', '<=30', '31...40', '31...40', '>40'],
    'income': ['high', 'high', 'high', 'medium', 'low', 'low', 'low', 'medium', 'low', 'medium', 'medium', 'high', 'medium', 'medium'],
    'student': ['no', 'no', 'no', 'no', 'yes', 'yes', 'yes', 'no', 'no', 'no', 'yes', 'yes', 'no', 'yes'],
    'credit_rating': ['fair', 'excellent', 'fair', 'fair', 'fair', 'excellent', 'excellent', 'fair', 'excellent', 'fair', 'excellent', 'fair', 'excellent', 'excellent'],
    'buys_computer': ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']
}

df=pd.DataFrame(data)
label_encoders={}
for col in df:
    le=LabelEncoder()
    df[col]=le.fit_transform(df[col])
    label_encoders[col]=le
x=df[['age','income','student','credit_rating']]
y=df['buys_computer']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
clf=DecisionTreeClassifier(criterion='gini',max_depth=3,random_state=42)
clf.fit(x_train,y_train)
y_pred=clf.predict(x_test)
print("Accuracy=",accuracy_score(y_pred,y_test))
print(export_text(clf,feature_names=x.columns.to_list()))

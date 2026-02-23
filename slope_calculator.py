import pandas as pd
import numpy as np
import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import os

dir="/home/yard/Desktop/current_data.csv"
hourly=pd.read_csv(dir)

#print(hourly)
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
              11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
              21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
              31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
              41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
              51, 52, 53, 54, 55, 56, 57, 58, 59]).reshape(-1,1)
#print(X)
y = np.array(hourly[["tempc"]])
#print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
slope=pd.DataFrame({'tempc':model.coef_[0]})

y = np.array(hourly[["humidper"]])
#print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
slope['humidper']=model.coef_[0]

y = np.array(hourly[["pressurehpa"]])
#print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
slope['pressurehpa']=model.coef_[0]
slope=round(slope, 4)
os.chdir("/home/yard/Desktop")
slope.to_csv("slope_data.csv", index=False)
#print(slope)

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score

#Import data
dataset = pd.read_csv("C:\\XXXX.csv")

#Transform columns into numerical values.
#Columsn are SourceName VehicleRef PublishedLineName DestinationName 
#Date Time Longitude Latitude Day
#label fit determines the mappings, transform swaps in the mappings

label = LabelEncoder()

label.fit(dataset.VehicleRef)
dataset.VehicleRef = label.transform(dataset.VehicleRef)

label.fit(dataset.PublishedLineName)
dataset.PublishedLineName = label.transform(dataset.PublishedLineName)

label.fit(dataset.DestinationName)
dataset.DestinationName = label.transform(dataset.DestinationName)
"""
label.fit(dataset.Time)
dataset.DestinationName = label.transform(dataset.Time)
"""
#For a given Latitude, Longitude, PublishedLineName, DestinationName tell me what the
#dataset Time is

#Split into training and test datasets
#drop is the pandas method for removing a column
x_lin = dataset.drop(['Time'], axis = 1)
y_lin = dataset[['Time']]

x_lin_train, x_lin_test, y_lin_train, y_lin_test = train_test_split(x_lin, y_lin, test_size = 0.3, random_state = 42)

#Fit a linear model
Linear_model = LinearRegression()
Linear_model.fit(x_lin_train, y_lin_train)

#Test predictions
pred = Linear_model.predict(x_lin_test)
print("Score")
print(Linear_model.score(x_lin_test,pred))

#Print coefficients
for idx, col_name in enumerate(x_lin_train.columns):
    print("The coefficient for {} is {}".format(col_name, Linear_model.coef_[0][idx]))

intercept = Linear_model.intercept_[0]
print("Intercept")
print(intercept)

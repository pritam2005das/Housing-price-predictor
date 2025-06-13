# import necessary libraries
import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

# loading the model
with open('housing.pkl', 'rb') as file:
    model = pickle.load(file)

# streamlit

# user input
st.title("House price Predictor")
area = st.number_input("area: ")
bedrooms = st.selectbox(
    'no of bedrooms:',
    [1,2,3,4,5,6]
)
bathrooms = st.selectbox(
    'no of bathrooms:',
    [1,2,3,4]
)
stories = st.selectbox(
    'no of stories:',
    [1,2,3,4]
)
parking = st.selectbox(
    'no of parkings:',
    [0,1,2,3]
)
furnishingstatus = st.selectbox(
    'furnishing status:',
    ['furnished', 'semi-furnished', 'unfurnished']
)
st.write("other freatures:")
mainroad = st.checkbox('beside main road')
guestroom = st.checkbox("guest room")
basement = st.checkbox("basement")
hotwaterheating = st.checkbox("water heater")
airconditioning = st.checkbox("air conditioner")
prefarea = st.checkbox("preferred area")

# prediction
if st.button("Predict"):
    data = {
        'area': area,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'stories': stories,
        'parking': parking,
        'mainroad': mainroad,
        'guestroom': guestroom,
        'basement': basement,
        'hotwaterheating': hotwaterheating,
        'airconditioning': airconditioning,
        'prefarea': prefarea,
        'furnishingstatus': furnishingstatus
    }
    data = pd.DataFrame([data])
    non_numeric_columns = data.select_dtypes(include=[bool,object]).columns.to_list()
    label = LabelEncoder()
    for i in non_numeric_columns:
        data[i] = label.fit_transform(data[i])
    scaler = StandardScaler()
    data = scaler.fit_transform(data)
    st.success("aproximated price: " + str(int(model.predict(data))) + "rs")
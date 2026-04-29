import pickle
import numpy as np

model = pickle.load(open("models/knn_model.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))

def predict_risk(age, goal, savings):
    data = np.array([[age, goal, savings]])
    data_scaled = scaler.transform(data)
    prediction = model.predict(data_scaled)
    return prediction[0]
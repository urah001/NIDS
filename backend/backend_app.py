# from fastapi import FastAPI, WebSocket
# from fastapi.middleware.cors import CORSMiddleware
# import joblib
# import numpy as np

# app = FastAPI()

# # Allow frontend (from another origin) to connect if needed
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Replace with frontend origin in production
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Load your trained model
# model = joblib.load("../nids_model.pkl")


# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         try:
#             # Receive comma-separated features (e.g., from JavaScript frontend)
#             data = await websocket.receive_text()
#             features = np.array([float(x) for x in data.split(",")]).reshape(1, -1)

#             # Predict using the loaded model
#             prediction = model.predict(features)[0]
#             is_intrusion = bool(prediction)

#             await websocket.send_text(f"Intrusion Detected: {is_intrusion}")

#         except Exception as e:
#             await websocket.send_text(f"Error: {str(e)}")
#             await websocket.close()
#             break

# # remember start like this : firstly : change environment o venv , then start with uvicorn

from flask import Flask, request, jsonify
import joblib
import preprocess_function  # your packet feature code

app = Flask(__name__)
model = joblib.load('../nids_model.pkl')

@app.route('/detect', methods=['POST'])
def detect_intrusion():
    data = request.json
    features = preprocess_function(data)
    prediction = model.predict([features])
    return jsonify({'intrusion': bool(prediction[0])})

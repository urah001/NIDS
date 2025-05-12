from fastapi import FastAPI, WebSocket
import joblib
import numpy as np
from scapy.all import sniff

app = FastAPI()

# Load model
model = joblib.load("nids_model.pkl")

# WebSocket to handle live data stream
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        packet = await websocket.receive_text()  # Receive data from frontend (e.g., packet features)
        features = np.array([float(x) for x in packet.split(',')])  # Assuming comma-separated features
        prediction = model.predict([features])[0]
        # Send prediction result back to frontend
        await websocket.send_text(f"Intrusion Detected: {bool(prediction)}")


#  python3 -m venv venv : creating new environment

                                                                           

#  source venv/bin/activate : activating the new environment
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import PassengerInput, PredictionOutput
from app.inference import predict

app = FastAPI(title="Titanic Survival Predictor API")

# Allow your frontend to call this API from the browser
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten this to your actual frontend domain later
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionOutput)
def predict_survival(passenger: PassengerInput):
    result = predict(passenger.dict())
    return result
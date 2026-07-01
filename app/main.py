from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from app.schemas import PassengerInput, PredictionOutput
from app.inference import predict

app = FastAPI(title="Titanic Survival Predictor API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return FileResponse("./index.html")

@app.post("/predict", response_model=PredictionOutput)
def predict_survival(passenger: PassengerInput):
    result = predict(passenger.dict())
    return result
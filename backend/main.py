from fastapi import FastAPI

## Creazione istanza dell'applicazione FASTAPI
app = FastAPI()

## Creazione Endpoint
@app.get("/ping")
def ping():
    return {"stato": "ok"}

## Endpoint per il "/"
@app.get("/")
def root():
    return {"messaggio": "Benvenuto nel corso di backend"}
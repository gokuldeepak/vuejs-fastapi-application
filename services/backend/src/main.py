from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # NEW


app = FastAPI()

# NEW
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://192.168.0.106:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return "Hello, Gokul!"
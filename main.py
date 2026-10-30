from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#Allowed Origin (Fronted url)

origin = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origin, # Allowed Frontend
    allow_credentials=True,
    allow_methods=["*"], # GET, PUT, POST, DELETE
    allow_headers=["*"]
)


@app.get("/")
def home():
    return{
        "message": "CORS enable API"
    }
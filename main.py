from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
import os
import shutil

app = FastAPI()

# Step-1: Ensure uploads folder exists

UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)


# Step-2: Static file set-up

app.mount("/files", StaticFiles(directory=UPLOAD_DIR), name="files")


# Step-3: Upload File API
@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    FileName = file.filename
    FilePath = os.path.join(UPLOAD_DIR, FileName)

    if not FileName:
        raise HTTPException(
            status_code=400,
            detail="File not selected"
        )
    
    with open(FilePath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

        return{
            "message": "File uploaded successfully",
            "Filename": FileName,
            "Fileurl": f"http://127.0.0.1:8000/files/{FileName}"
        }



# Step-4: Get File URL API

@app.get("/files/{filename}")
def get_file(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)

    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )

    return{
        "file_url": f"http://127.0.0.1:8000/files/{filename}"
    }


@app.get("/")
def home():
    return{
        "message": "File Uploaded api Running"
    }
##pip install python-multipart

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, FileResponse
import uvicorn
import os

app = FastAPI()


##INITIAL PAGE
@app.get("/") 
def main():
    content = """
<body>
</form>
<form action="/uploadfile/" enctype="multipart/form-data" method="post">
<input name="a_file" type="file" >
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)


#UPLOAD FILE
@app.post("/uploadfile")
async def upload_save_file(a_file: UploadFile = File(...)):

    SAVE_DIR = "./storage"
    content = await a_file.read()
    
    with open(os.path.join(SAVE_DIR, a_file.filename), "wb") as f:
        f.write(content)
    
    print(os.path.join(SAVE_DIR, a_file.filename))
    return {"saved in server":a_file.filename}


#DOWNLOAD FILE
@app.get("/result")
async def download_file(file_path:str="./storage", file_name:str="escape!.docx"):
    FILE_PATH = os.path.join(file_path, file_name)
    print(FILE_PATH)
    return FileResponse(FILE_PATH)


if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

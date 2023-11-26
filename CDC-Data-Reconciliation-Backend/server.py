import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import csv
import os
import uuid

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.post("/manual_report")
async def manual_report(state_file: UploadFile = File(None), cdc_file:  UploadFile = File(None)):
    folder_name = "temp"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    id = str(uuid.uuid4())
    os.makedirs(f"{folder_name}/{id}")
    
    cdc_content = await cdc_file.read()
    cdc_save_to = f"./{folder_name}/{id}/{cdc_file.filename}"
    with open(cdc_save_to, "wb") as f:
        f.write(cdc_content)

    state_content = await state_file.read()
    state_save_to = f"./{folder_name}/{id}/{state_file.filename}"
    with open(state_save_to, "wb") as f:
        f.write(state_content)

    res_file = f'./{folder_name}/{id}/results.csv'
    process = await asyncio.create_subprocess_exec('python', './compare.py', '-c', cdc_save_to, '-s', state_save_to, '-o', res_file)
    await process.wait()

    res = []
    with open(res_file, newline='') as csvfile:
        # Create a CSV reader object
        reader = csv.DictReader(csvfile)
        # Loop through each row in the CSV file
        for row in reader:
            # Add the row as a dictionary to the list
            res.append(row)

    # remove temp files / folder
    os.remove(cdc_save_to)
    os.remove(state_save_to)
    os.remove(res_file)
    os.rmdir(f"{folder_name}/{id}")

    return res

if __name__ == "__main__":
    # Run the API with uvicorn
    uvicorn.run("server:app", host="localhost", port=8000)

    # Use this command to run the API with reloading enabled (DOES NOT WORK ON WINDOWS)
    # uvicorn.run("server:app", host="localhost", port=8000, reload=True)

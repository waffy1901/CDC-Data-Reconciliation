from fastapi import FastAPI, File, UploadFile
#import pandas as pd
app = FastAPI()
import os

# Create an empty folder

@app.post("/manual_report")
async def read_file(state_file: UploadFile = File(...), cdc_file:  UploadFile = File(...)):
  folder_name = "temp"
  if not os.path.exists(folder_name):
    os.makedirs(folder_name)
  print(cdc_file.filename)
  cdc_content = await cdc_file.read()
  cdc_save_to = f"./temp/{cdc_file.filename}"
  with open(cdc_save_to, "wb") as f:
    f.write(cdc_content)
  state_content = await state_file.read()
  state_save_to = f"./temp/{state_file.filename}"
  with open(state_save_to, "wb") as f:
    f.write(state_content)
  print(state_file.filename)
  #return {"filename": filename, "content": content}
  return f"We have read the file! Content: {cdc_content}"
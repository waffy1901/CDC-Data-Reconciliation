import { useState } from "react"
import config from "../config.json"

export default function ManualReport() {
  const [stateFile, setStateFile] = useState(null)
  const [cdcFile, setCDCFile] = useState(null)

  const handleStateFileChange = (e) => {
    setStateFile(e.target.files[0])
  }

  const handleCDCFileChange = (e) => {
    setCDCFile(e.target.files[0])
  }

  const handleSubmit = async (e) => {
    e.preventDefault()

    if (stateFile === null || cdcFile === null) {
      console.error("Files not uploaded!")
      return
    }

    const formdata = new FormData()
    formdata.append("state_file", stateFile)
    formdata.append("cdc_file", cdcFile)

    try {
      const response = await fetch(config.API_URL + "/manual_report", {
        method: "POST",
        body: formdata,
      })

      if (response.ok) {
        console.log("Files uploaded successfully!")
      } else {
        console.error("Files failed to upload!")
      }
    } catch (e) {
      console.error(e)
    }
  }

  return (
    <div className='flex flex-col items-center justify-center h-full w-full'>
      <div className='bg-slate-400 w-[600px] h-[400px] rounded-xl mx-auto'>
        <form onSubmit={handleSubmit} className='h-full'>
          <div className='flex flex-col gap-6 items-center justify-center h-full'>
            <label htmlFor='cdc_file'>Upload CDC .csv File</label>
            <input type='file' id='cdc_file' onChange={handleCDCFileChange} />
            <label htmlFor='state_file'>Upload State .csv File</label>
            <input type='file' id='state_file' onChange={handleStateFileChange} />
            <button type='submit' className='bg-blue-400 text-white px-4 py-2 rounded-md hover:bg-blue-600'>
              Submit
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}

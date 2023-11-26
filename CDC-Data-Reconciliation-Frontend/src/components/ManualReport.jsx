import { useState } from "react"
import config from "../config.json"

export default function ManualReport() {
  const [stateFile, setStateFile] = useState(null)
  const [cdcFile, setCDCFile] = useState(null)
  const [results, setResults] = useState(null)

  const handleStateFileChange = (e) => {
    setStateFile(e.target.files[0])
    setResults(null)
  }

  const handleCDCFileChange = (e) => {
    setCDCFile(e.target.files[0])
    setResults(null)
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setResults(null)

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
        const data = await response.json()
        setResults(data)
      } else {
        console.error("Files failed to upload!")
      }
    } catch (e) {
      console.error("Error Creating Report - " + e)
    }
  }

  return (
    <div className='flex flex-col items-center h-full w-full'>
      <div className='bg-slate-300 w-[400px] min-h-[300px] rounded-xl mx-auto mt-20'>
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
      <div className='mt-5 py-5 w-5/6 max-w-6xl flex flex-col items-center'>
        {results && (
          <>
            <div className='flex flex-col items-center mb-5'>
              <h2 className='text-2xl font-bold'>Results</h2>
              <h3>Number of Cases Different: {results.length}</h3>
            </div>

            <table className='w-full text-center'>
              <tr className='border-b-2 border-slate-900'>
                <th>CaseID</th>
                <th>Disease</th>
                <th>State</th>
                <th>Date</th>
                <th>Reason</th>
              </tr>
              {results.map((result) => {
                return (
                  <tr key={result.CaseID}>
                    <td>{result.CaseID}</td>
                    <td>{result.EventName}</td>
                    <td>{result.State}</td>
                    <td>{result.EventDate}</td>
                    <td>{result.Reason}</td>
                  </tr>
                )
              })}
            </table>
          </>
        )}
      </div>
    </div>
  )
}

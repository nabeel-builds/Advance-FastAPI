import { useState, useEffect } from "react";

const App = () => {
  const [data, setData] = useState(null)


  useEffect(() => {
    const fetchData = async () => {
      try{
        const res = await fetch("http://127.0.0.1:8000")

        if(!res.ok){
          throw new Error(`HTTP Error: ${res.status}`)
        }


        const result = await res.json()
        setData(result)
      }catch(err){
        console.error("Error fetching data", err)
      }
    } 
    fetchData()
  },[])

  return(
    <div className="p-20">
      <h1>API Data</h1>
      {
        data ? (
          <p>Message: {data.message}</p>
        ) : (
          <p>Loading...</p>
        )
      }
    </div>
  )
}

export default App
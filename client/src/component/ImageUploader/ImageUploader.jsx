import React, { useState } from "react"
import axios from 'axios'
import "./ImageUploader.css"
function ImageUploader() {
    const [link, setLink] = useState("")
    const [image, setImage] = useState(null)
    const [data, setData] = useState(null)
    const [submitted, setSubmitted] = useState(false)
    const [error, setError] = useState(null)
    const formSubmitHandler = async (e) => {
        e.preventDefault()
        try {
            setError(" ")
            setData(" ")
            const response = await axios.post('http://172.16.227.111:3000/model', { url: link })
            setData(response.data)
            setImage(link)
            setSubmitted(true)
        } catch (error) {
            setError(error)
        }
        setLink("")
    }
    return (
        <div className="form">
            <form onSubmit={formSubmitHandler}>
                <input type="text" placeholder="Enter the Image URL" value={link} onChange={(e) => setLink(e.target.value)} />
                <button type="submit">▶</button>
            </form>
            {submitted && <img src={image} alt="Preview" />}
            {data && <h3>{data.class}</h3>}
            {error && <p>{error.message}</p>}
        </div>
    )
}

export default ImageUploader
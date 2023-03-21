import React, { useState } from 'react';

function Uploader() {
    const [image, setImage] = useState(null);

    const handleImageChange = (event) => {
        setImage(event.target.files[0]);
    };

    const handleUpload = () => {
        // Create FormData object to send image file to backend
        const formData = new FormData();
        formData.append('image', image);

        // Send POST request to backend to upload image
        fetch('/upload', {
            method: 'POST',
            body: formData,
        })
            .then((response) => response.text())
            .then((text) => {
                // Display any text extracted from the image
                console.log(text);
            });
    };

    return (
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
            <div>
                <h1>Image Uploader</h1>
                <form style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                    <label htmlFor="image-input">Upload Image</label>
                    <input
                        type="file"
                        id="image-input"
                        onChange={handleImageChange}
                        accept="image/*"
                        required
                    />
                    <br />
                    <br />
                    <button style={{ backgroundColor: 'pink', color: 'black' }} type="button" onClick={handleUpload}>
                        Upload Image
                    </button>
                </form>
            </div>
        </div>

    );
}

export default Uploader;

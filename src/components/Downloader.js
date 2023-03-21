import React, { useState } from 'react';

function Downloader() {
    const [text, setText] = useState('');

    const handleTextChange = (event) => {
        setText(event.target.value);
    };

    const handleDownload = () => {
        // Send GET request to backend to download image
        window.open(`/download?text=${text}`, '_blank');
    };

    return (
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
            <div style={{ margin: 'auto' }}>
                <h1>Image Downloader</h1>
                <form className=' justify-content-between m-auto align-items-center d-flex flex-column'>
                    <label htmlFor="text-input">Enter Text:</label>
                    <input className='mx-2'
                        type="text"
                        id="text-input"
                        value={text}
                        onChange={handleTextChange}
                        required
                    />
                    <br />
                    <br />
                    <button type="button" style={{ backgroundColor: 'pink', color: 'black' }} onClick={handleDownload}>
                        Download Image
                    </button>
                </form>
            </div>
        </div>

    );
}

export default Downloader;

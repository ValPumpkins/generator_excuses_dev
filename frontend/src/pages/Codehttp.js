// Code HTTP page : displays the excuses for a given HTTP code

import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import Error404 from './Error404';
import axios from 'axios';

const Codehttp = () => {
  const { http_code } = useParams();
  const [excuse, setExcuses] = useState('');
  const [validCode, setValidCode] = useState(true);

  useEffect(() => {
    const code = parseInt(http_code);

    if (isNaN(code) || code < 100 || code > 999) {
      // Check if the code is a valid HTTP code
      setValidCode(false);
      return;
    }

    // Retrieve the excuses for the given HTTP code
    axios
      .get('http://localhost:5000/api/excuses')
      .then((response) => {
        const filteredExcuses = response.data.filter(
          (excuseData) => excuseData.http_code === code
        );
        setExcuses(filteredExcuses);
      })
      .catch((error) => {
        console.error('Error fetching excuses :', error);
      });
  }, [http_code]);

  // If the HTTP code is invalid, display an error message
    if (!validCode) {
      return <Error404 />;
    }

  return (
      <div className="code-container">
        <h1>HTTP Code ➡️ Code ✨ {http_code} ✨</h1>
        <div className="excuse-container">
          {excuse.length > 0 ? (
            <ul>
              {excuse.map((excuse, index) => (
                <li key={index}>{excuse.message}</li>
              ))}
            </ul>
          ) : (
            <p>No excuses found for this HTTP code</p>
          )}
        </div>
      </div>
      );
};

export default Codehttp;

// The ExcuseGenerator component is responsible for fetching excuses from the backend and displaying them to the user

import React, { useState, useEffect } from 'react';
import RandomBtn from './RandomBtn';
import axios from 'axios';
import CreateExcuses from '../modals/CreateExcuses';

const ExcuseGenerator = () => {
  const [excuses, setExcuses] = useState([]); // Excuses from the API
  const [excuse, setExcuse] = useState(''); // Random excuse
  const [usedExcuses, setUsedExcuses] = useState([]);
  const [empty] = useState("Need an excuse ? We've got you 🫵"); // Empty state, before first click
  const [firstClick, setFirstClick] = useState(false); // Flag to track first click
  const [loading, setLoading] = useState(false); // Flag to track loading state
  const [showButtonRandom, setShowButtonRandom] = useState(false); // Track if button should be shown
  const [showButtonModal, setShowButtonModal] = useState(false); // Track if button should be shown


  const updateExcuses = () => {
    axios
      .get('http://localhost:5000/api/excuses')
      .then((response) => {
        setExcuses(response.data);
      })
      .catch((error) => {
        console.error('Error fetching excuses:', error);
      });
  };

  useEffect(() => {
    // Trigger button appearance and title animation after 2 seconds
    const timer = setTimeout(() => {
      setShowButtonRandom(true);
    }, 2000);
    return () => clearTimeout(timer);
  }, []);

  useEffect(() => {
    // Trigger button appearance and title animation after 2 seconds
    const timer = setTimeout(() => {
      setShowButtonModal(true);
    }, 3000);
    return () => clearTimeout(timer);
  }, []);

  useEffect(() => {
    // Retrieve excuses from the API when the component mounts
    updateExcuses();
  }, []);

  // Update excuses when a new excuse is created
  const handleExcuseCreated = () => {
    updateExcuses();
  };

  const generateExcuse = () => {
    console.log('Excuses:', excuses.length);
    console.log('Used excuses:', usedExcuses.length);

    // Set first click to true
    if (!firstClick) {
      setFirstClick(true);
    }

    setLoading(true);

    setTimeout(() => {
      // Check if all excuses have been used
      const availableIndices = excuses
        .map((_, index) => index)
        .filter((index) => !usedExcuses.includes(index));
      const randomIndex =
        availableIndices[Math.floor(Math.random() * availableIndices.length)];
      const singleExcuse = excuses[randomIndex];

      setExcuse(singleExcuse);
      setUsedExcuses([...usedExcuses, randomIndex]); // Add the index to the usedExcuses array

      // Reset the usedExcuses array when all excuses have been used
      if (usedExcuses.length === excuses.length) {
        setUsedExcuses([]);
      }
      setLoading(false);
    }, Math.floor(Math.random() * 4000) + 1000); // Random delay between 1s and 5s
  };

  return (
    <div className={`excuse-generator ${firstClick ? 'first-click' : ''}`}>
      <div className={`title-gen ${firstClick ? 'small-title' : ''}`}>
        <h1>
          {firstClick ? '- excuses de dev -' : 'Les excuses de dev'}
        </h1>
      </div>
      <div className="loader-container">
        {loading ? (
          <div className="loader"></div>
        ) : (
          <div className={`excuse-gen ${firstClick ? 'big-excuse' : ''}`}>
            {excuse ? <p>{excuse.message}</p> : <p className='empty-msg'>{empty}</p>}
          </div>
        )}{' '}
      </div>
      <div className={`btn-container ${showButtonRandom ? 'show' : ''}`}>
        <RandomBtn onClick={generateExcuse} />
      </div>
      <div className={`btn-container ${showButtonModal ? 'show' : ''}`}>
        <CreateExcuses onExcuseCreated={handleExcuseCreated} />
      </div>
    </div>
  );
};

export default ExcuseGenerator;

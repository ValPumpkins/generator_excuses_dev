// Lost page (with redirection to Home page after 5 seconds)

import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Logo from '../components/Logo';

const Lost = () => {
  const navigate = useNavigate();

    useEffect(() => {
      // Redirect to the home page after 5 seconds
      const timeout = setTimeout(() => {
        navigate('/');
      }, 5000);

      // Clean up the timeout
      return () => clearTimeout(timeout);
    }, [navigate]);

  return (
    <div className="lost-container">
      <Logo />
      <p className="lost-text">I'm lost</p>
      <img
        className="lost-gif"
        src="/lost.gif"
        alt="Character, Jin, from the TV show Lost gives a thumbs-up, then a black screen with the show's title."
      />
    </div>
  );
};

export default Lost;

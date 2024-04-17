// Button that will generate a random excuse when clicked

import React, { useState } from 'react';

const RandomBtn = ({ onClick }) => {
  const [clickedOnce, setClickedOnce] = useState(false); // State to track if the button has been clicked once

  // Text for the button based on the clickedOnce state
  const buttonText = clickedOnce ? 'Another excuse ?' : "Let's get started !";

  const handleClick = () => {
    setClickedOnce(true);
    onClick();
  };

  return (
    <button className="randombtn" onClick={handleClick}>
      {buttonText}
    </button>
  );
};

export default RandomBtn;

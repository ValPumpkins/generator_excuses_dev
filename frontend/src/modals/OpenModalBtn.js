// Button to open the modal

import React from 'react';

const OpenModalBtn = ({ onClick }) => {
  return (
    <div className="modalbtn-container">
      <button className="modalbtn" onClick={onClick}>
        Create your own excuse
      </button>
    </div>
  );
};

export default OpenModalBtn;

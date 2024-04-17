// Error404 page

import React from 'react';

const Error404 = () => {
	return (
    <div className="error-container">
      <p className="error-text">404</p>
      <div className="overlay">
        <p className="notfound-text">Page not found</p>
      </div>
    </div>
  );
};

export default Error404;

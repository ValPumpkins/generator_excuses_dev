// All routes definition and rendering of the components are done here

import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Lost from './pages/Lost';
import Codehttp from './pages/Codehttp';
import Error404 from './pages/Error404';


const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        {/* Home page route */}
        <Route path="/" element={<Home />} />
        {/* Lost page route */}
        <Route path="/lost" element={<Lost />} />
        {/* Codehttp page route */}
        <Route path="/:http_code" element={<Codehttp />} />
        {/* Error404 page route */}
        <Route path="*" element={<Error404 />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;

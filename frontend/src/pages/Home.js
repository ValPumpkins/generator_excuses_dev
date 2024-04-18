// MAIN HOME PAGE (with the excuse generator)

import React from 'react';
import ExcuseGenerator from '../components/ExcuseGenerator';
import Logo from '../components/Logo';


const Home = () => {
  return (
    <div>
      <Logo />
      <ExcuseGenerator />
    </div>
  );
};

export default Home;

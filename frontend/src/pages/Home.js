// MAIN HOME PAGE (with the excuse generator)

import React from 'react';
import ExcuseGenerator from '../components/ExcuseGenerator';
import CreateExcuses from '../modals/CreateExcuses';

const Home = () => {
  return (
    <div>
      <ExcuseGenerator />
      <CreateExcuses />
    </div>
  );
};

export default Home;

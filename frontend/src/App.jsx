import React, { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import HomePage from './pages/HomePage';
// import Programmes from './pages/Programmes'; // Exemple de page Programme
import ReservationPage from './pages/ReservationPage'; 
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        {/* <Route path="/programmes" element={<Programmes />} /> */}
        <Route path="/reserver" element={<ReservationPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/login" element={<LoginPage />} /> 
      </Routes>
    </Router>
  );
};

export default App

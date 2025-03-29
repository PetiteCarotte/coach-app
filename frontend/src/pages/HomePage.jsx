import React from 'react';
import NavBar from '../components/NavBar';
import HeroSection from '../components/HeroSection';
import CardSection from '../components/CardSection';
import Footer from '../components/Footer';

const HomePage = () => {
  return (
    <div>
      <NavBar />
      <HeroSection />
      <CardSection />
      <Footer />
    </div>
  );
};

export default HomePage;

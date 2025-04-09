import { Container } from 'react-bootstrap';
import accueilImage from '../assets/accueil.png';

function HeroSection() {
  return (
    <div
      className="hero-section text-center text-white d-flex align-items-center"
      style={{
        height: '60vh',
        backgroundImage: `url(${accueilImage})`,
        backgroundSize: 'cover',
      }}
    >
      <Container>
        <h1>Bienvenue chez votre coach personnel</h1>
        <p>Votre coach personnel à portée de main. Découvrez nos programmes et réservez des sessions facilement.</p>
        <p>Atteignez vos objectifs avec un accompagnement personnalisé.</p>
      </Container>
    </div>
  );
}

export default HeroSection;

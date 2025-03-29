import React from 'react';
import NavBar from '../components/NavBar';
import Footer from '../components/Footer'; 
import { Container, Row, Col, Card } from 'react-bootstrap';
import CalendarComponent from '../components/Calendar'; // Le composant Calendar que nous avons créé
import '../style/ReservationPage.css';

const ReservationPage = () => {
  return (
    <div>
    <NavBar />
    <Container className="my-5">
      <Row className="align-items-start">
        {/* Calendrier à gauche */}
        <Col md={6} className="mb-4">
          <Card>
            <Card.Header as="h5">Sélectionnez une date</Card.Header>
            <Card.Body>
              <CalendarComponent /> {/* Affichage du calendrier */}
            </Card.Body>
          </Card>
        </Col>

        {/* Liste des créneaux à droite */}
        <Col md={6} className="mb-4">
          <Card>
            <Card.Header as="h5">Créneaux Disponibles</Card.Header>
            <Card.Body>
              <ul className="list-group">
                {/* Créer une liste de créneaux disponibles pour la journée */}
                <li className="list-group-item">10:00 - 11:00</li>
                <li className="list-group-item">11:00 - 12:00</li>
                <li className="list-group-item">12:00 - 13:00</li>
                <li className="list-group-item">14:00 - 15:00</li>
                <li className="list-group-item">15:00 - 16:00</li>
                {/* Ajouter d'autres créneaux ici */}
              </ul>
            </Card.Body>
          </Card>
        </Col>
        
      </Row>
    </Container>
    <Footer />
    </div>
  );
};

export default ReservationPage;

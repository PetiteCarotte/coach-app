import React, { useState, useEffect } from 'react';
import NavBar from '../components/NavBar';
import Footer from '../components/Footer';
import { Container, Row, Col, Card, DropdownButton, Dropdown, Button } from 'react-bootstrap';
import CalendarComponent from '../components/Calendar';
import { FaCalendarAlt, FaClock, FaDumbbell, FaUser } from 'react-icons/fa';
import ConfirmationModal from '../components/ConfirmationModal';
import '../style/ReservationPage.css';

import {
  fetchCoaches,
  fetchPrograms,
  fetchAvailableSlots,
  makeReservation,
} from '../services/reservationService';

const ReservationPage = () => {
  const [coaches, setCoaches] = useState([]);
  const [programs, setPrograms] = useState([]);
  const [availableSlots, setAvailableSlots] = useState([]);

  const [selectedCoach, setSelectedCoach] = useState(null);
  const [selectedProgram, setSelectedProgram] = useState(null);
  const [selectedDate, setSelectedDate] = useState(null);
  const [selectedSlot, setSelectedSlot] = useState(null);

  const [showModal, setShowModal] = useState(false);
  const [isAuthenticated, setIsAuthenticated] = useState(false); // État pour vérifier si le client est connecté

  const formatDate = (date) => {
    if (!date) return '';
    const options = { day: 'numeric', month: 'long', year: 'numeric' };
    return new Date(date).toLocaleDateString('fr-FR', options); // Format 6 avril 2025
  };

  // Initial fetch
  useEffect(() => {
    fetchCoaches().then(setCoaches).catch(console.error);
    fetchPrograms().then(setPrograms).catch(console.error);

    // Vérifiez si le client est connecté (exemple avec un token dans le localStorage)
    const token = localStorage.getItem('userToken');
    setIsAuthenticated(!!token); // Si le token existe, le client est connecté
  }, []);

  useEffect(() => {
    if (selectedCoach && selectedDate) {
      fetchAvailableSlots(selectedCoach.id, selectedDate)
        .then(setAvailableSlots)
        .catch(console.error);
    }
  }, [selectedCoach, selectedDate]);

  const handleReservation = async () => {
    if (!isAuthenticated) {
      alert("Vous devez être connecté pour effectuer une réservation.");
      return;
    } else if (!selectedCoach) {
      alert("Veuillez sélectionner un coach.");
      return;
    } else if (!selectedProgram) {
      alert("Veuillez sélectionner un programme.");
      return;
    } else if (!selectedDate) {
      alert("Veuillez sélectionner une date.");
      return;
    } else if (!selectedSlot) {
      alert("Veuillez sélectionner un créneau.");
      return;
    }

    setShowModal(true); // Affiche la boîte de confirmation
  };

  const confirmReservation = async () => {
    try {
      await makeReservation({
        coach_id: selectedCoach.id,
        program_id: selectedProgram.id,
        slot_id: selectedSlot.id,
        date: selectedDate,
      });

      alert("Réservation confirmée !");
      setShowModal(false); // Ferme la boîte de confirmation
    } catch (error) {
      alert(error.message);
    }
  };

  return (
    <div className="reservation-page">
      <NavBar />
      <Container className="my-5">
        <Row>
          {/* Choix du programme */}
          <Col md={6}>
            <Card className="shadow-sm mb-4">
              <Card.Header className="bg-orange text-white">
                <FaDumbbell className="me-2" /> Choisir un programme
              </Card.Header>
              <Card.Body>
                <DropdownButton
                  title={selectedProgram ? selectedProgram.name : 'Choisir un programme'}
                  onSelect={(id) => {
                    const program = programs.find(p => p.id === parseInt(id));
                    setSelectedProgram(program);
                  }}
                >
                  {programs.map(program => (
                    <Dropdown.Item key={program.id} eventKey={program.id}>
                      {program.name}
                    </Dropdown.Item>
                  ))}
                </DropdownButton>
              </Card.Body>
            </Card>
          </Col>

          {/* Choix du coach */}
          <Col md={6}>
            <Card className="shadow-sm mb-4">
              <Card.Header className="bg-orange text-white">
                <FaUser className="me-2" /> Choisir un coach
              </Card.Header>
              <Card.Body>
                <DropdownButton
                  title={selectedCoach ? `${selectedCoach.first_name} ${selectedCoach.last_name}` : 'Choisir un coach'}
                  onSelect={(id) => {
                    const coach = coaches.find(c => c.id === parseInt(id));
                    setSelectedCoach(coach);
                    setSelectedSlot(null); // Reset slot selection
                  }}
                >
                  {coaches.map(coach => (
                    <Dropdown.Item key={coach.id} eventKey={coach.id}>
                      {coach.first_name} {coach.last_name}
                    </Dropdown.Item>
                  ))}
                </DropdownButton>
              </Card.Body>
            </Card>
          </Col>
        </Row>

        <Row>
          {/* Choix de la date */}
          <Col md={6}>
            <Card className="shadow-sm mb-4">
              <Card.Header className="bg-orange text-white">
                <FaCalendarAlt className="me-2" /> Sélectionner une date
              </Card.Header>
              <Card.Body>
                <CalendarComponent 
                  onDateSelect={(date) => {
                    console.log("Date sélectionnée :", date); // Debugging log
                    setSelectedDate(date);
                  }} 
                />
                {selectedDate && <p className="mt-3">Date sélectionnée : {formatDate(selectedDate)}</p>}
              </Card.Body>
            </Card>
          </Col>

          {/* Créneaux disponibles */}
          <Col md={6}>
            <Card className="shadow-sm mb-4">
              <Card.Header className="bg-orange text-white">
                <FaClock className="me-2" /> Créneaux disponibles
              </Card.Header>
              <Card.Body>
                <ul className="list-group">
                  {availableSlots.map(slot => (
                    <li
                      key={slot.id}
                      className={`list-group-item ${slot.is_reserved ? 'disabled' : ''} ${selectedSlot?.id === slot.id ? 'active' : ''}`}
                      style={{ cursor: slot.is_reserved ? 'not-allowed' : 'pointer', opacity: slot.is_reserved ? 0.5 : 1 }}
                      onClick={() => {
                        if (!slot.is_reserved) {
                          setSelectedSlot(slot);
                        }
                      }}
                    >
                      {slot.start_time} - {slot.end_time} {slot.is_reserved}
                    </li>
                  ))}
                  {availableSlots.length === 0 && <p>Aucun créneau disponible.</p>}
                </ul>
              </Card.Body>
            </Card>
          </Col>
        </Row>

        {/* Bouton de réservation */}
        <Row>
          <Col className="text-center">
            <Button variant="primary" size="lg" onClick={handleReservation}>
              Réserver
            </Button>
          </Col>
        </Row>
      </Container>
      <Footer />

      {/* Boîte de confirmation */}
      <ConfirmationModal
        show={showModal}
        onHide={() => setShowModal(false)}
        onConfirm={confirmReservation}
        reservationDetails={{
          coach: selectedCoach ? `${selectedCoach.first_name} ${selectedCoach.last_name}` : '',
          program: selectedProgram ? selectedProgram.name : '',
          date: selectedDate,
          slot: selectedSlot ? `${selectedSlot.start_time} - ${selectedSlot.end_time}` : '',
        }}
      />
    </div>
  );
};

export default ReservationPage;

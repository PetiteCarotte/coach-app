import React, { useEffect, useState } from "react";
import { Container, Row, Col, Card, Table, Button } from "react-bootstrap";
import { useNavigate } from "react-router-dom";
import { isAuthenticated } from "../services/authService";
import { cancelReservation } from "../services/reservationService";
import NavBar from "../components/NavBar";
import Footer from "../components/Footer";

const MyReservationsPage = () => {
  const [reservations, setReservations] = useState([]);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    if (!isAuthenticated()) {
      alert("Vous devez être connecté pour voir vos réservations.");
      navigate("/login");
      return;
    }

    const fetchReservations = async () => {
      try {
        const response = await fetch("http://localhost:5000/api/my_reservations", {
          headers: {
            Authorization: `Bearer ${localStorage.getItem("userToken")}`,
          },
        });

        if (!response.ok) {
          throw new Error("Erreur lors de la récupération des réservations.");
        }

        const data = await response.json();
        setReservations(data);
      } catch (err) {
        setError(err.message);
      }
    };

    fetchReservations();
  }, [navigate]);

  const handleCancel = async (reservationId) => {
    if (window.confirm("Êtes-vous sûr de vouloir annuler cette réservation ?")) {
      try {
        await cancelReservation(reservationId);
        alert("Réservation annulée avec succès.");
        setReservations((prev) => prev.filter((res) => res.id !== reservationId));
      } catch (err) {
        alert("Erreur lors de l'annulation de la réservation.");
      }
    }
  };

  return (
    <div>
      <NavBar />
      <Container className="my-5">
        <Row>
          <Col>
            <Card className="shadow-sm">
              <Card.Header className="bg-primary text-white">
                Mes Réservations
              </Card.Header>
              <Card.Body>
                {error && <p className="text-danger">{error}</p>}
                {reservations.length > 0 ? (
                  <Table striped bordered hover>
                    <thead>
                      <tr>
                        <th>#</th>
                        <th>Programme</th>
                        <th>Coach</th>
                        <th>Date</th>
                        <th>Créneau</th>
                        <th>Actions</th>
                      </tr>
                    </thead>
                    <tbody>
                      {reservations.map((reservation, index) => (
                        <tr key={reservation.id}>
                          <td>{index + 1}</td>
                          <td>{reservation.program_name}</td>
                          <td>{`${reservation.coach_name}`}</td>
                          <td>{reservation.date}</td>
                          <td>{`${reservation.start_time} - ${reservation.end_time}`}</td>
                          <td>
                            <Button
                              variant="danger"
                              size="sm"
                              onClick={() => handleCancel(reservation.id)}
                            >
                              Annuler
                            </Button>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </Table>
                ) : (
                  <p>Aucune réservation trouvée.</p>
                )}
              </Card.Body>
            </Card>
          </Col>
        </Row>
      </Container>
      <Footer />
    </div>
  );
};

export default MyReservationsPage;

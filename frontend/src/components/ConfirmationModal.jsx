import React from 'react';
import { Modal, Button, Table } from 'react-bootstrap';

const ConfirmationModal = ({ show, onHide, onConfirm, reservationDetails }) => {
  const formatDate = (date) => {
    if (!date) return '';
    const options = { day: 'numeric', month: 'long', year: 'numeric' };
    return new Date(date).toLocaleDateString('fr-FR', options); // Format 6 avril 2025
  };

  return (
    <Modal show={show} onHide={onHide} centered>
      <Modal.Header closeButton className="bg-primary text-white">
        <Modal.Title>Confirmer la réservation</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <Table bordered hover>
          <tbody>
            <tr>
              <td><strong>Coach</strong></td>
              <td>{reservationDetails.coach}</td>
            </tr>
            <tr>
              <td><strong>Programme</strong></td>
              <td>{reservationDetails.program}</td>
            </tr>
            <tr>
              <td><strong>Date</strong></td>
              <td>{formatDate(reservationDetails.date)}</td>
            </tr>
            <tr>
              <td><strong>Créneau</strong></td>
              <td>{reservationDetails.slot}</td>
            </tr>
          </tbody>
        </Table>
        <p className="text-center text-muted">
          Veuillez vérifier les informations avant de confirmer votre réservation.
        </p>
      </Modal.Body>
      <Modal.Footer className="justify-content-center">
        <Button variant="secondary" onClick={onHide} className="px-4">
          Annuler
        </Button>
        <Button variant="success" onClick={onConfirm} className="px-4">
          Confirmer
        </Button>
      </Modal.Footer>
    </Modal>
  );
};

export default ConfirmationModal;

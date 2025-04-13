// services/reservationService.js

const API_BASE_URL = 'http://localhost:5000/api';

// 🔁 Récupérer tous les coachs
export const fetchCoaches = async () => {
  const res = await fetch(`${API_BASE_URL}/coaches`);
  if (!res.ok) throw new Error("Erreur lors de la récupération des coachs");
  return await res.json();
};

// 🔁 Récupérer tous les programmes
export const fetchPrograms = async () => {
  const res = await fetch(`${API_BASE_URL}/programs`);
  if (!res.ok) throw new Error("Erreur lors de la récupération des programmes");
  return await res.json();
};

// 🔁 Récupérer les créneaux disponibles pour un coach donné à une date donnée
export const fetchAvailableSlots = async (coachId, date) => {
  const res = await fetch(`${API_BASE_URL}/available_slots?coach_id=${coachId}&date=${date}`);
  if (!res.ok) throw new Error("Erreur lors de la récupération des créneaux");
  return await res.json();
};

// ✅ Envoyer une réservation
export const makeReservation = async (reservationData) => {
  const res = await fetch(`${API_BASE_URL}/reservations`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${localStorage.getItem('userToken')}`,
    },
    body: JSON.stringify(reservationData),
  });

  const data = await res.json();

  if (!res.ok) {
    throw new Error(data.error || 'Erreur lors de la réservation');
  }

  return data;
};

// ✅ Annuler une réservation
export const cancelReservation = async (reservationId) => {
  const res = await fetch(`${API_BASE_URL}/reservations/${reservationId}`, {
    method: 'DELETE',
    headers: {
      Authorization: `Bearer ${localStorage.getItem('userToken')}`,
    },
  });

  if (!res.ok) {
    const data = await res.json();
    throw new Error(data.error || 'Erreur lors de l\'annulation de la réservation');
  }
};

import React, { useState } from 'react';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css'; // Styles par défaut

const CalendarComponent = () => {
  const [date, setDate] = useState(new Date());

  const handleDateChange = (newDate) => {
    setDate(newDate);
    // Logique pour charger les créneaux disponibles pour cette date
  };

  return (
    <div className="text-center">
      <Calendar
        onChange={handleDateChange}
        value={date}
        className="react-calendar custom-calendar" // Ajout d'une classe personnalisée
      />
    </div>
  );
};

export default CalendarComponent;

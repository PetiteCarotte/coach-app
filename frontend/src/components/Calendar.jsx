import React, { useState } from 'react';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css'; 

const CalendarComponent = ({ onDateSelect }) => {
  const [date, setDate] = useState(null); 

  const handleDateChange = (newDate) => {
    setDate(newDate);
  };

  const handleDateClick = (value) => {
    const adjustedDate = new Date(value.getTime() - value.getTimezoneOffset() * 60000)
      .toISOString()
      .split('T')[0]; 
    onDateSelect(adjustedDate);
  };

  return (
    <div className="text-center">
      <Calendar
        onChange={handleDateChange}
        value={date}
        className="react-calendar custom-calendar" // Classe personnalisée
        onClickDay={handleDateClick}
      />
    </div>
  );
};

export default CalendarComponent;

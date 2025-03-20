import React, { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/users')
      .then(response => {
        setUsers(response.data);
      })
      .catch(error => {
        console.error('Il y a une erreur lors de la récupération des utilisateurs:', error);
      });
  }, []);

  return (
    <div>
      <h1>Liste des utilisateurs</h1>
      <ul>
        {users.map((user, index) => (
          <li key={index}>{user.name} - {user.email}</li>
        ))}
      </ul>
    </div>
  );
}

export default App

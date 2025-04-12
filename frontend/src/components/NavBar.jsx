import React, { useState, useEffect } from 'react';
import { Container, Nav, Navbar as BootstrapNavbar, Button } from 'react-bootstrap';
import { Link, useNavigate } from 'react-router-dom';
import { isAuthenticated, logoutUser } from '../services/authService'; 
import logo from '../assets/loto.png';

function Navbar() {
    const [isLoggedIn, setIsLoggedIn] = useState(isAuthenticated());
    const navigate = useNavigate();

    useEffect(() => {
        const handleStorageChange = () => setIsLoggedIn(isAuthenticated());
        window.addEventListener('storage', handleStorageChange);

        return () => window.removeEventListener('storage', handleStorageChange);
    }, []);

    const handleLogout = () => {
        logoutUser();
        setIsLoggedIn(false);
        navigate('/'); 
    };

    const linkStyle = { fontSize: '1.25rem' }; 

    return (
        <BootstrapNavbar bg="light" expand="lg">
            <Container>
                <BootstrapNavbar.Brand as={Link} to="/">
                    <img src={logo} className="d-inline-block align-top" alt="logo" height={50} />
                </BootstrapNavbar.Brand>
                <BootstrapNavbar.Toggle aria-controls="basic-navbar-nav" />
                <BootstrapNavbar.Collapse id="basic-navbar-nav">
                    <Nav className="ms-auto">
                        <Nav.Link as={Link} to="/" className="me-3" style={linkStyle}>Accueil</Nav.Link>
                        <Nav.Link as={Link} to="/reserver" className="me-3" style={linkStyle}>Réservez</Nav.Link>
                        <Nav.Link as={Link} to="/rendezvous" className="me-3" style={linkStyle}>Mes réservations</Nav.Link>
                    </Nav>
                    {isLoggedIn ? (
                        <Button onClick={handleLogout} variant="outline-secondary" className="ms-2 btn-outline-orange" style={linkStyle}>
                            Déconnexion
                        </Button>
                    ) : (
                        <Button as={Link} to="/login" variant="outline-secondary" className="ms-2 btn-outline-orange" style={linkStyle}>
                            Connexion
                        </Button>
                    )}
                </BootstrapNavbar.Collapse>
            </Container>
        </BootstrapNavbar>
    );
}

export default Navbar;

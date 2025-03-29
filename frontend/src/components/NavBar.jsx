import { Container, Nav, Navbar as BootstrapNavbar, Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import logo from '../assets/loto.png';



function Navbar() {
    return (
        <BootstrapNavbar bg="light" expand="lg">
            <Container>
                <BootstrapNavbar.Brand as={Link} to="/">
                    <img src={logo} className="d-inline-block align-top" alt="logo" height={50} /> 
                </BootstrapNavbar.Brand>
                <BootstrapNavbar.Toggle aria-controls="basic-navbar-nav" />
                <BootstrapNavbar.Collapse id="basic-navbar-nav">
                    <Nav className="ms-auto">
                        <Nav.Link as={Link} to="/">Accueil</Nav.Link>
                        <Nav.Link href="#">Programmes</Nav.Link>
                        <Nav.Link as={Link} to="/reserver">Réservez</Nav.Link>
                    </Nav>
                    <Button as={Link} to="/login" variant="outline-secondary" className='ms-2 btn-outline-orange'>Connexion</Button>
                </BootstrapNavbar.Collapse>
            </Container>
        </BootstrapNavbar>
    );
}

export default Navbar;

import { Container, Row, Col, Card } from 'react-bootstrap';
import { Button } from 'react-bootstrap';
import {Link} from 'react-router-dom'

function CardSection() {
  return (
    <Container className="my-5">
      <Row>
        <Col md={4}>
          <Card>
            <Card.Img variant="top" src="/path/to/image1.jpg" />
            <Card.Body>
              <Card.Title>Coaching Personnalisé</Card.Title>
              <Card.Text>Un accompagnement sur mesure pour atteindre vos objectifs.</Card.Text>
            </Card.Body>
          </Card>
        </Col>
        <Col md={4}>
          <Card>
            <Card.Img variant="top" src="/path/to/image2.jpg" />
            <Card.Body>
              <Card.Title>Suivi de Progrès</Card.Title>
              <Card.Text>Des outils et conseils pour mesurer vos performances.</Card.Text>
            </Card.Body>
          </Card>
        </Col>
        <Col md={4}>
          <Card>
            <Card.Img variant="top" src="/path/to/image3.jpg" />
            <Card.Body>
              <Card.Title>Réservez Facilement</Card.Title>
              <Card.Text>Un calendrier interactif pour réserver votre séance.</Card.Text>
            </Card.Body>
          </Card>
        </Col>
      </Row>
      <Row>
        <Col md={4}></Col>
        <Col md={4}>
          <Button as={Link} to="/reserver" variant="outine-secondary" className='btn-orange mt-4'>
            Réserve ton rendez-vous !
          </Button>
        </Col>
      </Row>
      
    </Container>
  );
}

export default CardSection;

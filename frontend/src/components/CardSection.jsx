import { Container, Row, Col, Card } from 'react-bootstrap';
import { Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';

function CardSection() {
  return (
    <Container className="my-5">
      <Row>
      <Col md={4}>
          <Link to="/reserver" style={{ textDecoration: 'none' }}>
            <Card
              className="text-white card-hover"
              style={{
                padding: '0px',
                cursor: 'pointer',
                transition: 'transform 0.3s, box-shadow 0.3s',
              }}
            >
              <div
                style={{
                  position: 'relative',
                  backgroundImage: `url('src/assets/image2.jpg')`,
                  backgroundSize: 'cover',
                  backgroundPosition: 'center',
                  height: '200px',
                  borderRadius: '10px',
                  overflow: 'hidden',
                }}
              >
                <div
                  style={{
                    position: 'absolute',
                    top: 0,
                    left: 0,
                    right: 0,
                    bottom: 0,
                    backgroundColor: 'rgba(0, 0, 0, 0.5)',
                    display: 'flex',
                    flexDirection: 'column',
                    justifyContent: 'center',
                    alignItems: 'center',
                    color: 'white',
                  }}
                >
                  <Card.Title>Muscle & Force</Card.Title>
                  <Card.Text>
                    Un programme intensif pour augmenter votre masse musculaire et renforcer votre corps.
                  </Card.Text>
                </div>
              </div>
            </Card>
          </Link>
        </Col>
        
        <Col md={4}>
          <Link to="/reserver" style={{ textDecoration: 'none' }}>
            <Card
              className="text-white card-hover"
              style={{
                padding: '0px',
                cursor: 'pointer',
                transition: 'transform 0.3s, box-shadow 0.3s',
              }}
            >
              <div
                style={{
                  position: 'relative',
                  backgroundImage: `url('src/assets/image1.jpg')`,
                  backgroundSize: 'cover',
                  backgroundPosition: 'center',
                  height: '200px',
                  borderRadius: '10px',
                  overflow: 'hidden',
                }}
              >
                <div
                  style={{
                    position: 'absolute',
                    top: 0,
                    left: 0,
                    right: 0,
                    bottom: 0,
                    backgroundColor: 'rgba(0, 0, 0, 0.5)',
                    display: 'flex',
                    flexDirection: 'column',
                    justifyContent: 'center',
                    alignItems: 'center',
                    color: 'white',
                    padding: '1rem',
                  }}
                >
                  <Card.Title>Objectif Minceur</Card.Title>
                  <Card.Text>
                    Un programme conçu pour brûler les graisses et affiner votre corps de manière saine et durable.
                  </Card.Text>
                </div>
              </div>
            </Card>
          </Link>
        </Col>
        
        <Col md={4}>
          <Link to="/reserver" style={{ textDecoration: 'none' }}>
            <Card
              className="text-white card-hover"
              style={{
                padding: '0px',
                cursor: 'pointer',
                transition: 'transform 0.3s, box-shadow 0.3s',
              }}
            >
              <div
                style={{
                  position: 'relative',
                  backgroundImage: `url('src/assets/image3.jpg')`,
                  backgroundSize: 'cover',
                  backgroundPosition: 'center',
                  height: '200px',
                  borderRadius: '10px',
                  overflow: 'hidden',
                }}
              >
                <div
                  style={{
                    position: 'absolute',
                    top: 0,
                    left: 0,
                    right: 0,
                    bottom: 0,
                    backgroundColor: 'rgba(0, 0, 0, 0.5)',
                    display: 'flex',
                    flexDirection: 'column',
                    justifyContent: 'center',
                    alignItems: 'center',
                    color: 'white',
                    padding: '1rem',
                  }}
                >
                  <Card.Title>Votre Bilan Fitness</Card.Title>
                  <Card.Text>
                    Une évaluation complète de votre condition physique pour définir un plan d'action sur-mesure.
                  </Card.Text>
                </div>
              </div>
            </Card>
          </Link>
        </Col>
      </Row>
      <Row>
        <Col md={4}></Col>
        <Col md={4}>
          <Button
            as={Link}
            to="/reserver"
            variant="outine-secondary"
            className="btn-orange mt-4"
            style={{ fontSize: '1.5rem', padding: '0.75rem 1.5rem' }}
          >
            Réserve ton rendez-vous !
          </Button>
        </Col>
      </Row>
    </Container>
  );
}

export default CardSection;

import React, { useState } from "react";
import { Container, Row, Col, Form, Button, Card, InputGroup } from "react-bootstrap";
import { Formik } from "formik";
import * as Yup from "yup";
import { Link } from "react-router-dom";
import { Eye, EyeSlash } from "react-bootstrap-icons";

const LoginPage = () => {
    const [showPassword, setShowPassword] = useState(false);

    const validationSchema = Yup.object({
        email: Yup.string().email("Email invalide").required("Champ requis"),
        password: Yup.string().min(6, "Au moins 6 caractères").required("Champ requis"),
    });

    return (
        <Container className="d-flex align-items-center justify-content-center vh-100">
            <Row className="w-100">
                <Col md={{ span: 6, offset: 3 }}>
                    <Card className="shadow-lg p-4" style={{ borderRadius: "12px" }}>
                        <h3 className="text-center mb-4">Connexion</h3>
                        <Formik
                            initialValues={{ email: "", password: "" }}
                            validationSchema={validationSchema}
                            onSubmit={(values) => console.log("Form submitted:", values)}
                        >
                            {({ handleChange, handleSubmit, values, errors, touched }) => (
                                <Form onSubmit={handleSubmit}>
                                    <Form.Group className="mb-3">
                                        <Form.Label>Email</Form.Label>
                                        <Form.Control
                                            type="email"
                                            name="email"
                                            placeholder="exemple@email.com"
                                            value={values.email}
                                            onChange={handleChange}
                                            isInvalid={touched.email && errors.email}
                                        />
                                        <Form.Control.Feedback type="invalid">
                                            {errors.email}
                                        </Form.Control.Feedback>
                                    </Form.Group>
                                    <Form.Group className="mb-3">
                                        <Form.Label>Mot de passe</Form.Label>
                                        <InputGroup>
                                            <Form.Control
                                                type={showPassword ? "text" : "password"}
                                                name="password"
                                                placeholder="••••••••"
                                                value={values.password}
                                                onChange={handleChange}
                                                isInvalid={touched.password && errors.password}
                                            />
                                            <Button
                                                variant="outline-secondary"
                                                onClick={() => setShowPassword(!showPassword)}
                                            >
                                                {showPassword ? <EyeSlash /> : <Eye />}
                                            </Button>
                                        </InputGroup>
                                        <Form.Control.Feedback type="invalid" className="d-block">
                                            {errors.password}
                                        </Form.Control.Feedback>
                                    </Form.Group>
                                    <Button variant="primary" type="submit" className="w-100 btn-orange">
                                        Se connecter
                                    </Button>
                                </Form>
                            )}
                        </Formik>
                        <p className="text-center mt-3">
                            Pas encore de compte ? <Link to="/register">Inscrivez-vous</Link>
                        </p>
                        <p className="text-center">
                            <Link to="/">Retour</Link>
                        </p>
                    </Card>
                </Col>
            </Row>
        </Container>
    );
};

export default LoginPage;

import React, { useState } from "react";
import { Container, Row, Col, Form, Button, Card, InputGroup } from "react-bootstrap";
import { Formik } from "formik";
import * as Yup from "yup";
import { data, Link, useNavigate } from "react-router-dom";
import { Eye, EyeSlash } from "react-bootstrap-icons";
import { registerUser } from "../services/authService";

const RegisterPage = () => {
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);
  const navigate = useNavigate(); // Redirection après l'inscription

  const validationSchema = Yup.object({
    firstName: Yup.string().required("Champ requis"),
    lastName: Yup.string().required("Champ requis"),
    email: Yup.string().email("Email invalide").required("Champ requis"),
    password: Yup.string().min(6, "Au moins 6 caractères").required("Champ requis"),
    confirmPassword: Yup.string()
      .oneOf([Yup.ref("password"), null], "Les mots de passe ne correspondent pas")
      .required("Champ requis"),
    role: Yup.string().oneOf(["Client", "Coach"], "Rôle invalide").required("Champ requis"),

  });

  const handleSubmit = async (values, { setSubmitting, setErrors }) => {
    try {
      const response = await registerUser(values);
      console.log("Inscription réussie:", response);
      alert("Inscription réussie !"); // Afficher un message de succès
      alert(data.message); // Afficher les données de l'utilisateur
      // Redirection vers la page de connexion ou une autre page après l'inscription
      navigate("/login");
    } catch (error) {
      console.error("Erreur lors de l'inscription:", error);
      setErrors({ general: error.message }); // Erreur à afficher
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <Container className="d-flex align-items-center justify-content-center vh-100">
      <Row className="w-100">
        <Col md={{ span: 6, offset: 3 }}>
          <Card className="shadow-lg p-4" style={{ borderRadius: "12px" }}>
            <h3 className="text-center mb-4">Inscription</h3>
            <Formik
              initialValues={{ firstName: "", lastName: "", email: "", password: "", confirmPassword: "", role: "" }}
              validationSchema={validationSchema}
              onSubmit={handleSubmit}
            >
              {({ handleChange, handleSubmit, values, errors, touched }) => (
                <Form onSubmit={handleSubmit}>
                  <Form.Group className="mb-3">
                    <Form.Label>Nom</Form.Label>
                    <Form.Control
                      type="text"
                      name="lastName"
                      placeholder="Votre nom"
                      value={values.lastName}
                      onChange={handleChange}
                      isInvalid={touched.lastName && errors.lastName}
                    />
                    <Form.Control.Feedback type="invalid">
                      {errors.lastName}
                    </Form.Control.Feedback>
                  </Form.Group>
                  <Form.Group className="mb-3">
                    <Form.Label>Prénom</Form.Label>
                    <Form.Control
                      type="text"
                      name="firstName"
                      placeholder="Votre prénom"
                      value={values.firstName}
                      onChange={handleChange}
                      isInvalid={touched.firstName && errors.firstName}
                    />
                    <Form.Control.Feedback type="invalid">
                      {errors.firstName}
                    </Form.Control.Feedback>
                  </Form.Group>
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
                  <Form.Group className="mb-3">
                    <Form.Label>Confirmer le mot de passe</Form.Label>
                    <InputGroup>
                      <Form.Control
                        type={showConfirmPassword ? "text" : "password"}
                        name="confirmPassword"
                        placeholder="••••••••"
                        value={values.confirmPassword}
                        onChange={handleChange}
                        isInvalid={touched.confirmPassword && errors.confirmPassword}
                      />
                      <Button
                        variant="outline-secondary"
                        onClick={() => setShowConfirmPassword(!showConfirmPassword)}
                      >
                        {showConfirmPassword ? <EyeSlash /> : <Eye />}
                      </Button>
                    </InputGroup>
                    <Form.Control.Feedback type="invalid" className="d-block">
                      {errors.confirmPassword}
                    </Form.Control.Feedback>
                  </Form.Group>

                  {/* Choix du rôle */}
                  <Form.Group className="mb-3">
                    <Form.Label>Rôle</Form.Label>
                    <Form.Control as="select" name="role" value={values.role} onChange={handleChange} isInvalid={touched.role && errors.role}>
                      <option value="">Sélectionnez un rôle</option>
                      <option value="Client">Client</option>
                      <option value="Coach">Coach</option>
                    </Form.Control>
                    <Form.Control.Feedback type="invalid">{errors.role}</Form.Control.Feedback>
                  </Form.Group>

                  {errors.general && <div className="alert alert-danger">{errors.general}</div>} {/* Affichage des erreurs générales */}

                  <Button variant="primary" type="submit" className="w-100 btn-orange" disabled={values.isSubmitting}> {/* Disable the button while submitting */}
                    S'inscrire
                  </Button>
                </Form>
              )}
            </Formik>
            <p className="text-center mt-3">
              Déjà inscrit ? <Link to="/login">Connectez-vous</Link>
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

export default RegisterPage;

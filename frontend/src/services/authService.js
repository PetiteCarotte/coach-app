// Importer jwtDecode pour décoder le token JWT

export const registerUser = async (values) => {

  const userData = {
    firstName: values.firstName,
    lastName: values.lastName,
    email: values.email,
    password: values.password,
    confirmPassword: values.confirmPassword,
    role: values.role
  };
  
  try {
    const response = await fetch("http://localhost:5000/api/register", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(userData),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.error || "Erreur lors de l'inscription");
    }

    return data; // Retourne la réponse du backend (message de succès)
  } catch (error) {
    throw error; // Propager l'erreur pour qu'on puisse l'afficher dans le formulaire
  }
};


// loginUser : Fonction pour se connecter que l'on va utiliser dans le formulaire de connexion
export const loginUser = async (values) => {
  const userData = {
    email: values.email,
    password: values.password,
  };

  try {
    const response = await fetch("http://localhost:5000/api/login"	, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(userData),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.error || "Erreur lors de la connexion");
    }

    if (data.token) {
      localStorage.setItem("userToken", data.token);
      // afficher le token dans la console pour le débogage
      console.log("FRONTToken JWT:", data.token);
    }

    return { success: true, message: data.message };
  } catch (error) {
    return { success: false, message: error.message };
  }
}
import { jwtDecode } from "jwt-decode";

export const isAuthenticated = () => {
  const token = localStorage.getItem("userToken");
  // Debuguer le token pour voir s'il est bien stocké
  console.log("222Token JWT:", token);
  if (!token) return false; // Si pas de token, pas authentifié
  // const decoded = jwtDecode(token);
  // // Debuguer le token décodé pour voir son contenu
  // console.log("Decoded JWT:", decoded);
  try {
    const decoded = jwtDecode(token);
    // Debuguer le token décodé pour voir son contenu
    console.log("Decoded JWT:", decoded);
    return decoded.exp * 1000 > Date.now(); // Vérifie si le token est expiré
  } catch (error) {
    console.error("Erreur lors du décodage du token:", error);
    return false; // Si le token est invalide ou expiré, on retourne false
  }
};

export const logoutUser = () => {
  localStorage.removeItem("userToken");
  // Afficher un message de déconnexion sur la page 
  alert("Vous avez été déconnecté avec succès.");
  window.location.href = "/"; // Rediriger vers la page d'accueil après la déconnexion
};
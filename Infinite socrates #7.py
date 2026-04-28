import pyrebase
from datetime import datetime


config = {
    "apiKey": "TU_API_KEY",
    "authDomain": "tu-proyecto.firebaseapp.com",
    "databaseURL": "https://tu-proyecto.firebaseio.com",
    "storageBucket": "tu-proyecto.appspot.com"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

class User:
    """Gestiona la identidad y persistencia del estudiante vía Firebase."""
    def __init__(self, user_id, email, display_name):
        self.user_id = user_id
        self.email = email
        self.display_name = display_name
        self.points = 0

    @staticmethod
    def register(email, password, name):
        """Registra un nuevo usuario en Firebase Auth."""
        try:
            user_auth = auth.create_user_with_email_and_password(email, password)
            print(f"\n✅ Cuenta creada exitosamente para {name}")
            return User(user_auth['localId'], email, name)
        except Exception as e:
            print(f"❌ Error al registrar: {e}")
            return None

    @staticmethod
    def login(email, password):
        """Inicia sesión y recupera el perfil."""
        try:
            user_auth = auth.sign_in_with_email_and_password(email, password)
            # En una app real, aquí buscaríamos el 'display_name' en la base de datos
            print(f"\nWelcome back!")
            return User(user_auth['localId'], email, "Estudiante ASUCQ")
        except Exception as e:
            print(f"❌ Error de credenciales: {e}")
            return None

class Session:
    """Simula el bloc de notas interactivo de Infinite Socrates."""
    def __init__(self, topic):
        self.topic = topic
        self.start_time = datetime.now()
        self.log = []

    def ask_socratic(self, handwritten_math):
        """Simula la lógica de la IA: Preguntar en lugar de resolver."""
        # Aquí iría la integración con el modelo de IA (Gemini/GPT)
        question = f"Veo que escribiste '{handwritten_math}'. ¿Qué pasaría con el equilibrio si restamos ese término en ambos lados?"
        self.log.append({"input": handwritten_math, "ai_prompt": question})
        return question

class ProgressTracker:
    """Maneja el sistema de puntos y el árbol de conceptos."""
    def __init__(self):
        self.points = 0
        self.mastery = {}

    def add_progress(self, concept, gain):
        self.points += gain
        self.mastery[concept] = self.mastery.get(concept, 0) + (gain / 100)
        return self.points
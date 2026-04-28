from datetime import datetime
from typing import List, Dict, Optional

class User:
    """
    Representa a un estudiante dentro de la plataforma Infinite Socrates.
    Gestiona la identidad del usuario y su puntaje global acumulado.
    """
    def __init__(self, user_id: str, username: str, email: str):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.total_points = 0
        self.sessions: List['Session'] = []

    def update_points(self, points: int):
        """Suma puntos al perfil del usuario tras completar desafíos."""
        self.total_points += points
        print(f"Puntos actualizados: {self.username} ahora tiene {self.total_points} puntos.")

    def get_summary(self) -> str:
        """Devuelve un resumen del estado actual del estudiante."""
        return f"Usuario: {self.username} | Nivel de Puntos: {self.total_points}"


class Session:
    """
    Gestiona una sesión de aprendizaje individual donde ocurre la interacción socrática.
    Rastrea las ecuaciones ingresadas y el flujo de preguntas de la IA.
    """
    def __init__(self, session_id: str, user_id: str, topic: str):
        self.session_id = session_id
        self.user_id = user_id
        self.topic = topic
        self.start_time = datetime.now()
        self.history: List[Dict[str, str]] = []  # Guarda pares de {input_estudiante: pregunta_ia}
        self.is_active = True

    def record_interaction(self, math_input: str, socratic_question: str):
        """
        Registra un ciclo de interacción: la ecuación reconocida y la pregunta de guía.
        """
        interaction = {
            "timestamp": datetime.now().isoformat(),
            "student_input": math_input,
            "ai_response": socratic_question
        }
        self.history.append(interaction)

    def end_session(self):
        """Finaliza la sesión actual."""
        self.is_active = False
        print(f"Sesión {self.session_id} sobre '{self.topic}' finalizada.")


class ProgressTracker:
    """
    Controla la jerarquía de conceptos (árbol) y adapta la dificultad.
    Determina qué tan cerca está el estudiante de 'descubrir' el concepto.
    """
    def __init__(self, user_id: str):
        self.user_id = user_id
        # El mapa de conceptos guarda: {nombre_concepto: estado_maestria}
        # Ejemplo: {"Ecuaciones Lineales": 0.85} donde 1.0 es dominio total
        self.concept_mastery: Dict[str, float] = {}

    def update_mastery(self, concept: str, mastery_gain: float):
        """
        Actualiza el progreso en un concepto específico del árbol jerárquico.
        """
        current_val = self.concept_mastery.get(concept, 0.0)
        self.concept_mastery[concept] = min(1.0, current_val + mastery_gain)
        print(f"Progreso en {concept}: {self.concept_mastery[concept] * 100}%")

    def get_next_difficulty_level(self, concept: str) -> str:
        """
        Analiza el dominio actual para decidir el tono de la siguiente pregunta de la IA.
        """
        mastery = self.concept_mastery.get(concept, 0.0)
        if mastery < 0.4:
            return "Fundamentos/Guía Directa"
        elif mastery < 0.8:
            return "Intermedio/Desafío Lógico"
        else:
            return "Avanzado/Abstracción"
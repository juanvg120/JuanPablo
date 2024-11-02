import re

class Lexer:
    def __init__(self, curp):
        self.curp = curp.upper()  # Convertir a mayúsculas para consistencia
        self.tokens = {}

    def tokenize(self):
        # Patrón para un CURP válido
        pattern = r"([A-Z]{2})([A-Z]{1})([A-Z]{1})(\d{6})([HM])([A-Z]{2})([A-Z]{3})([A-Z\d]{1})(\d{1})"
        match = re.match(pattern, self.curp)

        if match:
            self.tokens = {
                "Apellido Paterno": match.group(1),
                "Apellido Materno": match.group(2),
                "Nombre": match.group(3),
                "Fecha de Nacimiento": match.group(4),
                "Género": match.group(5),
                "Estado": match.group(6),
                "Consonantes Internas": match.group(7),
                "Homoclave": match.group(8),
                "Dígito Verificador": match.group(9)
            }
            return True
        else:
            self.tokens = {}
            return False

    def get_tokens(self):
        return self.tokens

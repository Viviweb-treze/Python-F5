from datetime import date


class User:
    def __init__(self, name: str, birth: int):
        self.name = name
        self.birth = birth

    def get_age(self) -> str:
        current_year = date.today().year
        return current_year - self.birth

    def is_adult(self) -> bool:
        return self.get_age() >= 18  # esto retorna "true - false"

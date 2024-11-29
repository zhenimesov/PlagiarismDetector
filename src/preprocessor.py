import re

class TextPreprocessor:
    def preprocess(self, text: str) -> str:
        """Метод для предобработки текста: приведение к нижнему регистру и удаление лишних символов."""
        text = text.lower()  # Приводим текст к нижнему регистру
        text = re.sub(r'\s+', ' ', text)  # Заменяем несколько пробелов на один
        text = re.sub(r'[^\w\s]', '', text)  # Убираем все знаки препинания
        return text

from src.preprocessor import TextPreprocessor
from src.similarity_calculator import JaccardSimilarityCalculator
from src.plagiarism_checker import PlagiarismChecker

def read_text_from_file(file_path: str) -> str:
    """Чтение текста из файла .txt."""
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().strip()
        if not text:
            raise ValueError(f"Файл {file_path} пустой!")
        return text

def main():
    # Объекты для предобработки текста и расчета схожести
    preprocessor = TextPreprocessor()  # Инициализация класса для предобработки текста
    similarity_calculator = JaccardSimilarityCalculator()
    plagiarism_checker = PlagiarismChecker(preprocessor, similarity_calculator)

    # Читаем текст из файлов
    original_text = read_text_from_file('data/original_text.txt')
    text_to_check = read_text_from_file('data/text_to_check.txt')

    # Проверка на плагиат
    similarity = plagiarism_checker.check_plagiarism(original_text, text_to_check)
    print(f"Коэффициент схожести: {similarity:.2f}")

if __name__ == "__main__":
    main()

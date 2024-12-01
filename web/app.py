import os
import sys

## НЕ ТРОГАТЬ либо потом не находит /src
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.insert(0, base_dir)

from flask import Flask, render_template, request
from src.plagiarism_checker import PlagiarismChecker
from src.preprocessor import TextPreprocessor
from src.similarity_calculator import JaccardSimilarityCalculator

app = Flask(__name__, template_folder='templates', static_folder='static')  # Указываем путь к шаблонам

# Инициализация компонентов
preprocessor = TextPreprocessor()
similarity_calculator = JaccardSimilarityCalculator()
plagiarism_checker = PlagiarismChecker(preprocessor, similarity_calculator)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check-files', methods=['POST'])
def check_files():
    original_file = request.files['original_file']
    check_file = request.files['check_file']

    original_text = original_file.read().decode('utf-8')
    text_to_check = check_file.read().decode('utf-8')

    similarity = plagiarism_checker.check_plagiarism(original_text, text_to_check)
    return render_template('result.html', similarity=similarity)

@app.route('/check-text', methods=['POST'])
def check_text():
    original_text = request.form['original_text']
    text_to_check = request.form['text_to_check']

    similarity = plagiarism_checker.check_plagiarism(original_text, text_to_check)
    return render_template('result.html', similarity=similarity)

if __name__ == '__main__':
    app.run(debug=True)

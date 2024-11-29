class PlagiarismChecker:
    def __init__(self, preprocessor, similarity_calculator):
        self.preprocessor = preprocessor
        self.similarity_calculator = similarity_calculator

    def check_plagiarism(self, original_text: str, text_to_check: str) -> float:
        original_text_processed = self.preprocessor.preprocess(original_text)
        text_to_check_processed = self.preprocessor.preprocess(text_to_check)
        return self.similarity_calculator.calculate(original_text_processed, text_to_check_processed)

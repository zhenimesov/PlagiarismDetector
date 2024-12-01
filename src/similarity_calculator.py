from abc import ABC, abstractmethod

class SimilarityCalculator(ABC):
    @abstractmethod
    def calculate(self, text1: str, text2: str) -> float:
        pass


class JaccardSimilarityCalculator(SimilarityCalculator):
    def calculate(self, text1: str, text2: str) -> float:
        set1, set2 = set(text1.split()), set(text2.split())
        intersection = set1 & set2
        union = set1 | set2
        return len(intersection) / len(union) if union else 0.0

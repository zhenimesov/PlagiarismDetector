from abc import ABC, abstractmethod

class SimilarityCalculator(ABC):
    @abstractmethod
    def calculate(self, text1: str, text2: str) -> float:
        pass


class JaccardSimilarity(SimilarityCalculator):
    def calculate(self, text1: str, text2: str) -> float:
        set1 = set(text1.split())
        set2 = set(text2.split())

        # Проверяем на случай пустых множеств
        if not set1 or not set2:
            return 0.0  # Если одно из множеств пустое, схожесть = 0

        intersection = set1.intersection(set2)
        union = set1.union(set2)

        if len(union) == 0:
            return 0.0  # Если объединение пусто, схожесть = 0

        return len(intersection) / len(union)

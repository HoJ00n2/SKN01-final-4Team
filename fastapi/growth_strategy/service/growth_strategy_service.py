from abc import ABC, abstractmethod

class GrowthStrategyService(ABC):

    @abstractmethod
    def generate_growth_strategy(self, age_group, gender, mbti, topic, platform, target_audience, content_style, post_frequency):
        pass
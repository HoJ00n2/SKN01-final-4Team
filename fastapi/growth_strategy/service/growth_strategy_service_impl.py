from growth_strategy.repository.growth_strategy_repository_impl import GrowthStrategyRepositoryImpl
from growth_strategy.service.growth_strategy_service import GrowthStrategyService

class GrowthStrategyServiceImpl(GrowthStrategyService):

    def __init__(self):
        self.__growthStrategyRepository = GrowthStrategyRepositoryImpl()

    async def generate_growth_strategy(self, gender, age_group, mbti, topic, strength, reveal, platform, interested_influencer):

        return await self.__growthStrategyRepository.fetch_growth_strategy(gender, age_group, mbti, topic, strength, reveal, platform, interested_influencer)


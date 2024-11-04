from pydantic import BaseModel
class GrowthStrategyRequestForm(BaseModel):
    gender: str
    age_group: str
    mbti: str
    topic: str
    strength: str
    reveal: str
    platform: str
    interested_influencer: str
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse

from growth_strategy.controller.growth_strategy_request_form import GrowthStrategyRequestForm
from growth_strategy.service.growth_strategy_service_impl import GrowthStrategyServiceImpl
import asyncio

growthStrategyRouter = APIRouter()


async def injectGrowthStrategyService():
    return GrowthStrategyServiceImpl()


@growthStrategyRouter.post("/growth-strategy")
async def create_growth_strategy(
        growthStrategyRequestForm: GrowthStrategyRequestForm,
        growthStrategyService: GrowthStrategyServiceImpl=
        Depends(injectGrowthStrategyService)):

    print(f"controller -> create_growth_strategy(): growthStrategyRequestForm: {growthStrategyRequestForm}")


    try:
        generatedStrategy = await growthStrategyService.generate_growth_strategy(
            growthStrategyRequestForm.gender,
            growthStrategyRequestForm.age_group,
            growthStrategyRequestForm.mbti,
            growthStrategyRequestForm.topic,
            growthStrategyRequestForm.strength,
            growthStrategyRequestForm.reveal,
            growthStrategyRequestForm.platform,
            growthStrategyRequestForm.interested_influencer
        )

        return JSONResponse(content={"generatedStrategy": generatedStrategy}, status_code=status.HTTP_200_OK)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


from pydantic import BaseModel, ConfigDict
from typing import Optional


class InvestorPurchaseSummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    inv_name: Optional[str] = None
    pan: Optional[str] = None
    scheme: Optional[str] = None
    total_amount: Optional[float] = None
    total_units: Optional[float] = None


class MutualFundInvestorSummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    scheme: Optional[str] = None
    inv_name: Optional[str] = None
    pan: Optional[str] = None
    total_amount: Optional[float] = None
    total_units: Optional[float] = None


class InvestorDetail(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    inv_name: Optional[str] = None
    pan: Optional[str] = None
    total_investment: Optional[float] = None


class MutualFundSummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    scheme: Optional[str] = None
    total_amount: Optional[float] = None
    total_units: Optional[float] = None
    avg_nav: Optional[float] = None

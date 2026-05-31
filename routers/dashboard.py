from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from datetime import date

from database import SessionLocal
from models import Transaction
from schemas import (
    InvestorPurchaseSummary,
    MutualFundInvestorSummary,
    InvestorDetail,
    MutualFundSummary,
)

router = APIRouter(prefix="/api/v1", tags=["Dashboard"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 1. Investor-wise Purchase Summary per Mutual Fund
@router.get("/investor-purchase-summary",response_model=List[InvestorPurchaseSummary],
    summary="Investor-wise purchase summary per mutual fund",
    description=(
        "Returns total purchase amount and NAV units per investor per mutual fund. "
        "Filterable by date range using `from_date` and `to_date`."
    ),
)
def investor_purchase_summary(
    from_date: Optional[date] = Query(None, description="Start date (YYYY-MM-DD)"),
    to_date: Optional[date] = Query(None, description="End date (YYYY-MM-DD)"),
    db: Session = Depends(get_db),
):
    query = db.query(
        Transaction.inv_name,
        Transaction.pan,
        Transaction.scheme,
        func.sum(Transaction.amount).label("total_amount"),
        func.sum(Transaction.units).label("total_units"),
    )

    if from_date:
        query = query.filter(Transaction.traddate >= from_date)
    if to_date:
        query = query.filter(Transaction.traddate <= to_date)

    data = query.group_by(
        Transaction.inv_name,
        Transaction.pan,
        Transaction.scheme,
    ).order_by(Transaction.inv_name, Transaction.scheme).all()

    return [
        InvestorPurchaseSummary(
            inv_name=row.inv_name,
            pan=row.pan,
            scheme=row.scheme,
            total_amount=row.total_amount,
            total_units=row.total_units,
        )
        for row in data
    ]



# 2. Mutual Fund-wise Summary per Investor

@router.get(
    "/mutualfund-investor-summary",
    response_model=List[MutualFundInvestorSummary],
    summary="Mutual fund-wise summary per investor",
    description=(
        "Returns the amount and NAV units purchased by each investor for each mutual fund. "
        "Filterable by date range."
    ),
)
def mutualfund_investor_summary(
    from_date: Optional[date] = Query(None, description="Start date (YYYY-MM-DD)"),
    to_date: Optional[date] = Query(None, description="End date (YYYY-MM-DD)"),
    db: Session = Depends(get_db),
):
    query = db.query(
        Transaction.scheme,
        Transaction.inv_name,
        Transaction.pan,
        func.sum(Transaction.amount).label("total_amount"),
        func.sum(Transaction.units).label("total_units"),
    )

    if from_date:
        query = query.filter(Transaction.traddate >= from_date)
    if to_date:
        query = query.filter(Transaction.traddate <= to_date)

    data = query.group_by(
        Transaction.scheme,
        Transaction.inv_name,
        Transaction.pan,
    ).order_by(Transaction.scheme, Transaction.inv_name).all()

    return [
        MutualFundInvestorSummary(
            scheme=row.scheme,
            inv_name=row.inv_name,
            pan=row.pan,
            total_amount=row.total_amount,
            total_units=row.total_units,
        )
        for row in data
    ]



# 3. Investor List with Purchase Details

@router.get(
    "/investors",
    response_model=List[InvestorDetail],
    summary="Investor list with purchase details",
    description=(
        "Returns each investor's PAN number and total amount invested within the selected date range."
    ),
)
def investors(
    from_date: Optional[date] = Query(None, description="Start date (YYYY-MM-DD)"),
    to_date: Optional[date] = Query(None, description="End date (YYYY-MM-DD)"),
    db: Session = Depends(get_db),
):
    query = db.query(
        Transaction.inv_name,
        Transaction.pan,
        func.sum(Transaction.amount).label("total_investment"),
    )

    if from_date:
        query = query.filter(Transaction.traddate >= from_date)
    if to_date:
        query = query.filter(Transaction.traddate <= to_date)

    data = query.group_by(
        Transaction.inv_name,
        Transaction.pan,
    ).order_by(Transaction.inv_name).all()

    return [
        InvestorDetail(
            inv_name=row.inv_name,
            pan=row.pan,
            total_investment=row.total_investment,
        )
        for row in data
    ]


# 4. Mutual Fund Summary

@router.get(
    "/mutualfund-summary",
    response_model=List[MutualFundSummary],
    summary="Mutual fund summary",
    description=(
        "Returns total amount invested, total NAV units purchased, and average NAV price "
        "per mutual fund across all investors. Filterable by date range."
    ),
)
def mutualfund_summary(
    from_date: Optional[date] = Query(None, description="Start date (YYYY-MM-DD)"),
    to_date: Optional[date] = Query(None, description="End date (YYYY-MM-DD)"),
    db: Session = Depends(get_db),
):
    query = db.query(
        Transaction.scheme,
        func.sum(Transaction.amount).label("total_amount"),
        func.sum(Transaction.units).label("total_units"),
        func.avg(Transaction.purprice).label("avg_nav"),
    )

    if from_date:
        query = query.filter(Transaction.traddate >= from_date)
    if to_date:
        query = query.filter(Transaction.traddate <= to_date)

    data = query.group_by(
        Transaction.scheme,
    ).order_by(func.sum(Transaction.amount).desc()).all()

    return [
        MutualFundSummary(
            scheme=row.scheme,
            total_amount=row.total_amount,
            total_units=row.total_units,
            avg_nav=row.avg_nav,
        )
        for row in data
    ]

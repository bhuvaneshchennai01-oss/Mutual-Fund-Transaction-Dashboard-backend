from sqlalchemy import Column, Integer, String, Float, DateTime, Index
from database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    amc_code = Column(String)
    folio_no = Column(String)
    prodcode = Column(String)

    scheme = Column(String)

    inv_name = Column(String)

    pan = Column(String)

    trxntype = Column(String)

    traddate = Column(DateTime, index=True)   

    purprice = Column(Float)

    units = Column(Float)

    amount = Column(Float)
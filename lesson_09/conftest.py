import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base

@pytest.fixture(scope="function")
def db_session():
    """Фикстура для сессии базы данных"""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    
    with Session(engine) as session:
        yield session
        session.rollback()
    
    engine.dispose()
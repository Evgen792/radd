from sqlalchemy import create_engine, text 
from sqlalchemy.orm import create_session
engine = create_session("postgresql+psycop2://postres:univer@localhost/avtoriz")
session = create_session(bind=engine)


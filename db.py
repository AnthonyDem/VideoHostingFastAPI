import databases
import sqlalchemy

metadata = sqlalchemy.MetaData()
database = databases.Database("sqlite:///host_vid.db")
engine = sqlalchemy.create_engine("sqlite:///host_vid.db")

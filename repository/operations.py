
from typing import  Final
from sqlmodel import Field, Session, SQLModel, create_engine,select
 


class Operation(SQLModel,  table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str

sqlite_file_name:Final[str] = "demo.db"
sqlite_url:Final[str] = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)

def get_operations():
    with Session(engine) as session:
        statement = select(Operation)
        results = session.exec(statement).all()
        rst:list[str] = list(map(lambda x: x.name, results))
        return rst
        # for operation in results:
        #     print(operation.name)
        #  with Session(engine) as session:
        # heroes = session.exec(select(Hero)).all()
        # return heroes
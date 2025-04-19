"""Repository to get operations from Datatabase"""
from typing import  Final
from sqlmodel import Field, Session, SQLModel, create_engine,select, Sequence
from sqlmodel.sql.expression import SelectOfScalar
 
class Operation(SQLModel,  table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str

__sqlite_file_name:Final[str] = "demo.db"
__sqlite_url:Final[str] = f"sqlite:///{__sqlite_file_name}"

__engine = create_engine(__sqlite_url, echo=True)

SQLModel.metadata.create_all(__engine)

def get_operations()->list[str]:
    """
    get_operations: List of String\n
    Retrieve operations from the Database
    """
    with Session(__engine) as session:
        statement:SelectOfScalar[Operation] = select(Operation)
        results:Sequence[Operation] = session.exec(statement).all()
        rst:list[str] = list(map(lambda x: x.name, results))
        return rst

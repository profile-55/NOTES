from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import Boolean, Integer, String, Text, Column

# TODO: task_uuid определённой длины
# TODO: param_1 (sid) определённой длины

class Task(Base):
    __tablename__='tasks'
    task_uuid=Column(String(255), primary_key=True, unique=True, nullable=False)
    description=Column(Text)
    param_1=Column(String(255), nullable=False)
    param_2=Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Item name={self.name} price={self.price}>"
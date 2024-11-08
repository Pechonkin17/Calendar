from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey
from typing import List

from base import Base
from .subject import Subject

class Semester(Base):
    __tablename__ = 'semesters'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    year: Mapped[int] = mapped_column(Integer)

    subjects: Mapped[List["Subject"]] = relationship("Subject",back_populates="semester",cascade="all, delete-orphan")
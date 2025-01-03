from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from typing import List

from base import Base
from .lab import Lab


class Subject(Base):
    __tablename__ = 'subjects'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(250))

    semester_id: Mapped[int] = mapped_column(ForeignKey("semesters.id"))
    semester: Mapped["Semester"] = relationship("Semester", back_populates="subjects")

    labs: Mapped[List["Lab"]] = relationship("Lab", back_populates="subject", cascade="all, delete-orphan")
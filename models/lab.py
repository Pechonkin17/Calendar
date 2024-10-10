from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Boolean, ForeignKey

from base import Base


class Lab(Base):
    __tablename__ = 'labs'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(250))
    max_points: Mapped[int] = mapped_column(Integer)
    is_submitted: Mapped[bool] = mapped_column(Boolean, default=False)
    received_points: Mapped[int] = mapped_column(Integer, default=0)
    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.id"))
    subject: Mapped["Subject"] = relationship("Subject", back_populates="labs")
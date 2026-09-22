import uuid
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Boolean,UUID as SQLUUID
class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[uuid.UUID] = mapped_column(
        SQLUUID(as_uuid=True), primary_key=True,default=uuid.uuid4, index=True)
    username: Mapped[str] = mapped_column(String(18), nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    is_verified: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)



    # created_at = Column(DateTime(timezone=True), nullable=False, default=now_utc)

    # id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    # short_url: Mapped[str] = mapped_column(String(15), unique=True)
    # original_url: Mapped[str] = mapped_column(String)
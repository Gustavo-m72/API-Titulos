from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    discordid: Mapped[str] = Column(String, primary_key=True)


@table_registry.mapped_as_dataclass
class Apelido:
    __tablename__ = 'apelidos'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    apelido: Mapped[str] = Column(String, nullable=False)
    user_id: Mapped[str | None] = Column(
        String, ForeignKey('users.discordid'), nullable=True
    )
    disponibilidade: Mapped[str] = Column(String, nullable=False)

from sqlalchemy import create_engine, Column, Integer, String, Text, Date, Time, ForeignKey, TIMESTAMP, MetaData
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .database import Base


# SCHEMA_NAME = 'atas'
# Base = declarative_base(metadata=MetaData(schema=SCHEMA_NAME))

class Reuniao(Base):
    __tablename__ = 'reunioes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
    titulo = Column(String(255))
    resumo = Column(Text)

    def __init__(self, data, hora, titulo, resumo):
        self.data = data
        self.hora = hora
        self.titulo = titulo
        self.resumo = resumo

    def __str__(self):
        return f'Data: {self.data} | Hora: {self.hora} | Título: {self.titulo}'


class Pauta(Base):
    __tablename__ = 'pautas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(Text, nullable=False)
    descricao = Column(Text, nullable=False)
    responsavel = Column(String(120))
    tempo_limite = Column(TIMESTAMP)
    docs = Column(Text)
    reuniao_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("reunioes.id"),
    )
    reuniao: Mapped[Reuniao] = relationship(
        "Reuniao",
        back_populates="reunioes",
    )


class Item(Base):
    __tablename__ = 'itens'
    id = Column(Integer, primary_key=True, autoincrement=True)
    item = Column(Text, nullable=False)
    descricao = Column(Text, nullable=False)
    deliberacao = Column(Text)
    pauta_id: Mapped[Integer] = mapped_column(
        Integer,
        ForeignKey("pautas.id"),
    )
    pauta: Mapped[Pauta] = relationship(
        "Pauta",
        back_populates="pautas",
    )


class Participante(Base):
    __tablename__ = 'participantes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_pessoa = Column(Integer)
    perfil = Column(String(30), nullable=False)
    reuniao_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("reunioes.id"),
    )
    reuniao: Mapped[Reuniao] = relationship(
        "Reuniao",
        back_populates="reunioes",
    )
    pauta_id: Mapped[Integer] = mapped_column(
        Integer,
        ForeignKey("pautas.id"),
    )
    pauta: Mapped[Pauta] = relationship(
        "Pauta",
        back_populates="pautas",
    )

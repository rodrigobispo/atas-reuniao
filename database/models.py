from sqlalchemy import create_engine, Column, Integer, String, Text, Date, Time, ForeignKey, TIMESTAMP, MetaData
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .database import Base
from datetime import date, time
# from dataclasses import dataclass

# SCHEMA_NAME = 'atas'
# Base = declarative_base(metadata=MetaData(schema=SCHEMA_NAME))

# @dataclass
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

    def __repr__(self):
        return f'<Reuniao(id={self.id}, data={self.data}, hora={self.hora}, titulo={self.titulo})>'

class Pauta(Base):
    __tablename__ = 'pautas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(Text, nullable=False)
    descricao = Column(Text, nullable=False)
    responsavel = Column(String(120))
    tempo_limite = Column(TIMESTAMP)
    docs = Column(Text)
    reuniao_id = Column(Integer, ForeignKey("reunioes.id"), nullable=False)
    reuniao = relationship("Reuniao", back_populates="pautas")

Reuniao.pautas = relationship("Pauta", back_populates="reuniao")


class Item(Base):
    __tablename__ = 'itens'
    id = Column(Integer, primary_key=True, autoincrement=True)
    item = Column(Text, nullable=False)
    descricao = Column(Text, nullable=False)
    deliberacao = Column(Text)
    pauta_id = Column(Integer, ForeignKey("pautas.id"), nullable=False)
    pauta = relationship("Pauta", back_populates="itens")

Pauta.itens = relationship("Item", back_populates="pauta")

class Participante(Base):
    __tablename__ = 'participantes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_pessoa = Column(Integer)
    perfil = Column(String(30), nullable=False)
    reuniao_id = Column(Integer, ForeignKey("reunioes.id"), nullable=False)
    reuniao = relationship("Reuniao", back_populates="participantes")
    pauta_id = Column(Integer, ForeignKey("pautas.id"), nullable=False)
    pauta = relationship("Pauta", back_populates="participantes")

Reuniao.participantes = relationship("Participante", back_populates="reuniao")
Pauta.participantes = relationship("Participante", back_populates="pauta")

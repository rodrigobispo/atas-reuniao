from fastapi import FastAPI, APIRouter, HTTPException
from database.database import SessionLocal, engine
from database.models import *


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Atas",
    description="API referente às funcionalidades de Atas"
)

router_atas = APIRouter()

def get_db():
    db = SessionLocal()
    if db is not None:
        return db
    else:
        db.close()

db = get_db()


@router_atas.get('/atas')
async def buscar_todas_atas():
    reunioes = db.query(Reuniao).all()
    return reunioes


app.include_router(router_atas, prefix="/infra/api")


# reuniao = Reuniao(data=date(2024, 7, 7), hora=time(8, 33), titulo='Alinhamento estratégico', resumo='Resumo X')
# print(reuniao)

# db.add(reuniao)
# db.commit()

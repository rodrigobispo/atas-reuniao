from pydantic import BaseModel, constr


class Reuniao(BaseModel):
    titulo: constr(min_length=10, max_length=255)

# atas

### Para gerar o database

Caso o database de nome 'db_atas.db' não esteja criado, no caminho raiz do projeto, digitar o comando:
```bash
$ python3 main.py
```
Neste arquivo main é possível realizar operações CRUD com o uso da session do alchemy.

### Para subir o servidor

No caminho raiz do projeto, digitar o comando:
```bash
$ uvicorn main:app --reload
```

URL de acesso a API após subir a aplicação: `http://localhost:8000/docs`


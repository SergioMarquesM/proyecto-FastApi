from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3


conn = sqlite3.connect('prueba.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS candidatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dni TEXT NOT NULL,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL
    )
''')
conn.commit()


class Candidato(BaseModel):
    dni: str
    nombre: str
    apellido: str

app = FastAPI()


@app.post("/candidato")
async def create_candidato(candidato: Candidato):
  
    cursor.execute('''
        INSERT INTO candidatos (dni, nombre, apellido)
        VALUES (?, ?, ?)
    ''', (candidato.dni, candidato.nombre, candidato.apellido))
    conn.commit()
    return {"mensaje": "Candidato creado exitosamente"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

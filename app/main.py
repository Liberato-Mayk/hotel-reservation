from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session, crear_tablas
from models import Habitacion, Reserva

app = FastAPI(title="API de Reservas de Hotel", version="1.0")

@app.on_event("startup")
def on_startup():
    crear_tablas()

@app.get("/")
def root():
    return {"message": "Bienvenido a la API de Reservas de Hotel"}

@app.get("/Habitaciones")
def get_habitaciones(session: Session = Depends(get_session)):
    habitaciones = session.exec(select(Habitacion)).all()
    return habitaciones

@app.get("/Habitaciones/{habitacion_id}")
def get_habitacion(habitacion_id:int, session: Session = Depends(get_session)):
    habitacion = session.get(Habitacion, habitacion_id)
    if not habitacion:
        raise HTTPException(status_code=404, detail="Habitación no encontrada")
    return habitacion

@app.post("/Habitaciones")
def crear_habitacion(habitacion: Habitacion, session:Session =Depends(get_session)):
    session.add(habitacion)
    session.commit()
    session.refresh(habitacion)
    return habitacion

@app.put("/Reserva")
def crear_reserva(reserva:Reserva, session : Session = Depends(get_session)):
    session.add(reserva)
    session.commit()
    session.refresh(reserva)
    return reserva

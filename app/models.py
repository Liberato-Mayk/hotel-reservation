from typing import Optional
from sqlmodel import SQLModel, Field

class Habitacion(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    nombre : str
    tipo: str
    precio_noche : float
    capacidad : int
    descripcion : Optional[str] = None
    disponible : bool = True
    
class Reserva(SQLModel, table = True):
    id : Optional[int] = Field(default= None, primary_key=True)
    usuario_id : int
    habitacion_id : int
    fecha_checkin : str
    fecha_checkout : str
    total : float
    estado : str = "pendiente"
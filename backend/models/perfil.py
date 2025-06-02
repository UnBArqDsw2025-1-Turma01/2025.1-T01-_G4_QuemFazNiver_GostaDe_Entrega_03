from typing import Optional
from pydantic import BaseModel

class Perfil(BaseModel):
    avatar: Optional[bytes] = None
    capa: Optional[bytes] = None
    sobre: Optional[str] = None

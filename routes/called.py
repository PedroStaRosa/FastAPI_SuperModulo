from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlmodel import Session, select
from database import get_session
from models.called import Calleds
from schemas.calleds import CalledCreate
from datetime import datetime
from middleware import create_token

router = APIRouter()

@router.get("/called", response_model=list[Calleds])
def get_called(session: Session = Depends(get_session)):
    calleds = session.exec(select(Calleds)).all()
    return calleds

@router.get("/called/{called_id}")
def get_called(called_id: int, session: Session =Depends(get_session)):

    called = session.get(Calleds, called_id)

    if not called:
        raise HTTPException(status_code=404, detail="called not found")
    
    return called

@router.post("/called")
def get_called(called: CalledCreate, session: Session =Depends(get_session)):

    called_db = Calleds(**called.model_dump())

    session.add(called_db)
    session.commit()
    session.refresh(called_db)

    return {
        "message" : "Called created sucessfull",
        "called" : called_db
    }

@router.put("/called/{called_id}")
def put_called(called_id: int , called: CalledCreate, session: Session =Depends(get_session)):
    called_db = session.get(Calleds, called_id)
   
    if not called_id:
        raise HTTPException(status_code=404, detail="Called not found")
    
    called_db.status = called.status
    called_db.updated_at = datetime.now()

    session.commit()
    session.refresh(called_db)

    return called_db

@router.delete("/called/{called_id}")
def delete_called(called_id: int, session: Session = Depends(get_session)):
    called_db = session.get(Calleds, called_id)

    if not called_db:
        raise HTTPException(status_code=400, detail="Called not found")
    
    session.delete(called_db)
    session.commit()

    return {'message': "Called deleted!"}

@router.post("/called_create_token")
def get_called(email: dict):

    token = create_token(email)
    
    return {"user_token": token}


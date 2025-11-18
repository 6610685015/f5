import models
import schemas
from database import get_db
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/")
def get_names(
    db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ""
):
    skip = (page - 1) * limit

    names = (
        db.query(models.Name)
        .filter(models.Name.title.contains(search))
        .limit(limit)
        .offset(skip)
        .all()
    )
    return {"status": "success", "results": len(names), "names": names}


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_name(payload: schemas.NameBaseSchema, db: Session = Depends(get_db)):
    new_name = models.Name(**payload.dict())
    db.add(new_name)
    db.commit()
    db.refresh(new_name)
    return {"status": "success", "name": new_name}


@router.patch("/{nameId}")
def update_name(
    nameId: str, payload: schemas.NameBaseSchema, db: Session = Depends(get_db)
):
    name_query = db.query(models.Name).filter(models.Name.id == nameId)
    db_name = name_query.first()

    if not db_name:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No name with this id: {nameId} found",
        )
    update_data = payload.dict(exclude_unset=True)
    name_query.filter(models.Name.id == nameId).update(
        update_data, synchronize_session=False
    )
    db.commit()
    db.refresh(db_name)
    return {"status": "success", "name": db_name}


@router.get("/{nameId}")
def get_post(nameId: str, db: Session = Depends(get_db)):
    name = db.query(models.Name).filter(models.Name.id == nameId).first()
    if not name:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No name with this id: {id} found",
        )
    return {"status": "success", "name": name}


@router.delete("/{nameId}")
def delete_post(nameId: str, db: Session = Depends(get_db)):
    name_query = db.query(models.Name).filter(models.Name.id == nameId)
    name = name_query.first()
    if not name:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No name with this id: {id} found",
        )
    name_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

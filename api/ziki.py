import fastapi, os
import sqlalchemy.orm as orm
from .schemas import ziki_schemas as schemas
from .models import ziki_models as models

from fastapi import FastAPI, status, APIRouter, Depends
from api.database.db import get_db

app = APIRouter()

# Get people you are following
@app.get("/api/get_following")
def get_following(username: str, db: orm.Session = fastapi.Depends(get_db)):
    return "The people you are following"

# create a new follow using a post request
@app.post("/api/create")
def create_newfollow(body: schemas.Feed, db: orm.Session = fastapi.Depends(get_db)):
    return "This allows you follow"
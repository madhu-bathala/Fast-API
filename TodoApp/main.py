
from fastapi import FastAPI, Depends, HTTPException, Path
from pydantic import BaseModel, Field
from sqlalchemy.sql.annotation import Annotated
from sqlalchemy.sql.functions import session_user

from typing import Annotated
from sqlalchemy.orm import Session
from sqlalchemy.testing.util import total_size
from starlette import status

import models
from routers import auth, todos, admin
from models import Todos
from database import SessionLocal
from database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from app.api.api_route import api_router
from app.db.dbconnect import Base, engine
from app.api.error import APIException
import app.db.schemas

load_dotenv()


def lifespan(app: FastAPI):
    print("DB connecting ...")
    Base.metadata.create_all(bind=engine)
    print("Server starting ...")
    yield
    print("Server shutting down ...")


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")


@app.exception_handler(HTTPException)
def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


@app.exception_handler(APIException)
def api_exception_handler(request, error: APIException):
    return error.getResponse()

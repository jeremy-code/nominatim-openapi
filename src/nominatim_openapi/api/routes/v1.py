from datetime import UTC, datetime
from typing import Literal

import pydantic
from fastapi import APIRouter
from nominatim_api import StatusResult
from nominatim_api.version import NOMINATIM_API_VERSION

router = APIRouter(prefix="/v1")


@router.get("/search")
def search():
    return {"message": "Hello World"}


@router.get("/reverse")
def reverse():
    return {"message": "Hello World"}


@router.get("/lookup")
def lookup():
    return {"message": "Hello World"}


@pydantic.dataclasses.dataclass
class StatusResultSuccess(StatusResult):
    data_updated: datetime  # pyright: ignore[reportIncompatibleVariableOverride, reportGeneralTypeIssues]
    database_version: str  # pyright: ignore[reportIncompatibleVariableOverride, reportGeneralTypeIssues]
    software_version: str = NOMINATIM_API_VERSION


@pydantic.dataclasses.dataclass
class StatusResultError:
    status: int
    message: str


@router.get("/status", response_model=StatusResultSuccess | StatusResultError)
def status(format: Literal["json", "text"]) -> StatusResult:
    return StatusResult(
        status=0,
        message="OK",
        data_updated=datetime.now(tz=UTC),
        database_version="3.6.0-0",
    )


@router.get("/deletable")
def deletable():
    return {"message": "Hello World"}


@router.get("/polygons")
def polygons():
    return {"message": "Hello World"}


@router.get("/details")
def details():
    return {"message": "Hello World"}

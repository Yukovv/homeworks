from fastapi import APIRouter, HTTPException
from pydantic import conint, constr
from starlette.status import HTTP_404_NOT_FOUND

from . import funcs
from .models import Stuff

router = APIRouter(prefix="/container", tags=["Container"])


@router.get("")
def check_container():
    return funcs.check_container()


@router.post("", response_model=Stuff)
def add_stuff(name: constr(min_length=2), amount: conint(gt=0) = 1):
    return funcs.add_stuff(name, amount)


@router.delete("", responses={HTTP_404_NOT_FOUND: {"description": "stuff not found"}})
def remove_stuff(name):
    if name not in funcs.CONTAINER:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=f"no {name} in container"
        )

    funcs.remove_stuff(name)
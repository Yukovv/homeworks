from fastapi import APIRouter

from .quote_generation import rand_quote_gen


router = APIRouter(prefix="/random_quote")


@router.get("")
def quote():
    """
    "GET /random_quote"
    """
    return rand_quote_gen()
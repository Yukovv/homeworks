from .models import Stuff

CONTAINER = {}


def add_stuff(name, amount) -> Stuff:
    if name in CONTAINER:
        CONTAINER[name].amount += amount
        return CONTAINER[name]
    else:
        new_stuff = Stuff(name=name, amount=amount)
        CONTAINER[name] = new_stuff
        return new_stuff


def check_container() -> dict[str: int]:
    return {name: CONTAINER[name].amount for name in CONTAINER}


def remove_stuff(name) -> None:
    CONTAINER[name].amount -= 1
    if not CONTAINER[name].amount:
        del CONTAINER[name]








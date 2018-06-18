origin = list(range(1, 8))
SIZE_TOWER = len(origin)
destine = []
temp = []


def move_tower(size, origin, destine, temporal):
    if size >= 1:
        move_tower(size - 1, origin, temporal, destine)
        move_disc(origin, destine)
        move_tower(size - 1, temporal, destine, origin)


def move_disc(from_, to_):
    obj = from_.pop(0)
    to_.insert(0, obj)
    print(f"Mover disco de {from_} a {to_}")


move_tower(
    size=SIZE_TOWER,
    origin=origin,
    destine=destine,
    temporal=temp
)

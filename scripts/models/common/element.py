from enum import Enum


class Element(Enum):
    fire = "fire"
    water = "water"
    earth = "earth"
    air = "air"

    blue_fire = "blue fire"
    ice = "ice"
    plant = "plant"
    lightning = "lightning"

    magma = "magma"
    metal = "metal"
    smoke = "smoke"
    mud = "mud"
    shadow = "shadow"
    sand = "sand"

    mist = "mist"
    oil = "oil"
    combustion = "combustion"
    decay = "decay"
    magnetic = "magnetic"
    luminescent = "luminescent"

    not_fire = "-fire"
    not_water = "-water"
    not_earth = "-earth"
    not_air = "-air"

    not_blue_fire = "-blue fire"
    not_ice = "-ice"
    not_plant = "-plant"
    not_lightning = "-lightning"

    not_magma = "-magma"
    not_metal = "-metal"
    not_smoke = "-smoke"
    not_mud = "-mud"
    not_shadow = "-shadow"
    not_sand = "-sand"

    not_mist = "-mist"
    not_oil = "-oil"
    not_combustion = "-combustion"
    not_decay = "-decay"
    not_magnetic = "-magnetic"
    not_luminescent = "-luminescent"

    any = "any"
    none = "none"
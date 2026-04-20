import ujson
import os

_resource_directory = "resources/dicts/conditions/"

with open(
    os.path.normpath("resources/dicts/backstories.json"), "r", encoding="utf-8"
) as read_file:
    BACKSTORIES = ujson.loads(read_file.read())

with open(
    os.path.normpath(f"{_resource_directory}illnesses.json"), "r", encoding="utf-8"
) as read_file:
    ILLNESSES = ujson.loads(read_file.read())

with open(
    os.path.normpath(f"{_resource_directory}injuries.json"), "r", encoding="utf-8"
) as read_file:
    INJURIES = ujson.loads(read_file.read())

with open(
    os.path.normpath(f"{_resource_directory}permanent_conditions.json"),
    "r",
    encoding="utf-8",
) as read_file:
    PERMANENT = ujson.loads(read_file.read())

with open(
    os.path.normpath(f"{_resource_directory}elemental_condition_block.json"),
    "r",
    encoding="utf-8",
) as read_file:
    ELEMENT_BLOCK = ujson.loads(read_file.read())

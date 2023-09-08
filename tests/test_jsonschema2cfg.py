from typing import List, Optional, Union
from pydantic import BaseModel
from lark import Lark
from schemallm.server.jsonschema2cfg import create_lark_cfg_for_schema
from schemallm.models.jsonschema import parse_json_schema

# TODO(j.swannack): set up tests with pytest


def test_mvp_schema():
    class Observation(BaseModel):
        reporter: str
        value: float

    class Details(BaseModel):
        season: str
        temperature_celsius: float
        observations: List[Observation]

    schema = parse_json_schema(Details.schema())
    cfg = create_lark_cfg_for_schema(schema)
    parser = Lark(cfg, parser="lalr")

    instance = Details(
        season="winter",
        temperature_celsius=-5,
        observations=[
            Observation(reporter="John", value=1.2),
            Observation(reporter="Jane", value=3.4),
        ],
    ).json()

    parse_tree = parser.parse(instance)
    print(parse_tree)


def test_optional():
    class Observation(BaseModel):
        reporter: Optional[str]
        value: float

    schema = parse_json_schema(Observation.schema())
    cfg = create_lark_cfg_for_schema(schema)

    print(cfg)

    parser = Lark(cfg, parser="lalr")

    instances = [
        Observation(value=3.4).json(),
        Observation(reporter="hey", value=3.4).json(),
    ]

    for instance in instances:
        parse_tree = parser.parse(instance)
        print(parse_tree)


def test_union():
    class ReporterDetails(BaseModel):
        name: str
        age: float

    class Observation(BaseModel):
        reporter: Union[str, ReporterDetails]
        value: float

    print(Observation.schema_json(indent=2))
    schema = parse_json_schema(Observation.schema())
    cfg = create_lark_cfg_for_schema(schema)

    print(cfg)

    parser = Lark(cfg, parser="lalr")

    instances = [
        Observation(reporter="hey", value=3.4).json(),
        Observation(reporter={"name": "hey", "age": 3}, value=3.4).json(),
    ]

    for instance in instances:
        parse_tree = parser.parse(instance)
        print(parse_tree)


def test_int():
    class Observation(BaseModel):
        value: int

    schema = parse_json_schema(Observation.schema())
    cfg = create_lark_cfg_for_schema(schema)

    instance = Observation(value=3).json()

    print(cfg)

    parser = Lark(cfg, parser="lalr")
    parse_tree = parser.parse(instance)


def main():
    test_mvp_schema()
    test_optional()
    test_union()
    test_int()


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()

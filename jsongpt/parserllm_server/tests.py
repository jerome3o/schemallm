from typing import List, Optional, Union
from pydantic import BaseModel
from jsonschema2cfg import create_lark_cfg_for_schema
from lark import Lark
from models import JsonSchema, parse_json_schema


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
    parser = Lark(cfg, parser="lalr")

    instance = Observation(value=3.4).json()

    parse_tree = parser.parse(instance)
    print(parse_tree)


def main():
    # test_mvp_schema()
    test_optional()


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()

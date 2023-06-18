from pydantic import BaseModel, Field
from typing import Optional, Any, Dict, Union, List
from enum import Enum
from pydantic import parse_obj_as


class Type(str, Enum):
    OBJECT = "object"
    ARRAY = "array"
    STRING = "string"
    NUMBER = "number"
    INTEGER = "integer"
    BOOLEAN = "boolean"
    NULL = "null"


class BaseJsonSchema(BaseModel):
    title: Optional[str]
    description: Optional[str]
    default: Optional[Any]
    enum: Optional[List[Any]]

    class Config:
        arbitrary_types_allowed = True


class StringJsonSchema(BaseJsonSchema):
    type: Type = Field(Type.STRING, const=True)
    minLength: Optional[int]
    maxLength: Optional[int]
    pattern: Optional[str]


class ObjectJsonSchema(BaseJsonSchema):
    type: Type = Field(Type.OBJECT, const=True)
    properties: Optional[Dict[str, "JsonSchema"]]
    required: Optional[List[str]]
    additionalProperties: Optional[Union[bool, "JsonSchema"]]


class ArrayJsonSchema(BaseJsonSchema):
    type: Type = Field(Type.ARRAY, const=True)
    items: Optional[Union["JsonSchema", List["JsonSchema"]]]
    minItems: Optional[int]
    maxItems: Optional[int]
    uniqueItems: Optional[bool]


class NumberJsonSchema(BaseJsonSchema):
    type: Type = Field(Type.NUMBER, const=True)
    minimum: Optional[float]
    maximum: Optional[float]
    exclusiveMinimum: Optional[bool]
    exclusiveMaximum: Optional[bool]
    multipleOf: Optional[float]


class IntegerJsonSchema(BaseJsonSchema):
    type: Type = Field(Type.INTEGER, const=True)
    minimum: Optional[int]
    maximum: Optional[int]
    exclusiveMinimum: Optional[bool]
    exclusiveMaximum: Optional[bool]
    multipleOf: Optional[int]


class BooleanJsonSchema(BaseJsonSchema):
    type: Type = Field(Type.BOOLEAN, const=True)


class NullJsonSchema(BaseJsonSchema):
    type: Type = Field(Type.NULL, const=True)


JsonSchema = Union[
    StringJsonSchema,
    ObjectJsonSchema,
    ArrayJsonSchema,
    NumberJsonSchema,
    IntegerJsonSchema,
    BooleanJsonSchema,
    NullJsonSchema,
]

ObjectJsonSchema.update_forward_refs()
ArrayJsonSchema.update_forward_refs()


def parse_json_schema(schema: Dict[str, Any]) -> JsonSchema:
    return parse_obj_as(JsonSchema, schema)


def main():
    class Details(BaseModel):
        season: str
        temperature_celsius: float

    schema = parse_obj_as(JsonSchema, Details.schema())
    print(schema)


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()

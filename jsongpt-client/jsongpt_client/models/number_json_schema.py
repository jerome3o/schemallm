from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.schema_type import SchemaType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.number_json_schema_definitions import NumberJsonSchemaDefinitions


T = TypeVar("T", bound="NumberJsonSchema")


@attr.s(auto_attribs=True)
class NumberJsonSchema:
    """
    Attributes:
        title (Union[Unset, str]):
        description (Union[Unset, str]):
        default (Union[Unset, Any]):
        enum (Union[Unset, List[Any]]):
        definitions (Union[Unset, NumberJsonSchemaDefinitions]):
        type (Union[Unset, SchemaType]): An enumeration. Default: SchemaType.NUMBER.
        minimum (Union[Unset, float]):
        maximum (Union[Unset, float]):
        exclusive_minimum (Union[Unset, bool]):
        exclusive_maximum (Union[Unset, bool]):
        multiple_of (Union[Unset, float]):
    """

    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    default: Union[Unset, Any] = UNSET
    enum: Union[Unset, List[Any]] = UNSET
    definitions: Union[Unset, "NumberJsonSchemaDefinitions"] = UNSET
    type: Union[Unset, SchemaType] = SchemaType.NUMBER
    minimum: Union[Unset, float] = UNSET
    maximum: Union[Unset, float] = UNSET
    exclusive_minimum: Union[Unset, bool] = UNSET
    exclusive_maximum: Union[Unset, bool] = UNSET
    multiple_of: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        description = self.description
        default = self.default
        enum: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.enum, Unset):
            enum = self.enum

        definitions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.definitions, Unset):
            definitions = self.definitions.to_dict()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        minimum = self.minimum
        maximum = self.maximum
        exclusive_minimum = self.exclusive_minimum
        exclusive_maximum = self.exclusive_maximum
        multiple_of = self.multiple_of

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if default is not UNSET:
            field_dict["default"] = default
        if enum is not UNSET:
            field_dict["enum"] = enum
        if definitions is not UNSET:
            field_dict["definitions"] = definitions
        if type is not UNSET:
            field_dict["type"] = type
        if minimum is not UNSET:
            field_dict["minimum"] = minimum
        if maximum is not UNSET:
            field_dict["maximum"] = maximum
        if exclusive_minimum is not UNSET:
            field_dict["exclusiveMinimum"] = exclusive_minimum
        if exclusive_maximum is not UNSET:
            field_dict["exclusiveMaximum"] = exclusive_maximum
        if multiple_of is not UNSET:
            field_dict["multipleOf"] = multiple_of

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.number_json_schema_definitions import NumberJsonSchemaDefinitions

        d = src_dict.copy()
        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        default = d.pop("default", UNSET)

        enum = cast(List[Any], d.pop("enum", UNSET))

        _definitions = d.pop("definitions", UNSET)
        definitions: Union[Unset, NumberJsonSchemaDefinitions]
        if isinstance(_definitions, Unset):
            definitions = UNSET
        else:
            definitions = NumberJsonSchemaDefinitions.from_dict(_definitions)

        _type = d.pop("type", UNSET)
        type: Union[Unset, SchemaType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = SchemaType(_type)

        minimum = d.pop("minimum", UNSET)

        maximum = d.pop("maximum", UNSET)

        exclusive_minimum = d.pop("exclusiveMinimum", UNSET)

        exclusive_maximum = d.pop("exclusiveMaximum", UNSET)

        multiple_of = d.pop("multipleOf", UNSET)

        number_json_schema = cls(
            title=title,
            description=description,
            default=default,
            enum=enum,
            definitions=definitions,
            type=type,
            minimum=minimum,
            maximum=maximum,
            exclusive_minimum=exclusive_minimum,
            exclusive_maximum=exclusive_maximum,
            multiple_of=multiple_of,
        )

        number_json_schema.additional_properties = d
        return number_json_schema

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

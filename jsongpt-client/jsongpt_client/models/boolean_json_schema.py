from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.schema_type import SchemaType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.boolean_json_schema_definitions import BooleanJsonSchemaDefinitions


T = TypeVar("T", bound="BooleanJsonSchema")


@attr.s(auto_attribs=True)
class BooleanJsonSchema:
    """
    Attributes:
        title (Union[Unset, str]):
        description (Union[Unset, str]):
        default (Union[Unset, Any]):
        enum (Union[Unset, List[Any]]):
        definitions (Union[Unset, BooleanJsonSchemaDefinitions]):
        type (Union[Unset, SchemaType]): An enumeration. Default: SchemaType.BOOLEAN.
    """

    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    default: Union[Unset, Any] = UNSET
    enum: Union[Unset, List[Any]] = UNSET
    definitions: Union[Unset, "BooleanJsonSchemaDefinitions"] = UNSET
    type: Union[Unset, SchemaType] = SchemaType.BOOLEAN
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.boolean_json_schema_definitions import BooleanJsonSchemaDefinitions

        d = src_dict.copy()
        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        default = d.pop("default", UNSET)

        enum = cast(List[Any], d.pop("enum", UNSET))

        _definitions = d.pop("definitions", UNSET)
        definitions: Union[Unset, BooleanJsonSchemaDefinitions]
        if isinstance(_definitions, Unset):
            definitions = UNSET
        else:
            definitions = BooleanJsonSchemaDefinitions.from_dict(_definitions)

        _type = d.pop("type", UNSET)
        type: Union[Unset, SchemaType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = SchemaType(_type)

        boolean_json_schema = cls(
            title=title,
            description=description,
            default=default,
            enum=enum,
            definitions=definitions,
            type=type,
        )

        boolean_json_schema.additional_properties = d
        return boolean_json_schema

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

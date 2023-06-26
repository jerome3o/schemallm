from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.any_of_json_schema_definitions import AnyOfJsonSchemaDefinitions
    from ..models.array_json_schema import ArrayJsonSchema
    from ..models.boolean_json_schema import BooleanJsonSchema
    from ..models.integer_json_schema import IntegerJsonSchema
    from ..models.null_json_schema import NullJsonSchema
    from ..models.number_json_schema import NumberJsonSchema
    from ..models.object_json_schema import ObjectJsonSchema
    from ..models.ref_json_schema import RefJsonSchema
    from ..models.string_json_schema import StringJsonSchema


T = TypeVar("T", bound="AnyOfJsonSchema")


@attr.s(auto_attribs=True)
class AnyOfJsonSchema:
    """
    Attributes:
        any_of (List[Union['AnyOfJsonSchema', 'ArrayJsonSchema', 'BooleanJsonSchema', 'IntegerJsonSchema',
            'NullJsonSchema', 'NumberJsonSchema', 'ObjectJsonSchema', 'RefJsonSchema', 'StringJsonSchema']]):
        title (Union[Unset, str]):
        description (Union[Unset, str]):
        default (Union[Unset, Any]):
        enum (Union[Unset, List[Any]]):
        definitions (Union[Unset, AnyOfJsonSchemaDefinitions]):
    """

    any_of: List[
        Union[
            "AnyOfJsonSchema",
            "ArrayJsonSchema",
            "BooleanJsonSchema",
            "IntegerJsonSchema",
            "NullJsonSchema",
            "NumberJsonSchema",
            "ObjectJsonSchema",
            "RefJsonSchema",
            "StringJsonSchema",
        ]
    ]
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    default: Union[Unset, Any] = UNSET
    enum: Union[Unset, List[Any]] = UNSET
    definitions: Union[Unset, "AnyOfJsonSchemaDefinitions"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.array_json_schema import ArrayJsonSchema
        from ..models.boolean_json_schema import BooleanJsonSchema
        from ..models.integer_json_schema import IntegerJsonSchema
        from ..models.number_json_schema import NumberJsonSchema
        from ..models.object_json_schema import ObjectJsonSchema
        from ..models.ref_json_schema import RefJsonSchema
        from ..models.string_json_schema import StringJsonSchema

        any_of = []
        for any_of_item_data in self.any_of:
            any_of_item: Dict[str, Any]

            if isinstance(any_of_item_data, RefJsonSchema):
                any_of_item = any_of_item_data.to_dict()

            elif isinstance(any_of_item_data, AnyOfJsonSchema):
                any_of_item = any_of_item_data.to_dict()

            elif isinstance(any_of_item_data, StringJsonSchema):
                any_of_item = any_of_item_data.to_dict()

            elif isinstance(any_of_item_data, ObjectJsonSchema):
                any_of_item = any_of_item_data.to_dict()

            elif isinstance(any_of_item_data, ArrayJsonSchema):
                any_of_item = any_of_item_data.to_dict()

            elif isinstance(any_of_item_data, NumberJsonSchema):
                any_of_item = any_of_item_data.to_dict()

            elif isinstance(any_of_item_data, IntegerJsonSchema):
                any_of_item = any_of_item_data.to_dict()

            elif isinstance(any_of_item_data, BooleanJsonSchema):
                any_of_item = any_of_item_data.to_dict()

            else:
                any_of_item = any_of_item_data.to_dict()

            any_of.append(any_of_item)

        title = self.title
        description = self.description
        default = self.default
        enum: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.enum, Unset):
            enum = self.enum

        definitions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.definitions, Unset):
            definitions = self.definitions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "anyOf": any_of,
            }
        )
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.any_of_json_schema_definitions import AnyOfJsonSchemaDefinitions
        from ..models.array_json_schema import ArrayJsonSchema
        from ..models.boolean_json_schema import BooleanJsonSchema
        from ..models.integer_json_schema import IntegerJsonSchema
        from ..models.null_json_schema import NullJsonSchema
        from ..models.number_json_schema import NumberJsonSchema
        from ..models.object_json_schema import ObjectJsonSchema
        from ..models.ref_json_schema import RefJsonSchema
        from ..models.string_json_schema import StringJsonSchema

        d = src_dict.copy()
        any_of = []
        _any_of = d.pop("anyOf")
        for any_of_item_data in _any_of:

            def _parse_any_of_item(
                data: object,
            ) -> Union[
                "AnyOfJsonSchema",
                "ArrayJsonSchema",
                "BooleanJsonSchema",
                "IntegerJsonSchema",
                "NullJsonSchema",
                "NumberJsonSchema",
                "ObjectJsonSchema",
                "RefJsonSchema",
                "StringJsonSchema",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    any_of_item_type_0 = RefJsonSchema.from_dict(data)

                    return any_of_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    any_of_item_type_1 = AnyOfJsonSchema.from_dict(data)

                    return any_of_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    any_of_item_type_2 = StringJsonSchema.from_dict(data)

                    return any_of_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    any_of_item_type_3 = ObjectJsonSchema.from_dict(data)

                    return any_of_item_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    any_of_item_type_4 = ArrayJsonSchema.from_dict(data)

                    return any_of_item_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    any_of_item_type_5 = NumberJsonSchema.from_dict(data)

                    return any_of_item_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    any_of_item_type_6 = IntegerJsonSchema.from_dict(data)

                    return any_of_item_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    any_of_item_type_7 = BooleanJsonSchema.from_dict(data)

                    return any_of_item_type_7
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                any_of_item_type_8 = NullJsonSchema.from_dict(data)

                return any_of_item_type_8

            any_of_item = _parse_any_of_item(any_of_item_data)

            any_of.append(any_of_item)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        default = d.pop("default", UNSET)

        enum = cast(List[Any], d.pop("enum", UNSET))

        _definitions = d.pop("definitions", UNSET)
        definitions: Union[Unset, AnyOfJsonSchemaDefinitions]
        if isinstance(_definitions, Unset):
            definitions = UNSET
        else:
            definitions = AnyOfJsonSchemaDefinitions.from_dict(_definitions)

        any_of_json_schema = cls(
            any_of=any_of,
            title=title,
            description=description,
            default=default,
            enum=enum,
            definitions=definitions,
        )

        any_of_json_schema.additional_properties = d
        return any_of_json_schema

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

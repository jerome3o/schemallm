from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.schema_type import SchemaType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.any_of_json_schema import AnyOfJsonSchema
    from ..models.array_json_schema_definitions import ArrayJsonSchemaDefinitions
    from ..models.boolean_json_schema import BooleanJsonSchema
    from ..models.integer_json_schema import IntegerJsonSchema
    from ..models.null_json_schema import NullJsonSchema
    from ..models.number_json_schema import NumberJsonSchema
    from ..models.object_json_schema import ObjectJsonSchema
    from ..models.ref_json_schema import RefJsonSchema
    from ..models.string_json_schema import StringJsonSchema


T = TypeVar("T", bound="ArrayJsonSchema")


@attr.s(auto_attribs=True)
class ArrayJsonSchema:
    """
    Attributes:
        title (Union[Unset, str]):
        description (Union[Unset, str]):
        default (Union[Unset, Any]):
        enum (Union[Unset, List[Any]]):
        definitions (Union[Unset, ArrayJsonSchemaDefinitions]):
        type (Union[Unset, SchemaType]): An enumeration. Default: SchemaType.ARRAY.
        items (Union[List[Union['AnyOfJsonSchema', 'ArrayJsonSchema', 'BooleanJsonSchema', 'IntegerJsonSchema',
            'NullJsonSchema', 'NumberJsonSchema', 'ObjectJsonSchema', 'RefJsonSchema', 'StringJsonSchema']],
            Union['AnyOfJsonSchema', 'ArrayJsonSchema', 'BooleanJsonSchema', 'IntegerJsonSchema', 'NullJsonSchema',
            'NumberJsonSchema', 'ObjectJsonSchema', 'RefJsonSchema', 'StringJsonSchema'], Unset]):
        min_items (Union[Unset, int]):
        max_items (Union[Unset, int]):
        unique_items (Union[Unset, bool]):
    """

    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    default: Union[Unset, Any] = UNSET
    enum: Union[Unset, List[Any]] = UNSET
    definitions: Union[Unset, "ArrayJsonSchemaDefinitions"] = UNSET
    type: Union[Unset, SchemaType] = SchemaType.ARRAY
    items: Union[
        List[
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
        ],
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
        ],
        Unset,
    ] = UNSET
    min_items: Union[Unset, int] = UNSET
    max_items: Union[Unset, int] = UNSET
    unique_items: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.any_of_json_schema import AnyOfJsonSchema
        from ..models.boolean_json_schema import BooleanJsonSchema
        from ..models.integer_json_schema import IntegerJsonSchema
        from ..models.null_json_schema import NullJsonSchema
        from ..models.number_json_schema import NumberJsonSchema
        from ..models.object_json_schema import ObjectJsonSchema
        from ..models.ref_json_schema import RefJsonSchema
        from ..models.string_json_schema import StringJsonSchema

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

        items: Union[Dict[str, Any], List[Dict[str, Any]], Unset]
        if isinstance(self.items, Unset):
            items = UNSET

        elif isinstance(
            self.items,
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
            ],
        ):
            if isinstance(self.items, Unset):
                items = UNSET

            elif isinstance(self.items, RefJsonSchema):
                items = UNSET
                if not isinstance(self.items, Unset):
                    items = self.items.to_dict()

            elif isinstance(self.items, AnyOfJsonSchema):
                items = UNSET
                if not isinstance(self.items, Unset):
                    items = self.items.to_dict()

            elif isinstance(self.items, StringJsonSchema):
                items = UNSET
                if not isinstance(self.items, Unset):
                    items = self.items.to_dict()

            elif isinstance(self.items, ObjectJsonSchema):
                items = UNSET
                if not isinstance(self.items, Unset):
                    items = self.items.to_dict()

            elif isinstance(self.items, ArrayJsonSchema):
                items = UNSET
                if not isinstance(self.items, Unset):
                    items = self.items.to_dict()

            elif isinstance(self.items, NumberJsonSchema):
                items = UNSET
                if not isinstance(self.items, Unset):
                    items = self.items.to_dict()

            elif isinstance(self.items, IntegerJsonSchema):
                items = UNSET
                if not isinstance(self.items, Unset):
                    items = self.items.to_dict()

            elif isinstance(self.items, BooleanJsonSchema):
                items = UNSET
                if not isinstance(self.items, Unset):
                    items = self.items.to_dict()

            else:
                items = UNSET
                if not isinstance(self.items, Unset):
                    items = self.items.to_dict()

        else:
            items = UNSET
            if not isinstance(self.items, Unset):
                items = []
                for items_type_1_item_data in self.items:
                    items_type_1_item: Dict[str, Any]

                    if isinstance(items_type_1_item_data, RefJsonSchema):
                        items_type_1_item = items_type_1_item_data.to_dict()

                    elif isinstance(items_type_1_item_data, AnyOfJsonSchema):
                        items_type_1_item = items_type_1_item_data.to_dict()

                    elif isinstance(items_type_1_item_data, StringJsonSchema):
                        items_type_1_item = items_type_1_item_data.to_dict()

                    elif isinstance(items_type_1_item_data, ObjectJsonSchema):
                        items_type_1_item = items_type_1_item_data.to_dict()

                    elif isinstance(items_type_1_item_data, ArrayJsonSchema):
                        items_type_1_item = items_type_1_item_data.to_dict()

                    elif isinstance(items_type_1_item_data, NumberJsonSchema):
                        items_type_1_item = items_type_1_item_data.to_dict()

                    elif isinstance(items_type_1_item_data, IntegerJsonSchema):
                        items_type_1_item = items_type_1_item_data.to_dict()

                    elif isinstance(items_type_1_item_data, BooleanJsonSchema):
                        items_type_1_item = items_type_1_item_data.to_dict()

                    else:
                        items_type_1_item = items_type_1_item_data.to_dict()

                    items.append(items_type_1_item)

        min_items = self.min_items
        max_items = self.max_items
        unique_items = self.unique_items

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
        if items is not UNSET:
            field_dict["items"] = items
        if min_items is not UNSET:
            field_dict["minItems"] = min_items
        if max_items is not UNSET:
            field_dict["maxItems"] = max_items
        if unique_items is not UNSET:
            field_dict["uniqueItems"] = unique_items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.any_of_json_schema import AnyOfJsonSchema
        from ..models.array_json_schema_definitions import ArrayJsonSchemaDefinitions
        from ..models.boolean_json_schema import BooleanJsonSchema
        from ..models.integer_json_schema import IntegerJsonSchema
        from ..models.null_json_schema import NullJsonSchema
        from ..models.number_json_schema import NumberJsonSchema
        from ..models.object_json_schema import ObjectJsonSchema
        from ..models.ref_json_schema import RefJsonSchema
        from ..models.string_json_schema import StringJsonSchema

        d = src_dict.copy()
        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        default = d.pop("default", UNSET)

        enum = cast(List[Any], d.pop("enum", UNSET))

        _definitions = d.pop("definitions", UNSET)
        definitions: Union[Unset, ArrayJsonSchemaDefinitions]
        if isinstance(_definitions, Unset):
            definitions = UNSET
        else:
            definitions = ArrayJsonSchemaDefinitions.from_dict(_definitions)

        _type = d.pop("type", UNSET)
        type: Union[Unset, SchemaType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = SchemaType(_type)

        def _parse_items(
            data: object,
        ) -> Union[
            List[
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
            ],
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
            ],
            Unset,
        ]:
            if isinstance(data, Unset):
                return data

            def _parse_items_type_0(
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
                Unset,
            ]:
                if isinstance(data, Unset):
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _items_type_0_type_0 = data
                    items_type_0_type_0: Union[Unset, RefJsonSchema]
                    if isinstance(_items_type_0_type_0, Unset):
                        items_type_0_type_0 = UNSET
                    else:
                        items_type_0_type_0 = RefJsonSchema.from_dict(_items_type_0_type_0)

                    return items_type_0_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _items_type_0_type_1 = data
                    items_type_0_type_1: Union[Unset, AnyOfJsonSchema]
                    if isinstance(_items_type_0_type_1, Unset):
                        items_type_0_type_1 = UNSET
                    else:
                        items_type_0_type_1 = AnyOfJsonSchema.from_dict(_items_type_0_type_1)

                    return items_type_0_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _items_type_0_type_2 = data
                    items_type_0_type_2: Union[Unset, StringJsonSchema]
                    if isinstance(_items_type_0_type_2, Unset):
                        items_type_0_type_2 = UNSET
                    else:
                        items_type_0_type_2 = StringJsonSchema.from_dict(_items_type_0_type_2)

                    return items_type_0_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _items_type_0_type_3 = data
                    items_type_0_type_3: Union[Unset, ObjectJsonSchema]
                    if isinstance(_items_type_0_type_3, Unset):
                        items_type_0_type_3 = UNSET
                    else:
                        items_type_0_type_3 = ObjectJsonSchema.from_dict(_items_type_0_type_3)

                    return items_type_0_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _items_type_0_type_4 = data
                    items_type_0_type_4: Union[Unset, ArrayJsonSchema]
                    if isinstance(_items_type_0_type_4, Unset):
                        items_type_0_type_4 = UNSET
                    else:
                        items_type_0_type_4 = ArrayJsonSchema.from_dict(_items_type_0_type_4)

                    return items_type_0_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _items_type_0_type_5 = data
                    items_type_0_type_5: Union[Unset, NumberJsonSchema]
                    if isinstance(_items_type_0_type_5, Unset):
                        items_type_0_type_5 = UNSET
                    else:
                        items_type_0_type_5 = NumberJsonSchema.from_dict(_items_type_0_type_5)

                    return items_type_0_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _items_type_0_type_6 = data
                    items_type_0_type_6: Union[Unset, IntegerJsonSchema]
                    if isinstance(_items_type_0_type_6, Unset):
                        items_type_0_type_6 = UNSET
                    else:
                        items_type_0_type_6 = IntegerJsonSchema.from_dict(_items_type_0_type_6)

                    return items_type_0_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _items_type_0_type_7 = data
                    items_type_0_type_7: Union[Unset, BooleanJsonSchema]
                    if isinstance(_items_type_0_type_7, Unset):
                        items_type_0_type_7 = UNSET
                    else:
                        items_type_0_type_7 = BooleanJsonSchema.from_dict(_items_type_0_type_7)

                    return items_type_0_type_7
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                _items_type_0_type_8 = data
                items_type_0_type_8: Union[Unset, NullJsonSchema]
                if isinstance(_items_type_0_type_8, Unset):
                    items_type_0_type_8 = UNSET
                else:
                    items_type_0_type_8 = NullJsonSchema.from_dict(_items_type_0_type_8)

                return items_type_0_type_8

            items_type_0 = _parse_items_type_0(data)

            return items_type_0
            if not isinstance(data, list):
                raise TypeError()
            items_type_1 = UNSET
            _items_type_1 = data
            for items_type_1_item_data in _items_type_1 or []:

                def _parse_items_type_1_item(
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
                        items_type_1_item_type_0 = RefJsonSchema.from_dict(data)

                        return items_type_1_item_type_0
                    except:  # noqa: E722
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        items_type_1_item_type_1 = AnyOfJsonSchema.from_dict(data)

                        return items_type_1_item_type_1
                    except:  # noqa: E722
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        items_type_1_item_type_2 = StringJsonSchema.from_dict(data)

                        return items_type_1_item_type_2
                    except:  # noqa: E722
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        items_type_1_item_type_3 = ObjectJsonSchema.from_dict(data)

                        return items_type_1_item_type_3
                    except:  # noqa: E722
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        items_type_1_item_type_4 = ArrayJsonSchema.from_dict(data)

                        return items_type_1_item_type_4
                    except:  # noqa: E722
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        items_type_1_item_type_5 = NumberJsonSchema.from_dict(data)

                        return items_type_1_item_type_5
                    except:  # noqa: E722
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        items_type_1_item_type_6 = IntegerJsonSchema.from_dict(data)

                        return items_type_1_item_type_6
                    except:  # noqa: E722
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        items_type_1_item_type_7 = BooleanJsonSchema.from_dict(data)

                        return items_type_1_item_type_7
                    except:  # noqa: E722
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    items_type_1_item_type_8 = NullJsonSchema.from_dict(data)

                    return items_type_1_item_type_8

                items_type_1_item = _parse_items_type_1_item(items_type_1_item_data)

                items_type_1.append(items_type_1_item)

            return items_type_1

        items = _parse_items(d.pop("items", UNSET))

        min_items = d.pop("minItems", UNSET)

        max_items = d.pop("maxItems", UNSET)

        unique_items = d.pop("uniqueItems", UNSET)

        array_json_schema = cls(
            title=title,
            description=description,
            default=default,
            enum=enum,
            definitions=definitions,
            type=type,
            items=items,
            min_items=min_items,
            max_items=max_items,
            unique_items=unique_items,
        )

        array_json_schema.additional_properties = d
        return array_json_schema

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

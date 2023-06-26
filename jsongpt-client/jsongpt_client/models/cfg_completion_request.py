from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CfgCompletionRequest")


@attr.s(auto_attribs=True)
class CfgCompletionRequest:
    """
    Attributes:
        prompt (str):
        cfg (str):
        max_tokens (Union[Unset, int]):  Default: 2000.
        stop (Union[Unset, List[str]]):
        temperature (Union[Unset, float]):  Default: 0.7.
    """

    prompt: str
    cfg: str
    max_tokens: Union[Unset, int] = 2000
    stop: Union[Unset, List[str]] = UNSET
    temperature: Union[Unset, float] = 0.7
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        prompt = self.prompt
        cfg = self.cfg
        max_tokens = self.max_tokens
        stop: Union[Unset, List[str]] = UNSET
        if not isinstance(self.stop, Unset):
            stop = self.stop

        temperature = self.temperature

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prompt": prompt,
                "cfg": cfg,
            }
        )
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens
        if stop is not UNSET:
            field_dict["stop"] = stop
        if temperature is not UNSET:
            field_dict["temperature"] = temperature

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        prompt = d.pop("prompt")

        cfg = d.pop("cfg")

        max_tokens = d.pop("max_tokens", UNSET)

        stop = cast(List[str], d.pop("stop", UNSET))

        temperature = d.pop("temperature", UNSET)

        cfg_completion_request = cls(
            prompt=prompt,
            cfg=cfg,
            max_tokens=max_tokens,
            stop=stop,
            temperature=temperature,
        )

        cfg_completion_request.additional_properties = d
        return cfg_completion_request

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

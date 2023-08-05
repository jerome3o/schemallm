from pydantic import BaseModel
from typing import List, Dict
from enum import Enum


class EndCondition(Enum):
    TOKEN_LOOKAHEAD = "token_lookahead"
    REPEAT = "repeat"
    MAX_TOKENS = "max_tokens"
    PROBABILITY_LIMIT = "probability_limit"
    NONE = "none"


class LogitTrackerStep(BaseModel):
    logits_raw: List[float]
    allowed_ids: List[int]


class LogitTracker(BaseModel):
    patterns: List[str]
    token_to_index: Dict[str, int]
    index_to_token: Dict[int, str]
    steps: List[LogitTrackerStep] = []
    result: str = ""
    result_tokens: List[str] = []
    end_condition: EndCondition = EndCondition.NONE

    def add_step(
        self,
        logits_raw: List[float],
        allowed_ids: List[int],
    ):
        self.steps.append(
            LogitTrackerStep(
                logits_raw=logits_raw,
                allowed_ids=allowed_ids,
            )
        )

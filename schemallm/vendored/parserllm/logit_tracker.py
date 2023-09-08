from typing import List
from pydantic import BaseModel

from schemallm.vendored.rellm.logit_tracker import LogitTracker


class LogitTrackerParserLLM(BaseModel):
    cfg: str
    prompt: str
    re_steps: List[LogitTracker] = []

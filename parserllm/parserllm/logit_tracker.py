from typing import List
from pydantic import BaseModel

from rellm.logit_tracker import LogitTracker


class LogitTrackerParserLLM(BaseModel):
    cfg: str
    re_steps: List[LogitTracker] = []

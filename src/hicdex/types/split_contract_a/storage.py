# generated by datamodel-codegen:
#   filename:  storage.json

from __future__ import annotations

from typing import Dict, List

from pydantic import BaseModel, Extra


class SplitContractAStorage(BaseModel):
    class Config:
        extra = Extra.forbid

    administrator: str
    coreParticipants: List[str]
    hicetnuncMinterAddress: str
    shares: Dict[str, str]
    totalShares: str

# generated by datamodel-codegen:
#   filename:  token_metadata.json

from __future__ import annotations

from typing import List

from pydantic import BaseModel


class TokenMetadataParameter(BaseModel):
    token_ids: List[str]
    handler: str
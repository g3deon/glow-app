from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, Field


def utc_now():
  return datetime.now(timezone.utc)

class Token(BaseModel):
  jti: Optional[int] = None
  exp: int
  iat: Optional[datetime] = Field(default_factory=utc_now)
  sub: str

from pydantic import BaseModel
from typing import Optional

class Meta(BaseModel):
    href: str
    metadataHref: Optional[str]
    type: str
    mediaType: Optional[str]
    size: Optional[int]
    limit: Optional[int]
    offset: Optional[int]

class OwnerGroup(BaseModel):
    meta: Meta

class Currency(BaseModel):
    meta: Meta

class PriceType(BaseModel):
    meta: Meta
    id: Optional[str]
    name: Optional[str]
    externalCode: Optional[str]

class Price(BaseModel):
    value: float
    currency: Currency
    priceType: Optional[PriceType]

class UOM(BaseModel):
    meta: Meta

class ImageList(BaseModel):
    meta: Meta

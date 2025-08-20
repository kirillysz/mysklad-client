from pydantic import BaseModel, UUID4
from typing import List, Optional

from src.models.base import Meta, OwnerGroup, Price, UOM, ImageList

class CounterParty(BaseModel):
    meta: Meta

class Barcode(BaseModel):
    ean13: str

class Product(BaseModel):
    meta: Meta
    id: UUID4
    accountId: UUID4
    owner: Optional[OwnerGroup]
    shared: bool
    group: Optional[OwnerGroup]
    updated: str
    name: str
    code: Optional[str]
    externalCode: Optional[str]
    archived: bool
    pathName: Optional[str]
    useParentVat: Optional[bool]
    vat: Optional[float]
    vatEnabled: Optional[bool]
    effectiveVat: Optional[float]
    effectiveVatEnabled: Optional[bool]
    uom: Optional[UOM]
    images: Optional[ImageList]
    minPrice: Optional[Price]
    salePrices: Optional[List[Price]] = []
    supplier: Optional[CounterParty]
    buyPrice: Optional[Price]
    article: Optional[str]
    weight: Optional[float]
    volume: Optional[float]
    barcodes: Optional[List[Barcode]] = []
    variantsCount: Optional[int]
    isSerialTrackable: Optional[bool]
    stock: Optional[float]
    reserve: Optional[float]
    inTransit: Optional[float]
    quantity: Optional[float]

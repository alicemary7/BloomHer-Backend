from pydantic import BaseModel
from typing import List, Optional, Any

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    rating: Optional[float] = 0
    stock: int
    image_url: str
    features: Optional[str] = ""
    review_count: Optional[int] = 0


class ProductOut(ProductCreate):
    id: int
    is_active: bool

    model_config = {"from_attributes": True}



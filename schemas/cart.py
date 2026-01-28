from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

from schemas.product import ProductOut

class CartCreate(BaseModel):
    product_id: int
    quantity: int = 1

class CartOut(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
    is_active: bool
    created_at: datetime
    product: ProductOut 
    
    model_config = {"from_attributes": True}
        

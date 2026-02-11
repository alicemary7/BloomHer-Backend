from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from dependencies import connect_db
from models import Product
from schemas.product import ProductCreate
from routers.users import get_current_user
from models.users import User

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_product(
    data: ProductCreate, 
    db: Session = Depends(connect_db),
    current_user: User = Depends(get_current_user)
):
    # Only admins can create
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Forbidden")
    product = Product(**data.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


@router.get("/")
def get_products(db: Session = Depends(connect_db)):
    return db.query(Product).filter(Product.is_active == True).all()


@router.get("/{product_id}")
def get_single_product(
    product_id: int, db: Session = Depends(connect_db)
):
    single_product = db.query(Product).filter(Product.id == product_id).first()
    if not single_product:
        raise HTTPException(status_code=404, detail="product not found")
    return single_product


@router.put("/{product_id}")
def update_product(
    product_id: int, 
    data: ProductCreate, 
    db: Session = Depends(connect_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Forbidden")
    target_product = db.query(Product).filter(Product.id == product_id).first()
    if not target_product:
        raise HTTPException(status_code=404, detail="product not found")
    
    target_product.name = data.name
    target_product.description = data.description
    target_product.price = data.price
    target_product.price_small = data.price_small
    target_product.price_regular = data.price_regular
    target_product.price_large = data.price_large
    target_product.price_xl = data.price_xl
    target_product.stock = data.stock
    target_product.image_url = data.image_url
    target_product.features = data.features
    target_product.rating = data.rating if data.rating is not None else target_product.rating
    target_product.review_count = data.review_count if data.review_count is not None else target_product.review_count

    db.commit()
    db.refresh(target_product)

    return target_product


@router.delete("/{product_id}", status_code=status.HTTP_200_OK)
def delete_product(
    product_id: int, 
    db: Session = Depends(connect_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Forbidden")
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="product not found")
    
    product.is_active = False
    db.commit()
    return {"message": "Product deactivated successfully"}

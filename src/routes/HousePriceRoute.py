
from fastapi import APIRouter

from schemas.HousePriceSchema import HousePriceSchema


router = APIRouter(prefix='/houseprice')


@router.post('/')
def predict_price(housePrice: HousePriceSchema):
    return ''
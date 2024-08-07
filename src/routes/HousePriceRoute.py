
import json
import pandas
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from app import index
from schemas.HousePriceSchema import HousePriceSchema
import pandas as pd
import joblib
import csv


file=r"D:\ayush.rana\VScodeProjects\HousePriceIndiaApi\src\utils\house_data_model.pkl"
file_two = r'D:\ayush.rana\VScodeProjects\HousePriceIndiaApi\src\utils\house_data_columns.pkl'

mlmodel = joblib.load(open(file, 'rb'))
columns = joblib.load(open(file_two, 'rb'))


router = APIRouter(prefix='/houseprice')


@router.post('/predict')
def predict_price(housePrice: HousePriceSchema):
   prices = housePrice.model_dump_json()
   df=pd.DataFrame(prices)
   print(type(df))
   df.reindex(columns=columns)
   return {
        'predictions': list("predictions")
    }
    
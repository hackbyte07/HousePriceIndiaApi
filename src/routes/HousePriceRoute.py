
from fastapi import APIRouter
from schemas.HousePriceSchema import HousePriceSchema
import pandas as pd
import joblib

file = r"D:\ayush.rana\VScodeProjects\HousePriceIndiaApi\src\utils\house_data_model.pkl"
file_two = r'D:\ayush.rana\VScodeProjects\HousePriceIndiaApi\src\utils\house_data_columns.pkl'

mlmodel = joblib.load(open(file, 'rb'))
columns = joblib.load(open(file_two, 'rb'))

router = APIRouter(prefix='/houseprice')

@router.post('/predict')
def predict_price(housePrice: HousePriceSchema):
    try:
        data = housePrice.model_dump()
        print("Data from model_dump:", data)  # Debug print
        df = pd.DataFrame(data, index=[0])
        df = df.reindex(columns=columns, fill_value=0)
        print("DataFrame:\n", df.head())  # Debug print
        
        predictions = mlmodel.predict(df)
        response = {'predictions': predictions.tolist()}  # Ensure the predictions are serializable
        print("Predictions:", response)  # Debug print
        return response
    
    except Exception as e:
        print(f"Error occurred: {e}")
        return {"error": str(e)}


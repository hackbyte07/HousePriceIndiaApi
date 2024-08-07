import joblib
import os

dirname = os.path.dirname(__file__)
file = os.path.join(dirname, './house_data_model.pkl')

file_two = os.path.join(dirname, './house_data_columns.pkl')

mlmodel = joblib.load(open(file, 'rb'))
columns = joblib.load(open(file_two, 'rb'))
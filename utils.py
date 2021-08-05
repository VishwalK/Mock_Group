import pickle
import json
import numpy as np

with open('./artifacts/home_pricePred_LR.pickle', 'rb') as f:
    __model = pickle.load(f)

with open('./artifacts/columns.json','r') as f1:
    __col = json.load(f1)['cols']

def prediction_price(size, total_sqft, bath, location):
    x_test2 = np.zeros(len(__col))
    x_test2[0] = size
    x_test2[1] = total_sqft
    x_test2[2] = bath

    # location = "location_ " + location
    loc_index = __col.index(location)
    x_test2[loc_index] = 1

    return __model.predict([x_test2])[0]   

def get_all_location():
    locations = __col[3:]
    return locations
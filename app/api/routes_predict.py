from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.core.dependencies import get_api_key,get_current_user
from app.services.model_service import predict_car_price


router = APIRouter()


class CarFeatures(BaseModel) :
    owner : str
    fuel :str
    seller_type : str
    transmission : str
    km_driven : str
    mileage_mpg : str
    engine_cc : str
    max_power_bhp : str
    torque_nm : str
    seats : float



@router.post('/predict')
def predict_price(car: CarFeatures, user=Depends(get_current_user),
                   _=Depends(get_api_key)) :
    prediction = predict_car_price(car.model_dump())
    return {'predicted_price' : f'{prediction:,.2f}'}
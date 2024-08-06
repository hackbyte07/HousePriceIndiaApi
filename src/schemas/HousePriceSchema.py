from pydantic import BaseModel


class HousePriceSchema(BaseModel):
    num_of_bedroom: int
    no_of_bathroom: int
    living_area: int
    lot_area: int
    no_of_floors: int
    waterfront_prsent: int
    no_of_views: int
    house_condition: int
    house_grade: int
    house_area_exclude_basement: int
    area_of_basement: int
    built_year: int
    renovation_area: int
    postal_code: int
    lattitude: int
    longitude: int
    living_area_renov: int
    lot_area_renov: int
    num_schools_nearby: int
    distance_area_from_airport: int
    
    
""" 'No of bedrooms', 'No of bathrooms', 'living area', 'lot area',
       'No of floors', 'waterfront present', 'No of views', 'house condition',
       'house grade', 'house area(excluding basement)', 'Area of the basement',
       'Built Year', 'Renovation Year', 'Postal Code', 'Lattitude',
       'Longitude', 'living_area_renov', 'lot_area_renov',
       'No of schools nearby', 'Distance from the airport', 'Price'"""
    
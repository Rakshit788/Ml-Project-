import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging
import os

@dataclass
class DataTransformationConfig: 
    preprocessor_file_path =  os.path.join('artifacts' ,  'preprocessor.pkl') 

class DataTransformation:
    def __init__(self):
        self.data_transformation_config  =  DataTransformationConfig()
    
    def gettransformation_obj(self):

        try: 
            
            categorical_cols = ['cut', 'color','clarity']
            numerical_cols = ['carat', 'depth','table', 'x', 'y', 'z']
            
            # Define the custom ranking for each ordinal variable
            cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']

        except Exception as e: 
             logging.info('Exception occured in initiate_data_transformation function')
             raise CustomException(e,sys)   

    


        
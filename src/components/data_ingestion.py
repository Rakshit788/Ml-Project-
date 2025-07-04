import os 
import sys
from src.exception import  CustomException
from src.logger import  logging
from dataclasses  import  dataclass
from sklearn.model_selection import  train_test_split
import  pandas as pd 



@dataclass

class DataIngestionConfig:
    train_data_path : str =  os.path.join('artifacts','train.csv')
    test_data_path : str =  os.path.join('artifacts','test.csv')
    raw_data_csv : str =  os.path.join('artifacts' ,  'data.csv')



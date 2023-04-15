import os
import sys

import numpy as np 
import pandas as pd
import dill
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException
from src.logger import logging
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_model(X_train,y_train,X_test,y_test,models,param):
    


    try:
        report={}

        for i in range(len(list(models))):
            model=list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)
            y_train_pred=model.predict(X_train)
            y_test_pred=model.predict(X_test)

            acc_score_train= accuracy_score(y_train,y_train_pred)
            acc_score_test= accuracy_score(y_test,y_test_pred)

            class_report= classification_report(y_test,y_test_pred)

            report[list(models.keys())[i]] = acc_score_test
        
        return report
    except Exception as e:
        raise CustomException(e,sys)
    
def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e,sys)
        

















    except:
        pass
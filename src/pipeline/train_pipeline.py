
from src.components.data_transformation import DataTransform
from src.components.model_trainer import ModelTrainer
from src.components.data_ingestion import DataIngestion


if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_trans=DataTransform()
    train_arr,test_arr,_=data_trans.initiate_data_transformer(train_data,test_data)

    modeltrainer= ModelTrainer()
    print(modeltrainer.initate_training(train_arr,test_arr))
    
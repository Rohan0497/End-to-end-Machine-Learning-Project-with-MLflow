from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen= True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen= True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE :str
    unzip_data_dir :Path
    all_schema: dict 



@dataclass(frozen= True)
class DataTransformationConfig:
    root_dir: Path    
    data_path: Path

@dataclass(frozen= True)
class ModelTrainerConfig:
    root_dir: Path    
    train_data_path :Path
    test_data_path :Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column : str

import os
os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/Rohan0497/End-to-end-Machine-Learning-Project-with-MLflow.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="Rohan0497" 
os.environ["MLFLOW_TRACKING_PASSWORD"]="b4ddf25ffbb97feda70db5309e2559c251860a4f"

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str
    mlflow_uri: str
    

# Imports
from sklearn.linear_model import LinearRegression
from pathlib import Path
import pandas as pd
import joblib
import json


def store_list_as_json(data_list, folder_path, file_name):
    json_data = json.dumps(data_list)
    file_path = folder_path + "/" + file_name
    
    # "w" - Write - Opens a file for writing, creates the file if it does not exist
    with open(file_path, "w") as json_file:
        json_file.write(json_data)
        
        
def read_json_file(file_path):
    with open(file_path, "r") as json_file:
        json_data = json_file.read()
    data_list = json.loads(json_data)
    return data_list


def train(
    X_train: pd.DataFrame = None,
    y_train: pd.DataFrame = None,
    model_directory_path: str = "resources",
) -> None:
    """
    At each retrain this function will have to save an updated version of
    the model under the model_directiory_path.
    Note: You can use other serialization methods than joblib.dump(), as
    long as it matches what reads the model in infer().

    Args:
        X_train, y_train: the data to train the model.
        model_directory_path: the path to save your updated model.

    Returns:
        None
    """
    # Load the selected features
    features = read_json_file(file_path=model_directory_path  + "/features.json")
    
    # Train the model
    model = LinearRegression()
    print("training...")
    model.fit(X_train.loc[:, features], y_train.iloc[:, 2:])

    # Make sure that the train function correctly save the trained model in the model_directory_path
    model_pathname = Path(model_directory_path) / "model.joblib"
    print(f"Saving model in {model_pathname}")
    joblib.dump(model, model_pathname)


def infer(
    X_test: pd.DataFrame = None,
    model_directory_path: str = "resources",
) -> pd.DataFrame:
    """
    This function will load the model saved at the previous iteration and use
    it to produce your inference on the current date.
    It is mandatory to send the inferences with the ids so the system
    can match it correctly.

    Args:
        model_directory_path: the path to the directory to the directory in which we will be saving your updated model.
        X_test: the independant  variables of the current date passed to your model.

    Returns:
        A dataframe (date, id, value) with the inferences of your model for the current date.
    """

    # Load the model saved by the train function at previous iteration
    model = joblib.load(Path(model_directory_path) / "model.joblib")

    # Create the predicted label dataframe with correct dates and ids
    y_test_predicted = X_test[["date", "id"]].copy()
    
    # Load the selected features
    features = read_json_file(file_path=model_directory_path  + "/features.json")
    y_test_predicted["value"] = model.predict(X_test.loc[:, features])

    return y_test_predicted

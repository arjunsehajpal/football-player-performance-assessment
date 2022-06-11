import json
import os


class Data:
    ROOT_DIR = os.getcwd()
    TRAIN_DATA_PATH = os.path.join(ROOT_DIR, "data", "train.csv")
    TEST_DATA_PATH = os.path.join(ROOT_DIR, "data", "test.csv")
    SAMPLE_SUB_PATH = os.path.join(ROOT_DIR, "data", "sample_submission.csv")
    SUB_PATH = os.path.join(ROOT_DIR, "data", "submission_01.csv")


class FeatureEngineering:
    categorical_columns = ["winner", "team"]

    # load magic features file
    with open(os.path.join(Data.ROOT_DIR, "config", "magic_features.json")) as json_file:
        feature_dict = json.load(json_file)

    magic_features = [
        {
            "groupby_col": ["player_position_2"],
            "feature_dict": feature_dict,
            "feature_family_identifier": "_player_position_2",
        }
    ]


class Model:
    remove_columns = ["row_id"]

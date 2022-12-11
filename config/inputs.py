import os

import yaml


class Data:
    ROOT_DIR = os.getcwd()
    TRAIN_DATA_PATH = os.path.join(ROOT_DIR, "data", "train.csv")
    TEST_DATA_PATH = os.path.join(ROOT_DIR, "data", "test.csv")
    SAMPLE_SUB_PATH = os.path.join(ROOT_DIR, "data", "sample_submission.csv")
    SUB_PATH = os.path.join(ROOT_DIR, "data", "submission_01.csv")


class FeatureEngineering:
    categorical_columns = ["winner", "team"]
    magic_features_path = os.path.join(Data.ROOT_DIR, "config", "magic_features.yaml")
    # magic_features = [
    #     {
    #         "groupby_col": ["player_position_2"],
    #         "feature_dict": feature_dict,
    #         "feature_family_identifier": "_player_position_2",
    #     }
    # ]


class Model:
    remove_columns = ["row_id"]
    target_column = []

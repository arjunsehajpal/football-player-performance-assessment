import os
import pandas as pd
from xgboost import train

from config.configurations import Data, FeatureEngineering, Model
from src import feature_engineering as FE
from src.model import xgb_regressor


def get_data():
    train_df = pd.read_csv(Data.TRAIN_DATA_PATH)
    test_df = pd.read_csv(Data.TEST_DATA_PATH)
    sub_df = pd.read_csv(Data.SAMPLE_SUB_PATH)
    print("Train data = {}".format(train_df.shape))
    print("Test data = {}".format(test_df.shape))
    return train_df, test_df, sub_df


def create_features(train_df, test_df):
    # encode categorical columns
    for i in FeatureEngineering.categorical_columns:
        train_df, test_df = FE.label_encoder(train_df, test_df, i)

    # create magic_features
    for magic_feature_dict in FeatureEngineering.magic_features:
        train_df, test_df = FE.create_magic_features(train_df, test_df, magic_feature_dict)

    # Drop columns that are not required
    train_df = train_df.drop(columns=Model.remove_columns)
    test_df = test_df.drop(columns=Model.remove_columns)
    print("Train data = {}".format(train_df.shape))
    print("Test data = {}".format(test_df.shape))

    return train_df, test_df


def run():
    train_df, test_df, sub_df = get_data()
    train_df, test_df = create_features(train_df, test_df)

    train_df.to_csv(os.path.join(Data.ROOT_DIR, "data", "train_with_magic_features.csv"), index=False)
    test_df.to_csv(os.path.join(Data.ROOT_DIR, "data", "test_with_magic_features.csv"), index=False)

    # sub_df = xgb_regressor(train_df, test_df, sub_df)
    # sub_df.to_csv(Data.SUB_PATH, index=False)


if __name__ == "__main__":
    run()

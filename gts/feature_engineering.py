import os

import numpy as np
import pandas as pd


def label_encoder(train_df, test_df, col_name):
    print("Encoding {}".format(col_name))
    encoder_dict = {}
    for i, element in enumerate(train_df[col_name].unique()):
        encoder_dict[element] = i

    # fit on train and test
    train_df[col_name] = train_df[col_name].map(encoder_dict)
    test_df[col_name] = test_df[col_name].map(encoder_dict)

    # fill Nulls with 999
    train_df[col_name] = train_df[col_name].fillna(999)
    test_df[col_name] = test_df[col_name].fillna(999)

    return train_df, test_df


def create_magic_features(train_df, test_df, magic_feature_dict):
    # extract elements
    groupby_col = magic_feature_dict["groupby_col"]
    feature_dict = magic_feature_dict["feature_dict"]
    feature_family_identifier = magic_feature_dict["feature_family_identifier"]

    print("Creating Magic Feature for {}".format(feature_family_identifier[1:]))

    stat_summary_df = train_df.groupby(groupby_col).agg(feature_dict)
    stat_summary_df.columns = ["_".join(i) + feature_family_identifier for i in stat_summary_df.columns]
    stat_summary_df = stat_summary_df.reset_index()
    train_df = train_df.merge(stat_summary_df, on=groupby_col, how="left")
    test_df = test_df.merge(stat_summary_df, on=groupby_col, how="left")

    return train_df, test_df

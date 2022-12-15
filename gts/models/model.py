import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split


def xgb_train_and_predict(train_df, test_df, sub_df, target_col, param=None, num_round=100, early_stopping_rounds=10):
    if param is None:
        param = {"max_depth": 2, "eta": 1, "objective": "reg:squarederror", "nthread": 4}

    label = train_df[target_col]
    train_df = train_df.drop(columns=[target_col])
    x_train, x_eval, y_train, y_eval = train_test_split(train_df, label, test_size=0.2, random_state=42)

    dtrain = xgb.DMatrix(x_train, label=y_train)
    deval = xgb.DMatrix(x_eval, label=y_eval)
    dtest = xgb.DMatrix(test_df)
    evallist = [(deval, "eval"), (dtrain, "train")]

    model = xgb.train(param, dtrain, num_round, evallist, early_stopping_rounds=early_stopping_rounds)

    # prediction
    predictions = model.predict(dtest)

    # create submission file
    sub_df[target_col] = predictions

    return sub_df

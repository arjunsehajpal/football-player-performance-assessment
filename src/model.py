import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split


def xgb_regressor(train_df, test_df, sub_df):
    label = train_df["rating_num"]
    train_df = train_df.drop(columns=["rating_num"])
    x_train, x_eval, y_train, y_eval = train_test_split(train_df, label, test_size=0.2, random_state=42)

    dtrain = xgb.DMatrix(x_train, label=y_train)
    deval = xgb.DMatrix(x_eval, label=y_eval)
    dtest = xgb.DMatrix(test_df)
    evallist = [(deval, "eval"), (dtrain, "train")]
    param = {"max_depth": 2, "eta": 1, "objective": "reg:squarederror", "nthread": 4}
    num_round = 100
    model = xgb.train(param, dtrain, num_round, evallist, early_stopping_rounds=10)

    # prediction
    predictions = model.predict(dtest)

    # create submission file
    sub_df["rating_num"] = predictions

    return sub_df

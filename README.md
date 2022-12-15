# GTS

GTS is a simple python module, built specifically for the building quick models for Kaggle Competitions. The vision is to built a library that like a lego, pieces together various components usually required for making quick submissions.


## Example Pipeline
`engineer_features >> select_features >> [train_xgb, train_lgb] >> ensemble >> make_submission`
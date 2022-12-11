class FeatureSelection(object):
    def __init__(self, model, folds, metric):
        self.model = model
        self.folds = folds
        self.metric = metric

    def fit(self, x_train, y_train, testset):
        cv_predictions, predictions, importance = self.get_oof(
            self.model,
            x_train,
            y_train,
            testset,
            self.folds,
            self.metric,
            permute_flag=True
        )

    def get_oof()
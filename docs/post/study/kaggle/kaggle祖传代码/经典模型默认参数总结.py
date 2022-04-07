# lgbm
import lightgbm
params = dict(n_estimators=3000,
              metric=["auc"],
              max_depth=9,
              num_leaves=80,
              min_data_in_leaf=20,
              learning_rate=0.05,
              min_sum_hessian_in_leaf=0.002,
              colsample_bytree=0.8,
              subsample=0.9,
              reg_alpha=0.0,
              reg_lambda=0.0)
lgbm = lightgbm.LGBMClassifier(**params)
lgbm.fit(train_x, train_y, eval_set=[(train_x, train_y), (test_x, test_y)], early_stopping_rounds=50, verbose=10)
## early_stopping_rounds 可以帮助进行早停。
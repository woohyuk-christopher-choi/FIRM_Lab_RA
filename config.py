import numpy as np




dlns_params = {
    'data_start': '2000-01-01',
    'pred_start': '2015-01-31',
    'pred_end': '2022-12-31',
    'resample': '1M',
    'time_horizon': 12,
    'data': './../Data/US_bond_drop.csv',
    'dt': 1,
    'lambdas': 0.036,
    'maturity': np.array([3 / 12, 6 / 12, 2, 5., 10., 30.]) * 12,
    'window_size': 120,
    'valid_size': 1,
    'valid': True,
    'past_data_size' : 12

}

dlns_macro_params0 = {
    'data_start': '2000-01-01',
    'pred_start': '2015-01-31',
    'pred_end': '2022-12-31',
    'resample': '1M',
    'time_horizon': 12,
    'data': './../Data/US_bond_drop.csv',
    'macro_data': './../Data/US_Macro_total.csv',
    'macro_feature_list': ['CPI YOY Index'],
    'pct_change_feature_list': [],
    'pct_change_length': 1,
    'dt': 1,
    'lambdas': 0.05,
    'maturity': np.array([3 / 12, 6 / 12, 2, 5., 10., 30.]) * 12,
    'window_size': 120,
    'valid_size': 1,
    'valid': True,
    'past_data_size' : 12

}

#'macro_feature_list': ['MPMIUSMA Index','MPMIUSSA Index','RSTATOTL Index','CPI YOY Index','CPI CHNG Index','USURTOT Index','SPX INDEX','DXY Curncy','M2 Index','M2% YOY Index']

dlns_macro_params1 = {
    'data_start': '2000-01-01',
    'pred_start': '2015-01-31',
    'pred_end': '2022-12-31',
    'resample': '1M',
    'time_horizon': 12,
    'data': './../Data/US_bond_drop.csv',
    'macro_data': './../Data/US_Macro_total.csv',
    'macro_feature_list': ['CPI YOY Index','USURTOT Index'],
    'pct_change_feature_list': [],
    'pct_change_length': 12,
    'dt': 1,
    'lambdas': 0.05,
    'maturity': np.array([3 / 12, 6 / 12, 2, 5., 10., 30.]) * 12,
    'window_size': 120,
    'valid_size': 1,
    'valid': True,
    'past_data_size' : 12

}

dlns_macro_params2 = {
    'data_start': '2000-01-01',
    'pred_start': '2015-01-31',
    'pred_end': '2022-12-31',
    'resample': '1M',
    'time_horizon': 12,
    'data': './../Data/US_bond_drop.csv',
    'macro_data': './../Data/US_Macro_total.csv',
    'macro_feature_list': ['CPI YOY Index','SPX INDEX'],
    'pct_change_feature_list': ['SPX INDEX'],
    'pct_change_length': 12,
    'dt': 1,
    'lambdas': 0.05,
    'maturity': np.array([3 / 12, 6 / 12, 2, 5., 10., 30.]) * 12,
    'window_size': 120,
    'valid_size': 1,
    'valid': True,
    'past_data_size' : 12

}

dlns_macro_params3 = {
    'data_start': '2000-01-01',
    'pred_start': '2015-01-31',
    'pred_end': '2022-12-31',
    'resample': '1M',
    'time_horizon': 12,
    'data': './../Data/US_bond_drop.csv',
    'macro_data': './../Data/US_Macro_total.csv',
    'macro_feature_list': ['CPI YOY Index','DXY Curncy'],
    'pct_change_feature_list': [],
    'pct_change_length': 12,
    'dt': 1,
    'lambdas': 0.05,
    'maturity': np.array([3 / 12, 6 / 12, 2, 5., 10., 30.]) * 12,
    'window_size': 120,
    'valid_size': 1,
    'valid': True,
    'past_data_size' : 12

}

dlns_macro_params4 = {
    'data_start': '2000-01-01',
    'pred_start': '2015-01-31',
    'pred_end': '2022-12-31',
    'resample': '1M',
    'time_horizon': 12,
    'data': './../Data/US_bond_drop.csv',
    'macro_data': './../Data/US_Macro_total.csv',
    'macro_feature_list': ['CPI YOY Index','M2 Index'],
    'pct_change_feature_list': [],
    'pct_change_length': 12,
    'dt': 1,
    'lambdas': 0.05,
    'maturity': np.array([3 / 12, 6 / 12, 2, 5., 10., 30.]) * 12,
    'window_size': 120,
    'valid_size': 1,
    'valid': True,
    'past_data_size' : 12

}

dlns_macro_params5 = {
    'data_start': '2000-01-01',
    'pred_start': '2015-01-31',
    'pred_end': '2022-12-31',
    'resample': '1M',
    'time_horizon': 12,
    'data': './../Data/US_bond_drop.csv',
    'macro_data': './../Data/US_Macro_total.csv',
    'macro_feature_list': ['CPI YOY Index','M2% YOY Index'],
    'pct_change_feature_list': [],
    'pct_change_length': 12,
    'dt': 1,
    'lambdas': 0.05,
    'maturity': np.array([3 / 12, 6 / 12, 2, 5., 10., 30.]) * 12,
    'window_size': 120,
    'valid_size': 1,
    'valid': True,
    'past_data_size' : 12

}

dlns_macro_params6 = {
    'data_start': '2000-01-01',
    'pred_start': '2015-01-31',
    'pred_end': '2022-12-31',
    'resample': '1M',
    'time_horizon': 12,
    'data': './../Data/US_bond_drop.csv',
    'macro_data': './../Data/US_Macro_total.csv',
    'macro_feature_list': ['CPI YOY Index','USURTOT Index','SPX INDEX'],
    'pct_change_feature_list': ['SPX INDEX'],
    'pct_change_length': 12,
    'dt': 1,
    'lambdas': 0.05,
    'maturity': np.array([3 / 12, 6 / 12, 2, 5., 10., 30.]) * 12,
    'window_size': 120,
    'valid_size': 1,
    'valid': True,
    'past_data_size' : 12

}

dlns_macro_params7 = {
    'data_start': '2000-01-01',
    'pred_start': '2015-01-31',
    'pred_end': '2022-12-31',
    'resample': '1M',
    'time_horizon': 12,
    'data': './../Data/US_bond_drop.csv',
    'macro_data': './../Data/US_Macro_total.csv',
    'macro_feature_list': ['CPI YOY Index','USURTOT Index','SPX INDEX','DXY Curncy'],
    'pct_change_feature_list': ['SPX INDEX'],
    'pct_change_length': 12,
    'dt': 1,
    'lambdas': 0.05,
    'maturity': np.array([3 / 12, 6 / 12, 2, 5., 10., 30.]) * 12,
    'window_size': 120,
    'valid_size': 1,
    'valid': True,
    'past_data_size' : 12

}

dlns_macro_params8 = {
    'data_start': '2000-01-01',
    'pred_start': '2015-01-31',
    'pred_end': '2022-12-31',
    'resample': '1M',
    'time_horizon': 12,
    'data': './../Data/US_bond_drop.csv',
    'macro_data': './../Data/US_Macro_total.csv',
    'macro_feature_list': ['CPI YOY Index','USURTOT Index','SPX INDEX','DXY Curncy','M2% YOY Index'],
    'pct_change_feature_list': ['SPX INDEX'],
    'pct_change_length': 12,
    'dt': 1,
    'lambdas': 0.05,
    'maturity': np.array([3 / 12, 6 / 12, 2, 5., 10., 30.]) * 12,
    'window_size': 120,
    'valid_size': 1,
    'valid': True,
    'past_data_size' : 12

}

dlns_macro_params9 = {
    'data_start': '2000-01-01',
    'pred_start': '2015-01-31',
    'pred_end': '2022-12-31',
    'resample': '1M',
    'time_horizon': 12,
    'data': './../Data/US_bond_drop.csv',
    'macro_data': './../Data/US_Macro_total.csv',
    'macro_feature_list': ['CPI YOY Index','USURTOT Index','SPX INDEX','M2% YOY Index'],
    'pct_change_feature_list': ['SPX INDEX'],
    'pct_change_length': 12,
    'dt': 1,
    'lambdas': 0.05,
    'maturity': np.array([3 / 12, 6 / 12, 2, 5., 10., 30.]) * 12,
    'window_size': 120,
    'valid_size': 1,
    'valid': True,
    'past_data_size' : 12

}

dlns_macro_params10 = {
    'data_start': '2000-01-01',
    'pred_start': '2015-01-31',
    'pred_end': '2022-12-31',
    'resample': '1M',
    'time_horizon': 12,
    'data': './../Data/US_bond_drop.csv',
    'macro_data': './../Data/US_Macro_total.csv',
    'macro_feature_list': ['CPI YOY Index','USURTOT Index','DXY Curncy','M2% YOY Index'],
    'pct_change_feature_list': [],
    'pct_change_length': 12,
    'dt': 1,
    'lambdas': 0.05,
    'maturity': np.array([3 / 12, 6 / 12, 2, 5., 10., 30.]) * 12,
    'window_size': 120,
    'valid_size': 1,
    'valid': True,
    'past_data_size' : 12

}

dlns_macro_params11 = {
    'data_start': '2000-01-01',
    'pred_start': '2015-01-31',
    'pred_end': '2022-12-31',
    'resample': '1M',
    'time_horizon': 12,
    'data': './../Data/US_bond_drop.csv',
    'macro_data': './../Data/US_Macro_total.csv',
    'macro_feature_list': ['CPI YOY Index','USURTOT Index','SPX INDEX','DXY Curncy','M2 Index','M2% YOY Index'],
    'pct_change_feature_list': ['SPX INDEX'],
    'pct_change_length': 1,
    'dt': 1,
    'lambdas': 0.05,
    'maturity': np.array([3 / 12, 6 / 12, 2, 5., 10., 30.]) * 12,
    'window_size': 120,
    'valid_size': 1,
    'valid': True,
    'past_data_size' : 12

}

dlns_macro_params12 = {
    'data_start': '2000-01-01',
    'pred_start': '2015-01-31',
    'pred_end': '2022-12-31',
    'resample': '1M',
    'time_horizon': 12,
    'data': './../Data/US_bond_drop.csv',
    'macro_data': './../Data/US_Macro_total.csv',
    'macro_feature_list': ['SPX INDEX'],
    'pct_change_feature_list': ['SPX INDEX'],
    'pct_change_length': 1,
    'dt': 1,
    'lambdas': 0.05,
    'maturity': np.array([3 / 12, 6 / 12, 2, 5., 10., 30.]) * 12,
    'window_size': 120,
    'valid_size': 1,
    'valid': True,
    'past_data_size' : 12

}

dlns_macro_params13 = {
    'data_start': '2000-01-01',
    'pred_start': '2015-01-31',
    'pred_end': '2022-12-31',
    'resample': '1M',
    'time_horizon': 12,
    'data': './../Data/US_bond_drop.csv',
    'macro_data': './../Data/US_Macro_total.csv',
    'macro_feature_list': ['CPI YOY Index','USURTOT Index','SPX INDEX','DXY Curncy','M2 Index'],
    'pct_change_feature_list': ['SPX INDEX','M2 Index'],
    'pct_change_length': 1,
    'dt': 1,
    'lambdas': 0.05,
    'maturity': np.array([3 / 12, 6 / 12, 2, 5., 10., 30.]) * 12,
    'window_size': 120,
    'valid_size': 1,
    'valid': True,
    'past_data_size' : 12

}


dlns_macro_params14 = {
    'data_start': '2000-01-01',
    'pred_start': '2015-01-31',
    'pred_end': '2022-12-31',
    'resample': '1M',
    'time_horizon': 12,
    'data': './../Data/US_bond_drop.csv',
    'macro_data': './../Data/US_Macro_total.csv',
    'macro_feature_list': ['CPI YOY Index','USURTOT Index','SPX INDEX','DXY Curncy','M2 Index','M2% YOY Index'],
    'pct_change_feature_list': ['SPX INDEX','M2 Index'],
    'pct_change_length': 1,
    'dt': 1,
    'lambdas': 0.05,
    'maturity': np.array([3 / 12, 6 / 12, 2, 5., 10., 30.]) * 12,
    'window_size': 120,
    'valid_size': 1,
    'valid': True,
    'past_data_size' : 12

}

dlns_macro_params_list = [dlns_macro_params0]
'''

'macro_feature_list': ['MPMIUSMA Index','MPMIUSSA Index','RSTATOTL Index','CPI YOY Index','CPI CHNG Index','USURTOT Index','SPX INDEX','DXY Curncy','M2 Index','M2% YOY Index'],


test_params = {
    'train_start': '2000-01-01',
    'test_start': '2019-01-01',
    'test_end': '2022-01-31',
    'valid_start': '2017-01-01',
    'resample': '1M',
    'time_horizon': 12,
    'min_train_size': 120, #10년치는 가지고 시작
    'data': './../Data/US_bond_drop.csv',
    'dt': 1,
    'lambdas': 0.038,
    'maturity': np.array([3 / 12, 6 / 12, 2, 5., 10., 30.]) * 12,

}
'''

# 논문
# dl_hyperparams = {
#     'epochs': 5000,
#     'batch_size': 100,
#     'learning_rate': 0.02,
#     'early_stop': 100,
#     'repeat_num': 20,
#     'hidden_size': 100,
#     'dropout_prob': 0,
#     'output_size': 3, # fixed lambda
#     'num_layers': 1,
#     'num_maturity': test_params['maturity'].shape[0],
# }
# test
dl_hyperparams = {
    'epochs': 5000,
    'batch_size': 100,
    'learning_rate': 0.01,
    'early_stopping_patience': 100,
    'repeat_num': 10,
    'hidden_size': 100,
    'dropout_prob': 0,
    'output_size': 3, # fixed lambda
    'num_layers': 1,
    'num_maturity': dlns_params['maturity'].shape[0],
    #'num_macro_feature': len(dlns_macro_params['macro_feature_list']),
    'maturity': dlns_params['maturity'],
    'lambdas': dlns_params['lambdas'],
}



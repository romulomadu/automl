import numpy as np

from sklearn.metrics import make_scorer, mean_squared_error, r2_score
from scipy.stats import uniform as sp_uniform
from skopt.space import Real


def nmse(y_true, y_pred, verbose=0):
	"""	Normalized mean squared error."""
	error = 1 - r2_score(y_true, y_pred)
	if verbose:
		print('NMSE: {:}'.format(error))
	return error


def grid_params():
	"""Grid Search parameters."""
	gamma = [2 ** i for i in range(-15, 4, 1)]
	C = [2 ** i for i in range(-5, 16, 1)]
	epsilon = [2 ** i for i in range(-8, 0, 1)]

	param_grid = {
		'param_grid': {'kernel': ['rbf'], 'C': C, 'gamma': gamma, 'epsilon': epsilon},
		#'scoring': make_scorer(nmse, greater_is_better=False),
		'scoring': 'neg_mean_squared_error',
		'verbose': 1,
		'cv': 10
	}

	return param_grid


def random_params():
	"""Random Search parameters."""
	gamma = sp_uniform(2 ** -15, 2 ** 3)
	C = sp_uniform(2 ** -5, 2 ** 15)
	epsilon = sp_uniform(2 ** -8, 2 ** -1)

	param_dist = {
		'param_distributions': {'kernel': ['rbf'], 'C': C, 'gamma': gamma, 'epsilon': epsilon},
		#'scoring': make_scorer(nmse, greater_is_better=False),
		'scoring': 'neg_mean_squared_error',
		'verbose': 0,
		'n_iter': 1000,
		'cv': 10
	}

	return param_dist


def bayes_params():
	"""Random Search parameters."""
	gamma = Real(2 ** -15, 2 ** 3, prior='log-uniform')
	C = Real(2 ** -5, 2 ** 15, prior='log-uniform')
	epsilon = Real(2 ** -8, 2 ** -1, prior='log-uniform')

	search_spaces = {
		'search_spaces': {'kernel': ['rbf'], 'C': C, 'gamma': gamma, 'epsilon': epsilon},
		#'scoring': make_scorer(nmse, greater_is_better=False),
		'scoring': 'neg_mean_squared_error',
		'verbose': 0,
		'n_iter': 100,
		'cv': 10
	}

	return search_spaces



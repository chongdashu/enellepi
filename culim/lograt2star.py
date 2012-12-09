def log_ratio_2_star_rating(log_ratio):
	if log_ratio < -3.0:
		return 1.0
	elif log_ratio < -0.75:
		return 2.0
	elif log_ratio < -0.25 or log_ratio == 0.0:
		return 3.0
	elif log_ratio < 2.0:
		return 4.0
	else:
		return 5.0
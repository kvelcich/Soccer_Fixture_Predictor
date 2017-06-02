from table import *

def extract_data_home(data, team, row, game_ID):
	team_data = data[team]
	length = len(team_data)
	if row[FT_RESULT].value == 'H':
		form = 3
	elif row[FT_RESULT].value == 'D':
		form = 1
	else:
		form = 0

	sample = []

	sample.append(team)
	sample.extend(fill(team_data, row[FT_GOALS_HOME].value, L1_GOALS, L5_GOALS, L10_GOALS, SEASON_GOALS))
	sample.extend(fill(team_data, row[HT_GOALS_HOME].value, L1_GOALS_HT, L5_GOALS_HT, L10_GOALS_HT, SEASON_GOALS_HT))
	sample.extend(fill(team_data, row[SHOTS_TARGET_HOME].value, L1_SHOTS_ON, L5_SHOTS_ON, L10_SHOTS_ON, SEASON_SHOTS_ON))
	sample.extend(fill(team_data, (row[SHOTS_HOME].value - row[SHOTS_TARGET_HOME].value), L1_SHOTS_OFF, L5_SHOTS_OFF, L10_SHOTS_OFF, SEASON_SHOTS_OFF))
	sample.extend(fill(team_data, row[CORNERS_HOME].value, L1_CORNERS, L5_CORNERS, L10_CORNERS, SEASON_CORNERS))
	sample.extend(fill(team_data, row[FOULS_HOME].value, L1_FOULS, L5_FOULS, L10_FOULS, SEASON_FOULS))
	sample.extend(fill(team_data, row[YELLOWS_HOME].value, L1_YELLOWS, L5_YELLOWS, L10_YELLOWS, SEASON_YELLOWS))
	sample.extend(fill(team_data, row[REDS_HOME].value, L1_REDS, L5_REDS, L10_REDS, SEASON_REDS))
	sample.extend(fill(team_data, row[FT_GOALS_AWAY].value, L1_GOALS_AGAINST, L5_GOALS_AGAINST, L10_GOALS_AGAINST, SEASON_GOALS_AGAINST))
	sample.extend(fill(team_data, row[HT_GOALS_AWAY].value, L1_GOALS_HT_AGAINST, L5_GOALS_HT_AGAINST, L10_GOALS_HT_AGAINST, SEASON_GOALS_HT_AGAINST))
	sample.extend(fill(team_data, row[SHOTS_TARGET_AWAY].value, L1_SHOTS_ON_AGAINST, L5_SHOTS_ON_AGAINST, L10_SHOTS_ON_AGAINST, SEASON_SHOTS_ON_AGAINST))
	sample.extend(fill(team_data, (row[SHOTS_AWAY].value - row[SHOTS_TARGET_AWAY].value), L1_SHOTS_OFF_AGAINST, L5_SHOTS_OFF_AGAINST, L10_SHOTS_OFF_AGAINST, SEASON_SHOTS_OFF_AGAINST))
	sample.extend(fill(team_data, row[CORNERS_AWAY].value, L1_CORNERS_AGAINST, L5_CORNERS_AGAINST, L10_CORNERS_AGAINST, SEASON_CORNERS_AGAINST))
	sample.extend(fill(team_data, row[FOULS_AWAY].value, L1_FOULS_AGAINST, L5_FOULS_AGAINST, L10_FOULS_AGAINST, SEASON_FOULS_AGAINST))
	sample.extend(fill(team_data, row[YELLOWS_AWAY].value, L1_YELLOWS_AGAINST, L5_YELLOWS_AGAINST, L10_YELLOWS_AGAINST, SEASON_YELLOWS_AGAINST))
	sample.extend(fill(team_data, row[REDS_AWAY].value, L1_REDS_AGAINST, L5_REDS_AGAINST, L10_REDS_AGAINST, SEASON_REDS_AGAINST))
	sample.extend(fill(team_data, form, L1_FORM, L5_FORM, L10_FORM, SEASON_FORM))
	sample.extend(fill_total(team_data, form))
	sample.extend(fill_percentage(team_data, form))
	sample.append(1)
	sample.append(game_ID)

	return sample

def extract_data_away(data, team, row, game_ID):
	team_data = data[team]
	length = len(team_data)
	if row[FT_RESULT].value == 'A':
		form = 3
	elif row[FT_RESULT].value == 'D':
		form = 1
	else:
		form = 0

	sample = []

	sample.append(team)
	sample.extend(fill(team_data, row[FT_GOALS_AWAY].value, L1_GOALS, L5_GOALS, L10_GOALS, SEASON_GOALS))
	sample.extend(fill(team_data, row[HT_GOALS_AWAY].value, L1_GOALS_HT, L5_GOALS_HT, L10_GOALS_HT, SEASON_GOALS_HT))
	sample.extend(fill(team_data, row[SHOTS_TARGET_AWAY].value, L1_SHOTS_ON, L5_SHOTS_ON, L10_SHOTS_ON, SEASON_SHOTS_ON))
	sample.extend(fill(team_data, (row[SHOTS_AWAY].value - row[SHOTS_TARGET_AWAY].value), L1_SHOTS_OFF, L5_SHOTS_OFF, L10_SHOTS_OFF, SEASON_SHOTS_OFF))
	sample.extend(fill(team_data, row[CORNERS_AWAY].value, L1_CORNERS, L5_CORNERS, L10_CORNERS, SEASON_CORNERS))
	sample.extend(fill(team_data, row[FOULS_AWAY].value, L1_FOULS, L5_FOULS, L10_FOULS, SEASON_FOULS))
	sample.extend(fill(team_data, row[YELLOWS_AWAY].value, L1_YELLOWS, L5_YELLOWS, L10_YELLOWS, SEASON_YELLOWS))
	sample.extend(fill(team_data, row[REDS_AWAY].value, L1_REDS, L5_REDS, L10_REDS, SEASON_REDS))
	sample.extend(fill(team_data, row[FT_GOALS_HOME].value, L1_GOALS_AGAINST, L5_GOALS_AGAINST, L10_GOALS_AGAINST, SEASON_GOALS_AGAINST))
	sample.extend(fill(team_data, row[HT_GOALS_HOME].value, L1_GOALS_HT_AGAINST, L5_GOALS_HT_AGAINST, L10_GOALS_HT_AGAINST, SEASON_GOALS_HT_AGAINST))
	sample.extend(fill(team_data, row[SHOTS_TARGET_HOME].value, L1_SHOTS_ON_AGAINST, L5_SHOTS_ON_AGAINST, L10_SHOTS_ON_AGAINST, SEASON_SHOTS_ON_AGAINST))
	sample.extend(fill(team_data, (row[SHOTS_HOME].value - row[SHOTS_TARGET_HOME].value), L1_SHOTS_OFF_AGAINST, L5_SHOTS_OFF_AGAINST, L10_SHOTS_OFF_AGAINST, SEASON_SHOTS_OFF_AGAINST))
	sample.extend(fill(team_data, row[CORNERS_HOME].value, L1_CORNERS_AGAINST, L5_CORNERS_AGAINST, L10_CORNERS_AGAINST, SEASON_CORNERS_AGAINST))
	sample.extend(fill(team_data, row[FOULS_HOME].value, L1_FOULS_AGAINST, L5_FOULS_AGAINST, L10_FOULS_AGAINST, SEASON_FOULS_AGAINST))
	sample.extend(fill(team_data, row[YELLOWS_HOME].value, L1_YELLOWS_AGAINST, L5_YELLOWS_AGAINST, L10_YELLOWS_AGAINST, SEASON_YELLOWS_AGAINST))
	sample.extend(fill(team_data, row[REDS_HOME].value, L1_REDS_AGAINST, L5_REDS_AGAINST, L10_REDS_AGAINST, SEASON_REDS_AGAINST))
	sample.extend(fill(team_data, form, L1_FORM, L5_FORM, L10_FORM, SEASON_FORM))
	sample.extend(fill_total(team_data, form))
	sample.extend(fill_percentage(team_data, form))
	sample.append(0)
	sample.append(game_ID)

	return sample

def fill(data, param, L1, L5_IDX, L10_IDX, TOTAL):
	entry = []

	entry.append(AVG(data, param, TOTAL))
	entry.append(param)
	entry.append(L5(data, param, TOTAL, L5_IDX, L1))
	entry.append(L10(data, param, TOTAL, L10_IDX, L1))
	entry.append(SEASON(data, param, TOTAL))

	return entry

def fill_total(data, form):
	entry = []

	entry.append(TOTAL_RESULT(data, form, TOTAL_WIN, 3))
	entry.append(TOTAL_RESULT(data, form, TOTAL_TIE, 1))
	entry.append(TOTAL_RESULT(data, form, TOTAL_LOSE, 0))

	return entry

def fill_percentage(data, form):
	entry = []

	entry.append(PERCENTAGE_RESULT(data, form, TOTAL_WIN, 3))
	entry.append(PERCENTAGE_RESULT(data, form, TOTAL_TIE, 1))
	entry.append(PERCENTAGE_RESULT(data, form, TOTAL_LOSE, 0))

	return entry

def AVG(data, param, TOTAL):
	length = len(data)

	if length == 0:
		return param
	else:
		return (data[length - 1][TOTAL] + param) / (length + 1)

def L5(data, param, TOTAL, L5, L1):
	length = len(data)

	if length == 0:
		return param
	elif length < 5:
		return data[length - 1][TOTAL] + param
	else:
		return data[length - 1][L5] - data[length - 5][L1] + param

def L10(data, param, TOTAL, L10, L1):
	length = len(data)

	if length == 0:
		return param
	elif length < 10:
		return data[length - 1][TOTAL] + param
	else:
		return data[length - 1][L10] - data[length - 10][L1] + param

def SEASON(data, param, TOTAL):
	length = len(data)

	if length == 0:
		return param
	else:
		return data[length - 1][TOTAL] + param

def TOTAL_RESULT(data, form, TOTAL, value):
	length = len(data)

	if length == 0:
		return int(form == value)
	else:
		return data[length - 1][TOTAL] + (form == value)

def PERCENTAGE_RESULT(data, form, TOTAL, value):
	length = len(data)

	if length == 0:
		return int(form == value)
	else:
		return (data[length - 1][TOTAL] + (form == value)) / (len(data) + 1.0)

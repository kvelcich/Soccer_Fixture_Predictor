import xlrd
from xlrd.sheet import ctype_text
from table import *

''' Variable list: '''
team_IDs = []
# HOME_ID, HOME_AVG_GOALS, HOME_L1_GOALS, HOME_L5_GOALS, HOME_L10_GOALS, HOME_SEASON_GOALS, ...
fixture_data = []

"""
Scraping Data.
"""
print 'Scraping Data...'

# Opening excel file
data = xlrd.open_workbook('all-euro-data-2016-2017.xls')
# Select sheet
sheet = data.sheet_by_index(0)

for idx, row_idx in enumerate(range(1, sheet.nrows)):
	row = sheet.row(row_idx)

	''' For every game, do the following... '''
	fixture_sample = []

	# Setting the home and away values
	if row[2].value not in team_IDs:
		team_IDs.append(row[2].value)
		fixture_data.append([])
	home = team_IDs.index(row[2].value)
	if row[3].value not in team_IDs:
		team_IDs.append(row[3].value)
		fixture_data.append([])
	away = team_IDs.index(row[3].value)

	# --- Filling fixture_sample values ---
	home_length = len(fixture_data[home])
	# HOME_ID,
	fixture_sample.append(home)

	# -- GOALS --
	goals_scored = row[FT_GOALS_HOME].value
	# HOME_AVG_GOALS,
	if home_length == 0:
		fixture_sample.append(goals_scored)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_GOALS]
		total = prev_total + goals_scored
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# HOME_L1_GOALS,
	fixture_sample.append(goals_scored)
	# HOME_L5_GOALS,
	if home_length == 0:
		fixture_sample.append(goals_scored)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_GOALS]
		entry = prev_total + goals_scored
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][HOME_L5_GOALS]
		l5_game = fixture_data[home][home_length - 5][HOME_L1_GOALS]
		entry = l5_total - l5_game + goals_scored
		fixture_sample.append(entry)
	# HOME_L10_GOALS,
	if home_length == 0:
		fixture_sample.append(goals_scored)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_GOALS]
		entry = prev_total + goals_scored
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][HOME_L10_GOALS]
		l10_game = fixture_data[home][home_length - 10][HOME_L1_GOALS]
		entry = l10_total - l10_game + goals_scored
		fixture_sample.append(entry)
	# HOME_SEASON_GOALS,
	if home_length == 0:
		fixture_sample.append(goals_scored)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_GOALS]
		entry = prev_total + goals_scored
		fixture_sample.append(entry)

	# -- SHOTS ON --
	shots_on = row[SHOTS_TARGET_HOME].value
	# HOME_AVG_SHOTS_ON,
	if home_length == 0:
		fixture_sample.append(shots_on)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_SHOTS_ON]
		total = prev_total + shots_on
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# HOME_L1_SHOTS_ON,
	fixture_sample.append(shots_on)
	# HOME_L5_SHOTS_ON,
	if home_length == 0:
		fixture_sample.append(shots_on)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_SHOTS_ON]
		entry = prev_total + shots_on
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][HOME_L5_SHOTS_ON]
		l5_game = fixture_data[home][home_length - 5][HOME_L1_SHOTS_ON]
		entry = l5_total - l5_game + shots_on
		fixture_sample.append(entry)
	# HOME_L10_SHOTS_ON,
	if home_length == 0:
		fixture_sample.append(shots_on)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_SHOTS_ON]
		entry = prev_total + shots_on
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][HOME_L10_SHOTS_ON]
		l10_game = fixture_data[home][home_length - 10][HOME_L1_SHOTS_ON]
		entry = l10_total - l10_game + shots_on
		fixture_sample.append(entry)
	# HOME_SEASON_SHOTS_ON,
	if home_length == 0:
		fixture_sample.append(shots_on)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_SHOTS_ON]
		entry = prev_total + shots_on
		fixture_sample.append(entry)

	# -- SHOTS OFF --
	shots_off = row[SHOTS_HOME].value - row[SHOTS_TARGET_HOME].value
	# HOME_AVG_SHOTS_OFF,
	if home_length == 0:
		fixture_sample.append(shots_off)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_SHOTS_OFF]
		total = prev_total + shots_off
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# HOME_L1_SHOTS_OFF,
	fixture_sample.append(shots_off)
	# HOME_L5_SHOTS_OFF,
	if home_length == 0:
		fixture_sample.append(shots_off)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_SHOTS_OFF]
		entry = prev_total + shots_off
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][HOME_L5_SHOTS_OFF]
		l5_game = fixture_data[home][home_length - 5][HOME_L1_SHOTS_OFF]
		entry = l5_total - l5_game + shots_off
		fixture_sample.append(entry)
	# HOME_L10_SHOTS_OFF,
	if home_length == 0:
		fixture_sample.append(shots_off)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_SHOTS_OFF]
		entry = prev_total + shots_off
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][HOME_L10_SHOTS_OFF]
		l10_game = fixture_data[home][home_length - 10][HOME_L1_SHOTS_OFF]
		entry = l10_total - l10_game + shots_off
		fixture_sample.append(entry)
	# HOME_SEASON_SHOTS_OFF,
	if home_length == 0:
		fixture_sample.append(shots_off)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_SHOTS_OFF]
		entry = prev_total + shots_off
		fixture_sample.append(entry)

	# -- CORNERS --
	corners = row[CORNERS_HOME].value
	# HOME_AVG_CORNERS,
	if home_length == 0:
		fixture_sample.append(corners)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_CORNERS]
		total = prev_total + corners
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# HOME_L1_CORNERS,
	fixture_sample.append(corners)
	# HOME_L5_CORNERS,
	if home_length == 0:
		fixture_sample.append(corners)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_CORNERS]
		entry = prev_total + corners
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][HOME_L5_CORNERS]
		l5_game = fixture_data[home][home_length - 5][HOME_L1_CORNERS]
		entry = l5_total - l5_game + corners
		fixture_sample.append(entry)
	# HOME_L10_CORNERS,
	if home_length == 0:
		fixture_sample.append(corners)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_CORNERS]
		entry = prev_total + corners
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][HOME_L10_CORNERS]
		l10_game = fixture_data[home][home_length - 10][HOME_L1_CORNERS]
		entry = l10_total - l10_game + corners
		fixture_sample.append(entry)
	# HOME_SEASON_CORNERS,
	if home_length == 0:
		fixture_sample.append(corners)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_CORNERS]
		entry = prev_total + corners
		fixture_sample.append(entry)

	# -- FOULS --
	fouls = row[FOULS_HOME].value
	# HOME_AVG_FOULS,
	if home_length == 0:
		fixture_sample.append(fouls)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_FOULS]
		total = prev_total + fouls
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# HOME_L1_FOULS,
	fixture_sample.append(fouls)
	# HOME_L5_FOULS,
	if home_length == 0:
		fixture_sample.append(fouls)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_FOULS]
		entry = prev_total + fouls
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][HOME_L5_FOULS]
		l5_game = fixture_data[home][home_length - 5][HOME_L1_FOULS]
		entry = l5_total - l5_game + fouls
		fixture_sample.append(entry)
	# HOME_L10_FOULS,
	if home_length == 0:
		fixture_sample.append(fouls)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_FOULS]
		entry = prev_total + fouls
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][HOME_L10_FOULS]
		l10_game = fixture_data[home][home_length - 10][HOME_L1_FOULS]
		entry = l10_total - l10_game + fouls
		fixture_sample.append(entry)
	# HOME_SEASON_FOULS,
	if home_length == 0:
		fixture_sample.append(fouls)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_FOULS]
		entry = prev_total + fouls
		fixture_sample.append(entry)

	print idx, ' ', fixture_sample
	fixture_data[home].append(fixture_sample)

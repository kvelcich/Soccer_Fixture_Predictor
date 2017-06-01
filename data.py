import xlrd
from xlrd.sheet import ctype_text
from table import *

''' Variable list: '''
team_IDs = []
# ID, AVG_GOALS, L1_GOALS, L5_GOALS, L10_GOALS, SEASON_GOALS, ...
fixture_data = []
game_ID = 1
# GAME_ID, HOME, AWAY
game_list = []
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

	game_sample = []
	game_sample.append(game_ID)
	game_sample.append(home)
	game_sample.append(away)
	game_list.append(game_sample)

	# --- Filling fixture_sample values ---
	home_length = len(fixture_data[home])
	# ID,
	fixture_sample.append(home)

	# -- GOALS --
	goals_scored = row[FT_GOALS_HOME].value
	# AVG_GOALS,
	if home_length == 0:
		fixture_sample.append(goals_scored)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_GOALS]
		total = prev_total + goals_scored
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# L1_GOALS,
	fixture_sample.append(goals_scored)
	# L5_GOALS,
	if home_length == 0:
		fixture_sample.append(goals_scored)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][SEASON_GOALS]
		entry = prev_total + goals_scored
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][L5_GOALS]
		l5_game = fixture_data[home][home_length - 5][L1_GOALS]
		entry = l5_total - l5_game + goals_scored
		fixture_sample.append(entry)
	# L10_GOALS,
	if home_length == 0:
		fixture_sample.append(goals_scored)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][SEASON_GOALS]
		entry = prev_total + goals_scored
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][L10_GOALS]
		l10_game = fixture_data[home][home_length - 10][L1_GOALS]
		entry = l10_total - l10_game + goals_scored
		fixture_sample.append(entry)
	# SEASON_GOALS,
	if home_length == 0:
		fixture_sample.append(goals_scored)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_GOALS]
		entry = prev_total + goals_scored
		fixture_sample.append(entry)

	# -- HALFTIME GOALS --
	goals_scored_ht = row[HT_GOALS_HOME].value
	# AVG_GOALS_HT,
	if home_length == 0:
		fixture_sample.append(goals_scored_ht)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_GOALS_HT]
		total = prev_total + goals_scored_ht
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# L1_GOALS_HT,
	fixture_sample.append(goals_scored_ht)
	# L5_GOALS_HT,
	if home_length == 0:
		fixture_sample.append(goals_scored_ht)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][SEASON_GOALS_HT]
		entry = prev_total + goals_scored_ht
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][L5_GOALS_HT]
		l5_game = fixture_data[home][home_length - 5][L1_GOALS_HT]
		entry = l5_total - l5_game + goals_scored_ht
		fixture_sample.append(entry)
	# L10_GOALS_HT,
	if home_length == 0:
		fixture_sample.append(goals_scored_ht)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][SEASON_GOALS_HT]
		entry = prev_total + goals_scored_ht
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][L10_GOALS_HT]
		l10_game = fixture_data[home][home_length - 10][L1_GOALS_HT]
		entry = l10_total - l10_game + goals_scored_ht
		fixture_sample.append(entry)
	# SEASON_GOALS_HT,
	if home_length == 0:
		fixture_sample.append(goals_scored_ht)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_GOALS_HT]
		entry = prev_total + goals_scored_ht
		fixture_sample.append(entry)

	# -- SHOTS ON --
	shots_on = row[SHOTS_TARGET_HOME].value
	# AVG_SHOTS_ON,
	if home_length == 0:
		fixture_sample.append(shots_on)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_SHOTS_ON]
		total = prev_total + shots_on
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# L1_SHOTS_ON,
	fixture_sample.append(shots_on)
	# L5_SHOTS_ON,
	if home_length == 0:
		fixture_sample.append(shots_on)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][SEASON_SHOTS_ON]
		entry = prev_total + shots_on
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][L5_SHOTS_ON]
		l5_game = fixture_data[home][home_length - 5][L1_SHOTS_ON]
		entry = l5_total - l5_game + shots_on
		fixture_sample.append(entry)
	# L10_SHOTS_ON,
	if home_length == 0:
		fixture_sample.append(shots_on)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][SEASON_SHOTS_ON]
		entry = prev_total + shots_on
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][L10_SHOTS_ON]
		l10_game = fixture_data[home][home_length - 10][L1_SHOTS_ON]
		entry = l10_total - l10_game + shots_on
		fixture_sample.append(entry)
	# SEASON_SHOTS_ON,
	if home_length == 0:
		fixture_sample.append(shots_on)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_SHOTS_ON]
		entry = prev_total + shots_on
		fixture_sample.append(entry)

	# -- SHOTS OFF --
	shots_off = row[SHOTS_HOME].value - row[SHOTS_TARGET_HOME].value
	# AVG_SHOTS_OFF,
	if home_length == 0:
		fixture_sample.append(shots_off)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_SHOTS_OFF]
		total = prev_total + shots_off
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# L1_SHOTS_OFF,
	fixture_sample.append(shots_off)
	# L5_SHOTS_OFF,
	if home_length == 0:
		fixture_sample.append(shots_off)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][SEASON_SHOTS_OFF]
		entry = prev_total + shots_off
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][L5_SHOTS_OFF]
		l5_game = fixture_data[home][home_length - 5][L1_SHOTS_OFF]
		entry = l5_total - l5_game + shots_off
		fixture_sample.append(entry)
	# L10_SHOTS_OFF,
	if home_length == 0:
		fixture_sample.append(shots_off)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][SEASON_SHOTS_OFF]
		entry = prev_total + shots_off
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][L10_SHOTS_OFF]
		l10_game = fixture_data[home][home_length - 10][L1_SHOTS_OFF]
		entry = l10_total - l10_game + shots_off
		fixture_sample.append(entry)
	# SEASON_SHOTS_OFF,
	if home_length == 0:
		fixture_sample.append(shots_off)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_SHOTS_OFF]
		entry = prev_total + shots_off
		fixture_sample.append(entry)

	# -- CORNERS --
	corners = row[CORNERS_HOME].value
	# AVG_CORNERS,
	if home_length == 0:
		fixture_sample.append(corners)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_CORNERS]
		total = prev_total + corners
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# L1_CORNERS,
	fixture_sample.append(corners)
	# L5_CORNERS,
	if home_length == 0:
		fixture_sample.append(corners)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][SEASON_CORNERS]
		entry = prev_total + corners
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][L5_CORNERS]
		l5_game = fixture_data[home][home_length - 5][L1_CORNERS]
		entry = l5_total - l5_game + corners
		fixture_sample.append(entry)
	# L10_CORNERS,
	if home_length == 0:
		fixture_sample.append(corners)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][SEASON_CORNERS]
		entry = prev_total + corners
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][L10_CORNERS]
		l10_game = fixture_data[home][home_length - 10][L1_CORNERS]
		entry = l10_total - l10_game + corners
		fixture_sample.append(entry)
	# SEASON_CORNERS,
	if home_length == 0:
		fixture_sample.append(corners)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_CORNERS]
		entry = prev_total + corners
		fixture_sample.append(entry)

	# -- FOULS --
	fouls = row[FOULS_HOME].value
	# AVG_FOULS,
	if home_length == 0:
		fixture_sample.append(fouls)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_FOULS]
		total = prev_total + fouls
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# L1_FOULS,
	fixture_sample.append(fouls)
	# L5_FOULS,
	if home_length == 0:
		fixture_sample.append(fouls)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][SEASON_FOULS]
		entry = prev_total + fouls
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][L5_FOULS]
		l5_game = fixture_data[home][home_length - 5][L1_FOULS]
		entry = l5_total - l5_game + fouls
		fixture_sample.append(entry)
	# L10_FOULS,
	if home_length == 0:
		fixture_sample.append(fouls)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][SEASON_FOULS]
		entry = prev_total + fouls
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][L10_FOULS]
		l10_game = fixture_data[home][home_length - 10][L1_FOULS]
		entry = l10_total - l10_game + fouls
		fixture_sample.append(entry)
	# SEASON_FOULS,
	if home_length == 0:
		fixture_sample.append(fouls)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_FOULS]
		entry = prev_total + fouls
		fixture_sample.append(entry)

	# -- YELLOWS --
	yellows = row[YELLOWS_HOME].value
	# AVG_YELLOWS,
	if home_length == 0:
		fixture_sample.append(yellows)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_YELLOWS]
		total = prev_total + yellows
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# L1_YELLOWS,
	fixture_sample.append(yellows)
	# L5_YELLOWS,
	if home_length == 0:
		fixture_sample.append(yellows)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][SEASON_YELLOWS]
		entry = prev_total + yellows
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][L5_YELLOWS]
		l5_game = fixture_data[home][home_length - 5][L1_YELLOWS]
		entry = l5_total - l5_game + yellows
		fixture_sample.append(entry)
	# L10_YELLOWS,
	if home_length == 0:
		fixture_sample.append(yellows)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][SEASON_YELLOWS]
		entry = prev_total + yellows
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][L10_YELLOWS]
		l10_game = fixture_data[home][home_length - 10][L1_YELLOWS]
		entry = l10_total - l10_game + yellows
		fixture_sample.append(entry)
	# SEASON_YELLOWS,
	if home_length == 0:
		fixture_sample.append(yellows)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_YELLOWS]
		entry = prev_total + yellows
		fixture_sample.append(entry)

	# -- REDS --
	reds = row[REDS_HOME].value
	# AVG_REDS,
	if home_length == 0:
		fixture_sample.append(reds)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_REDS]
		total = prev_total + reds
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# L1_REDS,
	fixture_sample.append(reds)
	# L5_REDS,
	if home_length == 0:
		fixture_sample.append(reds)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][SEASON_REDS]
		entry = prev_total + reds
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][L5_REDS]
		l5_game = fixture_data[home][home_length - 5][L1_REDS]
		entry = l5_total - l5_game + reds
		fixture_sample.append(entry)
	# L10_REDS,
	if home_length == 0:
		fixture_sample.append(reds)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][SEASON_REDS]
		entry = prev_total + reds
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][L10_REDS]
		l10_game = fixture_data[home][home_length - 10][L1_REDS]
		entry = l10_total - l10_game + reds
		fixture_sample.append(entry)
	# SEASON_REDS,
	if home_length == 0:
		fixture_sample.append(reds)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_REDS]
		entry = prev_total + reds
		fixture_sample.append(entry)

	# -- GOALS AGAINST --
	goals_scored_against = row[FT_GOALS_AWAY].value
	# AVG_GOALS_AGAINST,
	if home_length == 0:
		fixture_sample.append(goals_scored_against)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_GOALS_AGAINST]
		total = prev_total + goals_scored_against
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# L1_GOALS_AGAINST,
	fixture_sample.append(goals_scored_against)
	# L5_GOALS_AGAINST,
	if home_length == 0:
		fixture_sample.append(goals_scored_against)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][SEASON_GOALS_AGAINST]
		entry = prev_total + goals_scored_against
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][L5_GOALS_AGAINST]
		l5_game = fixture_data[home][home_length - 5][L1_GOALS_AGAINST]
		entry = l5_total - l5_game + goals_scored_against
		fixture_sample.append(entry)
	# L10_GOALS_AGAINST,
	if home_length == 0:
		fixture_sample.append(goals_scored_against)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][SEASON_GOALS_AGAINST]
		entry = prev_total + goals_scored_against
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][L10_GOALS_AGAINST]
		l10_game = fixture_data[home][home_length - 10][L1_GOALS_AGAINST]
		entry = l10_total - l10_game + goals_scored_against
		fixture_sample.append(entry)
	# SEASON_GOALS_AGAINST,
	if home_length == 0:
		fixture_sample.append(goals_scored_against)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_GOALS_AGAINST]
		entry = prev_total + goals_scored_against
		fixture_sample.append(entry)

	# -- HALFTIME GOALS AGAINST --
	goals_scored_ht_against = row[HT_GOALS_AWAY].value
	# AVG_GOALS_HT_AGAINST,
	if home_length == 0:
		fixture_sample.append(goals_scored_ht_against)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_GOALS_HT_AGAINST]
		total = prev_total + goals_scored_ht_against
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# L1_GOALS_HT_AGAINST,
	fixture_sample.append(goals_scored_ht_against)
	# L5_GOALS_HT_AGAINST,
	if home_length == 0:
		fixture_sample.append(goals_scored_ht_against)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][SEASON_GOALS_HT_AGAINST]
		entry = prev_total + goals_scored_ht_against
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][L5_GOALS_HT_AGAINST]
		l5_game = fixture_data[home][home_length - 5][L1_GOALS_HT_AGAINST]
		entry = l5_total - l5_game + goals_scored_ht_against
		fixture_sample.append(entry)
	# L10_GOALS_HT_AGAINST,
	if home_length == 0:
		fixture_sample.append(goals_scored_ht_against)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][SEASON_GOALS_HT_AGAINST]
		entry = prev_total + goals_scored_ht_against
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][L10_GOALS_HT_AGAINST]
		l10_game = fixture_data[home][home_length - 10][L1_GOALS_HT_AGAINST]
		entry = l10_total - l10_game + goals_scored_ht_against
		fixture_sample.append(entry)
	# SEASON_GOALS_HT_AGAINST,
	if home_length == 0:
		fixture_sample.append(goals_scored_ht_against)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_GOALS_HT_AGAINST]
		entry = prev_total + goals_scored_ht_against
		fixture_sample.append(entry)

	# -- SHOTS ON AGAINST --
	shots_on_against = row[SHOTS_TARGET_AWAY].value
	# AVG_SHOTS_ON_AGAINST,
	if home_length == 0:
		fixture_sample.append(shots_on_against)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_SHOTS_ON_AGAINST]
		total = prev_total + shots_on_against
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# L1_SHOTS_ON_AGAINST,
	fixture_sample.append(shots_on_against)
	# L5_SHOTS_ON_AGAINST,
	if home_length == 0:
		fixture_sample.append(shots_on_against)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][SEASON_SHOTS_ON_AGAINST]
		entry = prev_total + shots_on_against
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][L5_SHOTS_ON_AGAINST]
		l5_game = fixture_data[home][home_length - 5][L1_SHOTS_ON_AGAINST]
		entry = l5_total - l5_game + shots_on_against
		fixture_sample.append(entry)
	# L10_SHOTS_ON_AGAINST,
	if home_length == 0:
		fixture_sample.append(shots_on_against)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][SEASON_SHOTS_ON_AGAINST]
		entry = prev_total + shots_on_against
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][L10_SHOTS_ON_AGAINST]
		l10_game = fixture_data[home][home_length - 10][L1_SHOTS_ON_AGAINST]
		entry = l10_total - l10_game + shots_on_against
		fixture_sample.append(entry)
	# SEASON_SHOTS_ON_AGAINST,
	if home_length == 0:
		fixture_sample.append(shots_on_against)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_SHOTS_ON_AGAINST]
		entry = prev_total + shots_on_against
		fixture_sample.append(entry)

	# -- SHOTS OFF AGAINST --
	shots_off_against = row[SHOTS_AWAY].value - row[SHOTS_TARGET_AWAY].value
	# AVG_SHOTS_OFF_AGAINST,
	if home_length == 0:
		fixture_sample.append(shots_off_against)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_SHOTS_OFF_AGAINST]
		total = prev_total + shots_off_against
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# L1_SHOTS_OFF_AGAINST,
	fixture_sample.append(shots_off_against)
	# L5_SHOTS_OFF_AGAINST,
	if home_length == 0:
		fixture_sample.append(shots_off_against)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][SEASON_SHOTS_OFF_AGAINST]
		entry = prev_total + shots_off_against
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][L5_SHOTS_OFF_AGAINST]
		l5_game = fixture_data[home][home_length - 5][L1_SHOTS_OFF_AGAINST]
		entry = l5_total - l5_game + shots_off_against
		fixture_sample.append(entry)
	# L10_SHOTS_OFF_AGAINST,
	if home_length == 0:
		fixture_sample.append(shots_off_against)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][SEASON_SHOTS_OFF_AGAINST]
		entry = prev_total + shots_off_against
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][L10_SHOTS_OFF_AGAINST]
		l10_game = fixture_data[home][home_length - 10][L1_SHOTS_OFF_AGAINST]
		entry = l10_total - l10_game + shots_off_against
		fixture_sample.append(entry)
	# SEASON_SHOTS_OFF_AGAINST,
	if home_length == 0:
		fixture_sample.append(shots_off_against)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_SHOTS_OFF_AGAINST]
		entry = prev_total + shots_off_against
		fixture_sample.append(entry)

	# -- CORNERS AGAINST --
	corners_against = row[CORNERS_AWAY].value
	# AVG_CORNERS_AGAINST,
	if home_length == 0:
		fixture_sample.append(corners_against)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_CORNERS_AGAINST]
		total = prev_total + corners_against
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# L1_CORNERS_AGAINST,
	fixture_sample.append(corners_against)
	# L5_CORNERS_AGAINST,
	if home_length == 0:
		fixture_sample.append(corners_against)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][SEASON_CORNERS_AGAINST]
		entry = prev_total + corners_against
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][L5_CORNERS_AGAINST]
		l5_game = fixture_data[home][home_length - 5][L1_CORNERS_AGAINST]
		entry = l5_total - l5_game + corners_against
		fixture_sample.append(entry)
	# L10_CORNERS_AGAINST,
	if home_length == 0:
		fixture_sample.append(corners_against)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][SEASON_CORNERS_AGAINST]
		entry = prev_total + corners_against
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][L10_CORNERS_AGAINST]
		l10_game = fixture_data[home][home_length - 10][L1_CORNERS_AGAINST]
		entry = l10_total - l10_game + corners_against
		fixture_sample.append(entry)
	# SEASON_CORNERS_AGAINST,
	if home_length == 0:
		fixture_sample.append(corners_against)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_CORNERS_AGAINST]
		entry = prev_total + corners_against
		fixture_sample.append(entry)

	# -- FOULS AGAINST --
	fouls_against = row[FOULS_AWAY].value
	# AVG_FOULS_AGAINST,
	if home_length == 0:
		fixture_sample.append(fouls_against)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_FOULS_AGAINST]
		total = prev_total + fouls_against
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# L1_FOULS_AGAINST,
	fixture_sample.append(fouls_against)
	# L5_FOULS_AGAINST,
	if home_length == 0:
		fixture_sample.append(fouls_against)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][SEASON_FOULS_AGAINST]
		entry = prev_total + fouls_against
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][L5_FOULS_AGAINST]
		l5_game = fixture_data[home][home_length - 5][L1_FOULS_AGAINST]
		entry = l5_total - l5_game + fouls_against
		fixture_sample.append(entry)
	# L10_FOULS_AGAINST,
	if home_length == 0:
		fixture_sample.append(fouls_against)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][SEASON_FOULS_AGAINST]
		entry = prev_total + fouls_against
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][L10_FOULS_AGAINST]
		l10_game = fixture_data[home][home_length - 10][L1_FOULS_AGAINST]
		entry = l10_total - l10_game + fouls_against
		fixture_sample.append(entry)
	# SEASON_FOULS_AGAINST,
	if home_length == 0:
		fixture_sample.append(fouls_against)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_FOULS_AGAINST]
		entry = prev_total + fouls_against
		fixture_sample.append(entry)

	# -- YELLOWS AGAINST --
	yellows_against = row[YELLOWS_AWAY].value
	# AVG_YELLOWS_AGAINST,
	if home_length == 0:
		fixture_sample.append(yellows_against)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_YELLOWS_AGAINST]
		total = prev_total + yellows_against
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# L1_YELLOWS_AGAINST,
	fixture_sample.append(yellows_against)
	# L5_YELLOWS_AGAINST,
	if home_length == 0:
		fixture_sample.append(yellows_against)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][SEASON_YELLOWS_AGAINST]
		entry = prev_total + yellows_against
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][L5_YELLOWS_AGAINST]
		l5_game = fixture_data[home][home_length - 5][L1_YELLOWS_AGAINST]
		entry = l5_total - l5_game + yellows_against
		fixture_sample.append(entry)
	# L10_YELLOWS_AGAINST,
	if home_length == 0:
		fixture_sample.append(yellows_against)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][SEASON_YELLOWS_AGAINST]
		entry = prev_total + yellows_against
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][L10_YELLOWS_AGAINST]
		l10_game = fixture_data[home][home_length - 10][L1_YELLOWS_AGAINST]
		entry = l10_total - l10_game + yellows_against
		fixture_sample.append(entry)
	# SEASON_YELLOWS_AGAINST,
	if home_length == 0:
		fixture_sample.append(yellows_against)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_YELLOWS_AGAINST]
		entry = prev_total + yellows_against
		fixture_sample.append(entry)

	# -- REDS AGAINST --
	reds_against = row[REDS_AWAY].value
	# AVG_REDS_AGAINST,
	if home_length == 0:
		fixture_sample.append(reds_against)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_REDS_AGAINST]
		total = prev_total + reds_against
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# L1_REDS_AGAINST,
	fixture_sample.append(reds_against)
	# L5_REDS_AGAINST,
	if home_length == 0:
		fixture_sample.append(reds_against)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][SEASON_REDS_AGAINST]
		entry = prev_total + reds_against
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][L5_REDS_AGAINST]
		l5_game = fixture_data[home][home_length - 5][L1_REDS_AGAINST]
		entry = l5_total - l5_game + reds_against
		fixture_sample.append(entry)
	# L10_REDS_AGAINST,
	if home_length == 0:
		fixture_sample.append(reds_against)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][SEASON_REDS_AGAINST]
		entry = prev_total + reds_against
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][L10_REDS_AGAINST]
		l10_game = fixture_data[home][home_length - 10][L1_REDS_AGAINST]
		entry = l10_total - l10_game + reds_against
		fixture_sample.append(entry)
	# SEASON_REDS_AGAINST,
	if home_length == 0:
		fixture_sample.append(reds_against)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_REDS_AGAINST]
		entry = prev_total + reds_against
		fixture_sample.append(entry)

	# -- FORM --
	if row[FT_RESULT].value == 'H':
		form = 3
	elif row[FT_RESULT].value == 'D':
		form = 1
	else:
		form = 0
	# AVG_FORM,
	if home_length == 0:
		fixture_sample.append(form)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_FORM]
		total = prev_total + form
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# L1_FORM,
	fixture_sample.append(form)
	# L5_FORM,
	if home_length == 0:
		fixture_sample.append(form)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][SEASON_FORM]
		entry = prev_total + form
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][L5_FORM]
		l5_game = fixture_data[home][home_length - 5][L1_FORM]
		entry = l5_total - l5_game + form
		fixture_sample.append(entry)
	# L10_FORM,
	if home_length == 0:
		fixture_sample.append(form)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][SEASON_FORM]
		entry = prev_total + form
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][L10_FORM]
		l10_game = fixture_data[home][home_length - 10][L1_FORM]
		entry = l10_total - l10_game + form
		fixture_sample.append(entry)
	# SEASON_FORM,
	if home_length == 0:
		fixture_sample.append(form)
	else:
		prev_total = fixture_data[home][home_length - 1][SEASON_FORM]
		entry = prev_total + form
		fixture_sample.append(entry)

	# --- PERCENTAGE ---
	# TOTAL_WIN
	if home_length == 0:
		if form == 3:
			fixture_sample.append(1.0)
		else:
			fixture_sample.append(0.0)
	else:
		fixture = 0.0
		if form == 3:
			fixture = 1.0
		prev_total = fixture_data[home][home_length - 1][TOTAL_WIN]
		entry = prev_total + fixture
		fixture_sample.append(entry)
	# TOTAL_TIE
	if home_length == 0:
		if form == 1:
			fixture_sample.append(1.0)
		else:
			fixture_sample.append(0.0)
	else:
		fixture = 0.0
		if form == 1:
			fixture = 1.0
		prev_total = fixture_data[home][home_length - 1][TOTAL_TIE]
		entry = prev_total + fixture
		fixture_sample.append(entry)
	# TOTAL_LOSE
	if home_length == 0:
		if form == 0:
			fixture_sample.append(1.0)
		else:
			fixture_sample.append(0.0)
	else:
		fixture = 0.0
		if form == 0:
			fixture = 1.0
		prev_total = fixture_data[home][home_length - 1][TOTAL_LOSE]
		entry = prev_total + fixture
		fixture_sample.append(entry)
	# PERCENTAGE_WIN
	if home_length == 0:
		if form == 3:
			fixture_sample.append(1.0)
		else:
			fixture_sample.append(0.0)
	else:
		fixture = 0.0
		if form == 3:
			fixture = 1.0
		prev_total = fixture_data[home][home_length - 1][TOTAL_WIN]
		total = prev_total + fixture
		entry = total / (len(fixture_data[home]) + 1.0)
		fixture_sample.append(entry)
	# PERCENTAGE_TIE
	if home_length == 0:
		if form == 1:
			fixture_sample.append(1.0)
		else:
			fixture_sample.append(0.0)
	else:
		fixture = 0.0
		if form == 1:
			fixture = 1.0
		prev_total = fixture_data[home][home_length - 1][TOTAL_TIE]
		total = prev_total + fixture
		entry = total / (len(fixture_data[home]) + 1.0)
		fixture_sample.append(entry)
	# PERCENTAGE_LOSE
	if home_length == 0:
		if form == 0:
			fixture_sample.append(1.0)
		else:
			fixture_sample.append(0.0)
	else:
		fixture = 0.0
		if form == 0:
			fixture = 1.0
		prev_total = fixture_data[home][home_length - 1][TOTAL_LOSE]
		total = prev_total + fixture
		entry = total / (len(fixture_data[home]) + 1.0)
		fixture_sample.append(entry)

	# --- HOME ---
	fixture_sample.append(1)
	fixture_sample.append(game_ID)

	fixture_data[home].append(fixture_sample)

	''' ----- Filling in Away team values ----- '''
	# --- Filling fixture_sample values ---
	away_length = len(fixture_data[away])
	# ID,
	fixture_sample.append(away)

	# -- GOALS --
	goals_scored = row[FT_GOALS_AWAY].value
	# AVG_GOALS,
	if away_length == 0:
		fixture_sample.append(goals_scored)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_GOALS]
		total = prev_total + goals_scored
		entry = total / (away_length + 1)
		fixture_sample.append(entry)
	# L1_GOALS,
	fixture_sample.append(goals_scored)
	# L5_GOALS,
	if away_length == 0:
		fixture_sample.append(goals_scored)
	elif away_length < 5:
		prev_total = fixture_data[away][away_length - 1][SEASON_GOALS]
		entry = prev_total + goals_scored
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[away][away_length - 1][L5_GOALS]
		l5_game = fixture_data[away][away_length - 5][L1_GOALS]
		entry = l5_total - l5_game + goals_scored
		fixture_sample.append(entry)
	# L10_GOALS,
	if away_length == 0:
		fixture_sample.append(goals_scored)
	elif away_length < 10:
		prev_total = fixture_data[away][away_length - 1][SEASON_GOALS]
		entry = prev_total + goals_scored
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[away][away_length - 1][L10_GOALS]
		l10_game = fixture_data[away][away_length - 10][L1_GOALS]
		entry = l10_total - l10_game + goals_scored
		fixture_sample.append(entry)
	# SEASON_GOALS,
	if away_length == 0:
		fixture_sample.append(goals_scored)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_GOALS]
		entry = prev_total + goals_scored
		fixture_sample.append(entry)

	# -- HALFTIME GOALS --
	goals_scored_ht = row[HT_GOALS_AWAY].value
	# AVG_GOALS_HT,
	if away_length == 0:
		fixture_sample.append(goals_scored_ht)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_GOALS_HT]
		total = prev_total + goals_scored_ht
		entry = total / (away_length + 1)
		fixture_sample.append(entry)
	# L1_GOALS_HT,
	fixture_sample.append(goals_scored_ht)
	# L5_GOALS_HT,
	if away_length == 0:
		fixture_sample.append(goals_scored_ht)
	elif away_length < 5:
		prev_total = fixture_data[away][away_length - 1][SEASON_GOALS_HT]
		entry = prev_total + goals_scored_ht
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[away][away_length - 1][L5_GOALS_HT]
		l5_game = fixture_data[away][away_length - 5][L1_GOALS_HT]
		entry = l5_total - l5_game + goals_scored_ht
		fixture_sample.append(entry)
	# L10_GOALS_HT,
	if away_length == 0:
		fixture_sample.append(goals_scored_ht)
	elif away_length < 10:
		prev_total = fixture_data[away][away_length - 1][SEASON_GOALS_HT]
		entry = prev_total + goals_scored_ht
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[away][away_length - 1][L10_GOALS_HT]
		l10_game = fixture_data[away][away_length - 10][L1_GOALS_HT]
		entry = l10_total - l10_game + goals_scored_ht
		fixture_sample.append(entry)
	# SEASON_GOALS_HT,
	if away_length == 0:
		fixture_sample.append(goals_scored_ht)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_GOALS_HT]
		entry = prev_total + goals_scored_ht
		fixture_sample.append(entry)

	# -- SHOTS ON --
	shots_on = row[SHOTS_TARGET_AWAY].value
	# AVG_SHOTS_ON,
	if away_length == 0:
		fixture_sample.append(shots_on)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_SHOTS_ON]
		total = prev_total + shots_on
		entry = total / (away_length + 1)
		fixture_sample.append(entry)
	# L1_SHOTS_ON,
	fixture_sample.append(shots_on)
	# L5_SHOTS_ON,
	if away_length == 0:
		fixture_sample.append(shots_on)
	elif away_length < 5:
		prev_total = fixture_data[away][away_length - 1][SEASON_SHOTS_ON]
		entry = prev_total + shots_on
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[away][away_length - 1][L5_SHOTS_ON]
		l5_game = fixture_data[away][away_length - 5][L1_SHOTS_ON]
		entry = l5_total - l5_game + shots_on
		fixture_sample.append(entry)
	# L10_SHOTS_ON,
	if away_length == 0:
		fixture_sample.append(shots_on)
	elif away_length < 10:
		prev_total = fixture_data[away][away_length - 1][SEASON_SHOTS_ON]
		entry = prev_total + shots_on
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[away][away_length - 1][L10_SHOTS_ON]
		l10_game = fixture_data[away][away_length - 10][L1_SHOTS_ON]
		entry = l10_total - l10_game + shots_on
		fixture_sample.append(entry)
	# SEASON_SHOTS_ON,
	if away_length == 0:
		fixture_sample.append(shots_on)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_SHOTS_ON]
		entry = prev_total + shots_on
		fixture_sample.append(entry)

	# -- SHOTS OFF --
	shots_off = row[SHOTS_AWAY].value - row[SHOTS_TARGET_AWAY].value
	# AVG_SHOTS_OFF,
	if away_length == 0:
		fixture_sample.append(shots_off)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_SHOTS_OFF]
		total = prev_total + shots_off
		entry = total / (away_length + 1)
		fixture_sample.append(entry)
	# L1_SHOTS_OFF,
	fixture_sample.append(shots_off)
	# L5_SHOTS_OFF,
	if away_length == 0:
		fixture_sample.append(shots_off)
	elif away_length < 5:
		prev_total = fixture_data[away][away_length - 1][SEASON_SHOTS_OFF]
		entry = prev_total + shots_off
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[away][away_length - 1][L5_SHOTS_OFF]
		l5_game = fixture_data[away][away_length - 5][L1_SHOTS_OFF]
		entry = l5_total - l5_game + shots_off
		fixture_sample.append(entry)
	# L10_SHOTS_OFF,
	if away_length == 0:
		fixture_sample.append(shots_off)
	elif away_length < 10:
		prev_total = fixture_data[away][away_length - 1][SEASON_SHOTS_OFF]
		entry = prev_total + shots_off
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[away][away_length - 1][L10_SHOTS_OFF]
		l10_game = fixture_data[away][away_length - 10][L1_SHOTS_OFF]
		entry = l10_total - l10_game + shots_off
		fixture_sample.append(entry)
	# SEASON_SHOTS_OFF,
	if away_length == 0:
		fixture_sample.append(shots_off)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_SHOTS_OFF]
		entry = prev_total + shots_off
		fixture_sample.append(entry)

	# -- CORNERS --
	corners = row[CORNERS_AWAY].value
	# AVG_CORNERS,
	if away_length == 0:
		fixture_sample.append(corners)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_CORNERS]
		total = prev_total + corners
		entry = total / (away_length + 1)
		fixture_sample.append(entry)
	# L1_CORNERS,
	fixture_sample.append(corners)
	# L5_CORNERS,
	if away_length == 0:
		fixture_sample.append(corners)
	elif away_length < 5:
		prev_total = fixture_data[away][away_length - 1][SEASON_CORNERS]
		entry = prev_total + corners
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[away][away_length - 1][L5_CORNERS]
		l5_game = fixture_data[away][away_length - 5][L1_CORNERS]
		entry = l5_total - l5_game + corners
		fixture_sample.append(entry)
	# L10_CORNERS,
	if away_length == 0:
		fixture_sample.append(corners)
	elif away_length < 10:
		prev_total = fixture_data[away][away_length - 1][SEASON_CORNERS]
		entry = prev_total + corners
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[away][away_length - 1][L10_CORNERS]
		l10_game = fixture_data[away][away_length - 10][L1_CORNERS]
		entry = l10_total - l10_game + corners
		fixture_sample.append(entry)
	# SEASON_CORNERS,
	if away_length == 0:
		fixture_sample.append(corners)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_CORNERS]
		entry = prev_total + corners
		fixture_sample.append(entry)

	# -- FOULS --
	fouls = row[FOULS_AWAY].value
	# AVG_FOULS,
	if away_length == 0:
		fixture_sample.append(fouls)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_FOULS]
		total = prev_total + fouls
		entry = total / (away_length + 1)
		fixture_sample.append(entry)
	# L1_FOULS,
	fixture_sample.append(fouls)
	# L5_FOULS,
	if away_length == 0:
		fixture_sample.append(fouls)
	elif away_length < 5:
		prev_total = fixture_data[away][away_length - 1][SEASON_FOULS]
		entry = prev_total + fouls
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[away][away_length - 1][L5_FOULS]
		l5_game = fixture_data[away][away_length - 5][L1_FOULS]
		entry = l5_total - l5_game + fouls
		fixture_sample.append(entry)
	# L10_FOULS,
	if away_length == 0:
		fixture_sample.append(fouls)
	elif away_length < 10:
		prev_total = fixture_data[away][away_length - 1][SEASON_FOULS]
		entry = prev_total + fouls
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[away][away_length - 1][L10_FOULS]
		l10_game = fixture_data[away][away_length - 10][L1_FOULS]
		entry = l10_total - l10_game + fouls
		fixture_sample.append(entry)
	# SEASON_FOULS,
	if away_length == 0:
		fixture_sample.append(fouls)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_FOULS]
		entry = prev_total + fouls
		fixture_sample.append(entry)

	# -- YELLOWS --
	yellows = row[YELLOWS_AWAY].value
	# AVG_YELLOWS,
	if away_length == 0:
		fixture_sample.append(yellows)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_YELLOWS]
		total = prev_total + yellows
		entry = total / (away_length + 1)
		fixture_sample.append(entry)
	# L1_YELLOWS,
	fixture_sample.append(yellows)
	# L5_YELLOWS,
	if away_length == 0:
		fixture_sample.append(yellows)
	elif away_length < 5:
		prev_total = fixture_data[away][away_length - 1][SEASON_YELLOWS]
		entry = prev_total + yellows
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[away][away_length - 1][L5_YELLOWS]
		l5_game = fixture_data[away][away_length - 5][L1_YELLOWS]
		entry = l5_total - l5_game + yellows
		fixture_sample.append(entry)
	# L10_YELLOWS,
	if away_length == 0:
		fixture_sample.append(yellows)
	elif away_length < 10:
		prev_total = fixture_data[away][away_length - 1][SEASON_YELLOWS]
		entry = prev_total + yellows
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[away][away_length - 1][L10_YELLOWS]
		l10_game = fixture_data[away][away_length - 10][L1_YELLOWS]
		entry = l10_total - l10_game + yellows
		fixture_sample.append(entry)
	# SEASON_YELLOWS,
	if away_length == 0:
		fixture_sample.append(yellows)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_YELLOWS]
		entry = prev_total + yellows
		fixture_sample.append(entry)

	# -- REDS --
	reds = row[REDS_AWAY].value
	# AVG_REDS,
	if away_length == 0:
		fixture_sample.append(reds)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_REDS]
		total = prev_total + reds
		entry = total / (away_length + 1)
		fixture_sample.append(entry)
	# L1_REDS,
	fixture_sample.append(reds)
	# L5_REDS,
	if away_length == 0:
		fixture_sample.append(reds)
	elif away_length < 5:
		prev_total = fixture_data[away][away_length - 1][SEASON_REDS]
		entry = prev_total + reds
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[away][away_length - 1][L5_REDS]
		l5_game = fixture_data[away][away_length - 5][L1_REDS]
		entry = l5_total - l5_game + reds
		fixture_sample.append(entry)
	# L10_REDS,
	if away_length == 0:
		fixture_sample.append(reds)
	elif away_length < 10:
		prev_total = fixture_data[away][away_length - 1][SEASON_REDS]
		entry = prev_total + reds
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[away][away_length - 1][L10_REDS]
		l10_game = fixture_data[away][away_length - 10][L1_REDS]
		entry = l10_total - l10_game + reds
		fixture_sample.append(entry)
	# SEASON_REDS,
	if away_length == 0:
		fixture_sample.append(reds)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_REDS]
		entry = prev_total + reds
		fixture_sample.append(entry)

	# -- GOALS AGAINST --
	goals_scored_against = row[FT_GOALS_HOME].value
	# AVG_GOALS_AGAINST,
	if away_length == 0:
		fixture_sample.append(goals_scored_against)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_GOALS_AGAINST]
		total = prev_total + goals_scored_against
		entry = total / (away_length + 1)
		fixture_sample.append(entry)
	# L1_GOALS_AGAINST,
	fixture_sample.append(goals_scored_against)
	# L5_GOALS_AGAINST,
	if away_length == 0:
		fixture_sample.append(goals_scored_against)
	elif away_length < 5:
		prev_total = fixture_data[away][away_length - 1][SEASON_GOALS_AGAINST]
		entry = prev_total + goals_scored_against
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[away][away_length - 1][L5_GOALS_AGAINST]
		l5_game = fixture_data[away][away_length - 5][L1_GOALS_AGAINST]
		entry = l5_total - l5_game + goals_scored_against
		fixture_sample.append(entry)
	# L10_GOALS_AGAINST,
	if away_length == 0:
		fixture_sample.append(goals_scored_against)
	elif away_length < 10:
		prev_total = fixture_data[away][away_length - 1][SEASON_GOALS_AGAINST]
		entry = prev_total + goals_scored_against
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[away][away_length - 1][L10_GOALS_AGAINST]
		l10_game = fixture_data[away][away_length - 10][L1_GOALS_AGAINST]
		entry = l10_total - l10_game + goals_scored_against
		fixture_sample.append(entry)
	# SEASON_GOALS_AGAINST,
	if away_length == 0:
		fixture_sample.append(goals_scored_against)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_GOALS_AGAINST]
		entry = prev_total + goals_scored_against
		fixture_sample.append(entry)

	# -- HALFTIME GOALS AGAINST --
	goals_scored_ht_against = row[HT_GOALS_HOME].value
	# AVG_GOALS_HT_AGAINST,
	if away_length == 0:
		fixture_sample.append(goals_scored_ht_against)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_GOALS_HT_AGAINST]
		total = prev_total + goals_scored_ht_against
		entry = total / (away_length + 1)
		fixture_sample.append(entry)
	# L1_GOALS_HT_AGAINST,
	fixture_sample.append(goals_scored_ht_against)
	# L5_GOALS_HT_AGAINST,
	if away_length == 0:
		fixture_sample.append(goals_scored_ht_against)
	elif away_length < 5:
		prev_total = fixture_data[away][away_length - 1][SEASON_GOALS_HT_AGAINST]
		entry = prev_total + goals_scored_ht_against
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[away][away_length - 1][L5_GOALS_HT_AGAINST]
		l5_game = fixture_data[away][away_length - 5][L1_GOALS_HT_AGAINST]
		entry = l5_total - l5_game + goals_scored_ht_against
		fixture_sample.append(entry)
	# L10_GOALS_HT_AGAINST,
	if away_length == 0:
		fixture_sample.append(goals_scored_ht_against)
	elif away_length < 10:
		prev_total = fixture_data[away][away_length - 1][SEASON_GOALS_HT_AGAINST]
		entry = prev_total + goals_scored_ht_against
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[away][away_length - 1][L10_GOALS_HT_AGAINST]
		l10_game = fixture_data[away][away_length - 10][L1_GOALS_HT_AGAINST]
		entry = l10_total - l10_game + goals_scored_ht_against
		fixture_sample.append(entry)
	# SEASON_GOALS_HT_AGAINST,
	if away_length == 0:
		fixture_sample.append(goals_scored_ht_against)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_GOALS_HT_AGAINST]
		entry = prev_total + goals_scored_ht_against
		fixture_sample.append(entry)

	# -- SHOTS ON AGAINST --
	shots_on_against = row[SHOTS_TARGET_HOME].value
	# AVG_SHOTS_ON_AGAINST,
	if away_length == 0:
		fixture_sample.append(shots_on_against)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_SHOTS_ON_AGAINST]
		total = prev_total + shots_on_against
		entry = total / (away_length + 1)
		fixture_sample.append(entry)
	# L1_SHOTS_ON_AGAINST,
	fixture_sample.append(shots_on_against)
	# L5_SHOTS_ON_AGAINST,
	if away_length == 0:
		fixture_sample.append(shots_on_against)
	elif away_length < 5:
		prev_total = fixture_data[away][away_length - 1][SEASON_SHOTS_ON_AGAINST]
		entry = prev_total + shots_on_against
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[away][away_length - 1][L5_SHOTS_ON_AGAINST]
		l5_game = fixture_data[away][away_length - 5][L1_SHOTS_ON_AGAINST]
		entry = l5_total - l5_game + shots_on_against
		fixture_sample.append(entry)
	# L10_SHOTS_ON_AGAINST,
	if away_length == 0:
		fixture_sample.append(shots_on_against)
	elif away_length < 10:
		prev_total = fixture_data[away][away_length - 1][SEASON_SHOTS_ON_AGAINST]
		entry = prev_total + shots_on_against
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[away][away_length - 1][L10_SHOTS_ON_AGAINST]
		l10_game = fixture_data[away][away_length - 10][L1_SHOTS_ON_AGAINST]
		entry = l10_total - l10_game + shots_on_against
		fixture_sample.append(entry)
	# SEASON_SHOTS_ON_AGAINST,
	if away_length == 0:
		fixture_sample.append(shots_on_against)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_SHOTS_ON_AGAINST]
		entry = prev_total + shots_on_against
		fixture_sample.append(entry)

	# -- SHOTS OFF AGAINST --
	shots_off_against = row[SHOTS_HOME].value - row[SHOTS_TARGET_HOME].value
	# AVG_SHOTS_OFF_AGAINST,
	if away_length == 0:
		fixture_sample.append(shots_off_against)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_SHOTS_OFF_AGAINST]
		total = prev_total + shots_off_against
		entry = total / (away_length + 1)
		fixture_sample.append(entry)
	# L1_SHOTS_OFF_AGAINST,
	fixture_sample.append(shots_off_against)
	# L5_SHOTS_OFF_AGAINST,
	if away_length == 0:
		fixture_sample.append(shots_off_against)
	elif away_length < 5:
		prev_total = fixture_data[away][away_length - 1][SEASON_SHOTS_OFF_AGAINST]
		entry = prev_total + shots_off_against
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[away][away_length - 1][L5_SHOTS_OFF_AGAINST]
		l5_game = fixture_data[away][away_length - 5][L1_SHOTS_OFF_AGAINST]
		entry = l5_total - l5_game + shots_off_against
		fixture_sample.append(entry)
	# L10_SHOTS_OFF_AGAINST,
	if away_length == 0:
		fixture_sample.append(shots_off_against)
	elif away_length < 10:
		prev_total = fixture_data[away][away_length - 1][SEASON_SHOTS_OFF_AGAINST]
		entry = prev_total + shots_off_against
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[away][away_length - 1][L10_SHOTS_OFF_AGAINST]
		l10_game = fixture_data[away][away_length - 10][L1_SHOTS_OFF_AGAINST]
		entry = l10_total - l10_game + shots_off_against
		fixture_sample.append(entry)
	# SEASON_SHOTS_OFF_AGAINST,
	if away_length == 0:
		fixture_sample.append(shots_off_against)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_SHOTS_OFF_AGAINST]
		entry = prev_total + shots_off_against
		fixture_sample.append(entry)

	# -- CORNERS AGAINST --
	corners_against = row[CORNERS_HOME].value
	# AVG_CORNERS_AGAINST,
	if away_length == 0:
		fixture_sample.append(corners_against)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_CORNERS_AGAINST]
		total = prev_total + corners_against
		entry = total / (away_length + 1)
		fixture_sample.append(entry)
	# L1_CORNERS_AGAINST,
	fixture_sample.append(corners_against)
	# L5_CORNERS_AGAINST,
	if away_length == 0:
		fixture_sample.append(corners_against)
	elif away_length < 5:
		prev_total = fixture_data[away][away_length - 1][SEASON_CORNERS_AGAINST]
		entry = prev_total + corners_against
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[away][away_length - 1][L5_CORNERS_AGAINST]
		l5_game = fixture_data[away][away_length - 5][L1_CORNERS_AGAINST]
		entry = l5_total - l5_game + corners_against
		fixture_sample.append(entry)
	# L10_CORNERS_AGAINST,
	if away_length == 0:
		fixture_sample.append(corners_against)
	elif away_length < 10:
		prev_total = fixture_data[away][away_length - 1][SEASON_CORNERS_AGAINST]
		entry = prev_total + corners_against
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[away][away_length - 1][L10_CORNERS_AGAINST]
		l10_game = fixture_data[away][away_length - 10][L1_CORNERS_AGAINST]
		entry = l10_total - l10_game + corners_against
		fixture_sample.append(entry)
	# SEASON_CORNERS_AGAINST,
	if away_length == 0:
		fixture_sample.append(corners_against)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_CORNERS_AGAINST]
		entry = prev_total + corners_against
		fixture_sample.append(entry)

	# -- FOULS AGAINST --
	fouls_against = row[FOULS_HOME].value
	# AVG_FOULS_AGAINST,
	if away_length == 0:
		fixture_sample.append(fouls_against)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_FOULS_AGAINST]
		total = prev_total + fouls_against
		entry = total / (away_length + 1)
		fixture_sample.append(entry)
	# L1_FOULS_AGAINST,
	fixture_sample.append(fouls_against)
	# L5_FOULS_AGAINST,
	if away_length == 0:
		fixture_sample.append(fouls_against)
	elif away_length < 5:
		prev_total = fixture_data[away][away_length - 1][SEASON_FOULS_AGAINST]
		entry = prev_total + fouls_against
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[away][away_length - 1][L5_FOULS_AGAINST]
		l5_game = fixture_data[away][away_length - 5][L1_FOULS_AGAINST]
		entry = l5_total - l5_game + fouls_against
		fixture_sample.append(entry)
	# L10_FOULS_AGAINST,
	if away_length == 0:
		fixture_sample.append(fouls_against)
	elif away_length < 10:
		prev_total = fixture_data[away][away_length - 1][SEASON_FOULS_AGAINST]
		entry = prev_total + fouls_against
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[away][away_length - 1][L10_FOULS_AGAINST]
		l10_game = fixture_data[away][away_length - 10][L1_FOULS_AGAINST]
		entry = l10_total - l10_game + fouls_against
		fixture_sample.append(entry)
	# SEASON_FOULS_AGAINST,
	if away_length == 0:
		fixture_sample.append(fouls_against)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_FOULS_AGAINST]
		entry = prev_total + fouls_against
		fixture_sample.append(entry)

	# -- YELLOWS AGAINST --
	yellows_against = row[YELLOWS_HOME].value
	# AVG_YELLOWS_AGAINST,
	if away_length == 0:
		fixture_sample.append(yellows_against)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_YELLOWS_AGAINST]
		total = prev_total + yellows_against
		entry = total / (away_length + 1)
		fixture_sample.append(entry)
	# L1_YELLOWS_AGAINST,
	fixture_sample.append(yellows_against)
	# L5_YELLOWS_AGAINST,
	if away_length == 0:
		fixture_sample.append(yellows_against)
	elif away_length < 5:
		prev_total = fixture_data[away][away_length - 1][SEASON_YELLOWS_AGAINST]
		entry = prev_total + yellows_against
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[away][away_length - 1][L5_YELLOWS_AGAINST]
		l5_game = fixture_data[away][away_length - 5][L1_YELLOWS_AGAINST]
		entry = l5_total - l5_game + yellows_against
		fixture_sample.append(entry)
	# L10_YELLOWS_AGAINST,
	if away_length == 0:
		fixture_sample.append(yellows_against)
	elif away_length < 10:
		prev_total = fixture_data[away][away_length - 1][SEASON_YELLOWS_AGAINST]
		entry = prev_total + yellows_against
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[away][away_length - 1][L10_YELLOWS_AGAINST]
		l10_game = fixture_data[away][away_length - 10][L1_YELLOWS_AGAINST]
		entry = l10_total - l10_game + yellows_against
		fixture_sample.append(entry)
	# SEASON_YELLOWS_AGAINST,
	if away_length == 0:
		fixture_sample.append(yellows_against)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_YELLOWS_AGAINST]
		entry = prev_total + yellows_against
		fixture_sample.append(entry)

	# -- REDS AGAINST --
	reds_against = row[REDS_HOME].value
	# AVG_REDS_AGAINST,
	if away_length == 0:
		fixture_sample.append(reds_against)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_REDS_AGAINST]
		total = prev_total + reds_against
		entry = total / (away_length + 1)
		fixture_sample.append(entry)
	# L1_REDS_AGAINST,
	fixture_sample.append(reds_against)
	# L5_REDS_AGAINST,
	if away_length == 0:
		fixture_sample.append(reds_against)
	elif away_length < 5:
		prev_total = fixture_data[away][away_length - 1][SEASON_REDS_AGAINST]
		entry = prev_total + reds_against
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[away][away_length - 1][L5_REDS_AGAINST]
		l5_game = fixture_data[away][away_length - 5][L1_REDS_AGAINST]
		entry = l5_total - l5_game + reds_against
		fixture_sample.append(entry)
	# L10_REDS_AGAINST,
	if away_length == 0:
		fixture_sample.append(reds_against)
	elif away_length < 10:
		prev_total = fixture_data[away][away_length - 1][SEASON_REDS_AGAINST]
		entry = prev_total + reds_against
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[away][away_length - 1][L10_REDS_AGAINST]
		l10_game = fixture_data[away][away_length - 10][L1_REDS_AGAINST]
		entry = l10_total - l10_game + reds_against
		fixture_sample.append(entry)
	# SEASON_REDS_AGAINST,
	if away_length == 0:
		fixture_sample.append(reds_against)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_REDS_AGAINST]
		entry = prev_total + reds_against
		fixture_sample.append(entry)

	# -- FORM --
	if row[FT_RESULT].value == 'A':
		form = 3
	elif row[FT_RESULT].value == 'D':
		form = 1
	else:
		form = 0
	# AVG_FORM,
	if away_length == 0:
		fixture_sample.append(form)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_FORM]
		total = prev_total + form
		entry = total / (away_length + 1)
		fixture_sample.append(entry)
	# L1_FORM,
	fixture_sample.append(form)
	# L5_FORM,
	if away_length == 0:
		fixture_sample.append(form)
	elif away_length < 5:
		prev_total = fixture_data[away][away_length - 1][SEASON_FORM]
		entry = prev_total + form
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[away][away_length - 1][L5_FORM]
		l5_game = fixture_data[away][away_length - 5][L1_FORM]
		entry = l5_total - l5_game + form
		fixture_sample.append(entry)
	# L10_FORM,
	if away_length == 0:
		fixture_sample.append(form)
	elif away_length < 10:
		prev_total = fixture_data[away][away_length - 1][SEASON_FORM]
		entry = prev_total + form
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[away][away_length - 1][L10_FORM]
		l10_game = fixture_data[away][away_length - 10][L1_FORM]
		entry = l10_total - l10_game + form
		fixture_sample.append(entry)
	# SEASON_FORM,
	if away_length == 0:
		fixture_sample.append(form)
	else:
		prev_total = fixture_data[away][away_length - 1][SEASON_FORM]
		entry = prev_total + form
		fixture_sample.append(entry)

	# --- PERCENTAGE ---
	# TOTAL_WIN
	if away_length == 0:
		if form == 3:
			fixture_sample.append(1.0)
		else:
			fixture_sample.append(0.0)
	else:
		fixture = 0.0
		if form == 3:
			fixture = 1.0
		prev_total = fixture_data[away][away_length - 1][TOTAL_WIN]
		entry = prev_total + fixture
		fixture_sample.append(entry)
	# TOTAL_TIE
	if away_length == 0:
		if form == 1:
			fixture_sample.append(1.0)
		else:
			fixture_sample.append(0.0)
	else:
		fixture = 0.0
		if form == 1:
			fixture = 1.0
		prev_total = fixture_data[away][away_length - 1][TOTAL_TIE]
		entry = prev_total + fixture
		fixture_sample.append(entry)
	# TOTAL_LOSE
	if away_length == 0:
		if form == 0:
			fixture_sample.append(1.0)
		else:
			fixture_sample.append(0.0)
	else:
		fixture = 0.0
		if form == 0:
			fixture = 1.0
		prev_total = fixture_data[away][away_length - 1][TOTAL_LOSE]
		entry = prev_total + fixture
		fixture_sample.append(entry)
	# PERCENTAGE_WIN
	if away_length == 0:
		if form == 3:
			fixture_sample.append(1.0)
		else:
			fixture_sample.append(0.0)
	else:
		fixture = 0.0
		if form == 3:
			fixture = 1.0
		prev_total = fixture_data[away][away_length - 1][TOTAL_WIN]
		total = prev_total + fixture
		entry = total / (len(fixture_data[away]) + 1.0)
		fixture_sample.append(entry)
	# PERCENTAGE_TIE
	if away_length == 0:
		if form == 1:
			fixture_sample.append(1.0)
		else:
			fixture_sample.append(0.0)
	else:
		fixture = 0.0
		if form == 1:
			fixture = 1.0
		prev_total = fixture_data[away][away_length - 1][TOTAL_TIE]
		total = prev_total + fixture
		entry = total / (len(fixture_data[away]) + 1.0)
		fixture_sample.append(entry)
	# PERCENTAGE_LOSE
	if away_length == 0:
		if form == 0:
			fixture_sample.append(1.0)
		else:
			fixture_sample.append(0.0)
	else:
		fixture = 0.0
		if form == 0:
			fixture = 1.0
		prev_total = fixture_data[away][away_length - 1][TOTAL_LOSE]
		total = prev_total + fixture
		entry = total / (len(fixture_data[away]) + 1.0)
		fixture_sample.append(entry)

	# --- HOME ---
	fixture_sample.append(0)
	fixture_sample.append(game_ID)

	fixture_data[away].append(fixture_sample)
	# -----     ------
	game_ID += 1
	''' ===== ===== ===== ===== ===== '''

print fixture_data

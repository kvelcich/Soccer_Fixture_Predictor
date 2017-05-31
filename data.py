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

	# -- HALFTIME GOALS --
	goals_scored_ht = row[HT_GOALS_HOME].value
	# HOME_AVG_GOALS_HT,
	if home_length == 0:
		fixture_sample.append(goals_scored_ht)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_GOALS_HT]
		total = prev_total + goals_scored_ht
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# HOME_L1_GOALS_HT,
	fixture_sample.append(goals_scored_ht)
	# HOME_L5_GOALS_HT,
	if home_length == 0:
		fixture_sample.append(goals_scored_ht)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_GOALS_HT]
		entry = prev_total + goals_scored_ht
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][HOME_L5_GOALS_HT]
		l5_game = fixture_data[home][home_length - 5][HOME_L1_GOALS_HT]
		entry = l5_total - l5_game + goals_scored_ht
		fixture_sample.append(entry)
	# HOME_L10_GOALS_HT,
	if home_length == 0:
		fixture_sample.append(goals_scored_ht)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_GOALS_HT]
		entry = prev_total + goals_scored_ht
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][HOME_L10_GOALS_HT]
		l10_game = fixture_data[home][home_length - 10][HOME_L1_GOALS_HT]
		entry = l10_total - l10_game + goals_scored_ht
		fixture_sample.append(entry)
	# HOME_SEASON_GOALS_HT,
	if home_length == 0:
		fixture_sample.append(goals_scored_ht)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_GOALS_HT]
		entry = prev_total + goals_scored_ht
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

	# -- YELLOWS --
	yellows = row[YELLOWS_HOME].value
	# HOME_AVG_YELLOWS,
	if home_length == 0:
		fixture_sample.append(yellows)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_YELLOWS]
		total = prev_total + yellows
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# HOME_L1_YELLOWS,
	fixture_sample.append(yellows)
	# HOME_L5_YELLOWS,
	if home_length == 0:
		fixture_sample.append(yellows)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_YELLOWS]
		entry = prev_total + yellows
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][HOME_L5_YELLOWS]
		l5_game = fixture_data[home][home_length - 5][HOME_L1_YELLOWS]
		entry = l5_total - l5_game + yellows
		fixture_sample.append(entry)
	# HOME_L10_YELLOWS,
	if home_length == 0:
		fixture_sample.append(yellows)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_YELLOWS]
		entry = prev_total + yellows
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][HOME_L10_YELLOWS]
		l10_game = fixture_data[home][home_length - 10][HOME_L1_YELLOWS]
		entry = l10_total - l10_game + yellows
		fixture_sample.append(entry)
	# HOME_SEASON_YELLOWS,
	if home_length == 0:
		fixture_sample.append(yellows)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_YELLOWS]
		entry = prev_total + yellows
		fixture_sample.append(entry)

	# -- REDS --
	reds = row[REDS_HOME].value
	# HOME_AVG_REDS,
	if home_length == 0:
		fixture_sample.append(reds)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_REDS]
		total = prev_total + reds
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# HOME_L1_REDS,
	fixture_sample.append(reds)
	# HOME_L5_REDS,
	if home_length == 0:
		fixture_sample.append(reds)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_REDS]
		entry = prev_total + reds
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][HOME_L5_REDS]
		l5_game = fixture_data[home][home_length - 5][HOME_L1_REDS]
		entry = l5_total - l5_game + reds
		fixture_sample.append(entry)
	# HOME_L10_REDS,
	if home_length == 0:
		fixture_sample.append(reds)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_REDS]
		entry = prev_total + reds
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][HOME_L10_REDS]
		l10_game = fixture_data[home][home_length - 10][HOME_L1_REDS]
		entry = l10_total - l10_game + reds
		fixture_sample.append(entry)
	# HOME_SEASON_REDS,
	if home_length == 0:
		fixture_sample.append(reds)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_REDS]
		entry = prev_total + reds
		fixture_sample.append(entry)

	# -- GOALS AGAINST --
	goals_scored_against = row[FT_GOALS_AWAY].value
	# HOME_AVG_GOALS_AGAINST,
	if home_length == 0:
		fixture_sample.append(goals_scored_against)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_GOALS_AGAINST]
		total = prev_total + goals_scored_against
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# HOME_L1_GOALS_AGAINST,
	fixture_sample.append(goals_scored_against)
	# HOME_L5_GOALS_AGAINST,
	if home_length == 0:
		fixture_sample.append(goals_scored_against)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_GOALS_AGAINST]
		entry = prev_total + goals_scored_against
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][HOME_L5_GOALS_AGAINST]
		l5_game = fixture_data[home][home_length - 5][HOME_L1_GOALS_AGAINST]
		entry = l5_total - l5_game + goals_scored_against
		fixture_sample.append(entry)
	# HOME_L10_GOALS_AGAINST,
	if home_length == 0:
		fixture_sample.append(goals_scored_against)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_GOALS_AGAINST]
		entry = prev_total + goals_scored_against
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][HOME_L10_GOALS_AGAINST]
		l10_game = fixture_data[home][home_length - 10][HOME_L1_GOALS_AGAINST]
		entry = l10_total - l10_game + goals_scored_against
		fixture_sample.append(entry)
	# HOME_SEASON_GOALS_AGAINST,
	if home_length == 0:
		fixture_sample.append(goals_scored_against)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_GOALS_AGAINST]
		entry = prev_total + goals_scored_against
		fixture_sample.append(entry)

	# -- SHOTS ON AGAINST --
	shots_on_against = row[SHOTS_TARGET_AWAY].value
	# HOME_AVG_SHOTS_ON_AGAINST,
	if home_length == 0:
		fixture_sample.append(shots_on_against)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_SHOTS_ON_AGAINST]
		total = prev_total + shots_on_against
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# HOME_L1_SHOTS_ON_AGAINST,
	fixture_sample.append(shots_on_against)
	# HOME_L5_SHOTS_ON_AGAINST,
	if home_length == 0:
		fixture_sample.append(shots_on_against)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_SHOTS_ON_AGAINST]
		entry = prev_total + shots_on_against
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][HOME_L5_SHOTS_ON_AGAINST]
		l5_game = fixture_data[home][home_length - 5][HOME_L1_SHOTS_ON_AGAINST]
		entry = l5_total - l5_game + shots_on_against
		fixture_sample.append(entry)
	# HOME_L10_SHOTS_ON_AGAINST,
	if home_length == 0:
		fixture_sample.append(shots_on_against)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_SHOTS_ON_AGAINST]
		entry = prev_total + shots_on_against
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][HOME_L10_SHOTS_ON_AGAINST]
		l10_game = fixture_data[home][home_length - 10][HOME_L1_SHOTS_ON_AGAINST]
		entry = l10_total - l10_game + shots_on_against
		fixture_sample.append(entry)
	# HOME_SEASON_SHOTS_ON_AGAINST,
	if home_length == 0:
		fixture_sample.append(shots_on_against)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_SHOTS_ON_AGAINST]
		entry = prev_total + shots_on_against
		fixture_sample.append(entry)

	# -- SHOTS OFF AGAINST --
	shots_off_against = row[SHOTS_AWAY].value - row[SHOTS_TARGET_AWAY].value
	# HOME_AVG_SHOTS_OFF_AGAINST,
	if home_length == 0:
		fixture_sample.append(shots_off_against)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_SHOTS_OFF_AGAINST]
		total = prev_total + shots_off_against
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# HOME_L1_SHOTS_OFF_AGAINST,
	fixture_sample.append(shots_off_against)
	# HOME_L5_SHOTS_OFF_AGAINST,
	if home_length == 0:
		fixture_sample.append(shots_off_against)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_SHOTS_OFF_AGAINST]
		entry = prev_total + shots_off_against
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][HOME_L5_SHOTS_OFF_AGAINST]
		l5_game = fixture_data[home][home_length - 5][HOME_L1_SHOTS_OFF_AGAINST]
		entry = l5_total - l5_game + shots_off_against
		fixture_sample.append(entry)
	# HOME_L10_SHOTS_OFF_AGAINST,
	if home_length == 0:
		fixture_sample.append(shots_off_against)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_SHOTS_OFF_AGAINST]
		entry = prev_total + shots_off_against
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][HOME_L10_SHOTS_OFF_AGAINST]
		l10_game = fixture_data[home][home_length - 10][HOME_L1_SHOTS_OFF_AGAINST]
		entry = l10_total - l10_game + shots_off_against
		fixture_sample.append(entry)
	# HOME_SEASON_SHOTS_OFF_AGAINST,
	if home_length == 0:
		fixture_sample.append(shots_off_against)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_SHOTS_OFF_AGAINST]
		entry = prev_total + shots_off_against
		fixture_sample.append(entry)

	# -- CORNERS AGAINST --
	corners_against = row[CORNERS_AWAY].value
	# HOME_AVG_CORNERS_AGAINST,
	if home_length == 0:
		fixture_sample.append(corners_against)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_CORNERS_AGAINST]
		total = prev_total + corners_against
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# HOME_L1_CORNERS_AGAINST,
	fixture_sample.append(corners_against)
	# HOME_L5_CORNERS_AGAINST,
	if home_length == 0:
		fixture_sample.append(corners_against)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_CORNERS_AGAINST]
		entry = prev_total + corners_against
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][HOME_L5_CORNERS_AGAINST]
		l5_game = fixture_data[home][home_length - 5][HOME_L1_CORNERS_AGAINST]
		entry = l5_total - l5_game + corners_against
		fixture_sample.append(entry)
	# HOME_L10_CORNERS_AGAINST,
	if home_length == 0:
		fixture_sample.append(corners_against)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_CORNERS_AGAINST]
		entry = prev_total + corners_against
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][HOME_L10_CORNERS_AGAINST]
		l10_game = fixture_data[home][home_length - 10][HOME_L1_CORNERS_AGAINST]
		entry = l10_total - l10_game + corners_against
		fixture_sample.append(entry)
	# HOME_SEASON_CORNERS_AGAINST,
	if home_length == 0:
		fixture_sample.append(corners_against)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_CORNERS_AGAINST]
		entry = prev_total + corners_against
		fixture_sample.append(entry)

	# -- FOULS AGAINST --
	fouls_against = row[FOULS_AWAY].value
	# HOME_AVG_FOULS_AGAINST,
	if home_length == 0:
		fixture_sample.append(fouls_against)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_FOULS_AGAINST]
		total = prev_total + fouls_against
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# HOME_L1_FOULS_AGAINST,
	fixture_sample.append(fouls_against)
	# HOME_L5_FOULS_AGAINST,
	if home_length == 0:
		fixture_sample.append(fouls_against)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_FOULS_AGAINST]
		entry = prev_total + fouls_against
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][HOME_L5_FOULS_AGAINST]
		l5_game = fixture_data[home][home_length - 5][HOME_L1_FOULS_AGAINST]
		entry = l5_total - l5_game + fouls_against
		fixture_sample.append(entry)
	# HOME_L10_FOULS_AGAINST,
	if home_length == 0:
		fixture_sample.append(fouls_against)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_FOULS_AGAINST]
		entry = prev_total + fouls_against
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][HOME_L10_FOULS_AGAINST]
		l10_game = fixture_data[home][home_length - 10][HOME_L1_FOULS_AGAINST]
		entry = l10_total - l10_game + fouls_against
		fixture_sample.append(entry)
	# HOME_SEASON_FOULS_AGAINST,
	if home_length == 0:
		fixture_sample.append(fouls_against)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_FOULS_AGAINST]
		entry = prev_total + fouls_against
		fixture_sample.append(entry)

	# -- YELLOWS AGAINST --
	yellows_against = row[YELLOWS_AWAY].value
	# HOME_AVG_YELLOWS_AGAINST,
	if home_length == 0:
		fixture_sample.append(yellows_against)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_YELLOWS_AGAINST]
		total = prev_total + yellows_against
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# HOME_L1_YELLOWS_AGAINST,
	fixture_sample.append(yellows_against)
	# HOME_L5_YELLOWS_AGAINST,
	if home_length == 0:
		fixture_sample.append(yellows_against)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_YELLOWS_AGAINST]
		entry = prev_total + yellows_against
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][HOME_L5_YELLOWS_AGAINST]
		l5_game = fixture_data[home][home_length - 5][HOME_L1_YELLOWS_AGAINST]
		entry = l5_total - l5_game + yellows_against
		fixture_sample.append(entry)
	# HOME_L10_YELLOWS_AGAINST,
	if home_length == 0:
		fixture_sample.append(yellows_against)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_YELLOWS_AGAINST]
		entry = prev_total + yellows_against
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][HOME_L10_YELLOWS_AGAINST]
		l10_game = fixture_data[home][home_length - 10][HOME_L1_YELLOWS_AGAINST]
		entry = l10_total - l10_game + yellows_against
		fixture_sample.append(entry)
	# HOME_SEASON_YELLOWS_AGAINST,
	if home_length == 0:
		fixture_sample.append(yellows_against)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_YELLOWS_AGAINST]
		entry = prev_total + yellows_against
		fixture_sample.append(entry)

	# -- REDS AGAINST --
	reds_against = row[REDS_AWAY].value
	# HOME_AVG_REDS_AGAINST,
	if home_length == 0:
		fixture_sample.append(reds_against)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_REDS_AGAINST]
		total = prev_total + reds_against
		entry = total / (home_length + 1)
		fixture_sample.append(entry)
	# HOME_L1_REDS_AGAINST,
	fixture_sample.append(reds_against)
	# HOME_L5_REDS_AGAINST,
	if home_length == 0:
		fixture_sample.append(reds_against)
	elif home_length < 5:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_REDS_AGAINST]
		entry = prev_total + reds_against
		fixture_sample.append(entry)
	else:
		l5_total = fixture_data[home][home_length - 1][HOME_L5_REDS_AGAINST]
		l5_game = fixture_data[home][home_length - 5][HOME_L1_REDS_AGAINST]
		entry = l5_total - l5_game + reds_against
		fixture_sample.append(entry)
	# HOME_L10_REDS_AGAINST,
	if home_length == 0:
		fixture_sample.append(reds_against)
	elif home_length < 10:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_REDS_AGAINST]
		entry = prev_total + reds_against
		fixture_sample.append(entry)
	else:
		l10_total = fixture_data[home][home_length - 1][HOME_L10_REDS_AGAINST]
		l10_game = fixture_data[home][home_length - 10][HOME_L1_REDS_AGAINST]
		entry = l10_total - l10_game + reds_against
		fixture_sample.append(entry)
	# HOME_SEASON_REDS_AGAINST,
	if home_length == 0:
		fixture_sample.append(reds_against)
	else:
		prev_total = fixture_data[home][home_length - 1][HOME_SEASON_REDS_AGAINST]
		entry = prev_total + reds_against
		fixture_sample.append(entry)

	''' ===== ===== ===== ===== ===== '''

	print idx, ' ', fixture_sample
	print ''
	fixture_data[home].append(fixture_sample)

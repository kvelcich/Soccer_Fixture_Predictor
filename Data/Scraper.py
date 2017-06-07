import xlrd
from xlrd.sheet import ctype_text
from data_calculation import *
from Data.Spreadsheets import List

''' Excel Spreadsheet '''
TEAM_HOME = 2
TEAM_AWAY = 3
FT_GOALS_HOME = 4
FT_GOALS_AWAY = 5
FT_RESULT = 6
HT_GOALS_HOME = 7
HT_GOALS_AWAY = 8
HT_RESULT = 9
SHOTS_HOME = 11
SHOTS_AWAY = 12
SHOTS_TARGET_HOME = 13
SHOTS_TARGET_AWAY = 14
FOULS_HOME = 15
FOULS_AWAY = 16
CORNERS_HOME = 17
CORNERS_AWAY = 18
YELLOWS_HOME = 19
YELLOWS_AWAY = 20
REDS_HOME = 21
REDS_AWAY = 22

"""
Scraping Data
"""
def scrape(file):
	''' Variable list: '''
	team_IDs = []
	fixture_data = []
	game_ID = 1
	game_list = []
	match_data = []

	data = xlrd.open_workbook(file)

	for sheet_name in List.leagues:
		sheet = data.sheet_by_name(sheet_name)
		print sheet_name

		row = sheet.row(0)
		count = 0
		for col_idx in range(sheet.ncols):
			if row[col_idx].value == 'HomeTeam':
				TEAM_HOME = col_idx
				count += 1
			elif row[col_idx].value == 'AwayTeam':
				TEAM_AWAY = col_idx
				count += 1
			elif row[col_idx].value == 'FTHG':
				FT_GOALS_HOME = col_idx
				count += 1
			elif row[col_idx].value == 'FTAG':
				FT_GOALS_AWAY = col_idx
				count += 1
			elif row[col_idx].value == 'FTR':
				FT_RESULT = col_idx
				count += 1
			elif row[col_idx].value == 'HTHG':
				HT_GOALS_HOME = col_idx
				count += 1
			elif row[col_idx].value == 'HTAG':
				HT_GOALS_AWAY = col_idx
				count += 1
			elif row[col_idx].value == 'HTR':
				HT_RESULT = col_idx
				count += 1
			elif row[col_idx].value == 'HS':
				SHOTS_HOME = col_idx
				count += 1
			elif row[col_idx].value == 'AS':
				SHOTS_AWAY = col_idx
				count += 1
			elif row[col_idx].value == 'HST':
				SHOTS_TARGET_HOME = col_idx
				count += 1
			elif row[col_idx].value == 'AST':
				SHOTS_TARGET_AWAY = col_idx
				count += 1
			elif row[col_idx].value == 'HF':
				FOULS_HOME = col_idx
				count += 1
			elif row[col_idx].value == 'AF':
				FOULS_AWAY = col_idx
				count += 1
			elif row[col_idx].value == 'HC':
				CORNERS_HOME = col_idx
				count += 1
			elif row[col_idx].value == 'AC':
				CORNERS_AWAY = col_idx
				count += 1
			elif row[col_idx].value == 'HY':
				YELLOWS_HOME = col_idx
				count += 1
			elif row[col_idx].value == 'AY':
				YELLOWS_AWAY = col_idx
				count += 1
			elif row[col_idx].value == 'HR':
				REDS_HOME = col_idx
				count += 1
			elif row[col_idx].value == 'AR':
				REDS_AWAY = col_idx
				count += 1
		if count != 20:
			print 'Error could not find all attributes'
			continue


		for idx, row_idx in enumerate(range(1, sheet.nrows)):
			row = sheet.row(row_idx)

			''' For every game, do the following... '''
			fixture_sample = []

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

			if len(fixture_data[home]) and len(fixture_data[away]) >= 5:
				home_game = fixture_data[home][-1]
				home_game[-2] = 1.0
				home_game.append(row[FT_GOALS_HOME].value)
				away_game = fixture_data[away][-1]
				away_game[-2] = 0.0
				away_game.append(row[FT_GOALS_AWAY].value)

				match_data.append(home_game)
				match_data.append(away_game)


			fixture_data[home].append(extract_data_home(fixture_data, home, row, game_ID, TEAM_HOME, TEAM_AWAY, FT_GOALS_HOME, FT_GOALS_AWAY, FT_RESULT, HT_GOALS_HOME, HT_GOALS_AWAY, HT_RESULT, SHOTS_HOME, SHOTS_AWAY, SHOTS_TARGET_HOME, SHOTS_TARGET_AWAY, FOULS_HOME, FOULS_AWAY, CORNERS_HOME, CORNERS_AWAY, YELLOWS_HOME, YELLOWS_AWAY, REDS_HOME, REDS_AWAY))
			fixture_data[away].append(extract_data_away(fixture_data, away, row, game_ID, TEAM_HOME, TEAM_AWAY, FT_GOALS_HOME, FT_GOALS_AWAY, FT_RESULT, HT_GOALS_HOME, HT_GOALS_AWAY, HT_RESULT, SHOTS_HOME, SHOTS_AWAY, SHOTS_TARGET_HOME, SHOTS_TARGET_AWAY, FOULS_HOME, FOULS_AWAY, CORNERS_HOME, CORNERS_AWAY, YELLOWS_HOME, YELLOWS_AWAY, REDS_HOME, REDS_AWAY))

			game_ID += 1
	return match_data

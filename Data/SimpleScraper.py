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

"""
Scraping Data
"""
def scrape(file):
	''' Variable list: '''
	team_IDs = []
	fixture_data = []
	game_ID = 1
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
		if count != 5:
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

			if row[FT_GOALS_HOME].value == '':
				continue

			if len(fixture_data[home]) and len(fixture_data[away]) >= 5:
				home_game = fixture_data[home][-1]
				home_game.append(row[FT_GOALS_HOME].value)
				away_game = fixture_data[away][-1]
				away_game.append(row[FT_GOALS_AWAY].value)

				match_data.append(home_game)
				match_data.append(away_game)

			fixture_data[home].append(simple_extract_data_home(fixture_data, home, row, game_ID, TEAM_HOME, TEAM_AWAY, FT_GOALS_HOME, FT_GOALS_AWAY, FT_RESULT))
			fixture_data[away].append(simple_extract_data_away(fixture_data, away, row, game_ID, TEAM_HOME, TEAM_AWAY, FT_GOALS_HOME, FT_GOALS_AWAY, FT_RESULT))

			game_ID += 1
	return match_data

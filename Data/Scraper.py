import xlrd
from xlrd.sheet import ctype_text
from data_calculation import *

"""
Scraping Data
"""
def scrape(file):
	''' Variable list: '''
	team_IDs = []
	fixture_data = []
	game_ID = 1
	game_list = []

	data = xlrd.open_workbook(file)
	sheet = data.sheet_by_index(0)

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

		fixture_data[home].append(extract_data_home(fixture_data, home, row, game_ID))
		fixture_data[away].append(extract_data_away(fixture_data, away, row, game_ID))

		game_ID += 1

	return fixture_data

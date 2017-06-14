import numpy
from Data import table

def simple_reduction(data):
	del data[13]
	del data[3]
	del data[2]
	del data[1]
	del data[0]
	a=1

def reduce_params(data):
	del data[table.GOALS]
	del data[table.GAME_ID]

	del data[table.HOME]

	del data[table.TOTAL_LOSE]
	del data[table.TOTAL_TIE]
	del data[table.TOTAL_WIN]

	del data[table.SEASON_FORM]

	del data[table.SEASON_REDS_AGAINST]
	del data[table.L10_REDS_AGAINST]
	del data[table.L5_REDS_AGAINST]
	del data[table.L1_REDS_AGAINST]
	del data[table.AVG_REDS_AGAINST]

	del data[table.SEASON_YELLOWS_AGAINST]
	del data[table.L10_YELLOWS_AGAINST]
	del data[table.L5_YELLOWS_AGAINST]
	del data[table.L1_YELLOWS_AGAINST]
	del data[table.AVG_YELLOWS_AGAINST]

	del data[table.SEASON_FOULS_AGAINST]
	del data[table.L10_FOULS_AGAINST]
	del data[table.L5_FOULS_AGAINST]
	del data[table.L1_FOULS_AGAINST]
	del data[table.AVG_FOULS_AGAINST]

	del data[table.SEASON_CORNERS_AGAINST]
	del data[table.L10_CORNERS_AGAINST]
	# del data[table.L5_CORNERS_AGAINST]
	# del data[table.L1_CORNERS_AGAINST]
	# del data[table.AVG_CORNERS_AGAINST]

	del data[table.SEASON_SHOTS_OFF_AGAINST]
	del data[table.L10_SHOTS_OFF_AGAINST]
	# del data[table.L5_SHOTS_OFF_AGAINST]
	# del data[table.L1_SHOTS_OFF_AGAINST]
	# del data[table.AVG_SHOTS_OFF_AGAINST]

	del data[table.SEASON_SHOTS_ON_AGAINST]
	del data[table.L10_SHOTS_ON_AGAINST]

	del data[table.SEASON_GOALS_HT_AGAINST]
	del data[table.L10_GOALS_HT_AGAINST]
	# del data[table.L5_GOALS_HT_AGAINST]
	# del data[table.L1_GOALS_HT_AGAINST]
	# del data[table.AVG_GOALS_HT_AGAINST]

	del data[table.SEASON_GOALS_AGAINST]
	del data[table.L10_GOALS_AGAINST]

	del data[table.SEASON_REDS]
	del data[table.L10_REDS]
	del data[table.L5_REDS]
	del data[table.L1_REDS]
	del data[table.AVG_REDS]

	del data[table.SEASON_YELLOWS]
	del data[table.L10_YELLOWS]
	del data[table.L5_YELLOWS]
	del data[table.L1_YELLOWS]
	del data[table.AVG_YELLOWS]

	del data[table.SEASON_FOULS]
	del data[table.L10_FOULS]
	del data[table.L5_FOULS]
	del data[table.L1_FOULS]
	del data[table.AVG_FOULS]

	del data[table.SEASON_CORNERS]
	del data[table.L10_CORNERS]
	# del data[table.L5_CORNERS]
	# del data[table.L1_CORNERS]
	# del data[table.AVG_CORNERS]

	del data[table.SEASON_SHOTS_OFF]
	del data[table.L10_SHOTS_OFF]
	# del data[table.L5_SHOTS_OFF]
	# del data[table.L1_SHOTS_OFF]
	# del data[table.AVG_SHOTS_OFF]

	del data[table.SEASON_SHOTS_ON]
	del data[table.L10_SHOTS_ON]

	del data[table.SEASON_GOALS_HT]
	del data[table.L10_GOALS_HT]
	# del data[table.L5_GOALS_HT]
	# del data[table.L1_GOALS_HT]
	# del data[table.AVG_GOALS_HT]

	del data[table.SEASON_GOALS]
	del data[table.L10_GOALS]

	del data[table.ID]

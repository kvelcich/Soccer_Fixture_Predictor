def fill(data, param, L1, L5_IDX, L10_IDX, TOTAL):
	entry = []

	entry.append(AVG(data, param, TOTAL))
	entry.append(param)
	entry.append(L5(data, param, TOTAL, L5_IDX, L1))
	entry.append(L10(data, param, TOTAL, L10_IDX, L1))
	entry.append(SEASON(data, param, TOTAL))

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

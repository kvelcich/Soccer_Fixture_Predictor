def calc_error(prediction, actual):
	correct = 0
	for i in range(0, len(actual), 2):
		difference = prediction[i] - prediction[i + 1]

		if difference > 0:
			if actual[i] > actual[i + 1]:
				correct += 1
		elif difference < 0:
			if actual[i] < actual[i + 1]:
				correct += 1

	return correct * 1.0 / (len(actual) / 2)

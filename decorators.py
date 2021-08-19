def analizer(function):
	def wrapper(moko, *args, **kwargs):
		print(moko['first_name'])
		print(moko['last_name'])

		return function(moko)

	return wrapper
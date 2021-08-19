from decorators import *

@analizer
def ModifyPerson(person):

	result = person['first_name'] + " " + person['last_name']
	return result

Person = {
	'first_name': 	'Silvio',
	'last_name'	: 	'Molina'
}

print(ModifyPerson(Person))
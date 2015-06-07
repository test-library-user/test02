class Pidgey(object) :
	
	def __init__(self, name) :
		self.name = name
		
	level = 7
	
	attributes = {
					'attack' : 11,
					'defense' : 8,
					'speed' : 14
				  }
	modifiers = {
					'attack' : 1.15,
					'defense' : 1.12,
					'speed' : 1.37
				}
				  
def level_up(pokemon) :
	pokemon.level += 1
	print '%s rises to level %i!' % (pokemon.name, pokemon.level)
	for each in pokemon.attributes :
		pokemon.attributes[each] += pokemon.modifiers[each] * pokemon.level - pokemon.level
		print each, pokemon.attributes[each]
	
	
bill = Pidgey('Bill')

print bill.level
print bill.attributes['attack']




	
level_up(bill)
level_up(bill)
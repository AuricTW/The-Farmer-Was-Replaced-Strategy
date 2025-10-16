import move_to 
import Farmer 
Farmer.till_soil()

x = 0

while True:
		use_item(Items.Fertilizer)
		for i in range(get_world_size()):
			for j in range(get_world_size()):
			
				if can_harvest():
					x = x + 1
				else:
					plant(Entities.Pumpkin)
					x = 0 #正常設0穩定
				if x >= 256:
					break
				move(East)
			move(North)
	
	
				
	if x >= 64:
		move_to.to_origin()
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if can_harvest():
					harvest()
				plant(Entities.Pumpkin)
				move(East)
			move(North)

from typing import List

class Fountain:
    def spray_water(self) -> None:
        pass
    
class SimpleFountain(Fountain):
    def spray_water(self) -> None:
        print("Вода просто идет из фонтана")

class MusicalFountain(Fountain):
    def spray_water(self) -> None:
        print("Вода из фонтана идет с музыкальным сопровождением")

class LightedFountain(Fountain):
    def spray_water(self) -> None:
        print("Вода из фонтана идет со световым сопровождением")

fountain_list: List[Fountain] = []
simple_fountain = SimpleFountain()
musical_fountain = MusicalFountain()
lighted_fountain = LightedFountain()

[fountain_list.append(element) for element in [simple_fountain, musical_fountain, lighted_fountain]]

for fountain_i in fountain_list:
    fountain_i.spray_water()
from Space.planet import Planet
from Space.calc import planet_mass, planet_vol

obj = Planet("rain",22,0.6,8.1,'CSGO')
print(planet_mass(obj.gravity, obj.radius))
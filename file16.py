class Planet:

    height = '1.85 m'

    def __init__(self, name, age,radius, gravity,system) -> None:
        self.name=name
        self.age=age
        self.radius=radius
        self.gravity=gravity
        self.system=system

    def orbit (self):
        return (f'{self.name} is oribiting in {self.system}')

    @classmethod
    def commons(cls):
        return f'All versions of me have height of {cls.height}'

    @staticmethod
    def walk(speed='40km/h'):
        return f'My avg speed is {speed}'

obj = Planet("rain",22,0.6,8.1,'CSGO')
print(f'Name is {obj.name}')
print(f'Age is {obj.age}')
print(f'Radius is {obj.radius}')
print(f'Gravoty is {obj.gravity}')
print(f'System is {obj.system}')
print(obj.orbit())


print('----------------------')
obj2 = Planet('mitchell',15,0.8,8.1,"Lycée")
print(f'Name is {obj2.name}')
print(f'Age is {obj2.age}')
print(f'Radius is {obj2.radius}')
print(f'Gravoty is {obj2.gravity}')
print(f'System is {obj2.system}')
print(obj2.orbit())

print(Planet.height)
print(Planet.commons())
print(Planet.walk('41km/h'))
print(obj2.walk())
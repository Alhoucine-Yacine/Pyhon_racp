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


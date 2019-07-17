class Space:

    location = 'off the world'
    speed = 'very fast'

    def size(self):
        return "big"

    def gravity():
        return "exists"

    def see(self):
        return "use a telescope"


stars = Space()
planets = Space()
moons = Space()

print(stars.size())
print(moons.see())
print(Space.gravity())

planets.location = 'in space and under your feet'

print(planets.location)
print(stars.location)
Space.location = "everywhere"
print(planets.location)
print(stars.location)

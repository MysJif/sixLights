from lights import Lights

lights = Lights()

lights.setPuzzle([[0], [1, 4], [0, 2], [3, 4], [1, 2], [4, 5]])

lights.pressButton(5)
lights.pressButton(3)
lights.pressButton(1)
lights.pressButton(2)
print (lights.checkLights())

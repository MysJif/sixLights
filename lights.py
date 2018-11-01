class Lights:
    def __init__(self, lights = [False, False, False, False, False, False], buttons = [[0], [1], [2], [3], [4], [5]]):
        self.lights = lights
        self.buttons = buttons

    def setPuzzle(self, buttons):
        self.buttons = buttons

    def pressButton(self, button):
        for light in self.buttons[button]:
            self.lights[light] = not self.lights[light]

    def checkLights(self):
        result = ""
        for light in self.lights:
            if light:
                result = result + "[■] "
            else:
                result = result + "[□] "

        return result

    def checkSolution(self):
        for light in self.lights:
            if light:
                continue
            else:
                return False
        return True
    

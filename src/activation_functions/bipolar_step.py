from .activation_function import ActivationFunction

class BipolarStep(ActivationFunction):
    def calculate(self, signal: float) -> float:
        return 1 if signal > 0 else -1
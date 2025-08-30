class Calculator():
    def __init__(self, performance: float, performance_hit: float, number_of_steps: int) -> None:
        self.performance = performance
        self.performance_hit = performance_hit
        self.number_of_steps = number_of_steps

    def calculate_decrease(self) -> float:
        self.performance_level = self.performance
        for step in range(self.number_of_steps):
            self.new_performance = self.performance_level - (self.performance_level * self.performance_hit)
            self.performance_level = self.new_performance
        
        return self.performance_level
    
newcalc = Calculator(100, 0.05, 5)

print(newcalc.calculate_decrease())



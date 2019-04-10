class School:
    def __init__(self, name):
        self.name = name
        self.roster_d = {}
        
        
    def roster(self):
        return self.roster_d
    
    
    def add_student(self, name, grade_input):
        if grade_input not in self.roster_d.keys():
            self.roster_d[grade_input] = []
        self.roster_d[grade_input].append(name)
        
    def grade(self, grade_input):
        return self.roster_d[grade_input]
    
    def sort_roster(self):
        self.roster_d = {key : sorted(value)  for (key, value) in self.roster_d.items() }
        print(self.roster_d)
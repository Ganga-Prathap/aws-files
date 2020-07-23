{"filter":false,"title":"business_developer.py","tooltip":"/clean_architecture/clean_architecture_resources/source_code_dependency_inversion_example/employees/business_developer.py","undoManager":{"mark":7,"position":7,"stack":[[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":1},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":1,"column":0},"end":{"row":17,"column":27},"action":"insert","lines":["from source_code_dependency_inversion_example.calculate_pay.employee_interface\\","    import EmployeeInterface","","","class Designer(EmployeeInterface):","    def __init__(self, name: str, age: int, base_salary: int):","        self.name = name","        self.age = age","        self.base_salary = base_salary","","    def _get_designer_bonus(self):","        return 5000","","    def get_total_salary(self):","        total_salary = self.base_salary + self._get_designer_bonus()","        print('{} - Designer: {}'.format(self.name, total_salary))","        return total_salary"],"id":2}],[{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"remove","lines":["r"],"id":3},{"start":{"row":5,"column":12},"end":{"row":5,"column":13},"action":"remove","lines":["e"]},{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"remove","lines":["n"]},{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"remove","lines":["g"]},{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"remove","lines":["i"]},{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"remove","lines":["s"]},{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"remove","lines":["e"]},{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"remove","lines":["D"]}],[{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":["B"],"id":4}],[{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"remove","lines":["B"],"id":5},{"start":{"row":5,"column":6},"end":{"row":5,"column":23},"action":"insert","lines":["BusinessDeveloper"]}],[{"start":{"row":12,"column":15},"end":{"row":12,"column":16},"action":"remove","lines":["5"],"id":6}],[{"start":{"row":12,"column":15},"end":{"row":12,"column":16},"action":"insert","lines":["4"],"id":7}],[{"start":{"row":16,"column":20},"end":{"row":16,"column":28},"action":"remove","lines":["Designer"],"id":8},{"start":{"row":16,"column":20},"end":{"row":16,"column":37},"action":"insert","lines":["BusinessDeveloper"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":18,"column":0},"end":{"row":18,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1589541680508,"hash":"8d6345aa998d0bee7fdd4ca29090f46cdeb9ce2b"}
# employees = {}

# employees["Karl"] = 12
# employees["Emma"] = 8
# print(employees)


# def add_employee(lst: dict, name: str, hours: int) -> dict:
#     lst[name]= hours
#     return lst

# def prompt_employee (lst: dict ) -> dict: 
#     name = input ("Name: ")
#     hours = int (input ("hours: "))
#     lst = add_employee(lst , name, hours)
#     return lst


# def more_employees ()-> dict:
#     keep_gooing = True
#     lst = {}
#     while keep_gooing:
#         lst = prompt_employee (lst) 
#         user_input = input ("Another? Y/N ")
#         if user_input != "Y" :
#             keep_gooing = False
#     return lst

# x = more_employees ()
# print(x)


class Database:
    employees: dict = {}
    tip_db : dict = {} 
    total_hours: int = 0
    tips: float = 0.0
    def __init__(self) -> None:
        pass

    def add_employee (self, name: str, hours: int):
        self.employees[name]= hours
        self.tip_db[name ]= 0
        self.total_hours+= hours

    
    def prompt_employee (self):
        name = input ("| Employee Name: ")
        s = input ("| Work Hours: ")
        if s.isnumeric() :
            print("| ")
            hours = int(s)
            self.add_employee(name, hours)
        else :
            print("| Please Enter a Numbers!")
            self.prompt_employee()

    def more_employee (self):
        keep_gooing = True
        while keep_gooing:
            self.prompt_employee()
            while True:
                user_input = input ("| Another? Y/N ")
                if user_input == "Y" or user_input == "y":
                    keep_gooing = True
                    print("+----------------------------------------")
                    break
                elif user_input == "N" or user_input == "n":
                    keep_gooing = False
                    print("+----------------------------------------")
                    break
                else :
                    print("| Please Only Type Y/N!")
                    keep_gooing = True

    def ask_tips (self):
        # self.tips = float(input("Tips? "))
        s = input("| Please Enter Total Tips! ")
        print("+----------------------------------------")
        if s.isnumeric() :
            self.tips = float(s)
        else : 
            print("| Please Enter a Numbers!")
            self.ask_tips()

    def tips_perhours (self):
        return self.tips / self.total_hours
    
    def personal_tip (self, name:str):
        return self.tips_perhours() * self.employees[name]
    
    def prompt_tip (self): 
        name = input ( "| Tip For whom? ")
        # return self.personal_tip(name)
        if name not in self.employees:
            print("| There is no %s" %name)
            return 0
        return self.personal_tip(name)

    def calc_tips (self):
        for name in self.employees:
            self.tip_db[name] = self.personal_tip(name)

    def write_into (self, filename: str):
        with open (filename, "w+") as f:
            for name in self.tip_db:
                s= "%s %i %f\n" %(name, self.employees[name], self.tip_db[name])
                f.write(s)

    def prompt_file (self):
        filename = input ("| Filename ? ")
        self.write_into(filename)


db = Database()
db.ask_tips()
db.more_employee()
db.calc_tips()
db.prompt_file()
# print(db.tip_db)
# tip = db.prompt_tip()
# print("| %f " %tip)

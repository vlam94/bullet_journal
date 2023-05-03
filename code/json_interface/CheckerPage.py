from Page import *

class CheckerPage (Page):

    def __str__(self):
        ret = "\n\nPlans for today:\n"
        it = [*zip(self.page['plans'].values(),self.checker['plans_check'].values())]
        for i, [plan, check] in enumerate(it, start=1):
            if check:
                ret+= f"{i}. {plan} [x]\n"
            else:
                ret+= f"{i}. {plan} [ ]\n"
        return ret
    
    def task_checker(self): 
        print('\nHere are the updated plans for today:\n')
        print(self)
        inp = input("\nHave you complete any task?\n(which/n): ").lower() 
        self.task_mark_done(True,inp)

    def task_mark_done(self,done,inp):
        try:
            inp=int(inp)
            self.checker["plans_check"][f"plan_{inp}"] = int(done)
            print(self)
        except ValueError:
            if done:
                inp = input("Do you wish to unmark any mistaken task?\n(which/n)").lower()
                self.task_mark_done(False,inp)
            return   
        except IndexError: 
            inp = input('Invalid task! Select from 1 to 7: ').lower()
            self.task_mark_done(done,inp)
        inp = input("\nDo you want to update another task?\n(which/n): ").lower()    
        self.task_mark_done(done,inp)
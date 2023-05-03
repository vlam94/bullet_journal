from CheckerPage import *

class CheckoutPage(CheckerPage):      
    
    def __str__(self):
        ret = '\nUpdated Page\n'
        ret += f"\nDate: {self.page['date']}\n"
        ret += "\nGood Things:"
        for i, good_thing in enumerate(self.page['good_things'].values(), start=1):
            ret += f"\n{i}. {good_thing}"
        ret += ("\n\nImprovements:")
        for i, improvement in enumerate(self.page['improvements'].values(), start=1):
            ret += f"\n{i}. {improvement}"
        ret += CheckerPage.__str__(self)
        return ret
    
    def rewrite_field(self,fieldcat):
        field = fieldcat.rstrip(fieldcat[-1]) + '_ '
        while True:
            fieldnum = input(f"\nWich {fieldcat[:-1]} would you like to re-enter?: ")
            field = field[:-1] + fieldnum
            try:     
                self.page[fieldcat][field] in self.page
                break
            except KeyError:
                print("\nOops!  Invalid index!")
    
        self.page[fieldcat][field] = input(f"\nre-type {field} bellow:\n")
        return
    

    def checkout(self):
        print(self)
        if input("\nWould you like to change anything?\n(y/n):").lower().startswith('n'):
            return
        field_type = input("\nWould you like to change a 'Good Thing'(G), 'Improvement'(I), 'Plan'(P) or 'Check'(C)").upper()
        while field_type not in ['P','I','C','G']:
            field_type = input("\nInvalid Input!\nType 'G','I','P','C' ").upper()
        if field_type.startswith('G'):
            self.rewrite_field('good_things')
        elif field_type.startswith('I'):
            self.rewrite_field('improvements')
        elif field_type.startswith('P'):
            self.rewrite_field('plans')
        else:
            self.task_checker()
        self.checkout()
    
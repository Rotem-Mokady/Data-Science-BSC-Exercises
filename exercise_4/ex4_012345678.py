''' Exercise #4. Python for Engineers.'''
from typing import Dict


class Minibar:
    def __init__(self, drinks: Dict[str, int] = {}, snacks: Dict[str, int] = {}, bill: int = 0) -> None:
        self._drinks = {key.lower(): val for key, val in drinks.items()}
        self._snacks = {key.lower(): val for key, val in snacks.items()}
        self._bill = bill

    def __repr__(self) -> str:
        drinks_repr = "No drinks left" if not self._drinks else f"Drinks: {', '.join(self._drinks)}"
        snacks_repr = "No snacks left" if not self._snacks else f"Snacks: {', '.join(self._snacks)}"
        bill_repr = "No bill yet" if not self._bill else f"Bill {self._bill}"

        return '\n'.join([drinks_repr, snacks_repr, bill_repr])

    @property
    def _constant_drink_price(self) -> int:
        return 20

    def eat(self, snack: str) -> None:
        fixed_name = snack.lower()
        price = self._snacks.get(fixed_name)

        if price is None:
            print(f'The snack {fixed_name} was not found')
            return

        self._bill += price
        self._snacks.pop(fixed_name)

    def drink(self, drink: str) -> None:
        fixed_name = drink.lower()
        amount_left = self._drinks.get(fixed_name)

        if amount_left is None:
            print(f'The drink {fixed_name} was not found')
            return

        self._drinks[fixed_name] -= 1
        self._bill += self._constant_drink_price

        if not self._drinks[fixed_name]:
            self._drinks.pop(fixed_name)



#########################################
# Question 2 - do not delete this comment
#########################################
class Room:
    def __init__(self, minibar, number, guests, clean_level, is_suite, satisfaction=0.5):
        pass # replace this with your implementation
    
    def __repr__(self):
        pass # replace this with your implementation

    def is_occupied(self):
        pass # replace this with your implementation

    def clean(self):
        pass # replace this with your implementation

    def better_than(self, other):
        pass # replace this with your implementation

    def check_in(self, guests):
        pass # replace this with your implementation

    def check_out(self):
        pass # replace this with your implementation
    
    def move_to(self, other):
        pass # replace this with your implementation


#########################################
# Question 3 - do not delete this comment
#########################################
class Hotel:
    def __init__(self, name, rooms):
        pass # replace this with your implementation
            
    def __repr__(self):
        pass # replace this with your implementation
                      
    def check_in(self, guests, is_suite):
        pass # replace this with your implementation

    def check_out(self, guest):
        pass # replace this with your implementation

    def upgrade(self, guest):
        pass # replace this with your implementation

    def send_cleaner(self, guest):
        pass  # replace this with your implementation


#########################################
# Question 4 - do not delete this comment
#########################################

class Roman:
    
    def get_int_from_roman(self):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman_string = self.roman_value.strip('-')
        int_val = 0
        for counter in range(len(roman_string)):
            if counter > 0 and rom_val[roman_string[counter]] > rom_val[roman_string[counter - 1]]:
                int_val += rom_val[roman_string[counter]] - 2 * rom_val[roman_string[counter - 1]]
            else:
                int_val += rom_val[roman_string[counter]]
        int_val = -int_val if self.is_neg else int_val
        return int_val
    
    def get_roman_from_int(self):
        num = self.int_value if not self.is_neg else -self.int_value
        roman_num = '' if not self.is_neg else '-'
        counter = 0
        
        roman_char = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        int_vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        while num > 0:
            for _ in range(num // int_vals[counter]):
                roman_num += roman_char[counter]
                num -= int_vals[counter]
            counter += 1
        return roman_num
    
    def __init__(self, input_value):
        pass


    def __repr__(self):
        pass


    def __neg__(self):
        pass


    def __add__(self, other):
        pass


    def __lt__(self, other):
        pass
    
    
    def __gt__(self, other):
        pass
    

    def __floordiv__(self, other):
        pass



if __name__ == '__main__':
    print("*")
    # def test_hotel():
    #     m1 = Minibar({'coke': 10, 'lemonade': 1}, {'bamba': 8, 'mars': 12})
    #     m2 = Minibar({'beer': 10, 'lemonade':4}, {'m&m': 6})
    #     rooms = [Room(m2, 514, [], 5, True),
    #              Room(m2, 210, ["Ronen", "Shir"], 6, True),
    #              Room(m1, 102, ["Liat"], 7, False),
    #              Room(m2, 223, [], 6, True)]
    #     h = Hotel("Dan", rooms)
    #     test_sep = '\n------------------'
    #     print('PRINT m1:\n', m1, test_sep, sep="")
    #     print('PRINT m2:\n', m2, test_sep, sep="")
    #     print('PRINT h:\n', h, test_sep, sep="")
    #     liat_room = h.send_cleaner('Liat')
    #     print('CALL: h.send_cleaner("Liat")', liat_room, test_sep, sep="")
    #     print('CALL: liat_room.eat("bamba")\n', liat_room.minibar.eat("bamba"), test_sep, sep="")
    #     print('PRINT liat_room.minibar:\n', liat_room.minibar, test_sep, sep="")
    #     print('CALL: liat_room.drink("lemonade")\n', liat_room.minibar.drink("lemonade"), test_sep, sep="")
    #     print('PRINT liat_room.minibar:\n', liat_room.minibar, test_sep, sep="")
    #     print('CALL: h.upgrade("Liat")', h.upgrade("Liat"), test_sep, sep="")
    #
    #     print('CALL: h.check_out("Ronen")', h.check_out("Ronen"), test_sep, sep="")
    #     print('CALL: h.check_out("Ronen")\n', h.check_out("Ronen"), test_sep, sep="")
    #     print('CALL: h.check_in(["Alice", "Wonder"], True)',
    #           h.check_in(["Alice", "Wonder"], True), test_sep, sep="")
    #     print('CALL: h.check_in(["Alex"], True)', h.check_in(["Alex"], True), test_sep,
    #           sep="")
    #     print('PRINT h:\n', h, test_sep, sep="")
    #     print('CALL: h.check_in(["Oded", "Shani"], False)',
    #           h.check_in(["Oded", "Shani"], False), test_sep, sep="")
    #     print('CALL: h.check_in(["Oded", "Shani"], False)',
    #           h.check_in(["Oded", "Shani"], False), test_sep, sep="")
    #     print('CALL: h.check_out("Liat")', h.check_out("Liat"), test_sep, sep="")
    #     print('CALL: h.check_out("Liat")\n', h.check_out("Liat"), test_sep, sep="")
    #     print('PRINT h:\n', h, test_sep, sep="")
    #
    #
    # # After you are done implementing all classes and methods, you can compare the results with the file test_hotel_output.txt
    # test_hotel()
    #
    # print('==== Q4: Basic tests/output====')
    # r2 = Roman(2)
    # print(Roman(2))
    # print(repr(r2))
    # print('====')
    # print(-Roman("IV"))
    # print('====')
    # r5 = Roman(2) + 3
    # print(r5)
    # print(repr(r5))
    # print(repr(Roman(6) // -5))

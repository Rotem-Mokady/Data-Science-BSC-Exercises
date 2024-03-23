''' Exercise #4. Python for Engineers.'''
from typing import Dict, List, Union, Any
from copy import deepcopy


class Minibar:

    def __init__(self, drinks: Dict[str, int] = {}, snacks: Dict[str, int] = {}, bill: int = 0) -> None:
        self.drinks = {key.lower(): val for key, val in drinks.items()}
        self.snacks = {key.lower(): val for key, val in snacks.items()}
        self.bill = bill

    def __repr__(self) -> str:
        drinks_repr = "No drinks left" if not self.drinks else f"Drinks: {', '.join(self.drinks)}"
        snacks_repr = "No snacks left" if not self.snacks else f"Snacks: {', '.join(self.snacks)}"
        bill_repr = "No bill yet" if not self.bill else f"Bill {self.bill}"

        return '\n'.join([drinks_repr, snacks_repr, bill_repr])

    @property
    def _constant_drink_price(self) -> int:
        return 20

    def eat(self, snack: str) -> None:
        fixed_name = snack.lower()
        price = self.snacks.get(fixed_name)

        if price is None:
            print(f'The snack {fixed_name} was not found')
            return

        self.bill += price
        self.snacks.pop(fixed_name)

    def drink(self, drink: str) -> None:
        fixed_name = drink.lower()
        amount_left = self.drinks.get(fixed_name)

        if amount_left is None:
            print(f'The drink {fixed_name} was not found')
            return

        self.drinks[fixed_name] -= 1
        self.bill += self._constant_drink_price

        if not self.drinks[fixed_name]:
            self.drinks.pop(fixed_name)


#########################################
# Question 2 - do not delete this comment
#########################################
class Room:
    def __init__(
            self, minibar: Minibar, number: int, guests: List[str], clean_level: int,
            is_suite: bool, satisfaction: Union[int, float] = 0.5
    ):
        self.minibar = minibar
        self._pure_room_number = number
        self.room_number = self._room_number_sanity_check(room_number=number)
        self.guests = self._guests_names_convertor(names_array=guests)
        self.clean_level = self._clean_level_sanity_check(clean_level=clean_level)
        self.is_suite = is_suite
        self.satisfaction = self._satisfaction_convertor(satisfaction=satisfaction)

    @property
    def _floor_number(self) -> int:
        return int(str(self._pure_room_number)[0])

    @property
    def _internal_room_number(self) -> int:
        return int(str(self._pure_room_number)[1:])

    def _room_number_sanity_check(self, room_number: int) -> int:
        if len(str(room_number)) != 3:
            raise ValueError(f"inappropriate room number, {room_number}")

        if not (1 <= self._floor_number <= 9):
            raise ValueError(f"inappropriate floor, {self._floor_number}")
        if not (1 <= self._internal_room_number <= 30):
            raise ValueError(f"inappropriate room, {self._internal_room_number}")

        return room_number

    @staticmethod
    def _guests_names_convertor(names_array: List[str]) -> List[str]:
        return [(name.lower() if name != name.lower() else name) for name in names_array]

    @staticmethod
    def _satisfaction_convertor(satisfaction: Union[int, float]) -> float:
        if isinstance(satisfaction, int):
            return float(satisfaction)
        return satisfaction

    @property
    def _max_clean_level(self) -> int:
        return 15

    @property
    def _default_satisfaction(self) -> float:
        return 0.5

    @property
    def _max_satisfaction(self) -> float:
        return 1.0

    def _clean_level_sanity_check(self, clean_level: int) -> int:
        if not (1 <= clean_level <= self._max_clean_level):
            raise ValueError(f"inappropriate clean level, {clean_level}")
        return clean_level

    @staticmethod
    def _repr_values_handler(key: str, val: Any) -> str:
        fixed_key_name = key.replace('_', ' ').strip().capitalize()

        if key == 'minibar':
            return f'{fixed_key_name}:\n{val.__repr__()}'
        if key != 'guests':
            return f'{fixed_key_name}: {val}'
        if not val:
            return f'{fixed_key_name}: empty'
        return f'{fixed_key_name}: {", ".join(sorted(val))}'

    @property
    def _ordered_attrs(self) -> Dict[str, Any]:
        minibar_key_name = 'minibar'
        result = {
            **{key: val for key, val in self.__dict__.items() if key != minibar_key_name and not key.startswith('_')},
            **{minibar_key_name: self.minibar}
        }

        return result
    
    def __repr__(self) -> str:
        repr_conf = [self._repr_values_handler(key=key, val=val) for key, val in self._ordered_attrs.items()]
        result = '\n'.join(repr_conf)

        return result

    def is_occupied(self) -> bool:
        return bool(self.guests)

    def clean(self) -> None:
        room_type_point = 1 if self.is_suite else 0
        self.clean_level = min(self._max_clean_level, self.clean_level + 1 + room_type_point)

    def better_than(self, other: 'Room') -> bool:
        if self.is_suite != other.is_suite:
            return self.is_suite

        if self._floor_number != other._floor_number:
            return self._floor_number > other._floor_number

        return self.clean_level > other.clean_level

    def check_in(self, guests: List[str]) -> None:
        if self.is_occupied():
            print("Can't check-in new guests to an occupied room.")
            return

        self.guests = self._guests_names_convertor(names_array=guests)
        self.satisfaction = self._default_satisfaction

    def check_out(self) -> None:
        if self.is_occupied():
            self.guests = []
            self.minibar.bill = 0
            return

        print("Cannot check-out an empty room")
    
    def move_to(self, other: 'Room') -> None:
        if not self.is_occupied():
            print("Cannot move guests from an empty room")
            return

        if other.is_occupied():
            print("Can't move guests into an occupied room")
            return

        other.guests = deepcopy(self.guests)
        other.minibar.bill = deepcopy(self.minibar.bill)

        if other.better_than(other=self):
            other.satisfaction = min(self._max_satisfaction, self.satisfaction + 0.1)
        else:
            other.satisfaction = self.satisfaction

        self.guests = []


#########################################
# Question 3 - do not delete this comment
#########################################
class Hotel:
    def __init__(self, name: str, rooms: List[Room]) -> None:
        self.name = name
        self.rooms = rooms

    @staticmethod
    def _fix_guest_name(name: str) -> str:
        return name.lower()
            
    def __repr__(self) -> str:
        occupied_rooms_amount = len([room for room in self.rooms if room.is_occupied()])
        total_rooms_amount = len(self.rooms)

        return f"{self.name} Hotel has: {occupied_rooms_amount}/{total_rooms_amount} occupied rooms."
                      
    def check_in(self, guests: List[str], is_suite: bool) -> Union[Room, None]:
        for room in self.rooms:
            if not room.is_occupied() and room.is_suite == is_suite:
                room.check_in(guests=guests)
                return room

    def check_out(self, guest: str) -> Union[Room, None]:
        for room in self.rooms:
            if self._fix_guest_name(guest) in room.guests:
                room.check_out()
                return room

    def upgrade(self, guest: str) -> Union[Room, None]:
        guest_current_room, second_check_list = None, []
        for room in self.rooms:
            # if the current guest room has been found and is still unknown, define it
            if guest_current_room is None and self._fix_guest_name(guest) in room.guests:
                guest_current_room = room
            # if the checked room is empty and there is still nothing to compare to, keep it
            elif not room.is_occupied() and guest_current_room is None:
                second_check_list.append(room)
            # if the current guest room is familiar and the checked room is empty, upgrade if possible
            elif not room.is_occupied():
                if room.better_than(guest_current_room):
                    guest_current_room.move_to(room)
                    return room
        # return nothing if the guest has not been found or there are no more empty rooms to compare to
        if guest_current_room is None or not second_check_list:
            return
        # do the upgrading check again for all the rooms that have not been checked
        for empty_room in second_check_list:
            if empty_room.better_than(guest_current_room):
                guest_current_room.move_to(empty_room)
                return empty_room

    def send_cleaner(self, guest: str) -> Union[Room, None]:
        for room in self.rooms:
            if self._fix_guest_name(guest) in room.guests:
                room.clean()
                return room


#########################################
# Question 4 - do not delete this comment
#########################################

class Roman:

    def __init__(self, input_value: Union[str, int]) -> None:
        self.input_value = input_value

        if isinstance(self.input_value, str):
            self.int_value, self.roman_value = self._get_int_from_roman(self.input_value), self.input_value
        else:
            self.int_value, self.roman_value = self.input_value, self._get_roman_from_int(self.input_value)

        self.is_neg = self.int_value < 0

    @property
    def _rom_char_to_number_conf(self) -> Dict[str, int]:
        return {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def _get_int_from_roman(self, roman_value: str) -> int:
        roman_string = roman_value.strip('-')
        int_val = 0

        for idx, char in enumerate(roman_string):
            current_rom_char = self._rom_char_to_number_conf[char]
            if idx and current_rom_char > self._rom_char_to_number_conf[roman_string[idx-1]]:
                int_val += current_rom_char - 2 * self._rom_char_to_number_conf[roman_string[idx-1]]
            else:
                int_val += current_rom_char

        return abs(int_val)

    @property
    def _number_to_rom_char_conf(self) -> Dict[int, str]:
        return {
             1000: 'M',
             900: 'CM',
             500: 'D',
             400: 'CD',
             100: 'C',
             90: 'XC',
             50: 'L',
             40: 'XL',
             10: 'X',
             9: 'IX',
             5: 'V',
             4: 'IV',
             1: 'I'
        }
    
    def _get_roman_from_int(self, int_value: int) -> str:
        if not int_value:
            raise ValueError("Unsupported result")
        abs_num, roman_repr = abs(int_value), '' if int_value > 0 else '-'

        for int_key, rom_val in self._number_to_rom_char_conf.items():
            if abs_num <= 0:
                break
            if abs_num < int_key:
                continue

            roman_repr += (abs_num // int_key) * rom_val
            abs_num -= int_key

        return roman_repr

    def __repr__(self) -> str:
        final_repr = f"int: {self.int_value}; Roman Numeral: '{self.roman_value}'"
        return final_repr

    def __neg__(self) -> 'Roman':
        return Roman(-self.int_value)

    def __add__(self, other: Union['Roman', int]) -> 'Roman':
        int_value = self.int_value + (other if isinstance(other, int) else other.int_value)
        return Roman(int_value)

    def __lt__(self, other: Union['Roman', int]) -> bool:
        other_int_value = other if isinstance(other, int) else other.int_value
        return self.int_value < other_int_value
    
    def __gt__(self, other: Union['Roman', int]) -> bool:
        other_int_value = other if isinstance(other, int) else other.int_value
        return self.int_value > other_int_value

    def __floordiv__(self, other: Union['Roman', str, int]) -> 'Roman':
        int_value = self.int_value // (other if isinstance(other, int) else other.int_value)
        return Roman(int_value)



if __name__ == '__main__':
    def test_hotel():
        m1 = Minibar({'coke': 10, 'lemonade': 1}, {'bamba': 8, 'mars': 12})
        m2 = Minibar({'beer': 10, 'lemonade':4}, {'m&m': 6})
        rooms = [Room(m2, 514, [], 5, True),
                 Room(m2, 210, ["Ronen", "Shir"], 6, True),
                 Room(m1, 102, ["Liat"], 7, False),
                 Room(m2, 223, [], 6, True)]
        h = Hotel("Dan", rooms)
        test_sep = '\n------------------'
        print('PRINT m1:\n', m1, test_sep, sep="")
        print('PRINT m2:\n', m2, test_sep, sep="")
        print('PRINT h:\n', h, test_sep, sep="")
        liat_room = h.send_cleaner('Liat')
        print('CALL: h.send_cleaner("Liat")\n', liat_room, test_sep, sep="")
        print('CALL: liat_room.eat("bamba")\n', liat_room.minibar.eat("bamba"), test_sep, sep="")
        print('PRINT liat_room.minibar:\n', liat_room.minibar, test_sep, sep="")
        print('CALL: liat_room.drink("lemonade")\n', liat_room.minibar.drink("lemonade"), test_sep, sep="")
        print('PRINT liat_room.minibar:\n', liat_room.minibar, test_sep, sep="")
        print('CALL: h.upgrade("Liat")\n', h.upgrade("Liat"), test_sep, sep="")

        print('CALL: h.check_out("Ronen")\n', h.check_out("Ronen"), test_sep, sep="")
        print('CALL: h.check_out("Ronen")\n', h.check_out("Ronen"), test_sep, sep="")
        print('CALL: h.check_in(["Alice", "Wonder"], True)\n',
              h.check_in(["Alice", "Wonder"], True), test_sep, sep="")
        print('CALL: h.check_in(["Alex"], True)\n', h.check_in(["Alex"], True), test_sep,
              sep="")
        print('PRINT h:\n', h, test_sep, sep="")
        print('CALL: h.check_in(["Oded", "Shani"], False)\n',
              h.check_in(["Oded", "Shani"], False), test_sep, sep="")
        print('CALL: h.check_in(["Oded", "Shani"], False)\n',
              h.check_in(["Oded", "Shani"], False), test_sep, sep="")
        print('CALL: h.check_out("Liat")\n', h.check_out("Liat"), test_sep, sep="")
        print('CALL: h.check_out("Liat")\n', h.check_out("Liat"), test_sep, sep="")
        print('PRINT h:\n', h, test_sep, sep="")


    # After you are done implementing all classes and methods, you can compare the results with the file test_hotel_output.txt
    test_hotel()

    print('==== Q4: Basic tests/output====')
    r2 = Roman(2)
    print(Roman(2))
    print(repr(r2))
    print('====')
    print(-Roman("IV"))
    print('====')
    r5 = Roman(2) + 3
    print(r5)
    print(repr(r5))
    print(repr(Roman(6) // -5))

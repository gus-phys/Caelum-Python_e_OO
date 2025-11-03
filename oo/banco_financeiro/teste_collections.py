#!/usr/bin/env python3

from collections import UserDict

class Pins(UserDict):

    def __contains__(self, key):
        return str(key) in self.keys()
    
    def __setitem__(self, key, value):
        self.data[str(key)] = value

if __name__ == "__main__":
    pins = Pins(one=1)
    print(pins)
    pins[3] = 1
    lista = [1, 2, 3]
    pins[lista] = 2
    print(pins)

    test_dict = {}
    test_dict[2] = 'dois'
    print(test_dict)
    print(type(list(test_dict.keys())[0]))
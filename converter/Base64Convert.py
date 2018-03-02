class Base64Convert:
    base_characters = \
        ("0","1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w",
         "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
         "T",
         "U", "V", "W", "X", "Y", "Z")

    def _convert(self, num, acc):

        target_base = len(self.base_characters)

        if num < target_base:
            acc.append(self.base_characters[num])
            return acc
        else:
            x = num // target_base
            remainder = int(num % target_base)
            acc.append(self.base_characters[remainder])
            return self._convert(x, acc)

    def convert(self, num):
        """ Converts a number to base64"""
        result = self._convert(num, [])
        result.reverse()
        reversed_result = "".join(result)

        return reversed_result

    def revert(self, _id):
        result = self._revert(_id, [], 0)
        return result

    def _revert(self, _id, acc, unit):

        if len(_id) == 0:
            return sum(acc)

        if type(_id) is not list:
            char_list = list(_id)
        else:
            char_list = _id

        base = len(self.base_characters)

        current_char = char_list.pop()
        idx = self.base_characters.index(current_char)
        multiplier = pow(base, unit)
        acc.append(multiplier * idx)

        unit += 1

        return self._revert(char_list, acc, unit)

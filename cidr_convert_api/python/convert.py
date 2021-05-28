import math
# These functions need to be implemented
class CidrMaskConvert:

    def cidr_to_mask(self, val):
        values = []
        val = int(val)
        if 0 >= val or val > 32:
            return "Invalid"
        for _ in range(4):
            values.append(val if val <= 8 else 8)
            val = val-val if val <=8 else val-8
        return ".".join(list(map(lambda x: str(2**8 - 2**(8-x)), values)))

    def mask_to_cidr(self, val):
        values = val.split(".")
        values = list(map(lambda x: 8 - math.log2(2**8 - int(x)), values))
        total = int(sum(values))
        if len(values) != 4 or any(int(num) > 255 or int(num) < 0 for num in values) or total == 0:
            return "Invalid"
        return str(total)

class IpValidate:

    def ipv4_validation(self, val):
        values = val.split('.')
        if not len(values) == 4 or any(char.isalpha() for char in val):
            return False
        for value in values:
            if not 0 <= int(value) <= 255:
                return False 
        return True

from random import choices
import string


def gen_key(hex_num):
    val = int(hex_num,16)
    stg_val = str(val)
    dig_list = [int(x) for x in stg_val]
    usable_dig = dig_list[0:3]
    ran_str = [''.join(choices(string.ascii_uppercase + string.digits, k=4)) for _ in range(3)]
    result = '-'.join(f'{d}{n}' for d, n in zip(usable_dig, ran_str)) + " " + stg_val[-2] + stg_val[-1]
    return result

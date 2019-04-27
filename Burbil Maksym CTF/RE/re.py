f = open("flag.txt", 'r')
flag = f.read().split(" ")
f.close()

def cancel_xor(flag_element, xor_num):
    flag_element = int(flag_element, 16)
    flag_element = flag_element ^ xor_num
    return flag_element

def ror(flag_element, bits_shift):
    flag_element = bin(int(flag_element, 16))[2:].zfill(8)
    temp = flag_element[8-bits_shift:]+ flag_element[:8-bits_shift]
    flag_element = int(temp, 2)
    return flag_element

def cancel_add(flag_element, add_num):
    flag_element = int(flag_element, 16)
    flag_element -= add_num
    return flag_element

def cancel_sub(flag_element, sub_num):
    flag_element = int(flag_element,16)
    flag_element += sub_num
    flag_element = int(hex(flag_element)[3:], 16)
    return flag_element

def cancel_not(flag_element, add_numb):
    flag_element = int(flag_element,16)
    flag_element ^= 0xFF
    flag_element -= add_numb
    return flag_element

f = open('funct.txt', 'r')
func_list = f.read().split(' ')
f.close()
result = []
for i in range(len(func_list)):
    if func_list[i] == '03':
        flag[i] = bytearray.fromhex(str(hex(cancel_xor(flag[i], 0x7A)))[2:]).decode()
    elif func_list[i] == '06':
        flag[i] = bytearray.fromhex(str(hex(ror(flag[i], 7)))[2:]).decode()
    elif func_list[i] == '04':
        flag[i] = bytearray.fromhex(str(hex(ror(flag[i], 5)))[2:]).decode()      
    elif func_list[i] == '02':
        flag[i] = bytearray.fromhex(str(hex(cancel_xor(flag[i], 0x6C)))[2:]).decode()
    elif func_list[i] == '01':
        flag[i] = bytearray.fromhex(str(hex(cancel_sub(flag[i], 0x75)))[2:]).decode()
    elif func_list[i] == '00':
        flag[i] = bytearray.fromhex(str(hex(cancel_add(flag[i], 0x6C)))[2:]).decode()
    elif func_list[i] == '07':
        flag[i] = bytearray.fromhex(str(hex(cancel_not(flag[i], 0x2A)))[2:]).decode()

print("".join(flag))

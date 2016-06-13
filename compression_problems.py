code_table = {' ': '11', 'e': '101', 't': '1001', 'o': '10001', 'n': '10000', 'a': '011', 's': '0101', 'i': '01001',
              'r': '01000', 'h': '0011', 'd': '00101', 'l': '001001', '!': '001000', 'u': '00011', 'c': '000101',
              'f': '000100', 'm': '000011', 'p': '0000101', 'g': '0000100', 'w': '0000011', 'b': '0000010',
              'y': '0000001', 'v': '00000001', 'j': '000000001', 'k': '0000000001', 'x': '00000000001',
              'q': '000000000001', 'z': '000000000000'}


def convert_to_bits(word):
    word_bits = ''
    for char in word:
        word_bits += code_table[char]
    return word_bits


def to_bit_array(bits):
    result = []
    current = ''
    counter = 0
    for b in bits:
        current += b
        counter += 1
        if counter >= 8:
            result.append(current)
            current = ''
            counter = 0

    current += '0' * (8 - len(current))
    result.append(current)
    return result


if __name__ == '__main__':
    with open('/home/ipatrikeev/dev/input.txt') as f:
        word = f.readline()
        print(' '.join(hex(int(w, 2))[2:].upper().zfill(2) for w in to_bit_array(convert_to_bits(word.strip()))))

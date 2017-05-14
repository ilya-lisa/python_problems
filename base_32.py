class Base32:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
    char_to_digit = {}
    digit_to_char = {}

    def __init__(self):
        symbols = list(self.alphabet)
        for ndx in range(len(symbols)):
            s = symbols[ndx]
            self.digit_to_char[ndx] = s
            self.char_to_digit[s] = ndx

    def enc(self, str_to_encode):
        padded_str = Base32.pad_string(str_to_encode)
        ascii_codes = [ord(c) for c in list(padded_str)]

        current_pos = 0
        result = []
        for i in range(len(ascii_codes) * 8 // 5):
            if (current_pos % 8 + 5) > 8:
                # first part
                first_bit_count = 8 - (current_pos % 8)
                n = ascii_codes[current_pos // 8] & Base32.mask_for(first_bit_count)
                n <<= (5 - first_bit_count)
                current_pos += first_bit_count

                # second part
                second_bit_count = 5 - first_bit_count
                shift = 8 - ((current_pos % 8) + second_bit_count)
                n += ((ascii_codes[current_pos // 8] >> shift) & Base32.mask_for(second_bit_count))
                result.append(self.digit_to_char[n])
                current_pos += second_bit_count
            else:
                shift = 8 - ((current_pos % 8) + 5)
                n = (ascii_codes[current_pos // 8] >> shift) & Base32.mask_for(5)
                result.append(self.digit_to_char[n])
                current_pos += 5
        return ''.join(result)

    def dec(self, str_to_decode):
        ascii_symbol_number = len(str_to_decode) * 5 / 8
        processed_symbols = 0
        current_symbol_bits = 0
        current_position = 0
        result = []
        while processed_symbols < ascii_symbol_number:
            ascii_bits_processed = current_position % 8
            bits_left_in_symbol = 5 - (current_position % 5)
            bits_needed = 8 - ascii_bits_processed
            if bits_needed <= bits_left_in_symbol:
                n = (self.char_to_digit[str_to_decode[current_position // 5]] >> (5 - bits_needed)) & Base32.mask_for(bits_needed)
                current_symbol_bits <<= bits_needed
                current_symbol_bits += n
                result.append(chr(current_symbol_bits))
                current_symbol_bits = 0
                current_position += bits_needed
                processed_symbols += 1
            else:
                n = (self.char_to_digit[str_to_decode[current_position // 5]]) & Base32.mask_for(bits_left_in_symbol)
                current_symbol_bits <<= bits_left_in_symbol
                current_symbol_bits += n
                current_position += bits_left_in_symbol
        return Base32.trim_string(''.join(result))

    @staticmethod
    def pad_string(string_to_pad):
        reminder = len(string_to_pad) % 5
        result = string_to_pad
        padding_number = 5 - reminder
        for i in range(padding_number):
            result += str(padding_number)

        return result

    @staticmethod
    def trim_string(string):
        if string[-1].isdigit():
            return string[:-int(string[-1])]
        else:
            return string

    @staticmethod
    def mask_for(digits):
        if digits < 1:
            raise ValueError('incorrect digit number: ' + str(digits))

        result = 0
        for i in range(digits):
            result += pow(2, i)
        return result


if __name__ == '__main__':
    with open("/Users/ipatrikeev/pdev/input.txt") as f:
        n_cases = int(f.readline())
        base32_processor = Base32()
        for case in range(n_cases):
            line_content = f.readline().strip()
            print(base32_processor.enc(line_content) if case % 2 == 0 else base32_processor.dec(line_content), end=' ')

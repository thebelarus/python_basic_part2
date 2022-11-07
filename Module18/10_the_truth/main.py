def caesars_encoder(string, offset):
    result = ''
    ord_big_letter_start = ord('A')
    ord_big_letter_end = ord('Z')
    ord_small_letter_start = ord('a')
    ord_small_letter_end = ord('z')
    for char in string:
        char_index = ord(char)
        if ord_big_letter_start <= char_index <= ord_big_letter_end:
            if char_index + offset > ord_big_letter_end:
                result += chr(ord_big_letter_start + (
                    char_index + offset - ord_big_letter_end - 1))
            else:
                result += chr(char_index + offset)
        elif ord_small_letter_start <= char_index <= ord_small_letter_end:
            if char_index + offset > ord_small_letter_end:
                result += chr(ord_small_letter_start + (
                    char_index + offset - ord_small_letter_end - 1))
            else:
                result += chr(char_index + offset)
        elif char != ' ':
            result += chr(char_index + offset)
        else:
            result += char
    return result


def offset_text(text, text_offset):
    result_text = []
    for word in text.split():
        word = list(word)
        for _ in range(text_offset):
            word.insert(0, word.pop())
        if '.' in word:
            text_offset += 1
        result_text.append(''.join(word))
    return ' '.join(result_text)


def decode_text(text, caesars_offset, text_offset):
    text_encoded = caesars_encoder(text, caesars_offset)
    text_ofseted = offset_text(text_encoded, text_offset)
    return text_ofseted


if __name__ == '__main__':
    result = decode_text(
        text='vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm ''fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe / bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft(ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju / Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv(i/Evud xOp tj scfuuf ibou / ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju(b bec / jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb / bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip',
        caesars_offset=-1,
        text_offset=3
        )
    print(result)

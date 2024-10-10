def stegano(img):
    binary_text = ''
    width, height = img.size
    for y in range(height):
        for x in range(width):
            binary_text += str(img.getpixel((x, y))[0] & 1)
            if binary_text[-8:] == '11111111':
                return ''.join(chr(int(binary_text[i:i + 8], 2)) for i in range(0, len(binary_text) - 8, 8))


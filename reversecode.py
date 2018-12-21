def reversecoding(code):
    output = ''
    print('code: ' + code)
    for i in range(len(code)-1, -1, -1):
        output += code[i]
    print('encrypt: ' + output)
    reversecoding_decrypt(output)
    
def reversecoding_decrypt(code):
    output = ''
    for i in range(len(code)-1, -1, -1):
        output += code[i]
    print('decrypt: ' + output)

reversecoding('space wars')

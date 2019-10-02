import pyperclip
import time
import re

if __name__ == '__main__':
    copyBuff=' '
    while True:
        time.sleep(10)
        copyedText=pyperclip.paste()
        print(copyedText)
        if copyBuff!=copyedText:
            copyBuff=copyedText
            normalizedText = re.sub(r"(\n)|(\s){2,}","",copyBuff)
            print(normalizedText)
            pyperclip.copy(normalizedText)
        else:
            print('no change')
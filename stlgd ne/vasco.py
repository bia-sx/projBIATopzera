import base64
import time as t

encostr = "ICAgX19fX18gICAgICAgICAgICAgICAgICAgICAgICBfICAgICAgICAgCiAgLyBfX19ffCAgICAgICAgICAgICAgICAgICAgICB8IHwgICAgICAgIAogfCAoX19fICAgX19fICAgXyBfXyBfX18gICBfXyBffCB8XyBfXyBfICAKICBcX19fIFwgLyBfIFwgfCAnXyBgIF8gXCAvIF9gIHwgX18vIF9gIHwgCiAgX19fXykgfCAgX18vIHwgfCB8IHwgfCB8IChffCB8IHx8IChffCB8IAogfF9fX19fLyBcX19ffCB8X3wgfF98IHxffFxfXyxffFxfX1xfXyxffCAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIA=="

decbytes = base64.b64decode(encostr)
decstr = decbytes.decode('utf-8')
def escreve(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        t.sleep(delay)
    print()

escreve(decstr)

t.sleep(1)

escreve("\nFeito com muito amor e carinho!")
"""
Gera um QR Code para colocar no convite.

Instalação:
    pip install qrcode[pil]

Uso:
    python gerar_qrcode.py "https://seu-site.com/lista-noivado"
"""

import qrcode
import os


url = "https://pdrognd.github.io/Valentines-Day/"

img = qrcode.make(url)
img.save("qrcode.png")

print("QR Code gerado!")
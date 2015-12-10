#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
from credit import credit

#display.set_mode((800,500))
display.set_mode((1280,768))

text = """REVERSE PAC-MAN
_                                                 _

Developed by\\Aeroli.to

Programmers\\Icaro Raupp Henrique
\\Igor H. de Oliveira

GitHub\\github.com/iraupph/pacman-python


Adapted from David Reilly’s Pac-Man Python Project

Based on “Pac-Man”
Developed by Namco
Published by Namco (Japan) & Midway (North America)
Released in May 22, 1980 (Japan) & October 26, 1980 (North America)

Also based on “Super Mario World”
Developed by Nintendo EAD
Published by Nintendo
Released in November 21, 1990 (Japan)

_                                                 _

Have you heard about Konami Code?"""


#font = font.Font("Roboto-MediumItalic.ttf",20)
font = font.Font("webpixel-bitmap_bold.otf",40)
color = 0xa0a0a000

credit(text,font,color)

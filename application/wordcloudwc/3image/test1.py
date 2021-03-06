#!/usr/bin/env python3

import numpy as np
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt

pic = np.array(Image.open("image.png"))
jsondict = {
	"Unix": 9,
	"Linus Torvalds": 8,
	"Richard Stallman": 8,
	"open source": 3,
	"Gentoo": 3,
	"Archlinux": 3,
	"Void Linux": 3,
	"Guix": 3,
	"free software": 8,
	"RadHat": 3,
	"php": 3,
	"SUSE": 3,
	"Ruby": 3,
	"Python": 3,
	"Go": 3,
	"Mandriva": 3,
	"root": 5,
	"Lisp": 6,
	"C": 3,
	"Haskell": 3,
	"XMonad": 3,
	"javascript": 6,
	"clojure": 3,
	"bash": 3,
	"vim": 4,
	"emacs": 4,
	"vis": 4,
	"ls": 3,
	"cd": 3,
	"grep": 3,
	"sed": 3,
	"awk": 3,
	"pascal": 3,
	"GNU": 9,
	"irc": 3,
	"inkscape": 3,
	"github": 5,
	"gitlab": 4,
	"FOSDEM": 5,
	"GPL": 4,
	"Free as in Freedom": 5,
	"FOSS": 4,
	"Mozilla": 3,
	"Busybox": 3,
	"qemu": 3,
	"gnome": 3,
	"android": 3,
	"Fedora": 3,
	"R": 3,
	"xelatex": 3,
	"mupdf": 3,
	"chromium": 3,
	"riot": 3,
	"pidgin": 3,
	"vlc": 3,
	"deadbeef": 3,
	"xarchiver": 3,
	"calibre": 3,
	"s6": 3,
	"json": 3,
	"chez scheme": 3,
	"GIMP": 3,
	"gcc": 3,
	"debian": 3,
	"printf(\"Linux\")": 3,
	"echo Linux": 3,
	"(println \"Linux\")": 3,
	"console.log \"Linux\"": 3,
	"(format t \"Linux\")": 3,
	"writeln(\"Linux\")": 3,
	"PRINT \"Linux\"": 3,
	"(insert \"Linux\")": 3,
	"fmt.Println(\"Linux\")": 3,
	"main = putStrLn \"Linux\"": 3,
	"(display \"Linux\")": 3,
	"System.out.println(\"Linux\");": 3,
	"document.write(\"Linux\")": 3,
	"type [Linux]": 3,
	"disp('Linux')": 3,
	"<?php\necho \"Linux\"\n?>": 3,
	"Ubuntu": 3
}
image_colors = ImageColorGenerator(pic, [255, 255, 255])
wc = WordCloud(background_color = "white", mask = pic)
wc.generate_from_frequencies(jsondict)

plt.imshow(wc.recolor(color_func = image_colors), interpolation = "bilinear")
plt.axis("off")
plt.show()
def bdoc():
    print(r"""\documentclass[center,10pt,cm,aspectratio=169]{beamer}

\usetheme{minicasual}

""")

def bdoc():
    print(r"""\begin{document}
\centering
""")

def edoc():
    print(r"\end{document}")

def bframe(title=''):
    print()
    print(r'\begin{frame}{%s}' % title)
    print()

def eframe():
    print()
    print(r'\end{frame}')
    print()

def spc():
    print()

def img(width, path):
    print(r'\includegraphics[width=%s\textwidth]{%s}' % (width, path))

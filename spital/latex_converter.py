import os

def to_pdf(empname, devicename, serialnumber, clientname, number, shwang):
    return

tex = open("template.tex","r")
text = tex.read()
tex.close()

text = text.replace("VAR-EMPNAME", "Kuba Jebapisowski")
#text.replace("VAR-SERIALNUMBER", str(2020203))
text.replace("Filipa", "dupy")


file = open("temp.tex","w")
file.write(text)
file.close()

#os.system("pdflatex temp.tex")
os.system("Portable_LaTeXCH2017\\texmfs\\install\\miktex\\bin\\pdflatex.exe temp.tex")
#os.system("temp.pdf")

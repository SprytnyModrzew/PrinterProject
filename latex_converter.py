import os

def to_pdf(empname, devicename, serialnumber, clientname, number, shwang):
    return
tex = open("C:\\Users\\Modrzew\\PycharmProjects\\qt\\template.tex","r")
text = tex.read()
tex.close()

text.replace("VAR-EMPNAME", "Kuba Jebapisowski")
text.replace("VAR-SERIALNUMBER", str(2020203))
print(text)

file = open("temp.tex","w")
file.write(text)
file.close()

os.system("pdflatex temp.tex")
os.system("temp.pdf")
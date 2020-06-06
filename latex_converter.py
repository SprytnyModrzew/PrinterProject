import os
import io


def to_pdf(empname, devicename, serialnumber, clientname, number, shwang, confirm, data, dicts):
    # print("woop")
    tex = open("template.tex", "r")
    with io.open("template.tex", 'r', encoding='utf8') as f:
        text = f.read()
    tex.close()
    # print(dicts)
    pretty_boxes = {"T": "X", "N": ""}
    pretty_strings = {
        "power": "Kabel zasilający",
        "signal": "Kabel sygnałowy",
        "power_box": "Zasilacz",
        "black_ink": "Czarny tusz",
        "color_ink": "Kolorowy tusz",
        "packing": "Opakowanie",
        "black_toner": "Czarny toner",
        "color_toner": "Kolorowy toner",
        "tape": "Taśma barwiąca",
        "mouse": "Mysz",
        "charger": "Ładowarka",
        "sim_card": "Karta SIM",
        "mem_card": "Karta pamięci",
        "case": "obudowa"
    }

    text_table = '''\\begin{tabular}{
  |p{\\dimexpr.40\\linewidth-2\\tabcolsep-1.3333\\arrayrulewidth}
  |p{\\dimexpr.10\\linewidth-2\\tabcolsep-1.3333\\arrayrulewidth}
  |p{\\dimexpr.40\\linewidth-2\\tabcolsep-1.3333\\arrayrulewidth}
  |p{\\dimexpr.10\\linewidth-2\\tabcolsep-1.3333\\arrayrulewidth}|
  }
  \\hline '''
    i = 0
    for key in dicts:
        temp = pretty_strings[key]
        # print(temp)
        text_table = text_table + temp + " & " + pretty_boxes[dicts[key]]
        i = i + 1
        if i % 2:
            text_table = text_table + " & "
        else:
            text_table = text_table + " \\\\ \\hline "
    if i % 2:
        text_table = text_table + " & \\\\ \\hline"
    text_table = text_table + " \\end{tabular} "
    # print(text_table)

    text = text.replace("VAR-CONFIRM", str(confirm))
    text = text.replace("VAR-TABLE", text_table)

    text = text.replace("VAR-EMPNAME", empname)
    text = text.replace("VAR-TIME", str(data))
    text = text.replace("VAR-DEVICENAME", devicename)
    text = text.replace("VAR-CLIENTNAME", clientname)
    text = text.replace("VAR-NUMBER", number)

    text = text.replace("VAR-SERIALNUMBER", serialnumber)
    text = text.replace("VAR-SHWANG", shwang)
    # print(text)
    # print("woop1")
    file = open("temp.tex", "wb")
    # print("woop2")
    text = bytes(text, "utf-8")
    file.write(text)
    # print("woop3")
    file.close()

    # os.system("pdflatex temp.tex")
    os.system(
        "Portable_LaTeXCH2017\\texmfs\\install\\miktex\\bin\\pdflatex.exe temp.tex -job-name=Potwierdzenie_nr" + str(
            confirm))
    # os.system("temp.pdf")
    return

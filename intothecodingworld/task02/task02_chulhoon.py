from pprint import pprint

def use_openpyxl(paths):
    from openpyxl import load_workbook
    ws = load_workbook(paths[0])['Sheet1']
    out = []

    for row in ws.rows:
        id_1, id_2, lines = [cell.value for cell in row]
        id = f"{id_1}#{id_2}"
        lines = lines if lines else ""
        lines = lines.split("\n")

        out.extend([(id, line) for line in lines])

    pprint(out)

    # TODO write output.xlsx


if __name__ == "__main__":
    paths = [
        r"C:\Users\happyhill24\Desktop\work\intothecodingworld\task02\data.xlsx",
        r"C:\Users\happyhill24\Desktop\work\intothecodingworld\task02\output.xlsx"
        ]
    use_openpyxl(paths)
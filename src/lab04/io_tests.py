from src.lab04.io_txt_csv import read_text, write_csv
txt = read_text("data/input.txt")  # должен вернуть строку
print(txt)
write_csv([("word","count"),("test",3)], "data/check.csv")  # создаст CSV
write_csv([], "data/empty.csv", None)
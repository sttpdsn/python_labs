from src.lib.text import count_freq, normalize, tokenize, top_n
import sys

def main() -> None:
    tokens = tokenize(normalize(sys.stdin.read()))
    freq = count_freq(tokens)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top_n(freq):
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()
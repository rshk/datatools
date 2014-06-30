import sys

if __name__ == '__main__':
    try:
        charset_from = sys.argv[1]
        charset_to = sys.argv[2]
    except IndexError:
        print("Usage: charset_convert.py <charset-from> <charset-to>")
        sys.exit(1)

    for line in sys.stdin:
        sys.stdout.write(line.decode(charset_from).encode(charset_to))

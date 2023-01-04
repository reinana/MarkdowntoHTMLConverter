import markdown
import sys

def main() :

    l = len(sys.argv)
    command = sys.argv[1]
    inputfile = sys.argv[2]
    outputfile = sys.argv[3]

    if command == 'markdown':
        if l != 4:
            print("入力に不備があります")
            sys.exit()
        try:
            with open(inputfile, 'r') as f:
                text = f.read()
        except FileNotFoundError:
            print('ファイルが存在しません')

        md = markdown.Markdown(extensions=['extra', 'toc', 'sane_lists', 'codehilite'])
        html = md.convert(text)
        with open(outputfile, 'w') as f:
            f.write(html)
    else:
        print("正しいコマンドを入力してください")

if __name__ == "__main__":
    main()
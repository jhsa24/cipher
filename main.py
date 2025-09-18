import argparse

def main():
    parser = argparse.ArgumentParser(description='Cipher Tool')
    subparsers = parser.add_subparsers(dest='command', required=True)

    caesar_parser = subparsers.add_parser('caesar', help='Encrypt an input file with a Caesar cipher.')
    caesar_parser.add_argument('input_filename', help='Path (relative or absoulute) to input file.')
    caesar_parser.add_argument('shift', type=int, help='Shift value for cipher, use a negative value for decryption.')
    caesar_parser.add_argument('-o', '--output', help='Optional path for output file, caesar creates new files only and will fail if file already exists. Defaults to stdout.')

    args = parser.parse_args()

    with open(args.input_filename) as file_in:
        plain_text = file_in.read()

    print(plain_text)
    if args.command == 'caesar':
        print("Starting encryption ...")
        caesar(plain_text, args.shift, args.output)
    else:
        print("Something went wrong...")

if __name__ == "__main__":
    main()

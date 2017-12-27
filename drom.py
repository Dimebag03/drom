"""Terminal application to download ROMs"""

import argparse


def main():
    """Main Function"""
    parser = argparse.ArgumentParser(
        description='Find the ROM you want to play and make the download from the terminal!',
        version='0.0.1', prog="drom")
    parser.add_argument('romname',
                        help='the ROM to be searched')
    parser.add_argument('-p', '--platform', metavar='',
                        choices=['psx', 'ps2', 'nes',
                                 'snes', 'n64', 'gc', 'wii'],
                        help='add platform to the search query')

    args = parser.parse_args()
    if args.platform:
        print 'ROM name: {} Platform: {}'.format(args.romname, args.platform)
        return

    print 'ROM name: {}'.format(args.romname)


if __name__ == "__main__":
    main()

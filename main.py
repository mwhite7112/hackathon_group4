import argparse

from modules import cleaning



if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('csv1', type=str)
    parser.add_argument('csv2', type=str)
    parser.add_argument('csv3', type=str)

    args = parser.parse_args()

    cleaning.extract(args.csv1)

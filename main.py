from argparse import ArgumentParser
import sys
import harvest


def harvestData(source, input):
    """Gathering data from sources for GitHub Repo."""
    with open(input) as fh:
        ids = [line.strip('\n') for line in fh.readlines()]

    if source.split('.')[0] == 'stanford':
        new_harvest = harvest.StanfordHarvest(source.split('.')[1], ids)
        new_harvest.download()
    elif source.split('.')[0] == 'princeton':
        new_harvest = harvest.PrincetonHarvest(source.split('.')[1], ids)
        new_harvest.download()
    elif source.split('.')[0] == 'penn':
        new_harvest = harvest.PennHarvest(source.split('.')[1], ids)
        new_harvest.download()
    elif source == 'europeana':
        print('europeana')
    elif source == 'qdl.scrape':
        print('qdl.scrape')
    elif source == 'met.csv':
        print('met.csv')
    else:
        print("This source is not currently supported.")


def main():
    # Basic CLI client for harvesting samples to analyze, report on, convert.
    parser = ArgumentParser(usage='%(prog)s [options] input_file')
    parser.add_argument("-s", "--source", dest="source",
                        help="source in form of institution.format")
    parser.add_argument("input", help="txt file with 1 record ID per line")

    args = parser.parse_args()

    if not len(sys.argv) > 0:
        parser.print_help()
        parser.exit()

    harvestData(args.source, args.input)


if __name__ == '__main__':
    main()

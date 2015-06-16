import csv
import sys


def main():
    logfile = sys.argv[1]
    try:
        outfile = open(sys.argv[2], 'wb')
    except:
        outfile = open('stats.csv', 'wb')

    writer = csv.writer(outfile)
    writer.writerow((
        'url', 'time', 't traverse', 't commit', 't transchain', 'setstate',
        'total', 'total cached', 'modified', 'rss before', 'rss after'
    ))

    for line in open(logfile, 'rb'):
        if 'collective.stats' not in line:
            continue

        try:
            info = line.split('collective.stats')[-1]
            i1, i2, i3, i4 = [i.strip() for i in info.split('|')[1:]]
        except:
            continue

        tital, after_traverse, before_commit, transchain, loads, \
            loads_total, loads_cached, modified = i1.split()
        rss1, rss2 = [i.strip() for i in i4.split('RSS:')[-1].split('-')]
        url = i2.strip()

        print '%s | %s' % (i1, i2)
        writer.writerow(
            (url, tital, after_traverse, before_commit, transchain, loads,
             loads_total, loads_cached, modified, rss1, rss2))

    outfile.close()


if __name__ == '__main__':
    main()

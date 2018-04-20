from DOBscraper import scrape

def scrapeCaller(addressFile, targetFile):
    addressFile = open(addressFile, 'r')
    for line in addressFile:
        if line != 'Borough,Block,Lot\n':
            print(line)
            Borough,Block,Lot = line.split(',')
            scrape(Borough, Block, Lot, targetFile)
            # print(Borough)

scrapeCaller("BBL-Eliyah.csv", "output.csv")

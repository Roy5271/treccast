import re
import os.path
from nltk.tokenize import sent_tokenize

# path to location of the datasets
CAR_TRECWEB_LOC = 'data/dedup.articles-paragraphs.cbor.xml'
# MARCO_TRECWEB_LOC='data/dedup.articles-paragraphs.cbor'
MARCO_TRECWEB_LOC = 'data/collection.tsv.xml'

cleanr = re.compile('<.*?>')


def process(loc, folder):
    with open(loc, 'r') as fp:
        line = fp.readline()
        id = ''
        cnt = 0
        while line:
            if "DOCNO" in line:
                id = re.sub(cleanr, '', line).replace('\n', '')
            if "<BODY>" in line:
                cnt += 1
                if cnt % 10000 == 0:
                    print(10)
                paragraph = fp.readline()
                if not os.path.isfile(folder + "/" + id + ".txt"):
                    with open(folder + "/" + id + ".txt", 'w') as out:
                        out.write(paragraph)
                        out.close()
            if cnt == 100000:
                break
            line = fp.readline()


# process(MARCO_TRECWEB_LOC, "data/marco_ids")
# process(CAR_TRECWEB_LOC, "data/car_ids")


def reformat(path):
    i = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            sentences = []
            print(i, ' : ', file)
            with open(path + file, 'r', encoding='UTF-8') as fp:
                for sen in sent_tokenize(fp.read().replace('\n', '')):
                    sentences.append(sen + '\n')
            with open(path + file, 'w') as fp:
                fp.writelines(sentences)
            i += 1


def test(file):
    sentences = []
    with open(file, 'r', encoding='UTF-8') as fp:
        for sen in sent_tokenize(fp.read()):
            sentences.append(sen + '\n')
            print(sen)
    with open(file, 'w') as fp:
        fp.writelines(sentences)


# reformat("data/marco_ids/")
# reformat("data/marco_test/")
reformat("data/car_ids/")
# test('MARCO_1.txt')


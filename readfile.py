# -*- conding: utf-8 -*-
def run():
    counter = 0
    with open('resourses/aleph.txt', 'r', encoding="utf-8") as f:
        for line in f:
            counter += line.count('Beatriz')

    print("Beatriz se encuentra {} en el texto. ".format(counter))
    
if __name__ == '__main__':
    run()
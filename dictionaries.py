# -*- condig: utf-8 -*-

def getAverage(dictionary):
    ratings = 0
    for value in dictionary.values():
        ratings += value

    average = ratings / len(dictionary.values())
    return average

def showSubjects(ratings):
    for key, value in ratings.items():
        print('Subject "{}" grade of: {} '.format(key, value))

    print('')
    
def run():
    ratings = {}
    ratings['Physical'] = 10
    ratings['Algebra'] = 9
    ratings['Trigonometry'] = 7
    ratings['programming'] = 9
    
    result = getAverage(ratings)
    
    showSubjects(ratings)
    print('The average of your final grades is: {} '.format(result))

if __name__ == '__main__':
    run()
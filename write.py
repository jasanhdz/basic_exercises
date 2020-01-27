def run():
    with open('resourses/numbers.txt', 'w') as f:
        for i in range(10):
            f.write(str(i))

    # try:
    #     f = open('resourses/numbers.txt')
    # finally:
    #     f.close()
    
if __name__ == '__main__':
    run()
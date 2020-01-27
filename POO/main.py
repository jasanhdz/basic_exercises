from Lamp import Lamp

def run():
    lamp = Lamp(is_turned_on=False)
    
    while True:
        command = str(input('''
    What do you want to do?

        [t]urn on the light
        [o]ff the light
        [g]o ut
'''))
        if command == 't':
            lamp.turn_on()
        elif command == 'o':
            lamp.turn_off()
        else:
            break


if __name__ == '__main__':
    run()
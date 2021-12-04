import keyboard
import pin_controller as controller


def init():
    print('Initializing GPIO setup')
    controller.motor_init()
    print('Completed GPIO setup')


if __name__ == '__main__':
    try:
        init()
        while True:
            current_key = ''
            if keyboard.is_pressed('Up'):
                if current_key is not 'Up':
                    current_key = 'Up'
                    controller.forward()
            elif keyboard.is_pressed('Down'):
                if current_key is not 'Down':
                    current_key = 'Down'
                    controller.back()
            elif keyboard.is_pressed('Left'):
                if current_key is not 'Left':
                    current_key = 'Left'
                    controller.left()
            elif keyboard.is_pressed('Right'):
                if current_key is not 'Right':
                    current_key = 'Right'
                    controller.right()
            else:
                current_key = ''
                controller.brake()
    except KeyboardInterrupt:
        controller.cleanup()
        print("Exited by user.")

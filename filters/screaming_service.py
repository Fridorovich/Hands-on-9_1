import multiprocessing

def screaming_service(pipe2, pipe3):
    while True:
        message = pipe2.pull()
        if message is None:
            break
        user, message = message.split(':', 1)
        upper_message = message.upper()
        pipe3.push(f"{user}:{upper_message}")

if __name__ == '__main__':
    multiprocessing.freeze_support()
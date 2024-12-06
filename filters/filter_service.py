import multiprocessing

STOP_WORDS = ["bird-watching", "ailurophobia", "mango"]

def filter_service(pipe1, pipe2):
    while True:
        message = pipe1.pull()
        if message is None:
            break
        user, message = message.split(':', 1)
        if any(word in message for word in STOP_WORDS):
            print(f"Filtered message from {user}: {message}")
        else:
            pipe2.push(f"{user}:{message}")

if __name__ == '__main__':
    multiprocessing.freeze_support()
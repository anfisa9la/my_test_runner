import schedule


def main(func):
    schedule.every().day.at('12:22').do(func)

    while True:
        schedule.run_pending()


# USAGE EXAMPLE
# def hello():
#     print('Hello!')

# main(hello)


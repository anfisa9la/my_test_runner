import schedule


def main(func):
    schedule.every().day.at('12:22').do(func)

    while True:
        schedule.run_pending()


# USAGE EXAMPLE
# def Jesse_answerphone():
#     print('YO 148, 369, Representing the ABQ')

# main(hello)


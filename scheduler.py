import schedule


def main(func, time):
    schedule.every().day.at(time).do(func)

    while True:
        schedule.run_pending()


# Usage example
# def Jesse_answerphone():
#     print('YO 148, 369, Representing the ABQ')
# main(hello, '21:00')


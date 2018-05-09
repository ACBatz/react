import datetime
import csv


class Utils:
    @staticmethod
    def seconds_between(d1, d2):
        return (datetime.datetime.fromtimestamp(d2) - datetime.datetime.fromtimestamp(d1)).total_seconds()

    @staticmethod
    def write(filename, data):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for item in data:
                l = [item.datetime, item.price]
                writer.writerow(l)

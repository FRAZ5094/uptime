import sys


def format_seconds(seconds, format_string):
    seconds = int(round(seconds, 0))
    days = int(seconds / (60 * 60 * 24))
    hours = int(seconds / (60 * 60)) - days * 24
    minutes = int(seconds / (60) - hours * 60 - days * 60 * 24)
    seconds = int(seconds - minutes * 60 - hours * 60 * 60 - days * 60 * 60 * 24)

    formatted_time = format_string.format(s=seconds, m=minutes, h=hours, d=days)

    return formatted_time


if __name__ == "__main__":
    time = sys.argv[1]
    formatted_time = format_seconds(float(time), "{d}:{h}:{m}")
    print(formatted_time)

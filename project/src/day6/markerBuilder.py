from utils import read_file


def init_build_start():
    return '', read_file('../resources/input_day_6.txt')[0]


def print_marker(marker: str, index: int):
    print('distinct characters:', marker, 'first marker:', index)


def build_start_of_packet_marker():
    marker, line = init_build_start()
    for index, char in enumerate(line):
        if len(marker) == 4:
            return print_marker(marker, index)
        else:
            marker = marker[marker.find(char) + 1:] + char


def build_start_of_message_marker():
    marker, line = init_build_start()
    for index, char in enumerate(line):
        if len(marker) == 14:
            return print_marker(marker, index)
        else:
            marker = marker[marker.find(char) + 1:] + char

import feedparser
import configparser


def handle_feed():
    entries = read_feed()

    return print_entries(entries)


def read_feed():
    url = determine_url_from_config()
    result = feedparser.parse(url)

    return result.entries


def determine_url_from_config():
    config = configparser.ConfigParser()
    config.read("config.ini")

    if 'url' in config['feed']:
        return config['feed']['url']
    else:
        raise KeyError("Please set the 'url' key to a (valid) RSS url in the 'config.ini' file!")


def print_entries(entries):
    for entry in entries:
        print(entry.title)
        print(entry.author)
        print(entry.published)
        print('Read it here: ' + entry.link)
        print('\n')


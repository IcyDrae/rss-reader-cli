import reader


if __name__ == "__main__":
    try:
        reader.handle_feed()
    except Exception as e:
        print(e)


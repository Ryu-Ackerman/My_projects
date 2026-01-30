command = dict_.get(sys.argv[1].lower())
        if command:
            command()
        else:
            print('Command not found, -h for help')
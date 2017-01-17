class Settings:
    def __init__(self, file):
        """Retrieves game settings from the given file and puts them into a
        dictionary.
        settings = Settings(file)"""

        load = open(file, "r")
        read_settings = load.readlines()

        self.settings = {}

        for line in read_settings:
            if line[0] != "#":
                values = line.strip("\n").split(":")
                values[1] = values[1].strip("\t ")

                try:
                    values[1] = int(values[1])
                    self.settings.update({values[0]: values[1]})
                except ValueError:
                    if values[1] == 'True':
                        self.settings.update({values[0]: True})
                    elif values[1] == 'False':
                        self.settings.update({values[0]: False})
                    else:
                        values[1] = str(values[1])
                        self.settings.update({values[0]: values[1]})

    def display(self):
        """Returns the settings dictionary."""
        return self.settings

    def access(self, value):
        """Returns the value of the given index."""
        return self.settings[value]

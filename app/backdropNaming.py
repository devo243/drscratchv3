from plugin import Plugin
import consts_plugins as consts


class BackdropNaming(Plugin):
    """
    Plugin that tracks how often backdrops default names (like Backdrop1, Backdrop2) are used in a scratch project
    """

    def __init__(self, filename):
        super().__init__(filename)
        self.total_default = 0
        self.list_default_names = []

    def finalize(self) -> str:
        """
        Output the default backdrop names found in the project
        """

        result = '{} default backdrop names found:\n'.format(self.total_default)

        for name in self.list_default_names:
            result += name
            result += "\n"

        return result

    def analyze(self):
        """
        Run and return the results from the SpriteNaming module.
        """

        for key, value in self.json_project.iteritems():
            if key == "targets":
                for dicc in value:
                    for dicc_key, dicc_value in dicc.iteritems():
                        if dicc_key == "costumes":
                            for backdrop in dicc_value:
                                for name_key, name_value in backdrop.iteritems():
                                    if name_key == "name":
                                        for default in consts.PLUGIN_NAMING_DEFAULT_NAMES:
                                            if default in name_value:
                                                self.total_default += 1
                                                self.list_default_names.append(name_value)


# def main(filename):
#     naming = BackdropNaming()
#     naming.analyze(filename)
#     return naming.finalize()





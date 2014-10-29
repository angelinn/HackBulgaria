from json import JSONEncoder


class PlaylistEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

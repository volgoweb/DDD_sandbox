class ICommand(object):
    def run(self, *args, **kwargs):
        raise NotImplementedError


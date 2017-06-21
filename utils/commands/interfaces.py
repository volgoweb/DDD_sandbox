class ICommand(object):
    def execute(self, *args, **kwargs):
        raise NotImplementedError

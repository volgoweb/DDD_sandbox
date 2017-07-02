class ICommand(object):
    @classmethod
    def get_command_type_name(cls):
        raise NotImplementedError

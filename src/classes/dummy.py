

class DummyPyRFCConnection:

    def __init__(self, **params):
        self.params = params
        self.__dummy__ = True
    
    def call(self, func_name, options, **params):
        return {
            'error': 'This is a dummy connection'
        }

    def close(self):
        return None

    def get_connection_attributes(self):
        return self.params

    def initialize_unit(self, background=True):
        return {}

    def get_unit_state(self, unit):
        return None

    def confirm_unit(self, unit):
        return None

    def destroy_unit(self, unit):
        return None

    def fill_and_submit_unit(self, unit, calls, queue_names=None, attributes=None):
        return None
    
    def get_function_description(self, func_name):
        return None
    
    def ping(self):
        return None

    def reset_server_context(self):
        return None

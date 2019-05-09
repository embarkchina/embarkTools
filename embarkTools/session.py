from tornado import gen
from notebook.services.sessions.sessionmanager import SessionManager


class PGSessionManager(SessionManager):

    @gen.coroutine
    def start_kernel_for_session(self, session_id, path, name, type, kernel_name):
        kernel_path = path
        kernel_id = yield gen.maybe_future(
            self.kernel_manager.start_kernel(path=kernel_path, kernel_name=kernel_name)
        )
        # py2-compat
        raise gen.Return(kernel_id)

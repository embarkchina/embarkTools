import os

from tornado import gen
from notebook.services.kernels.kernelmanager import MappingKernelManager
from notebook.utils import to_os_path


class PGKernelManager(MappingKernelManager):

    @gen.coroutine
    def start_kernel(self, kernel_id=None, path=None, **kwargs):
        if path:
            env = kwargs.pop('env', os.environ).copy()
            env["virtual_path"] = to_os_path(path, "/")
            kwargs["env"] = env
        kernel_id = yield super(PGKernelManager, self).start_kernel(kernel_id=kernel_id, path=path, **kwargs)
        # py2-compat
        raise gen.Return(kernel_id)

import shutil
from subprocess import PIPE, Popen

from proxmoxer.backends.command_base import CommandBaseBackend, CommandBaseSession


class LocalSession(CommandBaseSession):
    def _exec(self, cmd):
        proc = Popen(cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = proc.communicate(timeout=self.timeout)
        return stdout.decode(), stderr.decode()

    def upload_file_obj(self, file_obj, remote_path):
        with open(remote_path, "wb") as dest_fp:
            shutil.copyfileobj(file_obj, dest_fp)


class Backend(CommandBaseBackend):
    def __init__(self, *args, **kwargs):
        self.session = LocalSession(*args, **kwargs)

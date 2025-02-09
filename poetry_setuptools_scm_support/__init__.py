import json

from cleo.commands.command import Command
from poetry.plugins.application_plugin import ApplicationPlugin
from poetry.factory import Factory

from setuptools_scm import Version, Configuration
from setuptools_scm._get_version_impl import _get_version

from cleo.io.io import IO

from poetry.plugins.plugin import Plugin
from poetry.poetry import Poetry


class CalculateVersion(Command):

    name = "version-calculate"

    def handle(self) -> int:
        f = Factory()
        p = f.create_poetry()
        c = Configuration.from_file(str(p.file))
        v = _get_version(c)
        p.pyproject.data.item('project').update(version=v)
        p.pyproject.file.write(p.pyproject.data)

        return 0



def factory():
    return CalculateVersion()

class ScmPlugin(ApplicationPlugin):
    @property
    def commands(self) -> list[type[Command]]:
        return [CalculateVersion]

    def activate(self, application):
        application.command_loader.register_factory("version-calculate", factory)

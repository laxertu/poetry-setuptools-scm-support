from cleo.commands.command import Command
from cleo.io.inputs.argument import Argument
from poetry.plugins.application_plugin import ApplicationPlugin
from poetry.factory import Factory

from setuptools_scm import Configuration, ScmVersion
from setuptools_scm._get_version_impl import _get_version, parse_scm_version
from setuptools_scm.version import guess_next_date_ver

class CalculateVersion(Command):
    """
    Calculates the version of the package.

    command:name {version-calculate : Controls output format}
    """

    name = "version-calculate"
    description = "Calculates the version of the package relying on setuptools_scm"

    args_description = """
        scm: formats according to setuptools_scm default bahavior.
        date: formats using last commit distance and dirty tag
    """
    arguments = [
        Argument(name="format", description=args_description),
    ]


    def __do_default(self, c: Configuration) -> str:
        return _get_version(c)

    def __do_inc(self, c: Configuration) -> str:
        scm_version: ScmVersion = parse_scm_version(c)

        return scm_version.format_next_version(
            guess_next_date_ver,
            date_fmt="%Y.%m.%d",
            fmt="{guessed}.dev{distance}+{node}",
        )

    def handle(self) -> int:
        poetry = Factory().create_poetry()
        c = Configuration.from_file(str(poetry.file))
        v = self.__do_default(c)

        format_to_use = self.argument("format")
        if format_to_use == "scm":
            v = self.__do_default(c)
        elif format_to_use == "date":
            v = self.__do_inc(c)
        else:
            self.line_error(f"Unknown format: {format_to_use}")

        confirm = self.ask(f'Dumping version "{v}" [YES / no]', 'YES')
        if confirm == "YES":
            poetry.pyproject.data.item('project').update(version=v)
            poetry.pyproject.file.write(poetry.pyproject.data)

        return 0



def factory():
    return CalculateVersion()

class ScmPlugin(ApplicationPlugin):
    @property
    def commands(self) -> list[type[Command]]:
        return [CalculateVersion]

    def activate(self, application):
        application.command_loader.register_factory("version-calculate", factory)

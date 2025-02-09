from cleo.io.io import IO

from poetry.plugins.plugin import Plugin
from poetry.poetry import Poetry

from setuptools_scm import Version, Configuration

class ScmPlugin:
    def activate(self, poetry: Poetry, io: IO):
        io.write_line("Setting readme")
        poetry.package.version = "1.0.0"
        #current_version = Version(version=poetry.package.version)

        c = Configuration.from_file()

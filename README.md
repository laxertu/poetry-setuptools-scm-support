A Poetry plugin that integrates setuptools_scm <https://pypi.org/project/setuptools-scm/> to console

Updates pyproject.toml file version with a calculated one

The idea is to add a mechanism for managing dev builds' versions guaranteeing uniqueness of them at deploy time  

usage:

    poetry version-calculate [scm:date]
        scm: formats according to setuptools_scm default behavior.
        date: formats versions as date. Result format is {guessed}.dev{distance}+{node}, date format is Y.m.d

See setuptools_scm documentation and project sources for details


A Poetry plugin that integrates setuptools_scm <https://pypi.org/project/setuptools-scm/> to console

Updates pyproject.toml file version with a calculated one

Versions are calculated taking into account the distance between current commit and last tagged one, and current commit revision hash

Supported schemes are the main ones exposed by setuptools-scm:

**scm**: formats according to setuptools_scm get_version default behavior. e.g. 0.1.dev1+g1e0ede4.
**date**: formats current date and distance, e.g. 2025.4.1.1.dev1+g9d4edec . Scheme used is calver_by_date function
**branch**: Use branch based versioning of library. Scheme used is release_branch_semver_version function

examples:

    poetry version-calculate
Ouputs something like 1.0.1.dev1+g1e0ede4

    poetry version-calculate date
2025.4.1.1.dev1+g1e0ede4

**Note about date format:**

Two digits year is taken by default, you can change this behaviour making a previous git tag with a different supporten format, in this case for example 

    git tag 2025.4.1
 




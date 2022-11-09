import git
from git_contributions_importer import *

repo = git.Repo("C:/Users/Konst/AndroidStudioProjects/umnoepitanie.android")
mock_repo = git.Repo("C:/Users/Konst/AndroidStudioProjects/Umnoepitanie_mock")

importer = Importer([repo], mock_repo)
importer.set_author('konstantinlikes@gmail.com')

importer.import_repository()

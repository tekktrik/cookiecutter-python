# SPDX-FileCopyrightText: 2024 Alec Delaney
# SPDX-License-Identifier: MIT

"""Python script for initializing git repository (platform independent)"""

import os

initialize_git = "{{ cookiecutter.initialize_git }}".lower()

if initialize_git == "true" and os.system("git init"):
    raise OSError("An issue occurred initializing the git repository")

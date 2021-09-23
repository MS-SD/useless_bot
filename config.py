#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get(
        "MicrosoftAppId", "5a94fb87-09f6-476c-8c9e-11638ff19baa")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "2`E/NL@jh!8e7Zrf")

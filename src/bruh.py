# Copyright 2022 Simon1511@github
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

try:
    # >= 4.0.0
    from userbot.version import VERSION as hubot_version
except:
    # <= 3.0.4
    from userbot import VERSION as hubot_version


def isSupportedVersion(version: str) -> bool:
    try:
        bot_ver = tuple(map(int, hubot_version.split(".")))
        req_ver = tuple(map(int, version.split(".")))
        if bot_ver >= req_ver:
            return True
    except:
        pass
    return False


if not isSupportedVersion("5.0.1"):
    raise ValueError(f"Unsupported HyperUBot version ({hubot_version}). "
                      "Minimum required version is 5.0.1")

from userbot.sysutils.configuration import getConfig  # noqa: E402
from userbot.sysutils.event_handler import EventHandler  # noqa: E402
from userbot.sysutils.registration import (register_cmd_usage,  # noqa: E402
                                           register_module_desc,  # noqa: E402
                                           register_module_info)  # noqa: E402
from logging import getLogger  # noqa: E402
from asyncio import sleep  # noqa: E402

log = getLogger(__name__)
ehandler = EventHandler(log)
LOGGING = getConfig("LOGGING")


@ehandler.on(command="bruh", hasArgs=False, outgoing=True)
async def bruh(event):
    if not event.text[0].isalpha() and event.text[0] in ("."):
        t = "bruh"
        for j in range(15):
            t = t[:-1] + "h"
            await event.edit(t)

DESC = (
    "bruh "
)
register_cmd_usage(
    "bruh",
    "",
    "Funny animated bruh"
)
register_module_desc(DESC)
register_module_info(
    name="bruh",
    authors="Risen",
    version="1.0.0"
)

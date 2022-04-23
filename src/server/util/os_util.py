import os
import platform as _platform


class OsUtil:
    platform = os.name
    name = _platform.system()
    release = _platform.release()
    # distro = _platform.linux_distribution()

    def __init__(self):
        pass

    @classmethod
    def is_windows(cls):
        return "windows" in cls.name.lower()

    @classmethod
    def log_info(cls, logger):
        if not cls.is_linux():
            logger.warn("This OS is not supported")
        # Log info
        logger.debug("OS platform: %s", cls.platform)
        logger.debug("OS name: %s", cls.name)
        # if cls.is_linux():
            # logger.debug("OS distro: %s", cls.distro)
        logger.debug("OS release: %s", cls.release)

    @classmethod
    def is_linux(cls):
        return "linux" in cls.name.lower()

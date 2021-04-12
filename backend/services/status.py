from typing import Optional


class Status:
    __stt__ = dict()

    def check_status(self, key: str) -> Optional[str]:
        return self.__stt__.get(key)

    def update_status(self, key: str, status: str):
        self.__stt__.update({key: status})

    def get_all(self):
        return self.__stt__

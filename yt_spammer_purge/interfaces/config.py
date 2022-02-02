from dataclasses import dataclass

from xdgconfig import JsonConfig


@dataclass
class ListFile:
    filename: str


@dataclass
class Lists:
    domains: ListFile
    accounts: ListFile
    threads: ListFile
    whitelist: ListFile


@dataclass
class ConfigMeta:
    version_info: ListFile


@dataclass
class IConfig:
    lists: Lists
    meta: ConfigMeta

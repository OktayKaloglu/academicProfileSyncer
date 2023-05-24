from enum import Enum
import logging
from typing import Dict, List, TypedDict

"""This file list common types of this project"""


def set_logger(enable: bool):
    handler = logging.StreamHandler()  # output to console
    formatter = logging.Formatter("DATA_TYPES: %(levelname)s: %(message)s")
    handler.setFormatter(formatter)
    logger = logging.getLogger("TYPES:")
    logger.addHandler(handler)
    logger.setLevel(logging.INFO if enable else logging.CRITICAL)
    return logger


class ProxyMode(str, Enum):
    """Proxy list"""

    FREE_PROXIES = "FREE_PROXIES"


class OrganizationSource(str, Enum):
    """University source list"""

    EGE_UNIVERSITY = "https://ebp.ege.edu.tr/DereceProgramlari/Detay/1/31/2626/932001"
    DOKUZ_EYLUL_UNIVERSITY = (
        "https://debis.deu.edu.tr/ders-katalog/2021-2022/tr/bolum_1210_tr.html"
    )
    IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITESI = "https://ceng.iyte.edu.tr/tr/egitim/lisans-programi/lisans-egitim-plani-2018-ve-sonrasi/"


class PathBlacklist(list, Enum):
    EGE_UNIVERSITY = ["DersOgretimPlaniPdf", "sayfa"]
    DOKUZ_EYLUL_UNIVERSITY = [
        "havuz",
        "index",
        ".pdf",
        "bolum_1210_eng.html",
        "bolum_1210_tr.html",
        "tr-",
    ]
    IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITESI = [
        "lidya",
        "kisiler",
        "arastirma",
        "egitim",
        "iletisim",
        "education",
        "hakkinda",
        "fakulte-dersleri",
        "math",
    ]


class SpecialBaseURLEnding(str, Enum):
    DOKUZ_EYLUL_UNIVERSITY = "/ders-katalog/2021-2022/tr/"


class OrganizationParserStruct:
    def __init__(
        self,
        university: str,
        initials: str,
        blacklist: List[str],
        source: str,
        base_url_ending: str,
    ) -> None:
        self.university = university
        self.initials = initials
        self.blacklist = blacklist
        self.source = source
        self.base_url_ending = base_url_ending

    def __str__(self) -> str:
        return f"University: {self.university}\nInitials: {self.initials}\nBlacklist: {self.blacklist}\nSource: {self.source}\nBase URL Ending: {self.base_url_ending}"


def _build_organization_source(shorthand: str) -> OrganizationParserStruct:
    logger = set_logger(enable=True)
    if shorthand.lower() == "ege":
        logger.info("Selection is, Ege University proceeding.")
        builded = OrganizationParserStruct(
            university="Ege University",
            initials="ege",
            source=OrganizationSource.EGE_UNIVERSITY.value,
            blacklist=PathBlacklist.EGE_UNIVERSITY.value,
            base_url_ending=None,
        )
        return builded
    elif shorthand.lower() == "deu":
        logger.info("Selection is, Dokuz Eylul University proceeding.")
        builded = OrganizationParserStruct(
            university="Dokuz Eylul University",
            initials="deu",
            source=OrganizationSource.DOKUZ_EYLUL_UNIVERSITY.value,
            blacklist=PathBlacklist.DOKUZ_EYLUL_UNIVERSITY.value,
            base_url_ending=SpecialBaseURLEnding.DOKUZ_EYLUL_UNIVERSITY.value,
        )
        return builded
    elif shorthand.lower() == "iyte":
        logger.info("Selection is, Dokuz Eylul University proceeding.")
        builded = OrganizationParserStruct(
            university="Izmir Yuksek Teknoliji University",
            initials="iyte",
            source=OrganizationSource.IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITESI.value,
            blacklist=PathBlacklist.IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITESI.value,
            base_url_ending=None,
        )
        return builded

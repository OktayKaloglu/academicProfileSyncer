from enum import Enum
import logging
from typing import List, NamedTuple
from sources.detail_sources import (
    SelectorTuple,
    _selector_tuple_builder,
)

from sources.organization_sources import OrganizationSource, SpecialBaseURLEnding
from sources.path_blacklist import Blacklist


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


class Parser(NamedTuple):
    university: str
    initials: str
    blacklist: List[str]
    source: str
    base_url_ending: str = ""
    selectors: SelectorTuple = None

    def __str__(self) -> str:
        return (
            f"University: {self.university}\n"
            f"Initials: {self.initials}\n"
            f"Blacklist: {self.blacklist}\n"
            f"Source: {self.source}\n"
            f"Base URL Ending: {self.base_url_ending}\n"
            f"Base URL Ending: {self.selectors}\n"
        )


def _build_organization_source(shorthand: str) -> Parser | None:
    logger = set_logger(enable=True)
    # works
    if shorthand.lower() == "ege":
        logger.info("Selection is, Ege University proceeding.")
        return Parser(
            university="Ege University",
            initials="ege",
            source=OrganizationSource.EGE_UNIVERSITY.value,
            blacklist=Blacklist.EGE_UNIVERSITY.value,
            selectors=_selector_tuple_builder("ege"),
        )
    # works
    elif shorthand.lower() == "iyte":
        logger.info("Selection is, Izmir Yuksek Teknoloji University proceeding.")
        return Parser(
            university="Izmir Yuksek Teknoloji University",
            initials="iyte",
            source=OrganizationSource.IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITY.value,
            blacklist=Blacklist.IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITY.value,
            selectors=_selector_tuple_builder("iyte"),
        )
    # works
    elif shorthand.lower() == "ieu":
        return Parser(
            university="Izmir Ekonomi University",
            initials="ieu",
            source=OrganizationSource.IZMIR_EKONOMI_UNIVERSITY.value,
            blacklist=Blacklist.IZMIR_EKONOMI_UNIVERSITY.value,
            base_url_ending=SpecialBaseURLEnding.IZMIR_EKONOMI_UNIVERSITY.value,
            selectors=_selector_tuple_builder("ieu"),
        )
    # works
    elif shorthand.lower() == "deu":
        return Parser(
            university="Dokuz Eylul University",
            initials="deu",
            source=OrganizationSource.DOKUZ_EYLUL_UNIVERSITY.value,
            blacklist=Blacklist.DOKUZ_EYLUL_UNIVERSITY.value,
            base_url_ending=SpecialBaseURLEnding.DOKUZ_EYLUL_UNIVERSITY.value,
            selectors=_selector_tuple_builder("deu"),
        )
    # works
    elif shorthand.lower() == "yasar":
        logger.info("Selection is, Yasar University proceeding.")
        return Parser(
            university="Yasar University",
            initials="yasar",
            source=OrganizationSource.YASAR_UNIVERSITY.value,
            blacklist=Blacklist.YASAR_UNIVERSITY.value,
            selectors=_selector_tuple_builder("yasar"),
        )
    # works
    elif shorthand.lower() == "boun":
        logger.info("Selection is, Bogazici University proceeding.")
        return Parser(
            university="Bogazici University",
            initials="boun",
            source=OrganizationSource.BOGAZICI_UNIVERSITY.value,
            blacklist=Blacklist.BOGAZICI_UNIVERSITY.value,
            selectors=_selector_tuple_builder("boun"),
        )
    # works
    elif shorthand.lower() == "bilkent":
        logger.info("Selection is, Bilkent University proceeding.")
        return Parser(
            university="Bilkent University",
            initials="bilkent",
            source=OrganizationSource.BILKENT_UNIVERSITY.value,
            blacklist=Blacklist.BILKENT_UNIVERSITY.value,
            base_url_ending=SpecialBaseURLEnding.BILKENT_UNIVERSITY.value,
            selectors=_selector_tuple_builder("bilkent"),
        )
    # works
    elif shorthand.lower() == "odtu":
        logger.info("Selection is, Orta Dogu Teknik University proceeding.")
        return Parser(
            university="Orta Dogu Teknik University",
            initials="odtu",
            source=OrganizationSource.ORTA_DOGU_TEKNIK_UNIVERSITY.value,
            blacklist=Blacklist.ORTA_DOGU_TEKNIK_UNIVERSITY.value,
            selectors=_selector_tuple_builder("odtu"),
        )
    # buggy
    elif shorthand.lower() == "itu":
        logger.info("Selection is, Istanbul Teknik University proceeding.")
        return Parser(
            university="Istanbul Teknik University",
            initials="itu",
            source=OrganizationSource.ISTANBUL_TEKNIK_UNIVERSITY.value,
            blacklist=Blacklist.ISTANBUL_TEKNIK_UNIVERSITY.value,
            selectors=_selector_tuple_builder("itu"),
        )
    elif shorthand.lower() == "yeditepe":
        logger.info("Selection is, Yeditepe University proceeding.")
        return Parser(
            university="Yeditepe University",
            initials="yeditepe",
            source=OrganizationSource.YEDITEPE_UNIVERSITY.value,
            blacklist=Blacklist.YEDITEPE_UNIVERSITY.value,
            selectors=_selector_tuple_builder("yeditepe"),
        )
    return None


# elif shorthand.lower() == "ikcu":
#     raise NotImplemented("Single page")
#     builded = OrganizationParserStruct(
#         university="Izmir Katip Celebi University",
#         initials="ikcu",
#         source=OrganizationSource.IZMIR_KATIP_CELEBI_UNIVERSITY.value,
#         blacklist=PathBlacklist.IZMIR_KATIP_CELEBI_UNIVERSITY.value,
#         instructor_selector=InstructorNameSelector.IZMIR_KATIP_CELEBI_UNIVERSITY.value,
#         course_code_selector=CourseCodeSelector.IZMIR_KATIP_CELEBI_UNIVERSITY.value,
#         course_name_selector=CourseNameSelector.IZMIR_KATIP_CELEBI_UNIVERSITY.value,
#         uses_single_page=True,
#     )
#     return builded

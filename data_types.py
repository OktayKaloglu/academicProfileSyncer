from enum import Enum
import logging
from typing import TypedDict

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


class CourseSource(str, Enum):
    """View pages"""

    COURSE_DETAIL_PAGE = "COURSE_DETAIL_PAGE"
    GENERAL_VIEW_PAGE = "GENERAL_VIEW_PAGE"


class BlackList(list, Enum):
    EGE_UNIVERSITY = ["DersOgretimPlaniPdf", "sayfa"]
    DOKUZ_EYLUL_UNIVERSITY = [
        "havuz",
        "index",
        ".pdf",
        "bolum_1210_eng.html",
        "bolum_1210_tr.html",
    ]


class SpecialBaseURLEnding(str, Enum):
    DOKUZ_EYLUL_UNIVERSITY = "/ders-katalog/2021-2022/tr/"


class FilterSource(str, Enum):
    """Filter list"""

    FILTER_URL_EXCEPT_ALL = "FILTER_URL_EXCEPT_ALL"


class Organization(TypedDict, total=False):
    """Organization class"""

    source: OrganizationSource
    filter_source: FilterSource
    name: str
    # email_domain: str
    # homepage: str


class Course(TypedDict, total=False):
    """Course class"""

    course_name: str
    organization: Organization
    container_type: str


# Define at least 3 source
def _define_organization_source(shorthand: str):
    logger = set_logger(enable=True)
    if shorthand.lower() == "ege":
        logger.info("Selection is, Ege University proceeding.")
        return (
            OrganizationSource.EGE_UNIVERSITY.value,
            BlackList.EGE_UNIVERSITY.value,
            None,
        )
    elif shorthand.lower() == "deu":
        logger.info("Selection is, Dokuz Eylul University proceeding.")
        return (
            OrganizationSource.DOKUZ_EYLUL_UNIVERSITY.value,
            BlackList.DOKUZ_EYLUL_UNIVERSITY.value,
            SpecialBaseURLEnding.DOKUZ_EYLUL_UNIVERSITY.value,
        )

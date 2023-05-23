from enum import Enum
from typing import TypedDict

"""This file list common types of this project"""


class ProxyMode(str, Enum):
    """Proxy list"""

    FREE_PROXIES = "FREE_PROXIES"


class OrganizationSource(str, Enum):
    """University source list"""

    EGE_UNIVERSITY = "https://ebp.ege.edu.tr/DereceProgramlari/Detay/1/31/2626/932001"


class CourseSource(str, Enum):
    """View pages"""

    COURSE_DETAIL_PAGE = "COURSE_DETAIL_PAGE"
    GENERAL_VIEW_PAGE = "GENERAL_VIEW_PAGE"


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


def _define_organization_source(shorthand: str):
    if shorthand.lower() == "ege":
        return OrganizationSource.EGE_UNIVERSITY.value

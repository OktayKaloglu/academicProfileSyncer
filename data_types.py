from enum import Enum
from typing import TypedDict


class ProxyMode(str, Enum):
    FREE_PROXIES = "FREE_PROXIES"


class OrganizationSource(str, Enum):
    EGE_UNIVERSITY = "https://ebp.ege.edu.tr/DereceProgramlari/Detay/1/31/2626/932001"


class CourseSource(str, Enum):
    COURSE_DETAIL_PAGE = "COURSE_DETAIL_PAGE"
    GENERAL_VIEW_PAGE = "GENERAL_VIEW_PAGE"


class FilterSource(str, Enum):
    FILTER_URL_EXCEPT_ALL = "FILTER_URL_EXCEPT_ALL"


class Organization(TypedDict, total=False):
    source: OrganizationSource
    filter_source: FilterSource
    name: str
    # email_domain: str
    # homepage: str


class Course(TypedDict, total=False):
    course_name: str
    organization: Organization
    container_type: str

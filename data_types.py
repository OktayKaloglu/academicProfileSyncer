from enum import Enum
import logging
from typing import List, NamedTuple
from sources.course_sources import CourseCodeSelector, CourseNameSelector
from sources.instructor_sources import InstructorNameSelector

from sources.organization_sources import OrganizationSource
from sources.path_blacklist import PathBlacklist
from sources.url_sources import SpecialBaseURLEnding


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


class OrganizationParserStruct(NamedTuple):
    university: str
    initials: str
    blacklist: List[str]
    source: str
    base_url_ending: str = ""
    instructor_selector: str = ""
    course_code_selector: str = ""
    course_name_selector: str = ""

    def __str__(self) -> str:
        return (
            f"University: {self.university}\n"
            f"Initials: {self.initials}\n"
            f"Blacklist: {self.blacklist}\n"
            f"Source: {self.source}\n"
            f"Base URL Ending: {self.base_url_ending}\n"
            f"Instructor Selector: {self.instructor_selector}\n"
            f"Course Code Selector: {self.course_code_selector}\n"
            f"Course Name Selector: {self.course_name_selector}\n"
        )


def _build_organization_source(shorthand: str) -> OrganizationParserStruct | None:
    logger = set_logger(enable=True)
    if shorthand.lower() == "ege":
        logger.info("Selection is, Ege University proceeding.")
        builded = OrganizationParserStruct(
            university="Ege University",
            initials="ege",
            source=OrganizationSource.EGE_UNIVERSITY.value,
            blacklist=PathBlacklist.EGE_UNIVERSITY.value,
            instructor_selector=InstructorNameSelector.EGE_UNIVERSITY.value,
            course_code_selector=CourseCodeSelector.EGE_UNIVERSITY.value,
            course_name_selector=CourseNameSelector.EGE_UNIVERSITY.value,
        )
        return builded
    elif shorthand.lower() == "iyte":
        logger.info("Selection is, Dokuz Eylul University proceeding.")
        builded = OrganizationParserStruct(
            university="Izmir Yuksek Teknoliji University",
            initials="iyte",
            source=OrganizationSource.IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITESI.value,
            blacklist=PathBlacklist.IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITY.value,
            instructor_selector=InstructorNameSelector.IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITY.value,
            course_code_selector=CourseCodeSelector.IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITY.value,
            course_name_selector=CourseNameSelector.IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITY.value,
        )
        return builded
    elif shorthand.lower() == "ieu":
        builded = OrganizationParserStruct(
            university="Izmir Ekonomi University",
            initials="ieu",
            source=OrganizationSource.IZMIR_EKONOMI_UNIVERSITY.value,
            blacklist=PathBlacklist.IZMIR_EKONOMI_UNIVERSITY.value,
            base_url_ending=SpecialBaseURLEnding.IZMIR_EKONOMI_UNIVERSITY.value,
            instructor_selector=InstructorNameSelector.IZMIR_EKONOMI_UNIVERSITY.value,
            course_code_selector=CourseCodeSelector.IZMIR_EKONOMI_UNIVERSITY.value,
            course_name_selector=CourseNameSelector.IZMIR_EKONOMI_UNIVERSITY.value,
        )
        return builded
    return None


# elif shorthand.lower() == "yasar":
#     logger.info("Selection is, Yasar University proceeding.")
#     raise NotImplemented("Instructor regex doesn't work!")
#     builded = OrganizationParserStruct(
#         university="Yasar University",
#         initials="yasar",
#         source=OrganizationSource.YASAR_UNIVERSITY.value,
#         blacklist=PathBlacklist.YASAR_UNIVERSITY.value,
#         instructor_selector=InstructorNameSelector.YASAR_UNIVERSITY.value,
#         course_code_selector=CourseCodeSelector.YASAR_UNIVERSITY.value,
#         course_name_selector=CourseNameSelector.YASAR_UNIVERSITY.value,
#         uses_single_line_information_on_course=True,
#         uses_single_line_information_on_instructor=True,
#         single_line_course_regex=SingleLineCourseRegex.YASAR_UNIVERSITY,
#         single_line_instructor_regex=SingleLineInstructorRegex.YASAR_UNIVERSITY,
#     )
#     return builded

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


# elif shorthand.lower() == "deu":
#     logger.info("Selection is, Dokuz Eylul University proceeding.")
#     raise NotImplemented("WHY THIS SHIT NOT WORKING!??!?")
#     builded = OrganizationParserStruct(
#         university="Dokuz Eylul University",
#         initials="deu",
#         source=OrganizationSource.DOKUZ_EYLUL_UNIVERSITY.value,
#         blacklist=PathBlacklist.DOKUZ_EYLUL_UNIVERSITY.value,
#         base_url_ending=SpecialBaseURLEnding.DOKUZ_EYLUL_UNIVERSITY.value,
#         instructor_selector=InstructorNameSelector.DOKUZ_EYLUL_UNIVERSITY.value,
#         course_code_selector=CourseCodeSelector.DOKUZ_EYLUL_UNIVERSITY.value,
#         course_name_selector=CourseNameSelector.DOKUZ_EYLUL_UNIVERSITY.value,
#     )
#     return builded

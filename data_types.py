from enum import Enum
import logging
from typing import List, NamedTuple


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
    YASAR_UNIVERSITY = "https://ce.yasar.edu.tr/dersler/"
    IZMIR_KATIP_CELEBI_UNIVERSITY = (
        "https://ceng.ikcu.edu.tr/S/16843/lisans-ogretim-plani"
    )
    IZMIR_EKONOMI_UNIVERSITY = "https://ce.ieu.edu.tr/tr/curr"


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
    IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITY = [
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
    YASAR_UNIVERSITY = [
        "kadro",
        "ders-plani",
        "progCourses",
        "mufredat",
        "arastirma",
        "lisans-form",
        "program-ciktilari",
        "program-yeterlilikleri",
        "konferans",
        "calistay",
        "paneller",
        "bolum-seminerleri",
        "egitim-seminerleri",
        "tarihce",
        "misyon",
        "altyapi",
        "etkinlikler",
        "category",
        "fotografvideo",
        "iletisim",
    ]
    IZMIR_KATIP_CELEBI_UNIVERSITY = []
    IZMIR_EKONOMI_UNIVERSITY = []


class ExactURLBlacklist(list, Enum):
    EGE_UNIVERSITY = ["https://ebp.ege.edu.tr/DereceProgramlari/1"]
    DOKUZ_EYLUL_UNIVERSITY = []
    IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITY = [
        "https://ceng.iyte.edu.tr/tr/",
        "https://lidya.iyte.edu.tr/",
    ]
    YASAR_UNIVERSITY = [
        "http://haber.yasar.edu.tr/",
        "http://tv.yasar.edu.tr/",
        "http://radyu.yasar.edu.tr/",
        "http://www.yasar.edu.tr/universitemiz-fotograflar",
        "http://www.yasar.edu.tr/erisim-kurumsal-gorsel",
        "http://www.yasar.edu.tr/birlikte-degerliyiz/",
        "http://www.investinizmir.com/tr/",
        "http://obs.yasar.edu.tr/",
        "http://yasarid.yasar.edu.tr/",
        "http://mail.yasar.edu.tr/",
        "http://oim.yasar.edu.tr",
        "http://kutuphane.yasar.edu.tr/yordam.htm",
        "https://www.facebook.com/",
        "https://www.twitter.com/",
        "https://plus.google.com/104633562508422409370/posts",
        "https://www.youtube.com/user/YasarUniversity",
        "https://instagram.com/yasaruniv/",
        "https://ce.yasar.edu.tr/",
        "https://ce.yasar.edu.tr/en/",
        "http://aday.yasar.edu.tr",
        "http://feng.yasar.edu.tr",
        "http://www.yasar.edu.tr",
        "https://ce.yasar.edu.tr/dersler/",
        "https://ce.yasar.edu.tr/staj/",
        "https://compmscwt.yasar.edu.tr"
        "https://compmscwot.yasar.edu.tr"
        "https://compphd.yasar.edu.tr",
        "https://compmscwt.yasar.edu.tr",
        "https://compmscwot.yasar.edu.tr",
        "https://compphd.yasar.edu.tr",
    ]
    IZMIR_KATIP_CELEBI_UNIVERSITY = []
    IZMIR_EKONOMI_UNIVERSITY = []


class InstructorNameSelector(str, Enum):
    IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITY = "div > div.wpb_column.vc_col-sm-3 > div.iyte_ins-ass > div.stm-teacher-bio.stm-teacher-bio_trainer > div > div > div.stm-teacher-bio__title > a"
    EGE_UNIVERSITY = "#wrapper > div > div > div > div > div > div > p:nth-child(17)"
    DOKUZ_EYLUL_UNIVERSITY = "body > div.main-wrapper > div.container > div.span-18.last > table:nth-child(12) > tbody > tr:nth-child(2) > td > p"
    YASAR_UNIVERSITY = (
        "#main-content > div > div > div > div > div > ul > li:nth-child(1) > strong"
    )
    IZMIR_KATIP_CELEBI_UNIVERSITY = "#main-wrapper > section.content-container > section > div > div > div > div > div.row.form-group > div > div > div > table > tbody > tr:nth-child(6) > td:nth-child(9) > h4 > span > span > strong"


class CourseCodeSelector(str, Enum):
    IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITY = "div > div.vc_col-sm-9 > h1"
    EGE_UNIVERSITY = "#wrapper > div > div > div > div > div > div > table:nth-child(5) > tbody > tr > td:nth-child(1)"
    DOKUZ_EYLUL_UNIVERSITY = "body > div.main-wrapper > div.container > div.span-18.last > table:nth-child(3) > tbody > tr > td > table > tbody > tr:nth-child(2) > td:nth-child(1)"
    YASAR_UNIVERSITY = "#main-content > div > div > div > div > div > h3"
    IZMIR_KATIP_CELEBI_UNIVERSITY = "#main-wrapper > section.content-container > section > div > div > div > div > div.row.form-group > div > div > div > table > tbody > tr:nth-child(6) > td:nth-child(1) > h4 > span > span > strong"


class CourseNameSelector(str, Enum):
    IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITY = "div > div.vc_col-sm-9 > h2"
    EGE_UNIVERSITY = "#wrapper > div > div > div > div > div > div > table:nth-child(5) > tbody > tr > td:nth-child(2)"
    DOKUZ_EYLUL_UNIVERSITY = "body > div.main-wrapper > div.container > div.span-18.last > table:nth-child(3) > tbody > tr > td > table > tbody > tr:nth-child(2) > td:nth-child(2)"
    YASAR_UNIVERSITY = "#main-content > div > div > div > div > div > h3"
    IZMIR_KATIP_CELEBI_UNIVERSITY = "#main-wrapper > section.content-container > section > div > div > div > div > div.row.form-group > div > div > div > table > tbody > tr:nth-child(6) > td:nth-child(2) > h4 > span > span > strong"


class SpecialBaseURLEnding(str, Enum):
    DOKUZ_EYLUL_UNIVERSITY = "/ders-katalog/2021-2022/tr/"
    IZMIR_EKONOMI_UNIVERSITY = "/tr/"


class SingleLineCourseRegex(str, Enum):
    YASAR_UNIVERSITY = r"((?:\w+\s+)*\w+\s*\d+)\s+(.*?)\s+–.*"


class SingleLineInstructorRegex(str, Enum):
    YASAR_UNIVERSITY = r",\s*([^,]+)$"


class OrganizationParserStruct(NamedTuple):
    university: str
    initials: str
    blacklist: List[str]
    exact_url_blacklist: List[str]
    source: str
    base_url_ending: str = ""
    instructor_selector: str = ""
    course_code_selector: str = ""
    course_name_selector: str = ""
    uses_single_line_information_on_course: bool = False
    uses_single_line_information_on_instructor: bool = False
    single_line_course_regex: str = ""
    single_line_instructor_regex: str = ""
    uses_single_page: bool = False

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
            f"Exact Blacklist: {self.exact_url_blacklist}\n"
            f"Uses single line information on course: {self.uses_single_line_information_on_course}\n"
            f"Uses single line information on instructor: {self.uses_single_line_information_on_instructor}\n"
            f"Single line course regex: {self.single_line_course_regex}\n"
            f"Single line instructor regex: {self.single_line_instructor_regex}\n"
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
            exact_url_blacklist=ExactURLBlacklist.EGE_UNIVERSITY.value,
        )
        return builded
    elif shorthand.lower() == "deu":
        logger.info("Selection is, Dokuz Eylul University proceeding.")
        raise NotImplemented("buggy?")
        builded = OrganizationParserStruct(
            university="Dokuz Eylul University",
            initials="deu",
            source=OrganizationSource.DOKUZ_EYLUL_UNIVERSITY.value,
            blacklist=PathBlacklist.DOKUZ_EYLUL_UNIVERSITY.value,
            base_url_ending=SpecialBaseURLEnding.DOKUZ_EYLUL_UNIVERSITY.value,
            instructor_selector=InstructorNameSelector.DOKUZ_EYLUL_UNIVERSITY.value,
            course_code_selector=CourseCodeSelector.DOKUZ_EYLUL_UNIVERSITY.value,
            course_name_selector=CourseNameSelector.DOKUZ_EYLUL_UNIVERSITY.value,
            exact_url_blacklist=ExactURLBlacklist.DOKUZ_EYLUL_UNIVERSITY.value,
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
            exact_url_blacklist=ExactURLBlacklist.IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITY.value,
        )
        return builded
    elif shorthand.lower() == "yasar":
        logger.info("Selection is, Yasar University proceeding.")
        raise NotImplemented("Instructor regex doesn't work!")
        builded = OrganizationParserStruct(
            university="Yasar University",
            initials="yasar",
            source=OrganizationSource.YASAR_UNIVERSITY.value,
            blacklist=PathBlacklist.YASAR_UNIVERSITY.value,
            instructor_selector=InstructorNameSelector.YASAR_UNIVERSITY.value,
            course_code_selector=CourseCodeSelector.YASAR_UNIVERSITY.value,
            course_name_selector=CourseNameSelector.YASAR_UNIVERSITY.value,
            exact_url_blacklist=ExactURLBlacklist.YASAR_UNIVERSITY.value,
            uses_single_line_information_on_course=True,
            uses_single_line_information_on_instructor=True,
            single_line_course_regex=SingleLineCourseRegex.YASAR_UNIVERSITY,
            single_line_instructor_regex=SingleLineInstructorRegex.YASAR_UNIVERSITY,
        )
        return builded
    elif shorthand.lower() == "ikcu":
        raise NotImplemented("Single page")
        builded = OrganizationParserStruct(
            university="Izmir Katip Celebi University",
            initials="ikcu",
            source=OrganizationSource.IZMIR_KATIP_CELEBI_UNIVERSITY.value,
            blacklist=PathBlacklist.IZMIR_KATIP_CELEBI_UNIVERSITY.value,
            instructor_selector=InstructorNameSelector.IZMIR_KATIP_CELEBI_UNIVERSITY.value,
            course_code_selector=CourseCodeSelector.IZMIR_KATIP_CELEBI_UNIVERSITY.value,
            course_name_selector=CourseNameSelector.IZMIR_KATIP_CELEBI_UNIVERSITY.value,
            exact_url_blacklist=ExactURLBlacklist.IZMIR_KATIP_CELEBI_UNIVERSITY.value,
            uses_single_page=True,
        )
        return builded
    elif shorthand.lower() == "ieu":
        builded = OrganizationParserStruct(
            university="Izmir Ekonomi University",
            initials="ieu",
            source=OrganizationSource.IZMIR_EKONOMI_UNIVERSITY.value,
            blacklist=PathBlacklist.IZMIR_EKONOMI_UNIVERSITY.value,
            base_url_ending=SpecialBaseURLEnding.IZMIR_EKONOMI_UNIVERSITY.value,
            instructor_selector=InstructorNameSelector.IZMIR_KATIP_CELEBI_UNIVERSITY.value,
            course_code_selector=CourseCodeSelector.IZMIR_KATIP_CELEBI_UNIVERSITY.value,
            course_name_selector=CourseNameSelector.IZMIR_KATIP_CELEBI_UNIVERSITY.value,
            exact_url_blacklist=ExactURLBlacklist.IZMIR_EKONOMI_UNIVERSITY.value,
        )
        return builded
    return None


# file_path = "path/to/your/file.txt"  # Replace with the actual file path
# Read the file and store each line as a separate string in a list
# with open(file_path, 'r') as file:
#    lines = [line.strip() for line in file]

# Print the list of strings
#    print(lines)

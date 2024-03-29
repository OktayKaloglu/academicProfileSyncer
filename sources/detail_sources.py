from enum import Enum
from typing import List, NamedTuple
import csv
import os


class INSelector(str, Enum):
    """Instructor Name Selector"""

    IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITY = "div.stm-teacher-bio__title"
    EGE_UNIVERSITY = "#wrapper > div > div > div > div > div > div > p:nth-child(17)"
    DOKUZ_EYLUL_UNIVERSITY = "body > div.main-wrapper > div.container > div.span-18.last > p > table:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > p:nth-child(1)"
    YASAR_UNIVERSITY = (
        "#main-content > div > div > div > div > div > ul > li:nth-child(1) > strong"
    )
    IZMIR_KATIP_CELEBI_UNIVERSITY = "#main-wrapper > section.content-container > section > div > div > div > div > div.row.form-group > div > div > div > table > tbody > tr:nth-child(6) > td:nth-child(9) > h4 > span > span > strong"
    IZMIR_EKONOMI_UNIVERSITY = "#coordinator_list > li > a"
    BOGAZICI_UNIVERSITY = "#block-system-main > div > div > div > div > div > div.panel-pane.pane-views.pane-course-offerings > div > div > div > table > tbody > tr.odd.views-row-first > td.views-field.views-field-field-instructor"
    BILKENT_UNIVERSITY = "td table tr td font i a"
    ORTA_DOGU_TEKNIK_UNIVERSITY = "#content > div.col-content > div > div > table > tr:nth-child(7) > td:nth-child(2) > a"
    ISTANBUL_TEKNIK_UNIVERSITY = ".dersBilgileri"
    YEDITEPE_UNIVERSITY = "div > div > div.field.field-name-field-dersin-koordinatoru.field-type-node-reference.field-label-inline.clearfix > div.field-items > div > a"
    GALATASARAY_UNIVERSITY = "#tab-icerik > div > div.table-responsive > div > table > tbody > tr:nth-child(4) > td:nth-child(2) > span:nth-child(1)"
    BAHCESEHIR_UNIVERSITY = 'td:contains("Dersin Koordinatörü:") + td'
    YILDIZ_TEKNIK_UNIVERSITY = "#coursegrid > tr:nth-child(2) > td > a"
    ISTANBUL_BILGI_UNIVERSITY = "body > div.container > div:nth-child(3) > div:nth-child(3) > table > tbody > tr:nth-child(4) > td:nth-child(2) > a:nth-child(1)"
    GEBZE_TEKNIK_UNIVERSITY = "#content > div:nth-child(7) > table:nth-child(1) > tbody > tr:nth-child(6) > td.dyazi1 > a"
    ANKARA_UNIVERSITY = "#content_sec > div > div.col1 > div > table:nth-child(10) > tbody > tr:nth-child(6) > td:nth-child(2)"
    BASKENT_UNIVERSITY = "#mytable > tr:nth-child(6) > td > a:nth-child(1)"
    ISTANBUL_UNIVERSITY_CERRAHPASA = "body > div > div > div > div > div.col-lg-9.col-md-9 > div > div:nth-child(1) > div.panel-body > table > tbody > tr:nth-child(5) > td:nth-child(4) > a"
    MARMARA_UNIVERSITY = (
        "#bbicerik > div > table > tbody > tr:nth-child(1) > td:nth-child(4)"
    )


class CCSelector(str, Enum):
    """Course Code Selector"""

    IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITY = "h1.course-code"
    EGE_UNIVERSITY = "#wrapper > div > div > div > div > div > div > table:nth-child(5) > tbody > tr > td:nth-child(1)"
    DOKUZ_EYLUL_UNIVERSITY = "body > div.main-wrapper > div.container > div.span-18.last > p > table:nth-child(2) tr > td > p > table > tbody > tr:nth-child(2) > td:nth-child(1)"
    YASAR_UNIVERSITY = "#main-content > div > div > div > div > div > h3"
    IZMIR_KATIP_CELEBI_UNIVERSITY = "#main-wrapper > section.content-container > section > div > div > div > div > div.row.form-group > div > div > div > table > tbody > tr:nth-child(6) > td:nth-child(1) > h4 > span > span > strong"
    IZMIR_EKONOMI_UNIVERSITY = "div:nth-child(3) > div >  div.col-xs-12.col-sm-12.col-md-8.col-lg-9.text-primary-color-content > div > div > div:nth-child(2) > table > tr:nth-child(2) > td:nth-child(1) > div"
    BOGAZICI_UNIVERSITY = "#page-title > span"
    BILKENT_UNIVERSITY = "td table tr td h2"
    ORTA_DOGU_TEKNIK_UNIVERSITY = "#content > div.col-content > div > div > h2"
    ISTANBUL_TEKNIK_UNIVERSITY = ".dersler h1"
    YEDITEPE_UNIVERSITY = "div > div > fieldset:nth-child(1) > div > div.field.field-name-field-ders-kodu.field-type-text.field-label-inline.clearfix > div.field-items > div"
    GALATASARAY_UNIVERSITY = "#tab-icerik > div > div.table-responsive > table:nth-child(1) > tbody > tr > td:nth-child(1)"
    BAHCESEHIR_UNIVERSITY = ".rows td:nth-child(1)"
    YILDIZ_TEKNIK_UNIVERSITY = "#courseshortinfo > td:nth-child(2)"
    ISTANBUL_BILGI_UNIVERSITY = "body > div.container > div:nth-child(3) > div.table-responsive > table > tbody > tr > td:nth-child(2)"
    GEBZE_TEKNIK_UNIVERSITY = "#content > div:nth-child(7) > table:nth-child(1) > tbody > tr:nth-child(5) > td.dyazi1"
    ANKARA_UNIVERSITY = "#body_content_lblDersKodu"
    BASKENT_UNIVERSITY = "#ders_bilgi > table > tr:nth-child(2) > td:nth-child(2)"
    ISTANBUL_UNIVERSITY_CERRAHPASA = "body > div > div > div > div > div.col-lg-9.col-md-9 > div > div:nth-child(1) > div.panel-body > table > tbody > tr:nth-child(1) > td:nth-child(4)"
    MARMARA_UNIVERSITY = "#bbicerik > table > tr:nth-child(2) > td:nth-child(2)"


class CNSelector(str, Enum):
    """Course Name Selector"""

    IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITY = "h2.course-name"
    EGE_UNIVERSITY = "#wrapper > div > div > div > div > div > div > table:nth-child(5) > tbody > tr > td:nth-child(2)"
    DOKUZ_EYLUL_UNIVERSITY = "body > div.main-wrapper > div.container > div.span-18.last > p > table:nth-child(2) tr > td > p > table > tbody > tr:nth-child(2) > td:nth-child(2)"
    YASAR_UNIVERSITY = "#main-content > div > div > div > div > div > h3"
    IZMIR_KATIP_CELEBI_UNIVERSITY = "#main-wrapper > section.content-container > section > div > div > div > div > div.row.form-group > div > div > div > table > tbody > tr:nth-child(6) > td:nth-child(2) > h4 > span > span > strong"
    IZMIR_EKONOMI_UNIVERSITY = "#course_name"
    BOGAZICI_UNIVERSITY = "#page-title > span"
    BILKENT_UNIVERSITY = "td table tr td h2"
    ORTA_DOGU_TEKNIK_UNIVERSITY = "#content > div.col-content > div > div > h2"
    ISTANBUL_TEKNIK_UNIVERSITY = ".dersler h1"
    YEDITEPE_UNIVERSITY = "#page-title"
    GALATASARAY_UNIVERSITY = "#tab-icerik > div > div.table-responsive > table:nth-child(1) > tbody > tr > td:nth-child(2)"
    BAHCESEHIR_UNIVERSITY = ".rows td:nth-child(2)"
    YILDIZ_TEKNIK_UNIVERSITY = "#courseshortinfo > td:nth-child(1) > strong"
    ISTANBUL_BILGI_UNIVERSITY = "body > div.container > div:nth-child(3) > div.table-responsive > table > tbody > tr > td:nth-child(3)"
    GEBZE_TEKNIK_UNIVERSITY = "#content > div:nth-child(7) > table:nth-child(1) > tbody > tr:nth-child(4) > td.dyazi1"
    ANKARA_UNIVERSITY = "#body_content_lblDersAdi"
    BASKENT_UNIVERSITY = "#ders_bilgi > table > tr:nth-child(2) > td:nth-child(1)"
    ISTANBUL_UNIVERSITY_CERRAHPASA = "body > div > div > div > div > div.col-lg-9.col-md-9 > div > div:nth-child(1) > div.panel-body > table > tbody > tr:nth-child(1) > td:nth-child(2)"
    MARMARA_UNIVERSITY = "#bbicerik > table > tr:nth-child(2) > td:nth-child(3)"


class CISelector(str, Enum):
    """Course info Selector"""

    EGE_UNIVERSITY = "#wrapper > div > div > div > div > div > div > p:nth-child(14)"
    IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITY = (
        "div > div.vc_col-sm-9 > div > div > div > div > div > div > p"
    )
    IZMIR_EKONOMI_UNIVERSITY = "td.sy-label + td"
    DOKUZ_EYLUL_UNIVERSITY = "div.span-18.last >p:nth-of-type(6)"
    YASAR_UNIVERSITY = "div > div > div > div > div > p:nth-child(2)"
    BOGAZICI_UNIVERSITY = 'div.field-item.odd[property="content:encoded"] p'
    BILKENT_UNIVERSITY = "td table tr td font"
    ORTA_DOGU_TEKNIK_UNIVERSITY = "#courseObjectives"
    ISTANBUL_TEKNIK_UNIVERSITY = ".dersler p"
    YEDITEPE_UNIVERSITY = "#div > div > div.field.field-name-field-dersin-amaci.field-type-text-long.field-label-above > div.field-items > div"


class Selector(NamedTuple):
    selector: str = ""
    regex_filter: str = ""
    regex_index: int = 0

    def __str__(self) -> str:
        return f"Selector: {self.selector}\n" f"Regex Filter: {self.regex_filter}\n"


class SelectorTuple(NamedTuple):
    instructor_selector: Selector = Selector()
    course_name_selector: Selector = Selector()
    course_code_selector: Selector = Selector()
    course_info_selector: Selector = Selector()
    course_info_selector_index: int = 0
    instructor_index: int = 0
    course_name_index: int = 0
    course_code_index: int = 0

    def __str__(self) -> str:
        return (
            f"Instructor selector: {self.instructor_selector}\n"
            f"Course Name selector: {self.course_name_selector}\n"
            f"Course Code selector: {self.course_code_selector}\n"
            f"Course info selector: {self.course_info_selector}\n"
            f"Instructor index: {self.instructor_index}\n"
            f"Course code index: {self.course_code_index}\n"
            f"Course name index: {self.course_name_index}\n"
            f"Course info index: {self.course_info_selector_index}\n"
        )


class ExportObjectCourse:
    def __init__(
        self,
        organization,
        initials,
        href,
        course_code,
        course_name,
        course_info,
        instructor,
    ):
        self.organization = organization
        self.initials = initials
        self.href = href
        self.course_code = course_code
        self.course_name = course_name
        self.course_info = course_info
        self.instructor = instructor

    def to_list(self):
        return [
            self.organization,
            self.initials,
            self.href,
            self.course_code,
            self.course_name,
            self.course_info,
            self.instructor,
        ]

    def __str__(self):
        return f"ExportObjectCourse(organization={self.organization}, initials={self.initials}, href={self.href}, course_code={self.course_code}, course_name={self.course_name}, course_info={self.course_info})"


def write_object_to_csv(
    obj: List[ExportObjectCourse], filename: str, write_headers=True
):
    file_exists = os.path.isfile(filename)
    with open(filename, mode="a" if file_exists else "w", newline="") as file:
        writer = csv.writer(file)
        if write_headers and (not file_exists or file.tell() == 0):
            writer.writerow(
                [
                    "organization",
                    "initials",
                    "href",
                    "course_code",
                    "course_name",
                    "course_info",
                    "instructor",
                ]
            )
        for i in obj:
            writer.writerow(i.to_list())


def _selector_tuple_builder(initials: str):
    if initials.lower() == "ege":
        return SelectorTuple(
            instructor_selector=Selector(selector=INSelector.EGE_UNIVERSITY.value),
            course_code_selector=Selector(selector=CCSelector.EGE_UNIVERSITY.value),
            course_name_selector=Selector(selector=CNSelector.EGE_UNIVERSITY.value),
            course_info_selector=Selector(selector=CISelector.EGE_UNIVERSITY.value),
        )
    elif initials.lower() == "iyte":
        return SelectorTuple(
            instructor_selector=Selector(
                selector=INSelector.IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITY.value
            ),
            course_code_selector=Selector(
                selector=CCSelector.IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITY.value
            ),
            course_name_selector=Selector(
                selector=CNSelector.IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITY.value
            ),
            course_info_selector=Selector(
                selector=CISelector.IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITY.value
            ),
        )

    elif initials.lower() == "ieu":
        return SelectorTuple(
            instructor_selector=Selector(
                selector=INSelector.IZMIR_EKONOMI_UNIVERSITY.value
            ),
            course_code_selector=Selector(
                selector=CCSelector.IZMIR_EKONOMI_UNIVERSITY.value
            ),
            course_name_selector=Selector(
                selector=CNSelector.IZMIR_EKONOMI_UNIVERSITY.value
            ),
            course_info_selector=Selector(
                selector=CISelector.IZMIR_EKONOMI_UNIVERSITY.value
            ),
            course_info_selector_index=9,
        )

    elif initials.lower() == "deu":
        return SelectorTuple(
            instructor_selector=Selector(
                selector=INSelector.DOKUZ_EYLUL_UNIVERSITY.value,
            ),
            course_code_selector=Selector(
                selector=CCSelector.DOKUZ_EYLUL_UNIVERSITY.value
            ),
            course_name_selector=Selector(
                selector=CNSelector.DOKUZ_EYLUL_UNIVERSITY.value
            ),
            course_info_selector=Selector(
                selector=CISelector.DOKUZ_EYLUL_UNIVERSITY.value
            ),
            instructor_index=2,
        )

    elif initials.lower() == "yasar":
        return SelectorTuple(
            instructor_selector=Selector(selector=INSelector.YASAR_UNIVERSITY.value),
            course_code_selector=Selector(
                selector=CCSelector.YASAR_UNIVERSITY.value,
                regex_filter=r"[A-Z]{2,4}\s\d{4}",
            ),
            course_name_selector=Selector(
                selector=CNSelector.YASAR_UNIVERSITY.value,
                regex_filter=r"\b[A-Z]{2,4}\s\d{4}\s(.+?)\s–",
                regex_index=1,
            ),
            course_info_selector=Selector(selector=CISelector.YASAR_UNIVERSITY.value),
        )
    elif initials.lower() == "boun":
        return SelectorTuple(
            instructor_selector=Selector(selector=INSelector.BOGAZICI_UNIVERSITY.value),
            course_code_selector=Selector(
                selector=CCSelector.BOGAZICI_UNIVERSITY.value,
                regex_filter=r"[A-Za-z]{2,4}\s\d{2,4}[a-zA-Z]?",
            ),
            course_name_selector=Selector(
                selector=CNSelector.BOGAZICI_UNIVERSITY.value,
                regex_filter=r"[A-Za-z]{2,4}\s\d{2,4}[a-zA-Z]?\s*(.+)",
                regex_index=1,
            ),
            course_info_selector=Selector(
                selector=CISelector.BOGAZICI_UNIVERSITY.value,
            ),
        )
    elif initials.lower() == "bilkent":
        return SelectorTuple(
            instructor_selector=Selector(selector=INSelector.BILKENT_UNIVERSITY.value),
            course_code_selector=Selector(
                selector=CCSelector.BILKENT_UNIVERSITY.value,
                regex_filter=r"[A-Za-z]{2,4}\s\d{2,4}[a-zA-Z]?",
            ),
            course_name_selector=Selector(
                selector=CNSelector.BILKENT_UNIVERSITY.value,
                regex_filter=r"[A-Za-z]{2,4}\s\d{2,4}[a-zA-Z]?\s*(.+)",
                regex_index=1,
            ),
            course_info_selector=Selector(
                selector=CISelector.BILKENT_UNIVERSITY.value,
            ),
        )
    elif initials.lower() == "odtu":
        return SelectorTuple(
            instructor_selector=Selector(
                selector=INSelector.ORTA_DOGU_TEKNIK_UNIVERSITY.value
            ),
            course_code_selector=Selector(
                selector=CCSelector.ORTA_DOGU_TEKNIK_UNIVERSITY.value,
                regex_filter=r"[A-Z]{2,4}\d{2,4}",
            ),
            course_name_selector=Selector(
                selector=CNSelector.ORTA_DOGU_TEKNIK_UNIVERSITY.value,
                regex_filter=r"[A-Za-z]{2,4}\d{2,4}[a-zA-Z]?\s*(.+)",
                regex_index=1,
            ),
            course_info_selector=Selector(
                selector=CISelector.ORTA_DOGU_TEKNIK_UNIVERSITY.value,
            ),
        )
    elif initials.lower() == "itu":
        return SelectorTuple(
            instructor_selector=Selector(
                selector=INSelector.ISTANBUL_TEKNIK_UNIVERSITY.value
            ),
            course_code_selector=Selector(
                selector=CCSelector.ISTANBUL_TEKNIK_UNIVERSITY.value,
                regex_filter=r"[A-Za-z]{2,4}\s\d{2,4}[a-zA-Z]?",
            ),
            course_name_selector=Selector(
                selector=CNSelector.ISTANBUL_TEKNIK_UNIVERSITY.value,
                regex_filter=r"[A-Za-z]{2,4}\s\d{2,4}[a-zA-Z]?\s*(.+)",
                regex_index=1,
            ),
            course_info_selector=Selector(
                selector=CISelector.ISTANBUL_TEKNIK_UNIVERSITY.value,
            ),
        )
    elif initials.lower() == "yeditepe":
        return SelectorTuple(
            instructor_selector=Selector(selector=INSelector.YEDITEPE_UNIVERSITY.value),
            course_code_selector=Selector(
                selector=CCSelector.YEDITEPE_UNIVERSITY.value
            ),
            course_name_selector=Selector(
                selector=CNSelector.YEDITEPE_UNIVERSITY.value
            ),
            course_info_selector=Selector(
                selector=CISelector.ISTANBUL_TEKNIK_UNIVERSITY.value,
            ),
        )
    elif initials.lower() == "gsu":
        return SelectorTuple(
            instructor_selector=Selector(
                selector=INSelector.GALATASARAY_UNIVERSITY.value
            ),
            course_code_selector=Selector(
                selector=CCSelector.GALATASARAY_UNIVERSITY.value
            ),
            course_name_selector=Selector(
                selector=CNSelector.GALATASARAY_UNIVERSITY.value
            ),
        )
    elif initials.lower() == "bau":
        return SelectorTuple(
            instructor_selector=Selector(
                selector=INSelector.BAHCESEHIR_UNIVERSITY.value
            ),
            course_code_selector=Selector(
                selector=CCSelector.BAHCESEHIR_UNIVERSITY.value
            ),
            course_name_selector=Selector(
                selector=CNSelector.BAHCESEHIR_UNIVERSITY.value
            ),
        )
    elif initials.lower() == "ytu":
        return SelectorTuple(
            instructor_selector=Selector(
                selector=INSelector.YILDIZ_TEKNIK_UNIVERSITY.value
            ),
            course_code_selector=Selector(
                selector=CCSelector.YILDIZ_TEKNIK_UNIVERSITY.value
            ),
            course_name_selector=Selector(
                selector=CNSelector.YILDIZ_TEKNIK_UNIVERSITY.value
            ),
        )
    elif initials.lower() == "bilgi":
        return SelectorTuple(
            instructor_selector=Selector(
                selector=INSelector.ISTANBUL_BILGI_UNIVERSITY.value,
                regex_filter=r"^([^,]+)",
            ),
            course_code_selector=Selector(
                selector=CCSelector.ISTANBUL_BILGI_UNIVERSITY.value
            ),
            course_name_selector=Selector(
                selector=CNSelector.ISTANBUL_BILGI_UNIVERSITY.value
            ),
        )
    elif initials.lower() == "gtu":
        return SelectorTuple(
            instructor_selector=Selector(
                selector=INSelector.GEBZE_TEKNIK_UNIVERSITY.value,
            ),
            course_code_selector=Selector(
                selector=CCSelector.GEBZE_TEKNIK_UNIVERSITY.value
            ),
            course_name_selector=Selector(
                selector=CNSelector.GEBZE_TEKNIK_UNIVERSITY.value
            ),
        )
    elif initials.lower() == "ankara":
        return SelectorTuple(
            instructor_selector=Selector(
                selector=INSelector.ANKARA_UNIVERSITY.value,
            ),
            course_code_selector=Selector(selector=CCSelector.ANKARA_UNIVERSITY.value),
            course_name_selector=Selector(selector=CNSelector.ANKARA_UNIVERSITY.value),
        )
    elif initials.lower() == "baskent":
        return SelectorTuple(
            instructor_selector=Selector(
                selector=INSelector.BASKENT_UNIVERSITY.value,
            ),
            course_code_selector=Selector(selector=CCSelector.BASKENT_UNIVERSITY.value),
            course_name_selector=Selector(selector=CNSelector.BASKENT_UNIVERSITY.value),
        )
    elif initials.lower() == "iuc":
        return SelectorTuple(
            instructor_selector=Selector(
                selector=INSelector.ISTANBUL_UNIVERSITY_CERRAHPASA.value,
            ),
            course_code_selector=Selector(
                selector=CCSelector.ISTANBUL_UNIVERSITY_CERRAHPASA.value
            ),
            course_name_selector=Selector(
                selector=CNSelector.ISTANBUL_UNIVERSITY_CERRAHPASA.value
            ),
        )
    elif initials.lower() == "marmara":
        return SelectorTuple(
            instructor_selector=Selector(
                selector=INSelector.MARMARA_UNIVERSITY.value,
            ),
            course_code_selector=Selector(selector=CCSelector.MARMARA_UNIVERSITY.value),
            course_name_selector=Selector(selector=CNSelector.MARMARA_UNIVERSITY.value),
        )

from enum import Enum
from typing import NamedTuple


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
    instructor_index: int = 0
    course_name_index: int = 0
    course_code_index: int = 0

    def __str__(self) -> str:
        return (
            f"Instructor selector: {self.instructor_selector}\n"
            f"Course Name selector: {self.course_name_selector}\n"
            f"Course Code selector: {self.course_code_selector}\n"
            f"Instructor index: {self.instructor_index}\n"
            f"Course code index: {self.course_code_index}\n"
            f"Course name index: {self.course_name_index}\n"
        )


def _selector_tuple_builder(initials: str):
    if initials.lower() == "ege":
        return SelectorTuple(
            instructor_selector=Selector(selector=INSelector.EGE_UNIVERSITY.value),
            course_code_selector=Selector(selector=CCSelector.EGE_UNIVERSITY.value),
            course_name_selector=Selector(selector=CNSelector.EGE_UNIVERSITY.value),
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

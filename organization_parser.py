from data_types import Course


class OrganizationParser:

    def __init__(self, nav):
        self.nav = nav
        self.sections = []

    def get_course_details(self, __data) -> Course:
        course: Course = {'container_type': 'Author'}

        # if isinstance(__data, str):
        #    course['course_name'] = __data
        #    course['source'] = CourseSource.COURSE_DETAIL_PAGE
        # else:
        #    course['source'] = CourseSource.GENERAL_VIEW_PAGE
        #    course['course_name'] = re.findall(_CITATIONAUTHRE, __data('a')[0]['href'])[0]

    def _find_tag_class_name(self, __data, tag, text):
        elements = __data.find_all(tag)
        for element in elements:
            if 'class' in element.attrs and text in element.attrs['class'][0]:
                return element.attrs['class'][0]

    def _fill_basics(self, soup, author):
        # author['name'] = soup.find('div', id='gsc_prf_in').text
        pass

    def fill(self, organization, url, sections: list = []):
        try:
            sections = [section.lower() for section in sections]
            sections.sort(reverse=True)
            soup = self.nav_get_soup(url)

        except Exception as e:
            raise (e)

        return organization

    def __repr__(self):
        return self.__str__()

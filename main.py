import datetime
import click
from navigator import Navigator
from data_types import _build_organization_source
from sources.detail_sources import ExportObjectCourse, write_object_to_csv


def generate_filename(appendix: str):
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{current_datetime}-{appendix}.csv"
    return filename


@click.command(no_args_is_help=True)
@click.option(
    "--debug",
    is_flag=True,
    show_default=True,
    default=False,
    help="Run with debug configuration",
)
@click.option(
    "-n", "--name", help="University name for parsing option", metavar="<name>"
)
@click.option(
    "--use-proxy",
    is_flag=True,
    show_default=True,
    help="Use proxy for client session",
)
@click.option(
    "-d",
    "--disable-course-extractor",
    is_flag=True,
    show_default=False,
    help="Disable course extract flag, disables course extraction tool",
)
def uni_parser(name, debug, use_proxy, disable_course_extractor):
    if name is None:
        raise NotImplemented("Should be all universities")
    navigator = Navigator(disable_course_flag=disable_course_extractor)

    if debug:
        navigator.set_logger(enable=True)

    if use_proxy:
        navigator.use_proxy()

    organization = _build_organization_source(name)
    # parsed_objs = navigator.search_organization(organization)
    obj = ExportObjectCourse(
        organization="asd",
        initials="Asd231j",
        href="Asdasd",
        course_code="asdasda",
        course_info="Asdasdsa",
        course_name="asdasasdsa",
        instructor="asdasdsadsa",
    )
    asd = []
    asd.append(obj)
    filename = generate_filename(organization.initials)
    write_object_to_csv(asd, filename)


if __name__ == "__main__":
    # pylint: disable = no-value-for-parameter   # isables the pylint check for the next line
    uni_parser()

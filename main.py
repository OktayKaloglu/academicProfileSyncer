import click
from navigator import Navigator
from data_types import _build_organization_source


@click.command()
@click.option(
    "--debug",
    is_flag=True,
    show_default=True,
    default=False,
    help="Run with debug configuration",
)
@click.option("-n", "--name", help="University name for parsing option")
@click.option(
    "-u",
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
    help="Disable course extract flag, when this flag is set CLI doesn't going to parse coure detail pages",
)
def uni_parser(name, debug, use_proxy, disable_course_extractor):
    print(disable_course_extractor)
    if name is None:
        raise NotImplemented("Should be all universities")
    navigator = Navigator(disable_course_flag=disable_course_extractor)

    if debug:
        navigator.set_logger(enable=True)

    if use_proxy:
        navigator.use_proxy()

    organization = _build_organization_source(name)
    print(organization)
    a = navigator.search_organization(organization)
    for i in a:
        print(i)


if __name__ == "__main__":
    # pylint: disable = no-value-for-parameter   # isables the pylint check for the next line
    uni_parser()

import click
from navigator import Navigator
from data_types import _build_organization_source


@click.command(no_args_is_help=True)
@click.option(
    "--debug",
    is_flag=True,
    show_default=True,
    default=False,
    help="Run with debug configuration",
)
@click.option(
    "-u", "--university", help="University name for parsing option", metavar="<name>"
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
    urls = navigator.search_organization(organization)
    for i in urls:
        print(i)


if __name__ == "__main__":
    # pylint: disable = no-value-for-parameter   # isables the pylint check for the next line
    uni_parser()

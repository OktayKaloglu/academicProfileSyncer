from navigator import Navigator
import click
from data_types import _build_organization_source


@click.command()
@click.option(
    "--debug",
    is_flag=True,
    show_default=True,
    default=False,
    help="Start with debugging prints",
)
@click.option("--name", help="University name for parsing option")
@click.option(
    "-u",
    "--use-proxy",
    is_flag=True,
    show_default=True,
    help="Use proxy for client session",
)
def uni_parser(name, debug, use_proxy):
    if name == None:
        raise NotImplemented("Should be all universities")
    navigator = Navigator()

    if debug:
        navigator.set_logger(enable=True)

    if use_proxy:
        navigator.use_proxy()

    organization = _build_organization_source(name)
    listOutput = navigator.search_organization(organization)


if __name__ == "__main__":
    uni_parser()

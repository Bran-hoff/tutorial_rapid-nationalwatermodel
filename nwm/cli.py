import click

from . import __version__
from .nwm import Nwm


@click.command()
@click.version_option(version=__version__)
@click.option(
    "--source",
    required=True,
    default="hydroshare",
    help="Source name for data download, including hydroshare and noaa.",
    show_default="HydroShare"
)
@click.option(
    "--archive",
    default="harvey",
    help="Archive type for data download, including harvey, irma, florence, and rolling.",
    show_default="harvey"
)
@click.option(
    "--config",
    default="short_range",
    help="Configuration type for data download, including short_range, medium_range, long_range, and analysis_assim.",
    show_default="short_range"
)
@click.option(
    "--geom",
    default="channel_rt",
    help="Geometry type for data download, including channel_rt, land, reservoir, and forcing.",
    show_default="channel_rt"
)
@click.option(
    "--variable",
    default="streamflow",
    help="Variable type for data download, such as streamflow and velocity.",
    show_default="streamflow"
)
@click.option(
    "--comid",
    metavar="<list>",
    default=5781915,
    help="COMID for a river reach e.g. [5781915] or a grid [1635, 2030]",
    show_default="5781915",
)
@click.option(
    "--init_time",
    metavar="<int>",
    default=0,
    help="Initiation time for data download, value between 0 an 23 hr.",
    show_default="0",
)
@click.option(
    "--time_lag",
    metavar="<int>",
    default=0,
    help="Time lag for data download, value between 0, 6, or 12 hr.",
    show_default="0",
)
@click.option(
    "--start_date",
    metavar="YYYY-MM-DD",
    default="2017-08-23",
    help="Start date for data download.",
    show_default="2017-08-23",
)
@click.option(
    "--end_date",
    metavar="YYYY-MM-DD",
    default="2017-09-06",
    help="End date for data download.",
    show_default="2017-09-06",
)
@click.option(
    "--output",
    default="",
    help="Output file path to store downloaded data.",
    show_default="",
)
def main(source, archive, config, geom, variable, comid, init_time, time_lag, start_date, end_date, output):
    if source == 'hydroshare':
        dataset = Nwm().get_data_from_hs(archive=archive, config=config, geom=geom,variable=variable, comid=comid,
                                         init_time=init_time, time_lag=time_lag, start_date=start_date,
                                         end_date=end_date, output=output)
        print(dataset)
    elif source == 'noaa':
        Nwm().get_data_from_noaa()
    else:
        raise ValueError('Wrong source name.')

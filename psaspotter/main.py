import logging
import click

from psaspotter.extract import  ExtractPlatformSpecificDir, Report
from psaspotter.projects import Project

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.INFO, filename='log.txt')
logger = logging.getLogger(__name__)

# See https://click.palletsprojects.com/en/8.1.x/documentation/#help-texts
CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}

@click.command(context_settings=CONTEXT_SETTINGS)
@click.option(
    "--output",
    "-o",
    help="The output CSV file where the usage of Platform-Specific APIs related to the repository will be stored. "
    "By default, the information will written to the standard output.",
    type=click.Path(exists=False, file_okay=True, dir_okay=False, writable=True),
)

@click.option(
    "--commit",
    "-c",
    help="The commit reference (i.e., commit SHA or TAG) to be considered for the extraction."
    "It is important to note that each commit references a local project.", 
    type=str,
)
@click.option(
    "--repository-name",
    "-n",
    help="The name's project to be considered for the extraction."
    "It is important to note that the name references a local project.", 
    type=str,
)
@click.option(
    '--platforms',
    '-p',
    help="The Platform-specific API group to figure out.", 
    type=click.Choice(['all', 'main', 'proprietary', 'unix-like','standards', 'webassembly', 'mobile'], case_sensitive=True), is_flag=False, flag_value="Flag", default="all"
)
@click.option(
    "--filter",
    "-f",
    help="The JSON file with the configuration of Platform-Specific APIs that will be filter. "
    "By default, this option is mandatory to option --platforms.",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, writable=False),
)
@click.argument(
    "repository",
    type=str,
)
def main(
    output, 
    repository, 
    commit, 
    platforms,
    filter,
    repository_name
):
    """Extract the usage of Platform-Specific APIs from a single Git repository `REPOSITORY`.
    The Git repository can be local or remote. In the latter case, it will be pulled
    locally in the folder `data`.
    Every extracted Platform-Specific APIs will be written in the CSV file given to `-o`,
    or in the standard output if not specified.

    Example of usage:
    psaspotter myRepository -n myRepositoryName -o output.csv
    """
    load_apis = ''
    if(filter):
        load_apis = filter
    else:
        if(platforms):
            load_apis = f'psaspotter/apis-{platforms}.json'
        #    if platforms == 'all':
        #         load_apis = 'psaspotter/apis-all.json'
        #    if platforms == 'main':
        #         load_apis = 'psaspotter/apis-main.json'
    logger.info(f'load: {load_apis}')
    project = Project.build(repository, repository_name, commit, load_apis)
    logger.info(project)
    extract = ExtractPlatformSpecificDir(project)
    apis = extract.touch()
    logger.info(f"Collected: {len(apis)} Platform-Specific APIs.")
    report = Report.build(output)
    report.write(apis) 
    logger.info(f"Hash: {project.project_hash}")
if __name__ == "__main__":
    main()
    
# - all - all  
# - OS (Linux, Windows, macOS, and Unix) => por default, a ferramenta computa esses dados
# - unix-like (BSD, OpenBSD, FreeBSD, DragonFlyBSD, and NetBSD)
# - other-os (Oracle Solaris, IBM AIX, and VxWorks) + android
    # - mobile OS (Android)
# - webassembly platforms (Emscripten and WASI)
# - standards (POSIX and pthreads)   

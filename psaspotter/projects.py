import logging
import os.path
from dataclasses import dataclass
from psaspotter.get_repo import Repo

logger = logging.getLogger(__name__)

@dataclass
class Project: 
    """A project representation."""
    project_name: str
    project_hash: str
    project_url_remote: str
    directory: str
    platform_apis_filename: str = 'psaspotter/apis-all.json'
    
    def read_apis(self):
        # import json
        # # file = open('psae/apis-os.json')
        # file = open(self.platform_apis_filename)
        # return json.load(file)
        from importlib.resources import files
        import json
        json_text = files("psaspotter").joinpath("apis-all.json").read_text()
        return  json.loads(json_text)
    
    def build(repository, project_name, commit, load_apis):
        # clone the repository if it does not exist
        try:
            if not os.path.exists(repository): #remote
                return ProjectRemote(load_apis).clone(repository, commit)
            else: #local
                return ProjectLocal(load_apis, repository, project_name, commit)
        except (Exception) as exception:
            logger.error("Could not read repository at '%s'", repository)
            logger.debug(exception)
    
class ProjectLocal (Project):
    def __init__(self, load_apis, directory: str = "temp", project_name: str="project_name", project_hash: str = "project_hash"):
        super().__init__(project_name, project_hash, project_url_remote=directory, directory=directory, platform_apis_filename=load_apis)
        
class ProjectRemote(Project):
    def __init__(self, load_apis, directory: str="data", project_name: str="project_name", project_hash: str = "project_hash"):
        super().__init__(project_name, project_hash, project_url_remote="https://github.com/", directory=directory, platform_apis_filename=load_apis)
        
    def clone(self, repository, commit):
        if "https://github.com/" in repository:
            self.project_url_remote = repository
        else:
            self.project_url_remote = f'https://github.com/{repository}'   
        # dir = tempfile.TemporaryDirectory(dir=".")
        dir = f'{self.directory}/{self.project_url_remote.replace("https://github.com/", "")}'
        logger.info(f'Cloning started in {dir}.')
        repo = Repo(self.project_url_remote)
        
        if commit:
            local = repo.clone_at_commit(dir, commit)
        else:
            local = repo.clone_at(dir)
            # local = repo.clone_at(dir)    
        logger.info(f'Cloning in {local}.')
        self.project_name = repo.repo_name()
        self.project_hash = local.commit_head()
        self.directory = local.path()
        logger.info(f'DEGUB name: {self.project_name}, hash: {self.project_hash}, local: {self.directory}')
        logger.info(f'Cloning of project {self.project_name} completed. ')
        return self
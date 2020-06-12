from pymongo import MongoClient
import os
def populate_database(projects):
    pass

class DataBase:
    def __init__(self, database=None, projects=None):
        self.client = MongoClient("mongo", username="alex",
                                  password=os.environ["MONGO_INITDB_ROOT_PASSWORD"], port=27017)
        if database is not None:
            self.db = self.client[database]
        else:
            self.db = self.client.projects

        if projects is not None:
            project = self.db.project
            prepared_projects = self.prepare_projects(projects)
            for i in range(len(prepared_projects)):
                if not self.check_project_exists(prepared_projects[i]["repo_name"]):
                    result = project.insert_one(prepared_projects[i])
                    print('single posts: {0}'.format(result))
                else:
                    continue


    def prepare_projects(self, projects):
        project_inserts = []
        for data in projects:
            project_data = {
                "repo_name": data['repo_name'],
                "readme": data['readme'],
                "repo_url": data['repo_url']
            }
            project_inserts.append(project_data)
        return project_inserts

    def add_projects(self, projects):
        pass
    def get_projects(self):
        projects = []
        project_collection = self.db.project
        cursor = project_collection.find({})
        for document in cursor:
            print(document)
            projects.append(document)
        return projects

    def get_project(self, project_name):
        project_collection = self.db.project
        query = {"repo_name": project_name}
        cursor = project_collection.find(query)
        for i in cursor:
            return i

    def check_project_exists(self, project_name):
        project_collection = self.db.project
        if project_collection.find({"repo_name": project_name}).count() > 0:
            return True
        else:
            return False
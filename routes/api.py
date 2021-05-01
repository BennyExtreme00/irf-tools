

import base64
import psutil
import os
import requests
from urllib3 import disable_warnings
import configparser

disable_warnings()


def get_process_by_name(process_name):
    while True:
        for proc in psutil.process_iter():
            try:
                if process_name in proc.name():
                    return proc
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

class LeagueOfLegendsClientAPI(object):
    def __init__(self):
        print('Waiting league client...')
        self.process = get_process_by_name("LeagueClientUx")

        self.lockfile = open(os.path.join(self.process.cwd(), "lockfile"), 'r').read()

        split = self.lockfile.split(":")

        self.process_name = split[0]
        self.process_id = split[1]
        self.port = split[2]
        self.password = str(base64.b64encode(("riot:" + split[3]).encode("utf-8")), "utf-8")
        self.protocol = split[4]

    def get(self, path):
        return requests.get(
            self.protocol + "://127.0.0.1:" + self.port + path,
            verify=False,
            headers={"Authorization": "Basic " + self.password}
        )

    def post(self, path, json=None):
        return requests.post(
            self.protocol + "://127.0.0.1:" + self.port + path,
            verify=False,
            headers={"Authorization": "Basic " + self.password},
            json=json
        )
    def postBoost(self, path, json=None):
        return requests.post(
            self.protocol + "://127.0.0.1:" + self.port + path,
            verify=False,
            headers={"Authorization": "Basic " + self.password},
            params=json
        )
    def postNick(self, path, json=None):
        return requests.post(
            self.protocol + "://127.0.0.1:" + self.port + path,
            verify=False,
            headers={"Authorization": "Basic " + self.password},
            params=json
        )
    def put(self, path, json=None):
        return requests.put(
            self.protocol + "://127.0.0.1:" + self.port + path,
            verify=False,
            headers={"Authorization": "Basic " + self.password},
            json=json
        )

    def delete(self, path, json=None):
        return requests.delete(
            self.protocol + "://127.0.0.1:" + self.port + path,
            verify=False,
            headers={"Authorization": "Basic " + self.password},
            json=json
        )

    def head(self, path, json=None):
        return requests.head(
            self.protocol + "://127.0.0.1:" + self.port + path,
            verify=False,
            headers={"Authorization": "Basic " + self.password},
            json=json
        )

    def patch(self, path, json=None):
        return requests.patch(
            self.protocol + "://127.0.0.1:" + self.port + path,
            verify=False,
            headers={"Authorization": "Basic " + self.password},
            json=json
        )



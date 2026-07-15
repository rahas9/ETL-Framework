"""
=============================================================
Project     : Enterprise Metadata Driven ETL Framework
File        : main.py
Author      : Shaik Rahamat

Description:
    Entry point of the ETL Framework.

Responsibilities
----------------
1. Initialize Logger
2. Read all metadata JSON files
3. Execute ETL for each metadata file
4. Handle Exceptions
=============================================================
"""

import os

from src.core.logger import Logger
from src.services.etl_service import ETLService


class ETLFramework:

    def __init__(self, config_folder):

        self.logger = Logger().get_logger()

        self.config_folder = config_folder


    def get_config_files(self):
        """
        Read all metadata JSON files from config folder
        """

        config_files = []

        if not os.path.exists(self.config_folder):
            raise FileNotFoundError(
                f"Config Folder Not Found : {self.config_folder}"
            )

        for file in os.listdir(self.config_folder):

            if file.endswith(".json"):

                config_files.append(

                    os.path.join(
                        self.config_folder,
                        file
                    )

                )

        return sorted(config_files)


    def run(self):

        try:

            self.logger.info("=" * 80)
            self.logger.info("Metadata Driven ETL Framework Started")
            self.logger.info("=" * 80)

            config_files = self.get_config_files()

            if len(config_files) == 0:

                self.logger.warning(
                    "No metadata json files found."
                )

                return

            self.logger.info(
                f"Total Metadata Files : {len(config_files)}"
            )

            for config_file in config_files:

                self.logger.info("-" * 80)
                self.logger.info(
                    f"Processing Metadata : {config_file}"
                )

                etl = ETLService(config_file)

                etl.run()

                self.logger.info(
                    f"Completed : {config_file}"
                )

            self.logger.info("=" * 80)
            self.logger.info("All Metadata Files Processed Successfully")
            self.logger.info("=" * 80)

        except Exception as ex:

            self.logger.exception(ex)

            raise


def main():

    CONFIG_FOLDER = "config"

    framework = ETLFramework(
        CONFIG_FOLDER
    )

    framework.run()


if __name__ == "__main__":

    main()

"""
=============================================================
Project     : Enterprise Metadata Driven ETL Framework
File        : main.py
Author      : Shaik Rahamat

Description:
    Entry point of the application.

Responsibilities:
    1. Initialize Logger
    2. Read Metadata Configuration Files
    3. Execute ETL Service
    4. Handle Exceptions
=============================================================
"""

import os

from src.core.logger import Logger
from src.core.config_reader import ConfigReader
from src.services.etl_service import ETLService


class ETLFramework:
    """
    Main Framework Controller
    """

    def __init__(self, config_folder: str):

        self.logger = Logger().get_logger()

        self.config_folder = config_folder

    def get_config_files(self):
        """
        Returns all metadata JSON files
        """

        config_files = []

        for file in os.listdir(self.config_folder):

            if file.endswith(".json"):

                config_files.append(

                    os.path.join(
                        self.config_folder,
                        file
                    )

                )

        return config_files

    def process_config(self, config_file):

        self.logger.info("=" * 80)
        self.logger.info(f"Reading Configuration : {config_file}")

        reader = ConfigReader(config_file)

        metadata = reader.read()

        etl_service = ETLService(metadata)

        etl_service.run()

        self.logger.info(f"Completed : {config_file}")
        self.logger.info("=" * 80)

    def run(self):

        try:

            self.logger.info("ETL Framework Started")

            config_files = self.get_config_files()

            if not config_files:

                self.logger.warning(
                    "No metadata configuration files found."
                )

                return

            for config_file in config_files:

                self.process_config(config_file)

            self.logger.info("ETL Framework Completed Successfully")

        except Exception as ex:

            self.logger.exception(ex)

            raise


def main():
    """
    Application Entry Point
    """

    CONFIG_FOLDER = "config"

    framework = ETLFramework(CONFIG_FOLDER)

    framework.run()


if __name__ == "__main__":

    main()

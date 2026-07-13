#
"""
=========================================================
Project : Enterprise Metadata Driven ETL Framework
File    : main.py
Author  : Shaik Rahamat
Purpose : Entry point for ETL Framework
=========================================================
"""

from src.core.logger import Logger
from src.core.config_reader import ConfigReader

from src.authentication.auth import Authentication

from src.api.api_client import APIClient
from src.api.pagination import Pagination

from src.processing.json_flattener import JSONFlattener
from src.processing.mapping_engine import MappingEngine
from src.processing.transformer import Transformer
from src.processing.validation import Validator

from src.loaders.s3_loader import S3Loader


class ETLFramework:

    def __init__(self, config_path):

        self.logger = Logger().get_logger()

        self.config_path = config_path

    def run(self):

        try:

            self.logger.info("=" * 70)
            self.logger.info("ETL Framework Started")
            self.logger.info("=" * 70)

            ####################################################
            # Read Metadata Configuration
            ####################################################

            config_reader = ConfigReader(self.config_path)

            metadata = config_reader.read()

            ####################################################
            # Loop Through Each Table
            ####################################################

            for table_config in metadata:

                table = table_config["table"]

                self.logger.info(f"Processing Table : {table}")

                ####################################################
                # Authentication
                ####################################################

                auth = Authentication(table_config)

                token = auth.authenticate()

                ####################################################
                # API Client
                ####################################################

                api_client = APIClient(
                    config=table_config,
                    token=token
                )

                ####################################################
                # Pagination
                ####################################################

                paginator = Pagination(
                    api_client=api_client,
                    config=table_config
                )

                json_response = paginator.fetch_all()

                self.logger.info(
                    f"Records Retrieved : {len(json_response)}"
                )

                ####################################################
                # Flatten JSON
                ####################################################

                flattener = JSONFlattener()

                df = flattener.flatten(
                    json_response,
                    table_config
                )

                self.logger.info(
                    f"DataFrame Shape : {df.shape}"
                )

                ####################################################
                # Mapping
                ####################################################

                mapper = MappingEngine(table_config)

                df = mapper.apply(df)

                ####################################################
                # Transformation
                ####################################################

                transformer = Transformer(table_config)

                df = transformer.transform(df)

                ####################################################
                # Validation
                ####################################################

                validator = Validator(table_config)

                validator.validate(df)

                ####################################################
                # Load to Amazon S3
                ####################################################

                loader = S3Loader(table_config)

                loader.write(df)

                ####################################################
                # Success Log
                ####################################################

                self.logger.info(
                    f"{table} Loaded Successfully."
                )

                self.logger.info("-" * 70)

            self.logger.info("=" * 70)
            self.logger.info("ETL Completed Successfully")
            self.logger.info("=" * 70)

        except Exception as ex:

            self.logger.exception(ex)

            raise ex


def main():

    CONFIG_PATH = "config/cloudiq.json"

    framework = ETLFramework(CONFIG_PATH)

    framework.run()


if __name__ == "__main__":

    main()

import os

from src.core.logger import Logger
from src.core.config_reader import ConfigReader
from src.services.etl_service import ETLService


class ETLFramework:


    def __init__(self, config_folder):

        self.logger = Logger().get_logger()

        self.config_folder = config_folder



    def get_config_files(self):

        """
        Dynamically read all JSON files
        """

        files = []

        for file in os.listdir(self.config_folder):

            if file.endswith(".json"):

                files.append(
                    os.path.join(
                        self.config_folder,
                        file
                    )
                )

        return files



    def run(self):

        try:

            self.logger.info(
                "ETL Framework Started"
            )


            # Get all metadata json files

            config_files = self.get_config_files()



            for config_file in config_files:


                self.logger.info(
                    f"Processing Config : {config_file}"
                )


                # Read metadata

                reader = ConfigReader(
                    config_file
                )


                metadata = reader.read()



                # Start ETL

                etl = ETLService(
                    metadata
                )


                etl.run()



                self.logger.info(
                    f"Completed : {config_file}"
                )



        except Exception as e:

            self.logger.exception(e)

            raise



def main():


    CONFIG_FOLDER = "config"


    framework = ETLFramework(
        CONFIG_FOLDER
    )


    framework.run()



if __name__ == "__main__":

    main()

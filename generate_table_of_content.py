import datetime
import os


class Config:
    def __init__(self, output_file_name="README.md", header_start_level=1, path_start_from=".",
                 exclude_dirs=".git,.idea",
                 exclude_files=".gitignore"):
        self.output_file_name = output_file_name
        self.header_start_level = header_start_level
        self.path_start_from = path_start_from
        self.exclude_dirs = exclude_dirs.split(",")
        self.exclude_files = exclude_files.split(",")

    @property
    def readme_start(self):
        return "{} Table of Content\n\n".format("#" * self.header_start_level)

    @property
    def readme_end(self):
        return "\n" * 2 + "Auto generate at {}".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))


def generate_table_of_content(config: Config):
    readme = config.readme_start

    for root, dirs, files in os.walk(config.path_start_from):
        dirs[:] = [d for d in dirs if d not in config.exclude_dirs]
        files[:] = [f for f in files if f not in config.exclude_files]

        if root == os.path.curdir:
            current_level = 1
            current_header = os.path.dirname(os.path.realpath(__file__)).split("/")[-1]
        else:
            root_list = root.split("/")
            current_level = len(root_list)
            current_header = root_list[-1]

        readme += "{} {}\n\n".format("#" * (config.header_start_level + current_level), current_header)

        for file in files:
            readme += "- [{}]({})\n".format(file.split(".")[0], os.path.join(root, file))

        readme += "\n"

    readme += config.readme_end

    with open(config.output_file_name, "w") as f:
        f.write(readme)


if __name__ == '__main__':
    config = Config()
    generate_table_of_content(config)

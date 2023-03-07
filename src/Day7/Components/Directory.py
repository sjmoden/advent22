from Day7.Components.File import File


class Directory:
    def __init__(self, name, parent):
        self.sub_directories = []
        self.files = []
        self.name = name
        self.parent = parent

    def input_ls_result(self, input_ls):
        line_split = input_ls.split(" ")
        if line_split[0] == "dir" and not any(x.name == line_split[1] for x in self.sub_directories):
            self.sub_directories.append(Directory(line_split[1], self))
        if line_split[0] != "dir" and not any(x.name == line_split[1] for x in self.files):
            self.files.append(File(line_split[1], int(line_split[0])))

    def return_directory_size(self):
        return sum(x.size for x in self.files) + sum(x.return_directory_size() for x in self.sub_directories)

    def cd(self, name):
        if name == "..":
            return self.parent
        return next((x for x in self.sub_directories if x.name == name), None)

    def return_all_subdirectories(self):
        all_subdirectories = self.sub_directories.copy()
        for sub_directories in self.sub_directories:
            sub_sub_directories = sub_directories.return_all_subdirectories()
            all_subdirectories.extend(sub_sub_directories)
        return all_subdirectories


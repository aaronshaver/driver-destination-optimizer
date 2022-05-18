class FileSystem:
    """Provides simple wrappers for file I/O like reading text files"""

    def get_lines(path):
        """Returns list of string objects from text file located at 'path'"""
        with open(path) as f:
            return f.readlines()
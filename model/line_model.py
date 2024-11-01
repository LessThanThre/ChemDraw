class LineModel:
    def __init__(self):
        self.lines = []  # Список для хранения линий

    def add_line(self, line):
        self.lines.append(line)

    def delete_last_line(self):
        if self.lines:
            return self.lines.pop()
        return None

    def get_lines(self):
        return self.lines
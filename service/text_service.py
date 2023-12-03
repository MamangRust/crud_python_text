class TextFileService:
    def __init__(self, repository):
        self.repository = repository

    def create_data(self, data):
        self.repository.create(data)

    def read_all_data(self):
        return self.repository.read_all()

    def find_by_id(self, target_id):
        return self.repository.find_by_id(target_id=target_id)

    def update_data(self, index, new_data):
        self.repository.update(index, new_data)

    def delete_data(self, index):
        self.repository.delete(index)

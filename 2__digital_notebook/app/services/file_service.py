from pathlib import Path

class FileService:
    @staticmethod
    def load_file(file_path: str) -> str:
        return Path(file_path).read_text(
            encoding="utf-8"
        )
    
    @staticmethod
    def save_file(file_path: str, content: str) -> None:
        Path(file_path).write_text(content, encoding="utf-8")
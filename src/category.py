class CategoryManager:
    """Quản lý danh mục chi tiêu."""

    def __init__(self):
        self._categories = []

    def create_category(self, name):
        """Tạo một danh mục mới và trả về tên danh mục."""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Tên danh mục không được để trống")

        normalized = name.strip()
        if any(category.casefold() == normalized.casefold()
               for category in self._categories):
            raise ValueError("Danh mục đã tồn tại")

        self._categories.append(normalized)
        return normalized

    def list_categories(self):
        """Trả về danh sách danh mục hiện có."""
        return self._categories.copy()

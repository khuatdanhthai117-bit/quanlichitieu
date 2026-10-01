from src.category import CategoryManager


def test_create_category_adds_category():
    manager = CategoryManager()

    manager.create_category("Ăn uống")

    assert manager.list_categories() == ["Ăn uống"]


def test_create_category_rejects_blank_name():
    manager = CategoryManager()

    try:
        manager.create_category("   ")
        assert False, "Tên danh mục rỗng phải bị từ chối"
    except ValueError:
        pass


def test_create_category_rejects_duplicate_name_case_insensitive():
    manager = CategoryManager()
    manager.create_category("Ăn uống")

    try:
        manager.create_category("ăn UỐNG")
        assert False, "Danh mục trùng tên phải bị từ chối"
    except ValueError:
        pass

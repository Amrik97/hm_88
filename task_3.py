import yaml

# Подготовка данных для записи в файл
data = {
     "items": ["computer", "printer", "keyboard", "mouse"],
    "items_quantity": 4,
    "items_price": {
        "computer": "200€-1000€",
        "keyboard": "5€-50€",
        "mouse": "4€-7€",
        "printer": "100€-300€"
    }
}

# Запись данных в файл в формате YAML
with open('file1.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True)

# Считывание данных из файла
with open('file1.yaml', 'r', encoding='utf-8') as f:
    loaded_data = yaml.safe_load(f)

# Проверка, что данные совпадают
assert data == loaded_data, "Данные в файле не совпадают с исходными!"
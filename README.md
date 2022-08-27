# e-diary
# Редактор электронного дневника

## Цели проекта
Учебный проект

### Как установить
1. Установить сайт и БД. Исходники здесь https://github.com/devmanorg/e-diary
2. Скачать репозиторий в корневой каталог проекта

## Как использовать

### Запуск sell
```python
  python manage.py shell
```

### Импортировать функции
```
from script import fix_marks
from script import remove_chastisements
from script import create_commendation
from script import get_schoolkid

```

### Найти свою учетную запись, например
```python
  schoolkid = get_schoolkid('Фролов Иван')
```
Если учетная запись не будет найдена, то выдаст ошибку, так же выдаст ошибку, если будет найдено несколько записей.

### Поменять двойки и тройки на пятерки
```python
  fix_marks(schoolkid)
```

### Удалить замечания
```python
  remove_chastisements(schoolkid)
```

### Добавить похвалу

```python
#suject_title – фрагмент названия предмета в кавычках
#full_name – фамилия имя в кавычках

create_commendation('Фролов Иван', 'Муз')
```

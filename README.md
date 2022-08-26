# e-diary
# Редактор электронного дневника

## Цели проекта
Учебный проект

### Как установить
1. Установить сайт и БД. Исходники здесь https://github.com/devmanorg/e-diary
2. Скачать скрипт в корневой каталог проекта

### Запуск sell
```python
  python manage.py shell
```

### Найти свою учетную запись
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
#suject_title – название предмета
#full_name – фамилия имя

create_commendation(full_name, suject_title)
```

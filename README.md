# e-diary
## Редактор электронного дневника

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

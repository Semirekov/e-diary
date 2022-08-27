from random import choice

from django.core.exceptions import MultipleObjectsReturned
from django.core.exceptions import ObjectDoesNotExist

from datacenter.models import Chastisement     
from datacenter.models import Commendation  
from datacenter.models import Lesson     
from datacenter.models import Mark
from datacenter.models import Schoolkid   
from datacenter.models import Teacher 
  

def find_lessons(schoolkid, suject_title):    
    return Lesson.objects.filter(
        year_of_study__contains=schoolkid.year_of_study, 
        group_letter=schoolkid.group_letter, 
        subject__title__contains=suject_title
    )


def get_random_commendation():
    with open('commendations.txt', 'r') as file:
        return choice([commendation for commendation in file])


def get_schoolkid(full_name):            
    try:        
        school_kid = Schoolkid.objects.get(full_name__contains=full_name)
        print('Найден(а):', school_kid)
        return school_kid
    except MultipleObjectsReturned:
        print('Найдено несколько учеников. Уточните условия поиска.')
    except ObjectDoesNotExist:
        print('Ученик не найден. Уточните условия поиска.')
    

def fix_marks(schoolkid):    
    if schoolkid:           
        BAD_MARK, BEST_MARK = 3, 5         
        return Mark.objects.filter(
            schoolkid=schoolkid, 
            points__lte=BAD_MARK
        ).update(points=BEST_MARK)  


def remove_chastisements(schoolkid):
    if schoolkid:                  
        return Chastisement.objects.filter(schoolkid=schoolkid).delete()    


def create_commendation(full_name, suject_title):
    schoolkid = get_schoolkid(full_name)
    if not schoolkid:
        return            

    lessons = find_lessons(schoolkid, suject_title)
    if lessons.count() == 0:
        print('Нет таких уроков в расписании. Уточните условия поиска.')
        return

    lesson = choice(lessons)        
    teacher = Teacher.objects.get(full_name__contains=lesson.teacher)      

    return Commendation.objects.create(
        text=get_random_commendation(),
        created=lesson.date,
        schoolkid=schoolkid,
        subject=lesson.subject,
        teacher=teacher
    )

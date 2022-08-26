def get_schoolkid(full_name):
    from django.core.exceptions import MultipleObjectsReturned
    from django.core.exceptions import ObjectDoesNotExist
    from datacenter.models import Schoolkid   
    try:
        return Schoolkid.objects.get(full_name__contains=full_name)
    except MultipleObjectsReturned:
        print('Найдено несколько учеников. Уточните условия поиска.')
    except ObjectDoesNotExist:
        print('Ученик не найден. Уточните условия поиска.')


def fix_marks(schoolkid):    
    if schoolkid is None:
        return        
    from datacenter.models import Mark
    BAD_MARK, BEST_MARK = 3, 5         
    Mark.objects.filter(schoolkid=schoolkid, points__lte=BAD_MARK).update(points=BEST_MARK)  


def remove_chastisements(schoolkid):
    if schoolkid is None:
        return        
    from datacenter.models import Chastisement     
    Chastisement.objects.filter(schoolkid=schoolkid).delete()    


def create_commendation(full_name, suject_title):
    from datacenter.models import Commendation  
    from datacenter.models import Lesson     
    from datacenter.models import Teacher 
    text = 'Хвалю!'    
    child = get_schoolkid(full_name)
    if child is None:
        return    
    lesson = Lesson.objects.filter(year_of_study__contains='6', group_letter='А', subject__title=suject_title).first()    
    teacher = Teacher.objects.get(full_name__contains=lesson.teacher)      
    Commendation.objects.create(
        text=text,
        created=lesson.date,
        schoolkid=child,
        subject=lesson.subject,
        teacher=teacher
    )

from django.db.models import Sum, Avg
from .models import *


class Responses:
    def api_response(self):
        return {
            'success': True,
            'code': '',
            'error_string': '',
            'data': ''
        }


def getStudentById(req, id):
    res = {}
    mark_queryset = Marks.objects.filter(student=id)
    res['role_number'] = mark_queryset[0].student.id
    res['name'] = mark_queryset[0].student.name
    marks = []
    for sub in mark_queryset:
        obj = {}
        obj[sub.subject.name] = sub.marks
        marks.append(obj)
    res['marks'] = marks
    return res


def getStudentsTotal():
    res = []
    total_marks = Marks.objects.values('student_id__name').annotate(total=Sum('marks')).order_by()
    for total in total_marks:
        obj = {}
        obj['name'] = total['student_id__name']
        obj['total'] = total['total']
        res.append(obj)
    return res


def getSubjectAverage():
    res = []
    sub_avg = Marks.objects.values('subject_id__name').annotate(avg=Avg('marks')).order_by()
    for avg in sub_avg:
        obj = {}
        obj['name'] = avg['subject_id__name']
        obj['average'] = round(avg['avg'], 2)
        res.append(obj)
    return res

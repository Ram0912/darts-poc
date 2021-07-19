import json
import pickle

from django.core.cache import cache
from django.db.models import Sum, Avg
from .models import *
import pandas
from django.db import connections


class Responses:
    def api_response(self):
        return {
            'success': True,
            'code': '',
            'error_string': '',
            'data': ''
        }


# def StudentSerializer(serializer.Seri):
#     role_number = serilizer.Interger()
#     name = se


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
    total_marks = Marks.objects.values('student_id').aggregate(total=Sum('marks'))
    # select student_name, sum(marks) from Marks order by student_id
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


def new_get_df(request):
    conn = connections
    df = pandas.read_sql(str(Marks.objects.values('subject_id__name').annotate(avg=Avg('marks')).query), conn['default'])
    cache.set("sample", pickle.dumps(df), 3000)
    request.session['dframe_cache'] = "sample"
    return df


def update_dataframe(request):
    # ... your code
    cache_key = request.session.get("dframe_cache")
    df = None
    if cache_key and cache.get(cache_key) is not None:
        df = pickle.loads(cache.get(cache_key))
    else:
        # generate new cache normally and store it to session just like above
        df = new_get_df(request)

    # perform your current action on dataframe
    cache.set(cache_key, pickle.dumps(df))

    # return your modified dataframe.
    return json.loads(df.to_json(orient='records'))


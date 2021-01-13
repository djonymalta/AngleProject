from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
import datetime
from clock.models import ClockApi
import math


@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def calc_angle(resquest, hours, minuts=0):
    if hours == 12:
        hours = 0
    try:
        clock = ClockApi.objects.filter(hours=hours, minuts=minuts).get()
        return Response({'message': f'{clock.angle}'})
    except:
        pass
        angle_hours = ((hours * 60) + minuts) * 0.5
        angle_minuts = minuts * 6
        angle_between = math.fabs(angle_hours-angle_minuts)
        calc_result = 0
        if angle_between < 360 - angle_between:
            calc_result = angle_between
        else:
            calc_result = 360 - angle_between

    ClockApi.objects.create(hours=hours, minuts=minuts, angle=calc_result, date=datetime.date.today())
    return Response({'angle': f'{calc_result}'})

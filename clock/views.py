from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
import datetime
from clock.models import ClockApi
import math


@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def calculate_angle(resquest, hours, minuts=0):

    hours = 0 if hours == 12 else hours
    try:
        clock = ClockApi.objects.filter(hours=hours, minuts=minuts).get()
        return Response({'message': f'{clock.angle}'})

    except:
        angle_hours = ((hours * 60) + minuts) * 0.5
        angle_minuts = minuts * 6
        angle_between = math.fabs(angle_hours-angle_minuts)

        calc_result = angle_between if angle_between < 360 - angle_between else 360 - angle_between

    ClockApi.objects.create(hours=hours, minuts=minuts, angle=calc_result, date=datetime.date.today())
    return Response({'angle': f'{calc_result}'})

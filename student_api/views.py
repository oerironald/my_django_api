from rest_framework.response import Response
from rest_framework.decorators import api_view
from student.models import Student
from .studentserializer import StudentSerializer


@api_view(['GET'])
def getStudents(request):
    students = Student.objects.all()
    serialized = StudentSerializer(students, many=True)
    return Response(serialized.data)


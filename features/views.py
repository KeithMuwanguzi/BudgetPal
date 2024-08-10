from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from income_expenses.models import IncomeData, ExpenseData
from . serializers import IncomeSerializer, ExpenseSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def incomeList(request):
    items = IncomeData.objects.filter(user = request.user)
    ser = IncomeSerializer(items, many = True)
    return Response({
        'message':'All income items fetched',
        'data':ser.data
    })

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def addIncome(request):
    serializer = IncomeSerializer(data = request.data,context = {'request':request})
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message':'New income entry made',
            'status':'success',
            'data':serializer.data
        })
    else:
        return Response({
            'message':'An error occurred',
            'status':'error',
            'data':serializer.errors
        })

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def expensesList(request):
    permission_classes([IsAuthenticated])
    items = ExpenseData.objects.filter(user = request.user)
    ser = ExpenseSerializer(items, many = True)
    return Response({
        'message':'All expense items fetched',
        'data':ser.data
    })

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def addExpense(request):
    serializer = ExpenseSerializer(data = request.data,context = {'request':request})
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message':'New expense entry made',
            'status':'success',
            'data':serializer.data
        })
    else:
        return Response({
            'message':'An error occurred',
            'status':'error',
            'data':serializer.errors
        })
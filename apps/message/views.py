from django.shortcuts import render

from .models import UserMessage

# 获取页面

# Create your views here.
# def get_form(request):
#     return render(request,'form_message.html')


#读取数据库数据
# def get_form(request):
#     all_name = UserMessage.objects.all()
#     # for i in all_name:
#     #     print(i.name)
#     return render(request,'form_message.html')

# #写到数据库
# # def get_form(request):
# #     if request.method == 'POST':
# #         user_message = UserMessage()
# #         user_message.name = request.POST.get('name','')
# #         user_message.email = request.POST.get('email', '')
# #         user_message.address = request.POST.get('address', '')
# #         user_message.message = request.POST.get('message', '')
# #         user_message.object_id='test1'
# #         user_message.save()
# #     return render(request,'form_message.html')




#查询数据库数据
def get_form(request):
    name = request.POST.get('name','')
    message = None
    all_name = UserMessage.objects.filter(name=name)
    if all_name:
        message = all_name[0]


    return render(request, 'form_message.html',{'my_message':message})



# myapp/views.py
from django.shortcuts import render, redirect

def home(request):
    if 'choices_count' not in request.session:
        request.session['choices_count'] = [0, 0, 0, 0, 0]
    return render(request, 'home.html')

def page1(request):
    return process_page(request, 1)

def page2(request):
    return process_page(request, 2)

def page3(request):
    return process_page(request, 3)

def page4(request):
    return process_page(request, 4)

def page5(request):
    return process_page(request, 5)

def page6(request):
    return process_page(request, 6)

def page7(request):
    return process_page(request, 7)

def page8(request):
    return process_page(request, 8)

def page9(request):
    return process_page(request, 9)

def page10(request):
    return process_page(request, 10)

def process_page(request, page_number):
    if request.method == 'POST':
        selected_choice = request.POST.get('choice')
        if selected_choice == 'choice1':
            request.session['choices_count'][0] += 1
        elif selected_choice == 'choice2':
            request.session['choices_count'][1] += 1
        elif selected_choice == 'choice3':
            request.session['choices_count'][2] += 1
        elif selected_choice == 'choice4':
            request.session['choices_count'][3] += 1
        elif selected_choice == 'choice5':
            request.session['choices_count'][4] += 1
        request.session.modified = True
        
        # ถ้าเป็น page10 ให้ไปที่ last_page
        if page_number == 10:
            return redirect('last_page')
        else:
            return redirect(f'page{page_number + 1}')  # ไปยังหน้าถัดไป

    return render(request, f'page{page_number}.html')

def last_page(request):
    # ค้นหาค่าที่มากที่สุด
    choices_count = request.session.get('choices_count', [0, 0, 0, 0, 0])
    max_choice = max(choices_count)
    max_choice_index = choices_count.index(max_choice)
    
    return render(request, 'last_page.html', {
        'max_choice_index': max_choice_index,
        'max_choice': max_choice
    })

def reset_choices(request):
    request.session['choices_count'] = [0, 0, 0, 0, 0]
    return redirect('home')

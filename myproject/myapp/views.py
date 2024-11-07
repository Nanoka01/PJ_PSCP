from django.shortcuts import render, redirect

def home(request):
    if 'choices_count' not in request.session:
        request.session['choices_count'] = [0, 0, 0, 0, 0]
    return render(request, 'home.html')

def page1story(request):
    if request.method == 'POST':
        return redirect('page1')
    return render(request, 'page1story.html')

def page1(request):
    return process_page(request, 1)

def page2story(request):
    if request.method == 'POST':
        return redirect('page2')
    return render(request, 'page2story.html')

def page2(request):
    return process_page(request, 2)

def page3story(request):
    if request.method == 'POST':
        return redirect('page3')
    return render(request, 'page3story.html')

def page3(request):
    return process_page(request, 3)

def page4story(request):
    if request.method == 'POST':
        return redirect('page4')
    return render(request, 'page4story.html')

def page4(request):
    return process_page(request, 4)

def page5story(request):
    if request.method == 'POST':
        return redirect('page5')
    return render(request, 'page5story.html')

def page5(request):
    return process_page(request, 5)

def page6story(request):
    if request.method == 'POST':
        return redirect('page6')
    return render(request, 'page6story.html')

def page6(request):
    return process_page(request, 6)

def page7story(request):
    if request.method == 'POST':
        return redirect('page7')
    return render(request, 'page7story.html')

def page7(request):
    return process_page(request, 7)

def page8story(request):
    if request.method == 'POST':
        return redirect('page8')
    return render(request, 'page8story.html')

def page8(request):
    return process_page(request, 8)

def page9story(request):
    if request.method == 'POST':
        return redirect('page9')
    return render(request, 'page9story.html')

def page9(request):
    return process_page(request, 9)

def page10story(request):
    if request.method == 'POST':
        return redirect('page10')
    return render(request, 'page10story.html')


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
        if page_number == 9:
            return redirect('last_page')
        else:
            return redirect(f'page{page_number + 1}story')  # ไปยังหน้า story ถัดไป

    return render(request, f'page{page_number}.html')

def last_page(request):
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

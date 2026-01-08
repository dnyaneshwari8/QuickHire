from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Job
from Categories.models import Category

@login_required

def postjob(request):
    
    categories = Category.objects.filter(is_active=True)

    if request.method == 'POST':
        category_id = request.POST.get('category')
        Job.objects.create(
            posted_by=request.user,
            category=Category.objects.get(id=category_id),
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            pay_rate=request.POST.get('pay_rate'),
            duration=request.POST.get('duration'),
            start_date=request.POST.get('start_date'),
            start_time=request.POST.get('start_time'),
            address=request.POST.get('address'),
            city=request.POST.get('city'),
            state=request.POST.get('state'),
        )

        return redirect('employer_dashboard')
    
    return render(request, 'post-job.html',{'Categories':categories})
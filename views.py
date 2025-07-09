# detector_app/views.py
from django.shortcuts import render
from .model_functions import check_if_real_profile_pic, analyze_content

def home(request):
    if request.method == 'POST':
        # Assuming you have a form with a 'profile_url' field
        profile_url = request.POST.get('profile_url')
        is_real_profile_pic = check_if_real_profile_pic(profile_url)

        # Assuming you have an authentication token
        access_token = 'your_access_token'
        content_type = analyze_content(username='some_username', access_token=access_token)

        return render(
            request,
            'result.html',
            {'is_real_profile_pic': is_real_profile_pic, 'content_type': content_type}
        )

    return render(request, 'home.html')

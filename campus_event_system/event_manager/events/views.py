from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .models import Event

def event_list(request):
    events = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    return render(request, 'events/list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/detail.html', {'event': event})

@csrf_exempt  # Temporary for testing - remove in production
def rsvp(request, event_id):
    if request.method == 'POST':
        try:
            event = get_object_or_404(Event, pk=event_id)
            email = request.POST.get('email')
            
            if not email:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Email is required'
                }, status=400)
                
            if email in event.attendees:
                return JsonResponse({
                    'status': 'error',
                    'message': 'You have already RSVPed'
                })
                
            event.attendees.append(email)
            event.save()
            
            return JsonResponse({
                'status': 'success',
                'message': 'RSVP confirmed!',
                'event_title': event.title
            })
            
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=500)
            
    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method'
    }, status=400)
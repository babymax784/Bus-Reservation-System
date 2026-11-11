from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from .models import BusInfo,BusDropArea,BusPickArea

import json
# Create your views here.
def index (request, template_name ='bus_resrv_system.html'):
    page_title = 'Bus'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def search_bus(request,template_name ='bus/search_bus.html'):
    page_title = 'Book a ticket'
    searched = False
    if request.method == 'POST':
        searched = True
        post_data = request.POST.copy()
        area_from_id = post_data.get('area_from_id')
        area_to_id = post_data.get('area_to_id') 
        bus_info_list= BusInfo.objects.filter(arriving_from_id=area_from_id,depature_at_id=area_to_id)
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def autocomplete_pick(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        areas = BusPickArea.objects.filter(area_name__icontains = q )[:20]
        results = []
        for area in areas:
            area_json = {}
            area_json['id'] = area.id
            area_json['label'] = area.area_name
            area_json['value'] = area.area_name
            results.append(area_json)
        data = json.dumps(results) 
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def autocomplete_drop(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        areas = BusDropArea.objects.filter(area_name__icontains = q )[:20]
        results = []
        for area in areas:
            area_json = {}
            area_json['id'] = area.id
            area_json['label'] = area.area_name
            area_json['value'] = area.area_name
            results.append(area_json)
        data = json.dumps(results) 
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
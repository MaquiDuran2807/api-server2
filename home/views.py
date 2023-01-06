from django.shortcuts import render
from .models import Home, Explore, Services, Contact, copyRight
from .models import FaqModel,SocialMedia

# Create your views here.

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        print('hola=======================================================')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        casa=Home.objects.get(pk=1)
        explore=Explore.objects.get(pk=1)
        services=Services.objects.get(pk=1)
        faq=FaqModel.objects.get(pk=1)
        contact=Contact.objects.get(pk=1)
        copy=copyRight.objects.get(pk=1)
        social=SocialMedia.objects.get(pk=1)
        context = super().get_context_data(**kwargs)
        context['casa'] = casa
        context['explore'] = explore
        context['services'] = services
        context['faq'] = faq
        context['contact'] = contact
        context['copy'] = copy
        context['social'] = social
        print(context)
        return context

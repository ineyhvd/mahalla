from django.shortcuts import render
from django.views import View
from .models import Viloyat, Tuman, Mahalla


class HomeView(View):
    def get(self, request):
        # Barcha viloyatlarni olish
        viloyatlar = Viloyat.objects.all()

        # Tanlangan viloyat, tuman va mahalla nomini olish
        viloyat_id = request.GET.get('viloyat')
        tuman_id = request.GET.get('tuman')
        mahalla_name = request.GET.get('mahalla', '').strip()

        # Tumanlarni filtrlash
        tumanlar = Tuman.objects.all()
        if viloyat_id:
            tumanlar = tumanlar.filter(viloyat_id=viloyat_id)

        # Mahallalarni faqat filtr qo‘llanilganda olish
        mahallalar = None
        if viloyat_id or tuman_id or mahalla_name:  # Agar hech bo‘lmaganda bitta filtr qo‘llanilgan bo‘lsa
            mahallalar = Mahalla.objects.all()
            if viloyat_id:
                mahallalar = mahallalar.filter(tuman__viloyat_id=viloyat_id)
            if tuman_id:
                mahallalar = mahallalar.filter(tuman_id=tuman_id)
            if mahalla_name:
                mahallalar = mahallalar.filter(name__icontains=mahalla_name)

        context = {
            'viloyatlar': viloyatlar,
            'tumanlar': tumanlar,
            'mahallalar': mahallalar,
            'selected_viloyat': int(viloyat_id) if viloyat_id else None,
            'selected_tuman': int(tuman_id) if tuman_id else None,
            'mahalla_name': mahalla_name,
        }
        return render(request, 'index.html', context)
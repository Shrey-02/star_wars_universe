from django.shortcuts import render
from .models import Planet, Resident
import requests

def home(request):
    planets = Planet.objects.all()
    return render(request, 'home.html', {'planets': planets})

def detail(request, planet_id):
    planet = Planet.objects.get(id=planet_id)
    residents = Resident.objects.filter(planet_id=planet_id)
    
    return render(request, 'detail.html', {'planet': planet, 'residents': residents})

def about(request):
    return render(request, 'about.html', {})

def fetch_planet_data(planet_id):
    url = f"https://swapi.dev/api/planets/{planet_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    

def fetch_and_save_residents(resident_urls, planet_id):
    planet = Planet.objects.get(id=planet_id)  
    for resident_url in resident_urls:
        response = requests.get(resident_url)
        if response.status_code == 200:
            resident_data = response.json()
           
            resident, created = Resident.objects.update_or_create(
                name=resident_data['name'],
                height=resident_data['height'],
                mass=resident_data['mass'],
                gender=resident_data['gender'],
                planet=planet,  
            )

def fetch_residents_for_planet(planet_data):
    planet_id = planet_data['url'].split('/')[-2]  
    for resident_url in planet_data['residents']:
        fetch_and_save_residents([resident_url], planet_id)






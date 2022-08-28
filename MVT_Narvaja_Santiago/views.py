from django.http import HttpResponse
from django.template import loader
from MVT_Familia.models import Familia

def familia(request):

    persona_1 = Familia(relacion = "Tio", nombre = "Gabriel" , apellido = "Narvaja" , hijos = 3 , cumpleaños = "1954-09-17")
    persona_2 = Familia(relacion = "Madre", nombre = "Stella" , apellido = "Toro" , hijos = 2 , cumpleaños = "1956-03-24")
    persona_3 = Familia(relacion = "Hermano", nombre = "Miguel" , apellido = "Contreras" , hijos = 1 , cumpleaños = "1976-03-07")
    
    persona_1.save()
    persona_2.save()
    persona_3.save()
    
    texto_1 = f"Tu {persona_1.relacion},{persona_1.nombre}, tiene {persona_1.hijos} hijos. Nacion el {persona_1.cumpleaños}, no te olvides de saludar"
    texto_2 = f"Tu {persona_2.relacion},{persona_2.nombre}, tiene {persona_2.hijos} hijos. Nacion el {persona_2.cumpleaños}, no te olvides de saludar"
    texto_3 = f"Tu {persona_3.relacion},{persona_3.nombre}, tiene {persona_3.hijos} hijos. Nacion el {persona_3.cumpleaños}, no te olvides de saludar"
    
    diccionario = {"familiar 1": persona_1 , "familiar 2": persona_2 , "familiar 3": persona_3 , "texto_1":texto_1 , "texto_2":texto_2 , "texto_3":texto_3}
    plantilla = loader.get_template("template_familia.html")
    
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)
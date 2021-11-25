from django.shortcuts import render, get_object_or_404, redirect
from .forms import MoveForm
from .models import Animal, Equipement
from django.contrib import messages


 
                  
def post_list(request):
    animaux = Animal.objects.all()
    equipements = Equipement.objects.all()
    return render(request, 'blog/post_list.html', {'animaux': animaux,"equipements":equipements})



def nourrir(animal, ancien_lieu, nouveau_lieu):
    if animal.etat != "affamé":
       message= f"désolé, {animal.id_animal} n'a pas faim"
    elif    nouveau_lieu.disponibilite == "Occupé":
        form.save(commit=False) 
        message='Désolé, la mangeoire est occupée '
    else:
        nouveau_lieu.disponibilite = "occupé"
        ancien_lieu.disponibilite = "libre"
        animal.etat = "repus"
        ancien_lieu.save()
        nouveau_lieu.save()
        animal.save()
        message=f"{animal.id_animal} passe à la mangeoire" 
    return message



def divertir(animal, ancien_lieu, nouveau_lieu):
    if animal.etat  != 'repus':
        message=f"désolé, {animal.id_animal} n'est pas en état de faire du sport"
    elif    nouveau_lieu.disponibilite == "Occupé":
        message='Désolé, la roue est occupée '
        form.save(commit=False) 
    else:
        nouveau_lieu.disponibilite = "occupé"
        ancien_lieu.disponibilite = "libre"
        animal.etat = "fatigué"
        ancien_lieu.save()
        nouveau_lieu.save()
        animal.save()
        message=f"{animal.id_animal} passe à : ", nouveau_lieu
    return message


def coucher(animal, ancien_lieu, nouveau_lieu):
    if animal.etat  != 'fatigué':
            message=f"désolé, {animal.id_animal} n'est pas fatigué."
    elif nouveau_lieu.disponibilite == "Occupé":
             message='Désolé, la roue est occupée '
             form.save(commit=False) 
    else:
        nouveau_lieu.disponibilite = "occupé"
        ancien_lieu.disponibilite = "libre"
        animal.etat = "endormi"
        ancien_lieu.save()
        nouveau_lieu.save()
        animal.save()
        message=f"{animal.id_animal} passe à : ", nouveau_lieu
    return message
        

def réveiller(animal, ancien_lieu, nouveau_lieu):
    if animal.etat  != 'endormi':
         message=f"désolé, {animal.id_animal} ne dort pas."
    else:
        nouveau_lieu.disponibilite = "occupé"
        ancien_lieu.disponibilite = "libre"
        animal.etat = "affamé"
        ancien_lieu.save()
        nouveau_lieu.save()
        animal.save()
        message=f"{animal.id_animal} passe à : ", nouveau_lieu

def animal_detail(request, id_animal):
    animal = get_object_or_404(Animal, id_animal=id_animal)
    ancien_lieu = get_object_or_404(Equipement, id_equip=animal.lieu.id_equip)
    message = ''
    if request.method == "POST":
        form = MoveForm(request.POST, instance=animal)
    else:
        form=MoveForm()
    if form.is_valid():
        nouveau_lieu = get_object_or_404(Equipement, id_equip=animal.lieu.id_equip)
        if nouveau_lieu.id_equip == "mangeoire":
             nourrir(animal,ancien_lieu, nouveau_lieu)
        if nouveau_lieu.id_equip == "roue":
             divertir(animal,ancien_lieu, nouveau_lieu)
        if nouveau_lieu.id_equip == "nid":
            message= coucher(animal,ancien_lieu, nouveau_lieu)
        if nouveau_lieu.id_equip == "litière":
             réveiller(animal,ancien_lieu, nouveau_lieu)
        
        form.save()
        return redirect('animal_detail', id_animal=id_animal)
    else:
        lieu = get_object_or_404(Equipement, id_equip=animal.lieu.id_equip)
        form = MoveForm()
        return render(request,
                  'blog/animal_detail.html',
                  {'animal': animal, 'lieu': lieu, 'form': form})

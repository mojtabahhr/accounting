from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from workers.models import CostsModel
from workers.forms import AddCostForm

# Create your views here.


def costs_views(request):
    costs = CostsModel.objects.all()
    context = {
        'costs':costs
    }
    return render(request=request, template_name='costs.html',context=context)
    
def cost_form(request):
    if request.method == 'POST':
        form = AddCostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if post.price == None:
                print(post.price)
                post.price = post.fee * post.amount
            post.save()
            print(CostsModel.objects.all())
            return HttpResponseRedirect('/costs/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddCostForm()
        return render(request, 'cost-form.html', {'form': form})


def edit_cost(request, pk=None):

    cost = CostsModel.objects.get(id=pk)
    form = AddCostForm()
    context = {
    'cost':cost,
    'form':form
    }
    return render(request, 'edit-cost-form.html', context=context)


def update_record(request, pk):
    who = request.POST['who']
    title = request.POST['title']
    amount = request.POST['amount']
    fee = request.POST['fee']
    price = request.POST['fee']
    cost_type = request.POST['cost_type']
    info = request.POST['info']
    cost = CostsModel.objects.get(id=pk)
    cost.who = who
    cost.title = title
    cost.amount = amount
    cost.fee = fee
    cost.cost_type = cost_type
    cost.info = info
    try:
        cost.price = eval(fee) * eval(amount)
    except:
        cost.price = price
    cost.save()
    return HttpResponseRedirect('/costs/')


def delete(request, pk):
  cost = CostsModel.objects.get(id=pk)
  cost.delete()
  return HttpResponseRedirect('/costs/')
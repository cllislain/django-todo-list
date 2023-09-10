from token import LSQB
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList


def todo_lists(response):
    ls = ToDoList.objects.all()
    post = response.POST

    return render(response, "main/todo_lists.html", {"todo_lists": ls})


def delete_todo_list(response, id):
    todo_list = get_object_or_404(ToDoList, id=id)
    if response.method == "POST":
        todo_list.delete()
    return redirect("todo_lists")


def todo_list_item(response, id):
    ls = ToDoList.objects.get(id=id)

    if response.method == "POST":
        post = response.POST
        if post.get("save"):
            for item in ls.item_set.all():
                if post.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()

        elif post.get("newItem"):
            txt = post.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("Invalid Input")

        for item in ls.item_set.all():
            if post.get("d" + str(item.id)) == "delete":
                item.delete()

    return render(response, "main/list.html", {"ls": ls})


def home(response):
    return render(response, "main/home.html", {})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
        return HttpResponseRedirect("/todo-list/{}/".format(t.id))

    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})

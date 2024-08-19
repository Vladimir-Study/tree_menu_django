from django.shortcuts import render


def index(request):
    path_name = request.resolver_match.view_name
    context = {
        "path_name": path_name
    }
    return render(request, 'tree_main_menu/base.html', context=context)
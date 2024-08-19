from django import template
from tree_main_menu.models import Menu

register = template.Library()


def new_search(menu: list, url: str, path: list, parent = 0) -> list:
    for elem in menu:
        if parent is None:
            return path
        elif elem.url == url:
            for j in menu:
                if elem.id == j.position_id:
                    path.append(j)
            path.append(menu.pop(menu.index(elem)))
            parent = path[-1].position_id
            return new_search(menu, url, path, parent)
        elif elem.id == parent:
            path.append(menu.pop(menu.index(elem)))
            parent = path[-1].position_id
            return new_search(menu, url, path, parent)


@register.inclusion_tag('tree_main_menu/menu.html')
def draw_menu(name_menu: str, url_name: str = ''):
    url_name = name_menu if url_name == '' else url_name
    sql = f"""SELECT * FROM tree_main_menu_menu WHERE name = '{name_menu}'"""
    menu = Menu.objects.raw(sql)
    new_menu = new_search(list(menu), url_name, [], 0)
    new_menu.reverse()
    return {"main_menu": new_menu}
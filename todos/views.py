import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Todo



def make_error(code, message, status_code):
    response = JsonResponse(
        {
            "error": {
                "code": code,
                "message": message
            }
        },
        status=status_code
    )
    return response


@csrf_exempt
@require_http_methods(["GET", "POST"])
def todos_view(request):
    if request.method == "GET":
        return get_todos(request)
    elif request.method == "POST":
        return create_todo(request)


def get_todos(request):
    all_todos = Todo.objects.all()
    todos_list = []

    for todo in all_todos:
        todos_list.append(todo.to_dict())

    return JsonResponse(todos_list, safe=False, status=200)


def create_todo(request):
    body = json.loads(request.body)
    text = body.get("text")

    # валидация
    if text is None:
        return make_error("VALIDATION_ERROR", "text is required", 400)

    if text.strip() == "":
        return make_error("VALIDATION_ERROR", "text is required", 400)

    if len(text) > 280:
        return make_error("VALIDATION_ERROR", "text must be 280 characters or fewer", 400)


    new_todo = Todo()
    new_todo.text = text
    new_todo.save()

    return JsonResponse(new_todo.to_dict(), status=201)

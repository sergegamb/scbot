import utils


task_message = "Таски"
request_message = "Заявки"

# TODO: ask jpt to convert description to human readable text
def request_template(request):
    clean_description = utils.extract_text(request.description)
    priority = "None"
    if request.priority:
        priority = request.priority.name
    message_text = (
            f"#{request.id} {request.subject}\n"
            f"Приоритет: {priority}\n"
            f"Статус: {request.status.name}\n"
            f"\n{clean_description[:1000]}"  # short_
            )
    return message_text

import utils


task_message = "Задачи"
request_message = "Заявки"
delete_task = "Удалить задачу"
open_sc = "Открыть"
menu = "Меню"
start_message = "Привет. Как я могу вам помочь?"
add_task = "Добавить задачу"
provide_task_title_message = "Что за задача?"
help_message = "Напишите @sgamb"
add_worklog_message = "Введите описание ворклога. Число часов можно указать плюсами в начале"

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

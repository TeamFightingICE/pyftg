from pyftg.aiinterface.ai_interface import AIInterface


def load_ai(ai_path: str) -> AIInterface:
    path = ai_path.split('.')
    module_name, class_name = path[0], path[int(len(path) == 2)]
    return getattr(__import__(module_name), class_name)()

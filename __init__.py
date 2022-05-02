from mycroft import MycroftSkill, intent_file_handler


class PrusaControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('control.prusa.intent')
    def handle_control_prusa(self, message):
        self.speak_dialog('control.prusa')


def create_skill():
    return PrusaControl()


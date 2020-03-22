"""A simple chatbot that directs students to office hours of CS professors."""

from chatbot import ChatBot


class OxyCSBot(ChatBot):
    """A simple chatbot that directs students to office hours of CS professors."""

    STATES = [
        'waiting',
        'yes_explained_crush',
        'has_crush',
        'middle_has_crush',
        'third_has_crush',
        'no_has_crush',
        'user_has_crush',
        'math',
        'biology',
        'history',
        'csp',
        'random',
        'communication_crush',
        'no_communication',
        'yes_communication',
        'no_response',
        'next_response',
        'unsure',
        'elaborate',
        'determine_state',
        'class',
        'text',
    ]

    TAGS = {

        # classes
        'math': 'Math',
        'history': 'History',
        'csp': 'CSP',
        'biology': 'Biology',

        # generic
        'thanks': 'thanks',
        'okay': 'yes',
        'yes': 'yes',
        'yep': 'yes',
        'yeah': 'yes',
        'no': 'no',
        'nope': 'no',
        'hilarious': 'hilarious',
        'haha': 'hilarious',
        'very funny': 'hilarious',
        'good joke': 'hilarious',
        'stop making fun of me': 'hilarious',
        'It is going well': 'good',
        'we get along': 'good',
        'good': 'good',
        'I really like them': 'good',
        'we talk a lot': 'good',
        'sort of': 'kind of',
        'sometimes': 'kind of',
        'on occasion': 'kind of',
        'a little bit': 'kind of',
        'probably talk to them': 'class',
        'after class': 'class',
    }

    def __init__(self):
        """Initialize the OxyCSBot.
        """
        print("Hey! Have I told you about the cute boy in my CSP Class?")
        super().__init__(default_state='waiting')
        self.firstresponse = None

    def respond_from_waiting(self, message, tags):
        """Decide what state to go to from the "waiting" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """

        self.firstresponse = None

        if 'no' in tags:
            return self.go_to_state('has_crush')
        elif 'yes' in tags:
            return self.go_to_state('yes_explained_crush')
        else:
            return self.finish('confused')

    # "has_crush" state functions

    def on_enter_has_crush(self):
        response = '\n'.join([
            f'Ooooohhhh. I have to tell you. Do you have time right now or are you in class?',
        ])
        return response

        # The users response from has_crush does not really matter since they will both lead down the same path

    def respond_from_has_crush(self, message, tags):
        if 'yes' in tags:
            return self.go_to_state('middle_has_crush')
        else:
            return self.go_to_state('middle_has_crush')

    def on_enter_middle_has_crush(self):
        response = '\n'.join([
            f'Oh I totally understand. Call me later?'
        ])
        return response

    def respond_from_middle_has_crush(self, message, tags):
        if 'yes' in tags:
            return self.go_to_state('third_has_crush')
        else:
            response = '\n'.join([
                f'Aww sad. Ok well I miss you!'
            ])
            return response

    def on_enter_third_has_crush(self):
        response = '\n'.join([
            f'Yay. Talk soon :)'
        ])
        return response

    # "yes_explained_crush" state functions

    def on_enter_yes_explained_crush(self):
        response = '\n'.join([
            f"Sorry about that I get really distracted. Have you ever had a crush in one of your classes?",
        ])
        return response

    def respond_from_yes_explained_crush(self, message, tags):
        if 'yes' in tags:
            return self.go_to_state('user_has_crush')
        else:
            return self.go_to_state('no_has_crush')

    def on_enter_no_has_crush(self):
        response = '\n'.join([
            f'You need to take some different classes maybe sign up for some econ! Maybe someone else can give me '
            f'better advice...thank you though! :)',
        ])
        return response

    def on_enter_user_has_crush(self):
        response = '\n'.join([
            f'You have to tell me all about it like what class are you both in?'
        ])
        return response

    def respond_from_user_has_crush(self, message, tags):
        if 'Math' in tags:
            return self.go_to_state('math')
        elif 'History' in tags:
            return self.go_to_state('history')
        elif 'CSP' in tags:
            return self.go_to_state('csp')
        elif 'Biology' in tags:
            return self.go_to_state('biology')
        else:
            return self.go_to_state('random')

    def on_enter_math(self):
        response = '\n'.join([
            f'Bet you did not know that 2+2 equals 4 because you were so distracted'
        ])
        return response

    def on_enter_biology(self):
        response = '\n'.join([
            f'Bet you did not know that what the powerhouse of the cell is because you were so distracted'
        ])
        return response

    def on_enter_csp(self):
        response = '\n'.join([
            f'Bet you did not know that what the theme was this year because you were so distracted'
        ])
        return response

    def on_enter_history(self):
        response = '\n'.join([
            f'Bet you did not know that George Washington was the 1st president because you were so distracted'
        ])
        return response

    def on_enter_random(self):
        response = '\n'.join([
            f'Bet you did not know a single thing on the final because you were so distracted'
        ])
        return response

    def respond_from_math(self, message, tags):
        if 'hilarious' in tags:
            return self.go_to_state('communication_crush')

    def respond_from_history(self, message, tags):
        if 'hilarious' in tags:
            return self.go_to_state('communication_crush')

    def respond_from_csp(self, message, tags):
        if 'hilarious' in tags:
            return self.go_to_state('communication_crush')

    def respond_from_biology(self, message, tags):
        if 'hilarious' in tags:
            return self.go_to_state('communication_crush')

    def respond_from_random(self, message, tags):
        if 'hilarious' in tags:
            return self.go_to_state('communication_crush')

    # A new function that will move along to the next part of the chat

    def on_enter_communication_crush(self):
        response = '\n'.join([
            f'So do you two talk a lot'
        ])
        return response

    def respond_from_communication_crush(self, message, tags):
        if 'no' in tags:
            return self.go_to_state('no_communication')
        else:
            return self.go_to_state('yes_communication')

    def on_enter_no_communication(self):
        response = '\n'.join([
            f'I feel you ... that is the worst'
        ])
        return response

    def on_enter_yes_communication(self):
        response = '\n'.join([
            f'andddd ... I wanna know!'
        ])
        return response

    def respond_from_yes_communication(self, message, tags):
        if 'good' in tags:
            return self.go_to_state('next_response')

    def on_enter_next_response(self):
        response = '\n'.join([
            f'How exciting! Do you see potential?'
        ])
        return response

    def respond_from_next_response(self, message, tags):
        if 'kind of' in tags:
            return self.go_to_state('unsure')
        else:
            return self.go_to_state('elaborate')

    def on_enter_unsure(self):
        response = '\n'.join([
            f'What does that mean? Explain!'
        ])
        return response

    def on_enter_elaborate(self):
        response = '\n'.join([
            f'Tell me more about them...'
        ])
        return response

    # The functions that correspond to saying no after responding no to communication with crush

    def respond_from_no_communication(self, message, tags):
        if 'yes' in tags:
            print("Have you ever tried talking to them? Maybe a little study date? ;)")
            response1 = input()
            return self.go_to_state('no_response')

    def on_enter_no_response(self):
        response = '\n'.join([
            f'You have to go and make your move!'
        ])
        return response

    def respond_from_no_response(self, message, tags):
        if 'yes' in tags:
            return self.go_to_state('determine_state')
        else:
            return self.go_to_state('no_response')

    def on_enter_determine_state(self):
        response = '\n'.join([
            f'Yes! That is what I like to hear! Would you talk to them after class or text them?'
        ])
        return response

    def respond_from_determine_state(self, message, tags):
        if 'class' in tags:
            return self.go_to_state('class')
        else:
            return self.go_to_state('text')

    def on_enter_class(self):
        return "I agree, irl is always better. You can really tell feelings. Let me know how it goes!!!"

    def on_enter_text(self):
        return "Wayyy less scary. Do it!!! Keep me updated."


    def finish_confused(self):
        """Send a message and go to the default state."""
        return "Sorry, I'm just a simple bot that can't understand much."

    def finish_success(self):
        """Send a message and go to the default state."""
        return 'Great, let me know if you need anything else!'

    def finish_fail(self):
        """Send a message and go to the default state."""
        return "I've tried my best but I still don't understand."

    def finish_thanks(self):
        """Send a message and go to the default state."""
        return "You're welcome!"


if __name__ == '__main__':
    OxyCSBot().chat()

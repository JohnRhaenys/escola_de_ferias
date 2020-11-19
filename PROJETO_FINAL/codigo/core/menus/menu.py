class Menu:
    def __init__(self, parent, title, options):
        self.parent = parent
        self.title = title
        self.options = options.option_function_mapping
        self.return_option = options.return_option

    def display(self):
        print()
        print(f'{"-=" * 10} {self.title} {"-=" * 10}')
        for position, option in enumerate(self.options):
            print(f'[{position}] - {option}')
        print(f'{"-=" * 10} {self.title} {"-=" * 10}')
        print()

    def get_user_choice(self):
        user_input = self.get_user_input()
        if user_input is None:
            return None

        for position, option in enumerate(self.options):
            if user_input == position:
                return option

        return None

    def get_user_input(self):
        user_input = input('Escolha uma opção: ')
        try:
            number = int(user_input)
            return number
        except ValueError:
            return None

    def open(self):
        while True:
            self.display()
            choice = self.get_user_choice()
            if choice is not None:
                if choice == self.return_option:
                    return None
                return self.options[choice]()

            print()
            input('Aperte ENTER para escolher outra opção')
            print()

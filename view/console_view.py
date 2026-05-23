class ConsoleView:

    def update(self, event, data):
        if event == "new_round":
            self.show_new_round(data)
        elif event == "cards_played":
            self.show_cards_played(data)
        elif event == "liar_called":
            self.show_liar_called(data)
        elif event == "liar_result":
            self.show_liar_result(data)
        elif event == "player_dead":
            self.show_player_dead(data)
        elif event == "player_survived":
            self.show_player_survived(data)
        elif event == "game_over":
            self.show_game_over(data)

    def show_new_round(self, data):
        print("\n" + "=" * 40)
        print("НОВИЙ РАУНД")
        print(f"Карта раунду: {data['round_card'].value}")
        alive = [str(p) for p in data["players"]]
        print(f"Гравці: {', '.join(alive)}")
        print("=" * 40)

    def show_cards_played(self, data):
        player = data["player"]
        count = data["claimed_count"]
        round_card = data["round_card"]
        print(f"\n{player.name} кладе {count} {round_card.value}")

    def show_liar_called(self, data):
        caller = data["caller"]
        target = data["target"]
        print(f"\n>>> {caller.name} кричить: LIAR! на {target.name} <<<")

    def show_liar_result(self, data):
        if data["was_lying"]:
            print(f"{data['target'].name} БРЕХАВ! Крутить револьвер...")
        else:
            print(f"{data['target'].name} був чесний! {data['caller'].name} крутить револьвер...")

    def show_player_dead(self, data):
        print(f"БАХ! {data['player'].name} вибув з гри!")

    def show_player_survived(self, data):
        print(f"Клік... {data['player'].name} пощастило.")

    def show_game_over(self, data):
        print("\n" + "=" * 40)
        print(f"ГРА ЗАКІНЧЕНА! Переможець: {data['winner'].name}")
        print("=" * 40)


    def show_turn_start(self, player):
        print(f"\n--- Хід: {player.name} ---")

    def show_hand(self, player):
        print("Твоя рука:")
        for i, card in enumerate(player.hand):
            print(f"  [{i}] {card}")

    def ask_card_indices(self, hand_size):
        while True:
            raw = input("Вибери карти (номери через пробіл, наприклад: 0 2 4): ")
            try:
                indices = [int(x) for x in raw.split()]
                if len(indices) < 1 or len(indices) > 3:
                    print("Можна покласти від 1 до 3 карт.")
                    continue
                if any(i < 0 or i >= hand_size for i in indices):
                    print(f"Номери від 0 до {hand_size - 1}.")
                    continue
                if len(set(indices)) != len(indices):
                    print("Не можна вибрати одну карту двічі.")
                    continue
                return indices
            except ValueError:
                print("Введи номери через пробіл.")

    def ask_call_liar(self, player):
        while True:
            answer = input("Викликати LIAR? (y/n): ").lower().strip()
            if answer in ("y", "n"):
                return answer == "y"
            print("Введи y або n.")

    def show_pass(self, player):
        print(f"{player.name} вірить і пасує.")
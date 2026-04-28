import tkinter as tk
import random


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - Human vs Computer")
        self.root.geometry("500x750")
        self.root.configure(bg="#1e1e1e")
        self.difficulty = None
        self.board = [''] * 9
        self.human = 'X'
        self.computer = 'O'
        self.game_active = True
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.stats_label = None

        self.show_player_selection_screen()

    def show_player_selection_screen(self):
        """Display player symbol selection screen"""
        for widget in self.root.winfo_children():
            widget.destroy()

        title_label = tk.Label(self.root, text="TIC TAC TOE", font=("Arial", 28, "bold"),
                               fg="#00ff00", bg="#1e1e1e")
        title_label.pack(pady=20)

        subtitle = tk.Label(self.root, text="Select Your Symbol", font=("Arial", 14),
                            fg="#00ddff", bg="#1e1e1e")
        subtitle.pack(pady=10)

        button_frame = tk.Frame(self.root, bg="#1e1e1e")
        button_frame.pack(pady=30)

        x_btn = tk.Button(button_frame, text="Play as X", font=("Arial", 12, "bold"),
                          bg="#00ff00", fg="#000000", width=15, height=2,
                          command=lambda: self.set_player_symbol('X'))
        x_btn.pack(pady=10)

        o_btn = tk.Button(button_frame, text="Play as O", font=("Arial", 12, "bold"),
                          bg="#ffff00", fg="#000000", width=15, height=2,
                          command=lambda: self.set_player_symbol('O'))
        o_btn.pack(pady=10)

        info_label = tk.Label(self.root, text="Choose your symbol to start the game",
                              font=("Arial", 10), fg="#ffffff", bg="#1e1e1e")
        info_label.pack(side=tk.BOTTOM, pady=20)

    def set_player_symbol(self, symbol):
        """Set player symbol and move to difficulty selection"""
        self.human = symbol
        self.computer = 'O' if symbol == 'X' else 'X'
        self.show_difficulty_screen()

    def show_difficulty_screen(self):
        """Display difficulty selection screen"""
        for widget in self.root.winfo_children():
            widget.destroy()

        title_label = tk.Label(self.root, text="TIC TAC TOE", font=("Arial", 28, "bold"),
                               fg="#00ff00", bg="#1e1e1e")
        title_label.pack(pady=20)

        subtitle = tk.Label(self.root, text="Select Difficulty Level", font=("Arial", 14),
                            fg="#00ddff", bg="#1e1e1e")
        subtitle.pack(pady=10)

        button_frame = tk.Frame(self.root, bg="#1e1e1e")
        button_frame.pack(pady=30)

        easy_btn = tk.Button(button_frame, text="Easy", font=("Arial", 12, "bold"),
                             bg="#00ff00", fg="#000000", width=15, height=2,
                             command=lambda: self.start_game("easy"))
        easy_btn.pack(pady=10)

        medium_btn = tk.Button(button_frame, text="Medium", font=("Arial", 12, "bold"),
                               bg="#ffff00", fg="#000000", width=15, height=2,
                               command=lambda: self.start_game("medium"))
        medium_btn.pack(pady=10)

        hard_btn = tk.Button(button_frame, text="Hard", font=("Arial", 12, "bold"),
                             bg="#ff0000", fg="#000000", width=15, height=2,
                             command=lambda: self.start_game("hard"))
        hard_btn.pack(pady=10)

        player_info = f"You are {self.human}, Computer is {self.computer}"
        info_label = tk.Label(self.root, text=player_info,
                              font=("Arial", 10), fg="#ffffff", bg="#1e1e1e")
        info_label.pack(side=tk.BOTTOM, pady=20)

    def start_game(self, difficulty):
        """Initialize game with selected difficulty"""
        self.difficulty = difficulty
        self.board = [''] * 9
        self.game_active = True
        self.show_game_screen()

    def show_game_screen(self):
        """Display the game board"""
        for widget in self.root.winfo_children():
            widget.destroy()

        # Stats display
        stats_frame = tk.Frame(self.root, bg="#1e1e1e")
        stats_frame.pack(pady=10)

        self.stats_label = tk.Label(stats_frame,
                                    text=f"Wins: {self.wins} | Losses: {self.losses} | Draws: {self.draws}",
                                    font=("Arial", 11, "bold"),
                                    fg="#00ff00", bg="#1e1e1e")
        self.stats_label.pack()

        # Header
        header_frame = tk.Frame(self.root, bg="#1e1e1e")
        header_frame.pack(pady=10)

        title = tk.Label(header_frame, text="TIC TAC TOE", font=("Arial", 20, "bold"),
                         fg="#00ff00", bg="#1e1e1e")
        title.pack()

        difficulty_label = tk.Label(header_frame, text=f"Difficulty: {self.difficulty.upper()}",
                                    font=("Arial", 10), fg="#00ddff", bg="#1e1e1e")
        difficulty_label.pack()

        # Game board
        self.buttons = []
        board_frame = tk.Frame(self.root, bg="#1e1e1e")
        board_frame.pack(pady=20)

        for i in range(9):
            btn = tk.Button(board_frame, text="", font=("Arial", 20, "bold"),
                            width=6, height=3, bg="#333333", fg="#555555",
                            command=lambda x=i: self.human_move(x),
                            activebackground="#5F0404")
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(btn)

        # Status and buttons
        status_frame = tk.Frame(self.root, bg="#1e1e1e")
        status_frame.pack(pady=10)

        turn_text = f"Your Turn ({self.human})"
        self.status_label = tk.Label(status_frame, text=turn_text,
                                     font=("Arial", 12), fg="#ffff00", bg="#1e1e1e")
        self.status_label.pack()

        button_frame = tk.Frame(self.root, bg="#1e1e1e")
        button_frame.pack(pady=10)

        reset_btn = tk.Button(button_frame, text="New Game", font=("Arial", 10, "bold"),
                              bg="#00ddff", fg="#000000", width=12,
                              command=self.show_difficulty_screen)
        reset_btn.pack(side=tk.LEFT, padx=5)

        exit_btn = tk.Button(button_frame, text="Exit", font=("Arial", 10, "bold"),
                             bg="#ff0000", fg="#ffffff", width=12,
                             command=self.root.quit)
        exit_btn.pack(side=tk.LEFT, padx=5)

    def human_move(self, index):
        """Handle human player move"""
        if not self.game_active or self.board[index] != '':
            return

        self.board[index] = self.human
        self.update_button(index, self.human)

        if self.check_winner(self.human):
            self.end_game(f"🎉 Player {self.human} Wins! 🎉")
            return

        if self.is_board_full():
            self.end_game("It's a Draw!")
            return

        self.status_label.config(text="Computer is thinking...", fg="#ff9900")
        self.root.after(500, self.computer_move)

    def computer_move(self):
        """Handle computer player move"""
        if not self.game_active:
            return

        move = self.get_computer_move()
        if move == -1:
            return

        self.board[move] = self.computer
        self.update_button(move, self.computer)

        if self.check_winner(self.computer):
            self.end_game(f"💻 Player {self.computer} Wins! 💻")
            return

        if self.is_board_full():
            self.end_game("It's a Draw!")
            return

        turn_text = f"Your Turn ({self.human})"
        self.status_label.config(text=turn_text, fg="#ffff00")

    def get_computer_move(self):
        """Determine computer move based on difficulty"""
        if self.difficulty == "easy":
            return self.easy_move()
        elif self.difficulty == "medium":
            return self.medium_move()
        else:
            return self.hard_move()

    def easy_move(self):
        """Random move"""
        empty_cells = [i for i in range(9) if self.board[i] == '']
        return random.choice(empty_cells) if empty_cells else -1

    def medium_move(self):
        """Smart move: 50% block/win, 50% random"""
        empty_cells = [i for i in range(9) if self.board[i] == '']

        # Try to win
        for cell in empty_cells:
            self.board[cell] = self.computer
            if self.check_winner(self.computer):
                self.board[cell] = ''
                return cell
            self.board[cell] = ''

        # Try to block
        for cell in empty_cells:
            self.board[cell] = self.human
            if self.check_winner(self.human):
                self.board[cell] = ''
                return cell
            self.board[cell] = ''

        # Random move
        return random.choice(empty_cells) if empty_cells else -1

    def hard_move(self):
        """Minimax algorithm for optimal play"""
        empty_cells = [i for i in range(9) if self.board[i] == '']

        best_score = float('-inf')
        best_move = empty_cells[0] if empty_cells else -1

        for cell in empty_cells:
            self.board[cell] = self.computer
            score = self.minimax(0, False)
            self.board[cell] = ''

            if score > best_score:
                best_score = score
                best_move = cell

        return best_move

    def minimax(self, depth, is_maximizing):
        """Minimax algorithm"""
        if self.check_winner(self.computer):
            return 10 - depth
        if self.check_winner(self.human):
            return depth - 10
        if self.is_board_full():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(9):
                if self.board[i] == '':
                    self.board[i] = self.computer
                    score = self.minimax(depth + 1, False)
                    self.board[i] = ''
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if self.board[i] == '':
                    self.board[i] = self.human
                    score = self.minimax(depth + 1, True)
                    self.board[i] = ''
                    best_score = min(score, best_score)
            return best_score

    def check_winner(self, player):
        """Check if player has won"""
        winning_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combos:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def is_board_full(self):
        """Check if board is full"""
        return '' not in self.board

    def update_button(self, index, player):
        """Update button display"""
        self.buttons[index].config(
            text=player, fg="#000000", state=tk.DISABLED)

    def end_game(self, message):
        """End game and show result"""
        self.game_active = False
        # Set color based on win/loss
        if "Draw" in message:
            color = "#ffff00"  # Yellow for draw
            self.draws += 1
        elif self.human == 'X' and "X" in message:
            color = "#00ff00"  # Green for human win
            self.wins += 1
        elif self.human == 'O' and "O" in message:
            color = "#00ff00"  # Green for human win
            self.wins += 1
        else:
            color = "#ff0000"  # Red for human loss
            self.losses += 1

        # Update stats display
        if self.stats_label:
            self.stats_label.config(
                text=f"Wins: {self.wins} | Losses: {self.losses} | Draws: {self.draws}")

        self.status_label.config(text=message, fg=color)
        for btn in self.buttons:
            btn.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()

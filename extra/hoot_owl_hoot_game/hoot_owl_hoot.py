import itertools
import logging
import random
import unittest
from enum import Enum

board_config = "D:\\OSU\\problems\\problems\\extra\\hoot_owl_hoot_board.txt"

NUM_COLOR_CARDS = 6
NUM_SUN_CARDS = 14
NUM_SUN_SPOTS = 13
NUM_CARDS_START = 3 
SUN_CARD = "SUN"
NUM_TESTS = 100

class Color(Enum):
    PINK = 1
    PURPLE = 2
    GREEN = 3
    ORANGE = 4
    BLUE = 5
    YELLOW = 6
"""
Game config:
-board

-filled spaces
-players/cards
-sun
-valid moves

Players
"""
# pink purple green blue orange yellow

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

class Space:
    def __init__(self, color: Color) -> None:
        self.occupied = False
        self.color = color
        self.owl_name = None
    
    def __str__(self) -> str:
        str = f"{self.color.name:8s}"
        if self.owl_name:
            str += f"  {self.owl_name}"
        return str

class Owl:
    def __init__(self, name) -> None:
        self.name = name
        self.position = 0
        self.at_end = False

class BoardConfig:
    def __init__(self, num_owls: int=3) -> None:
        self.board = self.read_board(board_config)
        self.deck = self.init_deck()
        self.discard = []
        self.sun_position = 0
        self.owl_positions = []
        self.owl_locs = {}
        self.owls = []

        for i in range(num_owls):
            owl = Owl(f"Owl_{i}")
            self.owls.append(owl)
            self.owl_locs[f"Owl_{i}"] = 0

        # print(self)

    def __str__(self) -> str:
        str = "START:"
        nest_str = "NEST: "
        for owl_name, owl_pos in self.owl_locs.items():
            if owl_pos == 0:
                str += f"{owl_name} "
            elif owl_pos == len(self.board):
                nest_str += f"{owl_name} "
        str += "\n"
        occupied_spots = self.owl_locs.values()
        for i in range(len(self.board)):
            str += f"\t{self.board[i]}\n"
        str += nest_str
        # print(f"Sun: {self.sun_position} of {NUM_SUN_SPOTS}")
        # print(f"{self.deck=}")
        return str

    def read_board(self, board_config):
        board = []
        with open(board_config, "r") as fh:
            for line in fh:
                # print(line.strip())
                try:
                    color = Color[line.strip()]
                    space = Space(color)
                    board.append(space)
                except:
                    print(f"Invalid board config: {line=}")
                
        return board
    
    def init_deck(self):
        deck = []
        for i in range(NUM_COLOR_CARDS):
            for color in Color:
                deck.append(color.name)
    
        for i in range(NUM_SUN_CARDS):
            deck.append(SUN_CARD)

        return deck

    def DrawCards(self, num_cards: int):
        if num_cards > len(self.deck):
            self.deck = self.init_deck()
        cards = random.sample(self.deck, num_cards)
        for card in cards:
            self.deck.remove(card)
            if len(self.deck) == 0:
                self.deck = self.init_deck()

        return cards
    
    def AllOwlsAtEnd(self):
        owls = self.GetAvailableOwls()
        return len(owls) == 0
    
    def GetAvailableOwls(self):
        owls = []
        # for owl_pos in self.owl_positions:
        #     if owl_pos < len(self.board):
        #         owls.append(owl_pos)
        for owl_name, owl_loc in self.owl_locs.items():
            if owl_loc < len(self.board):
                owls.append(owl_name)
        
        return owls
        
    def GameOver(self):
        if self.sun_position >= NUM_SUN_SPOTS:
            self.game_won = False
            return True
        
        if self.AllOwlsAtEnd():
            self.game_won = True
            return True
        
    def IsMoveValid(self, move) -> bool:
        # Return True iff the given move is valid
        # check if a color is skipped
        return False
    
    def PlayerMove(self, move):
        if move.card == SUN_CARD:
            self.sun_position += 1
        else:
            logger.info(move)
            owl_loc = self.owl_locs[move.owl]
            color = move.card
            logger.info(f"Owl at {owl_loc}, board color {self.board[owl_loc]}, card {color}")
            # remove owl from current location
            self.board[owl_loc].owl_name = None
            position_found = False
            for i in range(owl_loc + 1, len(self.board)):
                logger.info(f"{self.board[i]}")
                if color == self.board[i].color.name:
                    occupied_spots = self.owl_locs.values()
                    if i in occupied_spots:
                        logger.info(f"Owl at position {i}, skipping")
                    else:
                        logger.info(f"Spot {i} open, taking")
                        self.owl_locs[move.owl] = i
                        self.board[i].owl_name = move.owl
                        position_found = True
                        break

            if not position_found:
                self.owl_locs[move.owl] = len(self.board)
                logger.info(f"Owl at nest: {move.owl}")

    def SimulateMove(self, move):
        """
        Return what would happen if the given move was chosen (do not actually update board though)
        
        """
        owl_loc = self.owl_locs[move.owl]
        result = Result()
        result.owl_at_end = True
        for space in range(owl_loc, len(self.board)):
            if self.board[space].occupied:
                result.owls_jumped += 1
            elif self.board[space].color == move.card:
                result.owl_at_end = False
                break
            result.spaces_moved += 1

        return result
    
class Player:
    def __init__(self, id: str) -> None:
        self.name = f"{id}_Random"
        self.cards = []

    def __str__(self) -> str:
        return f"{self.name}: " + ", ".join(self.cards)
        
    def DealCards(self, cards):
        for card in cards:
            self.cards.append(card)

    def Move(self, board):
        for card in self.cards:
            if card == SUN_CARD:
                self.cards.remove(card)
                return Move(card)
        
        return self.StrategicMove(board)
    
    def StrategicMove(self, board):
        # default random
        card = random.choice(self.cards)
        owl = random.choice(board.GetAvailableOwls())
        self.cards.remove(card)
        return Move(card, owl)

class PlayerFirstOwl(Player):
    # select the owl closest to the nest
    def __init__(self, id: str) -> None:      
        super().__init__(id)
        self.name = f"{id}_FirstOwl"
        
    def StrategicMove(self, board):
        # print("TODO pick first owl")
        # default random
        card = random.choice(self.cards)
        owls = board.GetAvailableOwls()
        # find owl that is furthest along
        max_owl = owls[0]
        for owl in owls[1:]:
            if board.owl_locs[owl] > board.owl_locs[max_owl]:
                max_owl = owl
        
        # find card that will move that owl the furthest
        best_result = None
        best_card = None
        for card in set(self.cards):
            move = Move(card, max_owl)
            result = board.SimulateMove(move)
            # print(f"Simulated result for {card=} is {result=}")
            if not best_result or result.spaces_moved > best_result.spaces_moved:
                best_result = result
                best_card = card
        # print(f"Furthest owl is {max_owl=}, best card is {card=}")
        self.cards.remove(best_card)
        return Move(best_card, max_owl)

class PlayerLastOwl(Player):
    # select the last owl (owl closest to start)
    def __init__(self, id: str) -> None:      
        super().__init__(id)
        self.name = f"{id}_LastOwl"
        
    def StrategicMove(self, board):
        # print("TODO pick first owl")
        # default random
        card = random.choice(self.cards)
        owls = board.GetAvailableOwls()
        # find owl that is furthest along
        min_owl = owls[0]
        for owl in owls[1:]:
            if board.owl_locs[owl] < board.owl_locs[min_owl]:
                min_owl = owl
        
        # find card that will move that owl the furthest
        best_result = None
        best_card = None
        for card in set(self.cards):
            move = Move(card, min_owl)
            result = board.SimulateMove(move)
            # print(f"Simulated result for {card=} is {result=}")
            if not best_result or result.spaces_moved > best_result.spaces_moved:
                best_result = result
                best_card = card
        # print(f"Furthest owl is {max_owl=}, best card is {card=}")
        self.cards.remove(best_card)
        return Move(best_card, min_owl)


class PlayerFactory:
    def __init__(self) -> None:
        self.player_types = [Player, PlayerFirstOwl, PlayerLastOwl]
        # self.player_types = [PlayerFirstOwl]

    def generate_combinations(self, min_size=2, max_size=2):
        combos = []
        for size in range(min_size, max_size + 1):
            for combo in itertools.product(self.player_types, repeat=size):
                combos.append(combo)

        return combos
    
    def create_instances(self, combo):
        instances = [cls(i + 1) for i, cls in enumerate(combo)]
        player_names = ', '.join(str(instance) for instance in instances)
        return instances, player_names

class Move:
    def __init__(self, card, owl=None, position=None):
        self.card = card
        self.owl = owl
        # self.position = position

    def __str__(self):
        return f"Move (Card: {self.card}, Owl: {self.owl})"

class Result:
    def __init__(self):
        self.spaces_moved = 0
        self.owls_jumped = 0
        self.owl_at_end = False

    def __str__(self) -> str:
        return f"Result (Spaces Moved {self.spaces_moved}, Owls Jumped {self.owls_jumped}, At Nest {self.owl_at_end})"

class Game:
    def __init__(self, players: list[Player], num_owls: int=3) -> None:
        logger.info("Starting board")
        self.board = BoardConfig(num_owls)
        if not 2 <= len(players) <= 4:
            raise ValueError("Number of players must be between 2 and 4.")
        # assert(2 <= len(players) <= 4, "Must have 2 to four players")
        self.players = players

    def RunGame(self):
        # deal cards
        for player in self.players:
            cards = self.board.DrawCards(NUM_CARDS_START)
            player.DealCards(cards)
            # print(f"Dealt cards to player: {player}")
            

        # game loop
        while True:
            if self.board.GameOver():
                break

            for player in self.players:
                # print(self.board)
                # print(f"Ready for turn: {player}")

                # input()

                move = player.Move(self.board)
                draw_card = self.board.DrawCards(1)
                player.DealCards(draw_card)
                self.board.PlayerMove(move)

                logger.info("Player Turn")
                logger.info(move)
                logger.info(f"Draw card {draw_card=}")

                if self.board.GameOver():
                    break


        logger.info(f"Game Over! {self.board.game_won=}")
        return True

class TestGame(unittest.TestCase):
    def setUp(self):
    
        self.board = BoardConfig()

    def test_game(self):
        players = [
            PlayerFirstOwl("player1"),
            PlayerFirstOwl("player2"),
            # Player("player3"),
            # Player("player4"),
        ]
        game = Game(players, num_owls=3
                    )
        self.assertTrue(game.RunGame())
        

class DatacCollection:
    def main(self):
        player_factory = PlayerFactory()
        player_combos = player_factory.generate_combinations()
        for combo in player_combos:
            players, player_str = player_factory.create_instances(combo)
            print(f"{player_str=}")
            for num_owls in range(3, 7):
                win_count = 0
                for i in range(NUM_TESTS):
                    players, player_str = player_factory.create_instances(combo)
                    
                    game = Game(players, num_owls=num_owls)
                    game.RunGame()
                    if game.board.game_won:
                        win_count += 1
                    # player_str = ", ".join(players)

                print(f"{len(players)=}, {num_owls=}, {win_count=}/{NUM_TESTS} win_pct={win_count/NUM_TESTS*100:2.0f}%")
                # print(f"   {player_str}")

                
         


if __name__ == '__main__':
    # unittest.main()
    DatacCollection().main()

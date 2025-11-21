import pytest
import pandas as pd
from unittest.mock import patch
from tictacto_functions import main, player1_turn, player2_turn, draw  # Remplacez your_script par le nom de votre fichier

@pytest.fixture
def empty_board():
    """Crée un plateau de jeu vide pour les tests"""
    return pd.DataFrame({
        'A': ['', '', ''],
        'B': ['', '', ''],
        'C': ['', '', '']
    })

def test_main_horizontal_win():
    """Teste la victoire sur une ligne horizontale"""
    df = pd.DataFrame({
        'A': ['X', '', ''],
        'B': ['X', 'O', ''],
        'C': ['X', 'O', '']
    })
    assert main(df) == "Player X won"

def test_main_vertical_win():
    """Teste la victoire sur une colonne verticale"""
    df = pd.DataFrame({
        'A': ['O', '', ''],
        'B': ['O', 'X', ''],
        'C': ['O', 'X', 'X']
    })
    assert main(df) == "Player O won"

def test_main_diagonal_win():
    """Teste la victoire sur une diagonale"""
    df = pd.DataFrame({
        'A': ['X', 'O', ''],
        'B': ['O', 'X', ''],
        'C': ['', '', 'X']
    })
    assert main(df) == "Player X won"

def test_main_no_winner():
    """Teste qu'il n'y a pas de gagnant"""
    df = pd.DataFrame({
        'A': ['X', 'O', ''],
        'B': ['O', 'X', ''],
        'C': ['', '', '']
    })
    assert main(df) is True

@patch('builtins.input', side_effect=['A0'])
def test_player1_turn_valid_move(mock_input, empty_board):
    """Teste un coup valide du joueur 1"""
    with patch('builtins.print'):  # Supprime l'affichage pendant le test
        player1_turn(empty_board)
        assert empty_board.at[0, 'A'] == 'X'

@patch('builtins.input', side_effect=['Z9', 'A0'])
def test_player1_turn_invalid_move(mock_input, empty_board):
    """Teste un coup invalide suivi d'un coup valide du joueur 1"""
    with patch('builtins.print'):
        player1_turn(empty_board)
        assert empty_board.at[0, 'A'] == 'X'

@patch('builtins.input', side_effect=['B1'])
def test_player2_turn_valid_move(mock_input, empty_board):
    """Teste un coup valide du joueur 2"""
    with patch('builtins.print'):
        player2_turn(empty_board)
        assert empty_board.at[1, 'B'] == 'O'

def test_draw_not_full():
    """Teste que le jeu continue quand le plateau n'est pas plein"""
    df = pd.DataFrame({
        'A': ['X', 'O', ''],
        'B': ['O', 'X', ''],
        'C': ['', '', '']
    })
    assert draw(df) is True

def test_draw_full_board():
    """Teste que le jeu se termine en égalité quand le plateau est plein"""
    df = pd.DataFrame({
        'A': ['X', 'O', 'X'],
        'B': ['O', 'X', 'O'],
        'C': ['O', 'X', 'O']
    })
    with pytest.raises(SystemExit) as exc_info:
        draw(df)
    assert str(exc_info.value) == "Draw"
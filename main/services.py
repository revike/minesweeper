import copy
import random
from uuid import UUID


def create_field(width, height):
    """Create field"""
    return [[' ' for _ in range(width)] for _ in range(height)]


def set_field(fields, field, col, row):
    """Set field"""
    result = 0

    def get_result(res):
        """Get result"""
        if 0 <= row < len(field) and 0 <= col < len(fields):
            if fields[col][row] == 'X':
                res += 1
        return res

    row -= 1
    result = get_result(result)
    col -= 1
    result = get_result(result)
    row += 1
    result = get_result(result)
    row += 1
    result = get_result(result)
    col += 1
    result = get_result(result)
    col += 1
    result = get_result(result)
    row -= 1
    result = get_result(result)
    row -= 1
    result = get_result(result)
    return f'{result}'


def create_bomb_field(width, height, fields, mines_count):
    """Create Bomb field"""
    result_fields = copy.deepcopy(fields)
    result = []
    while len(result) != mines_count:
        col, row = random.randint(0, height - 1), random.randint(0, width - 1)
        if [col, row] not in result:
            result.append([col, row])
            result_fields[col][row] = 'X'

    row, col = 0, 0
    for field in result_fields:
        for _ in field:
            if field[row] == 'X':
                row += 1 if len(field) > row + 1 else 0
                if row == 0:
                    col += 1 if len(result_fields) > col + 1 else 0
                    if col == 0:
                        break
                continue
            else:
                result_fields[col][row] = set_field(result_fields, field, col, row)
                row += 1 if len(field) > row + 1 else 0
                if row == 0:
                    col += 1 if len(result_fields) > col + 1 else 0
                    if col == 0:
                        break
        row, col = 0, col + 1 if len(result_fields) > col + 1 else 0
    return result_fields


def check_uuid(value, version=4):
    """Check UUID"""
    try:
        UUID(value, version=version)
        return True
    except ValueError:
        return False


def get_game_data(game, col, row):
    """get game data. Todo: [col][row]"""
    return game

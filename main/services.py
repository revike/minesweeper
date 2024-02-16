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
    """Get game data"""
    if not game.completed:
        field = copy.deepcopy(game.game.field)
        field_bomb = copy.deepcopy(game.game.field_bomb)
        obj_bomb = field_bomb[row][col]
        if obj_bomb not in ('0', 'X'):
            if obj_bomb != 'X':
                field[row][col] = obj_bomb
        elif obj_bomb == 'X':
            field = game.game.field_bomb
            game.completed = True
            game.save()
        elif obj_bomb == '0':
            field, cells = set_field_zero(field, field_bomb, obj_bomb, row, col)
            for cell in cells:
                set_field_zero(field, field_bomb, obj_bomb, cell[0], cell[1], cells)
        game.game.field = field
        game.game.save()
        game = check_win_game(game)
    return game


def set_field_zero(fields, field_bomb, obj_bomb, row, col, cells=None):
    """Set field zero"""
    if cells is None:
        cells = []
    fields[row][col] = obj_bomb

    def get_cell_value(fields_list, fields_bomb, row_value, col_value):
        """Get cell value"""
        check_cell_zero = False
        if 0 <= row_value < len(fields_list) and 0 <= col_value < len(fields_list[0]):
            cell_value = fields_bomb[row_value][col_value]
            fields_list[row_value][col_value] = cell_value
            if cell_value == '0':
                check_cell_zero = True
        return fields_list, check_cell_zero

    row -= 1
    fields, cell_zero = get_cell_value(fields, field_bomb, row, col)
    if cell_zero and (row, col,) not in cells:
        cells.append((row, col,))
    col -= 1
    fields, cell_zero = get_cell_value(fields, field_bomb, row, col)
    if cell_zero and (row, col,) not in cells:
        cells.append((row, col,))
    row += 1
    fields, cell_zero = get_cell_value(fields, field_bomb, row, col)
    if cell_zero and (row, col,) not in cells:
        cells.append((row, col,))
    row += 1
    fields, cell_zero = get_cell_value(fields, field_bomb, row, col)
    if cell_zero and (row, col,) not in cells:
        cells.append((row, col,))
    col += 1
    fields, cell_zero = get_cell_value(fields, field_bomb, row, col)
    if cell_zero and (row, col,) not in cells:
        cells.append((row, col,))
    col += 1
    fields, cell_zero = get_cell_value(fields, field_bomb, row, col)
    if cell_zero and (row, col,) not in cells:
        cells.append((row, col,))
    row -= 1
    fields, cell_zero = get_cell_value(fields, field_bomb, row, col)
    if cell_zero and (row, col,) not in cells:
        cells.append((row, col,))
    row -= 1
    fields, cell_zero = get_cell_value(fields, field_bomb, row, col)
    if cell_zero and (row, col,) not in cells:
        cells.append((row, col,))

    return fields, cells


def check_win_game(game):
    """Check Win Game"""
    mines_count = 0
    for fields in game.game.field:
        for field in fields:
            if field == ' ':
                mines_count += 1
    if mines_count == game.mines_count:
        game.completed = True
        result_win = copy.deepcopy(game.game.field_bomb)
        for i, l in enumerate(result_win):
            for k, j in enumerate(l):
                if j == 'X':
                    result_win[i][k] = 'M'
        game.game.field = result_win
        game.game.save()
        game.completed = True
        game.save()
    return game

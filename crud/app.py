import argparse
from expenses_commands import add_expense, get_expenses

# Commands: 
# python app.py --set "name" price
# python app.py --getlist

def main():
    parser = argparse.ArgumentParser(description='Budget CLI App')
    
    group = parser.add_mutually_exclusive_group(required=True)
    
    group.add_argument(
        "--set",
        nargs=2,
        metavar=("NAME", "PRICE"),
        help='Установить значение NAME=PRICE'
    )
    
    group.add_argument(
        "--getlist",
        action='store_true',
        help='Получить список расходов'
    )
    
    args = parser.parse_args()
    
    if args.set:
        key, value = args.set
        add_expense(key, value)
    elif args.getlist:
        get_expenses()

if __name__ == '__main__':
    main()
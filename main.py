def arb_calc(start_sum, input_rate, output_rate, iter_num):
    try:
        total = start_sum
        iter_profit_list = []
        for i in range(iter_num):
            convert_to = round(total/input_rate, 3)
            buy = round(convert_to * output_rate, 3)
            iter_profit = buy - start_sum
            iter_profit_list.append(round(iter_profit, 3))
            total += (buy - total)
        return total - start_sum, iter_profit_list
    except Exception as e:
        print(e)


start_sum = int(input('Enter start sum: '))
input_rate = int(input('Enter exchange rate in first place: '))
output_rate = int(input('Enter exchange rate in second place: '))
iter_num = int(input('Enter number of iteration: '))

try:
    profit_percent = (round(output_rate / input_rate * 100 - 100, 2))
    profit, iteration_profit = arb_calc(start_sum, input_rate, output_rate, iter_num)
    profit_usd = round(profit / input_rate, 2)
    total_money = profit + start_sum

    print('\nCord percent profit: {}%'.format(profit_percent))
    print('\nYour clear profit(without entering sum) is {}rub or {}$.\nProfit of '
          'every iteration is {}'.format(round(profit, 3), profit_usd, iteration_profit))
    print(('\nMoney in your pocket: {}rub. Congrats!'.format(total_money)))
except Exception as e:
    print(e)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arb_calc(start_sum, input_rate, output_rate, iter_num)


from slither.slither import Slither

slither = Slither('smartcontract.sol')



for contract in slither.contracts:
    print('Contract: '+ contract.name)

    for function in contract.functions:
        print('Function: {}'.format(function.name))

        print('\tRead: {}'.format([v.name for v in function.state_variables_read]))
        print('\tWritten {}'.format([v.name for v in function.state_variables_written]))


# if __name__ == '__main__':
#     print(slither.contracts(list(Contracts)))

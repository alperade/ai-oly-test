from subpro import run_command
from aiSummary import summary
import time

def olympix():
    command = 'slither smartcontract.sol'
    output = run_command(command)
    a = summary(output)
    return a
    # return summary(output)



if __name__ == '__main__':
    print(olympix())

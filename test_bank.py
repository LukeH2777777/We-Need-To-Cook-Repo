from bank import Bank

bank = Bank()



def test_withdraw():
    bank.withdraw(100)
    assert bank.balance() == 400

    # this might look odd but since it runs all of the functions together
    # it isnt isolated 
    bank.dev_add(100)


def test_deposit():
    bank.deposit(100)
    assert bank.balance() == 600


import turingarena as ta


def evaluate(n):
    a, b = 1, n
    trials = 0

    print(f"guess({a}, {b})... ")

    def answer(c):
        nonlocal a, b, trials
        trials += 1
        p.check(trials <= ta.parameters.easy_max_trials, "too many guesses")

        assert a <= b

        if a == b == c:
            print("guessed correctly!")
            p.exit()

        if c < a:
            return +1
        if c > b:
            return -1

        if c < (a+b) / 2:
            a = c+1
            return +1
        else:
            b = c-1
            return -1

    try:
        with ta.run_algorithm(ta.submission.source) as p:
            p.procedures.guess(a, b, callbacks=[answer])
            p.fail("procedure guess returned before guessing correctly")
    except ta.InterfaceExit:
        return trials
    except ta.AlgorithmError as e:
        print(f"{e}")
        return None
    
    assert False, "unexpected end"


def main():
    for n in (10, 100, 1000, 1000000000):
        trials = evaluate(n)
        if trials is None or trials > n:
            ta.goals["easy"] = False
        if trials is None or trials > ta.parameters.hard_max_trials:
            ta.goals["hard"] = False

    ta.goals.setdefault("easy", True)
    ta.goals.setdefault("hard", True)

if __name__ == '__main__':
    main()

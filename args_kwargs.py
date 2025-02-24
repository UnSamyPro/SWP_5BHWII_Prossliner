
# Was passiert, wenn man *args und **kwargs vertauscht (def test(**kwargs,*args))?
# -> Syntax fehler

# Warum sollte man *args nicht mit list oder dict verwechseln?
# -> *args ist ein tuple, **kwargs ist ein dict

# Wann ist **kwargs nützlich? (z. B. für flexible Konfigurationsparameter)
# -> Named parameter, nicht alle Parameter müssen übergeben werden, default werte

# Wie kann man *args in einer rekursiven Funktion verwenden?
# -> erstes element herausnehmen und mit dem rest rekursiv aufrufen
def sum_recursive(*args):
    if not args:
        return 0
    return args[0] + sum_recursive(*args[1:])


def generate_power(exponent: int):
    print("exponent", exponent)
    def power(base: int) -> int:
        print("base", base)
        return base ** exponent
    return power


def outer_function(*args, **kwargs):
    def sum_args():
        try:
            return sum(args) if args else 0
        except TypeError:
            return "args must be numbers"

    def values_kwargs():
        return ", ".join(f"{key}={value}" for key, value in kwargs.items())

    return f"sum args: {sum_args()}\nkwargs: {values_kwargs()}"


def main():
    print(sum_recursive(1, 2, 3, 4, 5))

    raise_2 = generate_power(2)
    print(raise_2(3))
    # 2^3 = 8; 3^2 = 9
    # output: 9

    print(outer_function(1, 2, 3, 4, 5, a="A", b="B", c="C", d="D", e="E"))
    print(outer_function(1, "2", 3, 4, 5, a="A", b="2", c="C", d="D", e="E"))


if __name__ == "__main__":
    main()

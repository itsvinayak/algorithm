def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print(f"Move disk 1 from rod {from_rod} to rod {to_rod}")
        return
    TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
    print(f"Move disk {n} from rod {from_rod} to rod {to_rod}")
    TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod)


def main():
    n = 4
    TowerOfHanoi(n, "A", "B", "C")


if __name__ == "__main__":
    main()
